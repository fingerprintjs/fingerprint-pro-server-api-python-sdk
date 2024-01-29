import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import zlib

from fingerprint_pro_server_api_sdk.models.event_response import EventResponse

SEALED_HEADER = bytes([0x9e, 0x85, 0xdc, 0xed])
DecryptionAlgorithm = {
    'Aes256Gcm': 'aes-256-gcm',
}


class DecryptionKey:
    def __init__(self, key, algorithm):
        self.key = key
        self.algorithm = algorithm


class UnsealError(Exception):
    exception: Exception
    key: DecryptionKey

    def __init__(self, exception, key):
        self.exception = exception
        self.key = key


class UnsealAggregateError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__("Unable to decrypt sealed data")


def parse_events_response(unsealed):
    json_data = json.loads(unsealed)

    if 'products' not in json_data:
        raise ValueError('Sealed data is not valid events response')

    return EventResponse(json_data['products'])


def unseal_events_response(sealed_data, decryption_keys):
    unsealed = unseal(sealed_data, decryption_keys)
    return parse_events_response(unsealed)


def unseal(sealed_data, decryption_keys):
    if sealed_data[:len(SEALED_HEADER)].hex() != SEALED_HEADER.hex():
        raise ValueError('Invalid sealed data header')

    errors = []
    for decryption_key in decryption_keys:
        if decryption_key.algorithm == DecryptionAlgorithm['Aes256Gcm']:
            try:
                return unseal_aes256gcm(sealed_data, decryption_key.key)
            except Exception as e:
                errors.append(UnsealError(e, decryption_key))
                continue
        else:
            raise ValueError(f"Unsupported decryption algorithm: {decryption_key.algorithm}")

    raise UnsealAggregateError(errors)


def unseal_aes256gcm(sealed_data, decryption_key):
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
