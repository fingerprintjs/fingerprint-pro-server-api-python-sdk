import json
from typing import List

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import zlib

from fingerprint_pro_server_api_sdk.api_client import ApiClientDeserializer
from fingerprint_pro_server_api_sdk.models.events_get_response import EventsGetResponse

SEALED_HEADER = bytes([0x9e, 0x85, 0xdc, 0xed])
DecryptionAlgorithm = {
    'Aes256Gcm': 'aes-256-gcm',
}


class DecryptionKey:
    """Key for decryption of sealed data."""
    exception: Exception
    algorithm: str

    def __init__(self, key: bytes, algorithm: str):
        self.key = key
        self.algorithm = algorithm


class UnsealError(Exception):
    """Error during unsealing."""
    exception: Exception
    key: DecryptionKey

    def __init__(self, exception: Exception, key: DecryptionKey):
        self.exception = exception
        self.key = key


class UnsealAggregateError(Exception):
    """Aggregated error during unsealing."""
    errors: List[UnsealError]

    def __init__(self, errors: List[UnsealError]):
        self.errors = errors
        super().__init__("Unable to decrypt sealed data")


def unseal_event_response(sealed_data: bytes, decryption_keys: List[DecryptionKey]) -> EventsGetResponse:
    """Unseal event response with one of the provided keys."""
    unsealed = __unseal(sealed_data, decryption_keys)
    return __parse_event_response(unsealed)


def __parse_event_response(unsealed: str) -> EventsGetResponse:
    """Parse event response from unsealed data."""
    json_data = json.loads(unsealed)

    if 'products' not in json_data:
        raise ValueError('Sealed data is not valid event response')

    result: EventsGetResponse = ApiClientDeserializer.deserialize(json_data, 'EventsGetResponse')
    return result


def __unseal(sealed_data: bytes, decryption_keys: List[DecryptionKey]) -> str:
    """Unseal data with one of the provided keys."""
    if sealed_data[:len(SEALED_HEADER)].hex() != SEALED_HEADER.hex():
        raise ValueError('Invalid sealed data header')

    errors = []
    for decryption_key in decryption_keys:
        if decryption_key.algorithm == DecryptionAlgorithm['Aes256Gcm']:
            try:
                return __unseal_aes256gcm(sealed_data, decryption_key.key)
            except Exception as e:
                errors.append(UnsealError(e, decryption_key))
                continue
        else:
            raise ValueError(f"Unsupported decryption algorithm: {decryption_key.algorithm}")

    raise UnsealAggregateError(errors)


def __unseal_aes256gcm(sealed_data: bytes, decryption_key: bytes) -> str:
    """Unseal data with AES-256-GCM."""
    nonce_length = 12
    nonce = sealed_data[len(SEALED_HEADER):len(SEALED_HEADER) + nonce_length]

    auth_tag_length = 16
    auth_tag = sealed_data[-auth_tag_length:]

    ciphertext = sealed_data[len(SEALED_HEADER) + nonce_length:-auth_tag_length]

    decipher = Cipher(
        algorithms.AES(decryption_key),
        modes.GCM(nonce, auth_tag),
        backend=default_backend()
    ).decryptor()

    compressed = decipher.update(ciphertext) + decipher.finalize()

    payload = zlib.decompress(compressed, -zlib.MAX_WBITS)

    return payload.decode('utf-8')
