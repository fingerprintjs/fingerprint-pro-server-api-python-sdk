# fingerprint_pro_server_api_sdk.FingerprintApi

All URIs are relative to *https://api.fpjs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_visits**](FingerprintApi.md#get_visits) | **GET** /visitors/{visitor_id} | 

# **get_visits**
> Response get_visits(visitor_id, request_id=request_id, linked_id=linked_id, limit=limit, before=before)



This endpoint allows you to get a history of visits with all available information. Use the visitorId as a URL path parameter. This API method is scoped to a visitor, i.e. all returned information is by visitorId.

### Example
```python
import fingerprint_pro_server_api_sdk
from fingerprint_pro_server_api_sdk import Response
from fingerprint_pro_server_api_sdk.rest import ApiException

# Configure API key authorization and region
configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
# configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY", region="eu")

# create an instance of the API class
api_instance = fingerprint_pro_server_api_sdk.FingerprintApi(configuration)
visitor_id = 'visitor_id_example'  # str |
#request_id = 'request_id_example'  # str | Filter events by requestId (optional)
#linked_id = 'linked_id_example'  # str | Filter events by custom identifier (optional)
limit = 10  # int | Limit scanned results (optional)
#before = 56  # int | Used to paginate results (optional)

try:
    api_response: Response = api_instance.get_visits(visitor_id, limit=2)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->visitors_visitor_id_get: %s\n" % e)
```

### Parameters

 **visitor_id** | **str**|  | 
 **request_id** | **str**| Filter events by requestId | [optional] 
 **linked_id** | **str**| Filter events by custom identifier | [optional] 
 **limit** | **int**| Limit scanned results | [optional] 
 **before** | **int**| Used to paginate results | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

