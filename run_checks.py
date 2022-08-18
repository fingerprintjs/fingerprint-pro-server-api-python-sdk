import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk import Response
from fingerprint_pro_server_api_sdk.rest import ApiException
import os

# configure
configuration = fingerprint_pro_server_api_sdk.Configuration(api_key=os.environ["PRIVATE_KEY"], region="us")

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)
visitor_id = os.environ["VISITOR_ID"]

try:
    api_response: Response = api_instance.get_visits(visitor_id, limit=2)
    first_response_last_timestamp = api_response.last_timestamp
    api_response: Response = api_instance.get_visits(visitor_id, limit=2, before=first_response_last_timestamp)
    exit(0)
except ApiException as e:
    print("Exception when calling DefaultApi->visitors_visitor_id_get: %s\n" % e)
    exit(1)




