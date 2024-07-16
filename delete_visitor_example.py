import os

import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk.rest import ApiException

from dotenv import load_dotenv

load_dotenv()
print(os.environ["PRIVATE_KEY"])

# configure
configuration = fingerprint_pro_server_api_sdk.Configuration(
    api_key=os.environ["PRIVATE_KEY"], region=os.environ.get("REGION", "us"))

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)
visitor_id = os.environ["VISITOR_ID_TO_DELETE"]

try:
    api_instance.delete_visitor_data(visitor_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_visitor_data: %s\n" % e)
    exit(1)

print("Visitor data deleted!")

exit(0)
