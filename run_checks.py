import os

import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk import EventResponse
from fingerprint_pro_server_api_sdk import Response
from fingerprint_pro_server_api_sdk.rest import ApiException

# configure
configuration = fingerprint_pro_server_api_sdk.Configuration(api_key=os.environ["PRIVATE_KEY"], region="us")

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)
visitor_id = os.environ["VISITOR_ID"]
request_id = os.environ["REQUEST_ID"]

try:
    api_response: Response = api_instance.get_visits(visitor_id, limit=2)
    pagination_key = api_response.pagination_key
    api_response: Response = api_instance.get_visits(visitor_id, limit=2, pagination_key=pagination_key)

except ApiException as e:
    print("Exception when calling DefaultApi->visitors_visitor_id_get: %s\n" % e)
    exit(1)

try:
    events_response: EventResponse = api_instance.get_event(request_id)

except ApiException as e:
    print("Exception when calling DefaultApi->get_event: %s\n" % e)
    exit(1)

print("Checks passed!")

exit(0)
