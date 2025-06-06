import os
from datetime import datetime, timedelta

import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk.rest import ApiException
from dotenv import load_dotenv

load_dotenv()

# configure
configuration = fingerprint_pro_server_api_sdk.Configuration(
    api_key=os.environ["PRIVATE_KEY"], region=os.environ.get("REGION", "us"))

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)

end = int(datetime.now().timestamp() * 1000)
start = int((datetime.now() - timedelta(days=90)).timestamp() * 1000)


# FingerprintApi->search_events usage example
try:
    search_events_response = api_instance.search_events(2, start=start, end=end)
    if len(search_events_response.events) == 0:
        print("FingerprintApi.search_events: is empty")
        exit(1)
    first_event = search_events_response.events[0]
    first_event_identification_data = first_event.products.identification.data
    visitor_id = first_event_identification_data.visitor_id
    request_id = first_event_identification_data.request_id
    print("\n\n\nSearch events response: \n", search_events_response)
    search_events_response_second_page = api_instance.search_events(2, start=start, end=end, pagination_key=search_events_response.pagination_key)

    if len(search_events_response_second_page.events) == 0:
        print("Second page of FingerprintApi.search_events: is empty")
        exit(1)

except ApiException as e:
    print("Exception when calling FingerprintApi.search_events: %s\n" % e)
    exit(1)

# Use existing visitor_id from FingerprintApi->search_events response to check FingerprintApi->get_visits method
try:
    visits_response = api_instance.get_visits(visitor_id, limit=2)
    print("\n\n\nVisits response: \n", visits_response)

except ApiException as e:
    print("Exception when calling FingerprintApi.get_visits: %s\n" % e)
    exit(1)

# Use existing request_id from FingerprintApi->search_events response to check FingerprintApi->get_event method
try:
    events_response = api_instance.get_event(request_id)
    print("\n\n\nEvent response: \n", events_response.products)

except ApiException as e:
    print("Exception when calling FingerprintApi.get_event: %s\n" % e)
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

# Check that old events are still match expected format
try:
    search_events_response_old = api_instance.search_events(1, start=start, end=end, reverse=True)
    if len(search_events_response_old.events) == 0:
        print("FingerprintApi.search_events: is empty for old events\n")
        exit(1)
    old_event_identification_data = search_events_response_old.events[0].products.identification.data
    visitor_id_old = old_event_identification_data.visitor_id
    request_id_old = old_event_identification_data.request_id

    if visitor_id_old == visitor_id or request_id_old == request_id:
        print("Old events are identical to new\n")
        exit(1)

    api_instance.get_visits(visitor_id_old, limit=2)
    api_instance.get_event(request_id_old)
    print("\n\n\nOld events are good\n")
except ApiException as e:
    print("Exception when trying to read old data: %s\n" % e)

print("Checks passed!")

exit(0)
