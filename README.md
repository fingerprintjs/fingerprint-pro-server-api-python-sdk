<p align="center">
  <a href="https://fingerprint.com">
    <picture>
     <source media="(prefers-color-scheme: dark)" srcset="https://fingerprintjs.github.io/home/resources/logo_light.svg" />
     <source media="(prefers-color-scheme: light)" srcset="https://fingerprintjs.github.io/home/resources/logo_dark.svg" />
     <img src="https://fingerprintjs.github.io/home/resources/logo_dark.svg" alt="Fingerprint logo" width="312px" />
   </picture>
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/fingerprint-pro-server-api-sdk/"><img alt="PyPI" src="https://img.shields.io/pypi/v/fingerprint-pro-server-api-sdk"></a>
  <a href="https://fingerprintjs.github.io/fingerprint-pro-server-api-python-sdk/"><img src="https://fingerprintjs.github.io/fingerprint-pro-server-api-python-sdk/badges.svg" alt="coverage"></a>
  <a href="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/release.yml"><img src="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/release.yml/badge.svg" alt="CI badge" /></a>
  <a href="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/test.yml"><img src="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/test.yml/badge.svg" alt="CI badge" /></a>
  <a href="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/functional_tests.yml"><img src="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/actions/workflows/functional_tests.yml/badge.svg" alt="CI badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/:license-mit-blue.svg?style=flat"/></a>
  <a href="https://discord.gg/39EpE2neBg"><img src="https://img.shields.io/discord/852099967190433792?style=logo&label=Discord&logo=Discord&logoColor=white" alt="Discord server"></a>
</p>

# Fingerprint Pro Server Python SDK

