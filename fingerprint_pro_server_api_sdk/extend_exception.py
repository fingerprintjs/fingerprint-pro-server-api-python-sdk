from fingerprint_pro_server_api_sdk.rest import KnownApiException


def extend_exception(exception, error_object):
    if exception.status == 429:
        error_object.retry_after = int(exception.headers.get('retry-after'))
    return KnownApiException(exception, error_object)
