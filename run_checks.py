from __future__ import print_function
import swagger_client
from swagger_client import Response
from swagger_client.rest import ApiException
from pprint import pprint
import os

# configure
configuration = swagger_client.Configuration(api_key=os.environ["API_KEY"], region="us")

# create an instance of the API class
api_instance = swagger_client.FingerprintApi(configuration)
visitor_id = 'mcEozNgqhKgmfXx7ZaMW'  # str |
# request_id = 'request_id_example' # str | Filter events by requestId (optional)
# linked_id = 'linked_id_example' # str | Filter events by custom identifier (optional)
# limit = 56 # int | Limit scanned results (optional)
# before = 56 # int | Used to paginate results (optional)

try:
    api_response: Response = api_instance.get_visits(visitor_id, limit=2)
    pprint(api_response.visitor_id)
except ApiException as e:
    print("Exception when calling DefaultApi->visitors_visitor_id_get: %s\n" % e)




