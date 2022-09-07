import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk import Response
from fingerprint_pro_server_api_sdk import EventResponse
from fingerprint_pro_server_api_sdk.rest import ApiException
from fingerprint_pro_server_api_sdk import ProductsResponse
import os

# configure
configuration = fingerprint_pro_server_api_sdk.Configuration(api_key=os.environ["PRIVATE_KEY"], region="us")

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)
visitor_id = os.environ["VISITOR_ID"]
request_id = os.environ["REQUEST_ID"]

try:
    api_response: Response = api_instance.get_visits(visitor_id, limit=2)
    first_response_last_timestamp = api_response.last_timestamp
    api_response: Response = api_instance.get_visits(visitor_id, limit=2, before=first_response_last_timestamp)

except ApiException as e:
    print("Exception when calling DefaultApi->visitors_visitor_id_get: %s\n" % e)
    exit(1)


try:
    events_response: EventResponse = api_instance.get_event(request_id)

except ApiException as e:
    print("Exception when calling DefaultApi->get_event: %s\n" % e)
    exit(1)

exit(0)