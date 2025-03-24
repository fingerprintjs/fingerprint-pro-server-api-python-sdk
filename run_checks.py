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

# FingerprintApi->search_events usage example
try:
    search_events_response = api_instance.search_events(2)
    first_event = search_events_response.events[0]
    first_event_identification_data = first_event.products.identification.data
    visitor_id = first_event_identification_data.visitor_id
    request_id = first_event_identification_data.request_id
    print("\n\n\nSearch events response: \n", search_events_response)
    search_events_response_second_page = api_instance.search_events(2, pagination_key=search_events_response.pagination_key)

    if len(search_events_response_second_page.events) == 0:
        print("Second page of FingerprintApi->search_events: is empty")
        exit(1)

except ApiException as e:
    print("Exception when calling FingerprintApi->search_events: %s\n" % e)
    exit(1)

# Use existing visitor_id from FingerprintApi->search_events response to check FingerprintApi->get_visits method
try:
    visits_response = api_instance.get_visits(visitor_id, limit=2)
    print("\n\n\nVisits response: \n", visits_response)

except ApiException as e:
    print("Exception when calling FingerprintApi->get_visits: %s\n" % e)
    exit(1)

# Use existing request_id from FingerprintApi->search_events response to check FingerprintApi->get_event method
try:
    events_response = api_instance.get_event(request_id)
    print("\n\n\nEvent response: \n", events_response.products)

except ApiException as e:
    print("Exception when calling FingerprintApi->get_event: %s\n" % e)
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