[Fingerprint](https://fingerprint.com) is a device intelligence platform offering 99.5% accurate visitor identification.
The Fingerprint Server Python SDK is an easy way to interact with the Fingerprint [Server API](https://dev.fingerprint.com/reference/pro-server-api) from your Python application. You can retrieve visitor history or individual identification events.


This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3
- Package version: 7.1.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements

The following Python versions are supported:

- Python >= 3.9

## Installation & Usage
### pip install

You can install the package directly from the Github

```sh
pip install git+https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk.git
```

Or from the PyPI

```sh
pip install fingerprint_pro_server_api_sdk
```

Then import the package:
```python
import fingerprint_pro_server_api_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import fingerprint_pro_server_api_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import fingerprint_pro_server_api_sdk

# Configure API key authorization and region
configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
# configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY", region="eu")

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)
```

## Examples

Fetching visits using visitorId:
```python
import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk.rest import ApiException, KnownApiException

configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)

visitor_id = 'visitor_id_example'  # str | Unique [visitor identifier](https://dev.fingerprint.com/docs/js-agent#visitorid) issued by Fingerprint Pro.
#request_id = 'request_id_example'  # str | The unique event [identifier](https://dev.fingerprint.com/docs/js-agent#requestid).
#linked_id = 'linked_id_example'  # str | Filter visits by your custom identifier.   You can use [`linkedId`](https://dev.fingerprint.com/docs/js-agent#linkedid) to associate identification requests with your own identifier, for example: session ID, purchase ID, or transaction ID. You can then use this `linked_id` parameter to retrieve all events associated with your custom identifier.  (optional)
limit = 10  # int | Limit scanned results.   For performance reasons, the API first scans some number of events before filtering them. Use `limit` to specify how many events are scanned before they are filtered by `requestId` or `linkedId`. Results are always returned sorted by the timestamp (most recent first). By default, the most recent 100 visits are scanned, the maximum is 500.  (optional)
#pagination_key = 'pagination_key_example' # str | Use `paginationKey` to get the next page of results.   When more results are available (e.g., you requested 200 results using `limit` parameter, but a total of 600 results are available), the `paginationKey` top-level attribute is added to the response. The key corresponds to the `requestId` of the last returned event. In the following request, use that value in the `paginationKey` parameter to get the next page of results:  1. First request, returning most recent 200 events: `GET api-base-url/visitors/:visitorId?limit=200` 2. Use `response.paginationKey` to get the next page of results: `GET api-base-url/visitors/:visitorId?limit=200&paginationKey=1683900801733.Ogvu1j`  Pagination happens during scanning and before filtering, so you can get less visits than the `limit` you specified with more available on the next page. When there are no more results available for scanning, the `paginationKey` attribute is not returned.  (optional)

try:
    api_response = api_instance.get_visits(visitor_id, limit=2)
    print(api_response)
except KnownApiException as e:
    structured_error = e.structured_error
    print("Error: %s\n" % structured_error.error)
except ApiException as e:
    print("Exception when calling FingerprintApi->visitors_visitor_id_get: %s\n" % e)
```

Delete visits using visitorId:
```python
import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk.rest import ApiException, KnownApiException

configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)

visitor_id = 'visitor_id_example'  # str | Unique [visitor identifier](https://dev.fingerprint.com/docs/js-agent#visitorid) issued by Fingerprint Pro.

try:
    api_instance.delete_visitor_data(visitor_id)
except KnownApiException as e:
    structured_error = e.structured_error
    print("Error: %s\n" % structured_error.error)
except ApiException as e:
    print("Exception when calling FingerprintApi->delete_visitor_data: %s\n" % e)
```

Fetching events for requestId:
```python
import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk.rest import ApiException, KnownApiException

configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)

request_id = 'request_id_example'  # str | The unique event [identifier](https://dev.fingerprint.com/docs/js-agent#requestid).

try:
    events_response = api_instance.get_event(request_id)

except KnownApiException as e:
    structured_error = e.structured_error
    print("Error code: %s. Error message: %s\n" % (structured_error.error.code, structured_error.error.message))
except ApiException as e:
    print("Exception when calling FingerprintApi->get_event: %s\n" % e)
```

Update event for requestId:
```python
import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk import EventUpdateRequest
from fingerprint_pro_server_api_sdk.rest import ApiException, KnownApiException

configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)

request_id = 'request_id_example'  # str | The unique event [identifier](https://dev.fingerprint.com/docs/js-agent#requestid).
body = EventUpdateRequest(linked_id='foo')  # EventUpdateRequest |
# body = EventUpdateRequest(tag={'bar': 123})
# body = EventUpdateRequest(suspect=True)
# body = EventUpdateRequest(linked_id='foo', tag={'bar': 123}, suspect=False)

try:
    api_instance.update_event(request_id, body)
except KnownApiException as e:
    structured_error = e.structured_error
    print("Error code: %s. Error message: %s\n" % (structured_error.error.code, structured_error.error.message))
except ApiException as e:
    print("Exception when calling FingerprintApi->update_event: %s\n" % e)
```

## Sealed results

This SDK provides utility methods for decoding [sealed results](https://dev.fingerprint.com/docs/sealed-client-results).
```python
import base64
import os

from dotenv import load_dotenv

from fingerprint_pro_server_api_sdk import unseal_event_response, DecryptionKey, DecryptionAlgorithm

load_dotenv()

sealed_result = base64.b64decode(os.environ["BASE64_SEALED_RESULT"])
key = base64.b64decode(os.environ["BASE64_KEY"])

try:
    event_response = unseal_event_response(sealed_result, [DecryptionKey(key, DecryptionAlgorithm['Aes256Gcm'])])
    print("\n\n\nEvent response: \n", event_response.products)
except Exception as e:
    print("Exception when calling unsealing events response: %s\n" % e)
    exit(1)

print("Unseal successful!")

exit(0)
```
To learn more, refer to example located in [sealed_results_example.py](sealed_results_example.py).

## Webhook signature validation

This SDK provides utility method for verifying the HMAC signature of the incoming webhook request.
```python
import os
from flask import Flask, request, jsonify
from fingerprint_pro_server_api_sdk import Webhook

app = Flask(__name__)

@app.route('/api/webhook', methods=['POST'])
def webhook_handler():
    try:
        # Retrieve the secret key from environment variables
        secret = os.getenv("WEBHOOK_SIGNATURE_SECRET")
        if not secret:
            return jsonify({"message": "Secret key is not configured."}), 400

        # Get the "fpjs-event-signature" header from the incoming request
        header = request.headers.get('fpjs-event-signature')
        if not header:
            return jsonify({"message": "Missing fpjs-event-signature header."}), 400

        # Read the raw body of the incoming request
        data = request.get_data()

        # Validate the webhook signature
        is_valid = Webhook.is_valid_webhook_signature(header, data, secret)
        if not is_valid:
            return jsonify({"message": "Webhook signature is invalid."}), 403

        # Process the webhook data here
        return jsonify({"message": "Webhook received."}), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```
To learn more, refer to example located in [webhook_signature_example.py](webhook_signature_example.py).

## Documentation for API Endpoints

All URIs are relative to *https://api.fpjs.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FingerprintApi* | [**delete_visitor_data**](docs/FingerprintApi.md#delete_visitor_data) | **DELETE** /visitors/{visitor_id} | Delete data by visitor ID
*FingerprintApi* | [**get_event**](docs/FingerprintApi.md#get_event) | **GET** /events/{request_id} | Get event by request ID
*FingerprintApi* | [**get_visits**](docs/FingerprintApi.md#get_visits) | **GET** /visitors/{visitor_id} | Get visits by visitor ID
*FingerprintApi* | [**update_event**](docs/FingerprintApi.md#update_event) | **PUT** /events/{request_id} | Update an event with a given request ID

## Documentation For Models

 - [ASN](docs/ASN.md)
 - [BotdDetectionResult](docs/BotdDetectionResult.md)
 - [BotdResult](docs/BotdResult.md)
 - [BrowserDetails](docs/BrowserDetails.md)
 - [ClonedAppResult](docs/ClonedAppResult.md)
 - [Common403ErrorResponse](docs/Common403ErrorResponse.md)
 - [Confidence](docs/Confidence.md)
 - [DataCenter](docs/DataCenter.md)
 - [DeprecatedIPLocation](docs/DeprecatedIPLocation.md)
 - [DeprecatedIPLocationCity](docs/DeprecatedIPLocationCity.md)
 - [DeveloperToolsResult](docs/DeveloperToolsResult.md)
 - [EmulatorResult](docs/EmulatorResult.md)
 - [ErrorCommon403Response](docs/ErrorCommon403Response.md)
 - [ErrorCommon429Response](docs/ErrorCommon429Response.md)
 - [ErrorCommon429ResponseError](docs/ErrorCommon429ResponseError.md)
 - [ErrorEvent404Response](docs/ErrorEvent404Response.md)
 - [ErrorEvent404ResponseError](docs/ErrorEvent404ResponseError.md)
 - [ErrorUpdateEvent400Response](docs/ErrorUpdateEvent400Response.md)
 - [ErrorUpdateEvent400ResponseError](docs/ErrorUpdateEvent400ResponseError.md)
 - [ErrorUpdateEvent409Response](docs/ErrorUpdateEvent409Response.md)
 - [ErrorUpdateEvent409ResponseError](docs/ErrorUpdateEvent409ResponseError.md)
 - [ErrorVisitor400Response](docs/ErrorVisitor400Response.md)
 - [ErrorVisitor400ResponseError](docs/ErrorVisitor400ResponseError.md)
 - [ErrorVisitor404Response](docs/ErrorVisitor404Response.md)
 - [ErrorVisitor404ResponseError](docs/ErrorVisitor404ResponseError.md)
 - [ErrorVisits403](docs/ErrorVisits403.md)
 - [EventResponse](docs/EventResponse.md)
 - [EventUpdateRequest](docs/EventUpdateRequest.md)
 - [FactoryResetResult](docs/FactoryResetResult.md)
 - [FridaResult](docs/FridaResult.md)
 - [HighActivityResult](docs/HighActivityResult.md)
 - [IPLocation](docs/IPLocation.md)
 - [IPLocationCity](docs/IPLocationCity.md)
 - [IdentificationError](docs/IdentificationError.md)
 - [IncognitoResult](docs/IncognitoResult.md)
 - [IpBlockListResult](docs/IpBlockListResult.md)
 - [IpBlockListResultDetails](docs/IpBlockListResultDetails.md)
 - [IpInfoResult](docs/IpInfoResult.md)
 - [IpInfoResultV4](docs/IpInfoResultV4.md)
 - [IpInfoResultV6](docs/IpInfoResultV6.md)
 - [JailbrokenResult](docs/JailbrokenResult.md)
 - [Location](docs/Location.md)
 - [LocationSpoofingResult](docs/LocationSpoofingResult.md)
 - [PrivacySettingsResult](docs/PrivacySettingsResult.md)
 - [ProductError](docs/ProductError.md)
 - [ProductsResponse](docs/ProductsResponse.md)
 - [ProductsResponseBotd](docs/ProductsResponseBotd.md)
 - [ProductsResponseIdentification](docs/ProductsResponseIdentification.md)
 - [ProductsResponseIdentificationData](docs/ProductsResponseIdentificationData.md)
 - [ProxyResult](docs/ProxyResult.md)
 - [RawDeviceAttributesResult](docs/RawDeviceAttributesResult.md)
 - [RemoteControlResult](docs/RemoteControlResult.md)
 - [Response](docs/Response.md)
 - [ResponseVisits](docs/ResponseVisits.md)
 - [RootAppsResult](docs/RootAppsResult.md)
 - [SeenAt](docs/SeenAt.md)
 - [SignalResponseClonedApp](docs/SignalResponseClonedApp.md)
 - [SignalResponseDeveloperTools](docs/SignalResponseDeveloperTools.md)
 - [SignalResponseEmulator](docs/SignalResponseEmulator.md)
 - [SignalResponseFactoryReset](docs/SignalResponseFactoryReset.md)
 - [SignalResponseFrida](docs/SignalResponseFrida.md)
 - [SignalResponseHighActivity](docs/SignalResponseHighActivity.md)
 - [SignalResponseIncognito](docs/SignalResponseIncognito.md)
 - [SignalResponseIpBlocklist](docs/SignalResponseIpBlocklist.md)
 - [SignalResponseIpInfo](docs/SignalResponseIpInfo.md)
 - [SignalResponseJailbroken](docs/SignalResponseJailbroken.md)
 - [SignalResponseLocationSpoofing](docs/SignalResponseLocationSpoofing.md)
 - [SignalResponsePrivacySettings](docs/SignalResponsePrivacySettings.md)
 - [SignalResponseProxy](docs/SignalResponseProxy.md)
 - [SignalResponseRawDeviceAttributes](docs/SignalResponseRawDeviceAttributes.md)
 - [SignalResponseRemoteControl](docs/SignalResponseRemoteControl.md)
 - [SignalResponseRootApps](docs/SignalResponseRootApps.md)
 - [SignalResponseSuspectScore](docs/SignalResponseSuspectScore.md)
 - [SignalResponseTampering](docs/SignalResponseTampering.md)
 - [SignalResponseTor](docs/SignalResponseTor.md)
 - [SignalResponseVelocity](docs/SignalResponseVelocity.md)
 - [SignalResponseVirtualMachine](docs/SignalResponseVirtualMachine.md)
 - [SignalResponseVpn](docs/SignalResponseVpn.md)
 - [Subdivision](docs/Subdivision.md)
 - [SuspectScoreResult](docs/SuspectScoreResult.md)
 - [TamperingResult](docs/TamperingResult.md)
 - [TooManyRequestsResponse](docs/TooManyRequestsResponse.md)
 - [TorResult](docs/TorResult.md)
 - [VelocityIntervalResult](docs/VelocityIntervalResult.md)
 - [VelocityIntervals](docs/VelocityIntervals.md)
 - [VelocityResult](docs/VelocityResult.md)
 - [VirtualMachineResult](docs/VirtualMachineResult.md)
 - [VpnResult](docs/VpnResult.md)
 - [VpnResultMethods](docs/VpnResultMethods.md)
 - [WebhookVisit](docs/WebhookVisit.md)

## Documentation For Authorization


## ApiKeyHeader

- **Type**: API key
- **API key parameter name**: Auth-API-Key
- **Location**: HTTP header

## ApiKeyQuery

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Documentation for sealed results

- [SealedResults](docs/SealedResults.md)
- [DecryptionKey](docs/DecryptionKey.md)

## Support

To report problems, ask questions or provide feedback, please use [Issues](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/issues).
If you need private support, you can email us at [oss-support@fingerprint.com](mailto:oss-support@fingerprint.com).

## License

This project is licensed under the [MIT License](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/blob/main/LICENSE).
