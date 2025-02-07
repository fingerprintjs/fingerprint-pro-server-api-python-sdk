import os

import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk.rest import ApiException
from dotenv import load_dotenv

load_dotenv()

# configure
configuration = fingerprint_pro_server_api_sdk.Configuration(
    api_key=os.environ["PRIVATE_KEY"], region=os.environ.get("REGION", "us"))

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)
visitor_id = os.environ["VISITOR_ID"]
request_id = os.environ["REQUEST_ID"]

try:
    visits_response = api_instance.get_visits(visitor_id, limit=2)
    pagination_key = visits_response.pagination_key
    print("\n\n\nVisits response: \n", visits_response)

    visits_response = api_instance.get_visits(
        visitor_id, limit=2, pagination_key=pagination_key)

except ApiException as e:
    print("Exception when calling DefaultApi->visitors_visitor_id_get: %s\n" % e)
    exit(1)

try:
    events_response = api_instance.get_event(request_id)
    print("\n\n\nEvent response: \n", events_response.products)

except ApiException as e:
    print("Exception when calling DefaultApi->get_event: %s\n" % e)
    exit(1)

try:
    search_events_response = api_instance.search_events(2, bot="bad")
    print("\n\n\nSearch events response: \n", search_events_response)

except ApiException as e:
    print("Exception when calling DefaultApi->search_events: %s\n" % e)
    exit(1)

# Async methods examples
try:
    visits_response_request = api_instance.get_visits(visitor_id, limit=2, async_req=True)
    events_response_request = api_instance.get_event(request_id, async_req=True)
    visits_response = visits_response_request.get()
    print("\n\n\nVisits async response: \n", visits_response)
    events_response = events_response_request.get()
    print("\n\n\nEvent async response: \n", events_response.products)
except ApiException as e:
    print("Exception when calling Async example: %s\n" % e)
    exit(1)

print("Checks passed!")

exit(0)
