# fingerprint_pro_server_api_sdk.FingerprintApi

All URIs are relative to *https://api.fpjs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](FingerprintApi.md#get_event) | **GET** /events/{request_id} | Get event by requestId
[**get_visits**](FingerprintApi.md#get_visits) | **GET** /visitors/{visitor_id} | Get visits by visitorId

# **get_event**
> EventResponse get_event(request_id)

Get event by requestId

This endpoint allows you to get a detailed analysis of an individual request.  **Only for Enterprise customers:** Please note that the response includes mobile signals (e.g. `rootApps`) even if the request orignated from a non-mobile platform. It is highly recommended that you **ignore** the mobile signals for such requests.   Use `requestId` as the URL path parameter. This API method is scoped to a request, i.e. all returned information is by `requestId`. 

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

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The unique [identifier](https://dev.fingerprint.com/docs/js-agent#requestid) of each analysis request. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visits**
> Response get_visits(visitor_id, request_id=request_id, linked_id=linked_id, limit=limit, pagination_key=pagination_key, before=before)

Get visits by visitorId

This endpoint allows you to get a history of visits for a specific `visitorId`. Use the `visitorId` as a URL path parameter. Only information from the _Identification_ product is returned.  #### Headers  * `Retry-After` — Present in case of `429 Too many requests`. Indicates how long you should wait before making a follow-up request. The value is non-negative decimal integer indicating the seconds to delay after the response is received. 

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

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visitor_id** | **str**| Unique identifier of the visitor issued by Fingerprint Pro. | 
 **request_id** | **str**| Filter visits by `requestId`.   Every identification request has a unique identifier associated with it called `requestId`. This identifier is returned to the client in the identification [result](https://dev.fingerprint.com/docs/js-agent#requestid). When you filter visits by `requestId`, only one visit will be returned.  | [optional] 
 **linked_id** | **str**| Filter visits by your custom identifier.   You can use [`linkedId`](https://dev.fingerprint.com/docs/js-agent#linkedid) to associate identification requests with your own identifier, for example: session ID, purchase ID, or transaction ID. You can then use this `linked_id` parameter to retrieve all events associated with your custom identifier.  | [optional] 
 **limit** | **int**| Limit scanned results.   For performance reasons, the API first scans some number of events before filtering them. Use `limit` to specify how many events are scanned before they are filtered by `requestId` or `linkedId`. Results are always returned sorted by the timestamp (most recent first). By default, the most recent 100 visits are scanned, the maximum is 500.  | [optional] 
 **pagination_key** | **str**| Use `paginationKey` to get the next page of results.   When more results are available (e.g., you requested 200 results using `limit` parameter, but a total of 600 results are available), the `paginationKey` top-level attribute is added to the response. The key corresponds to the `requestId` of the last returned event. In the following request, use that value in the `paginationKey` parameter to get the next page of results:  1. First request, returning most recent 200 events: `GET api-base-url/visitors/:visitorId?limit=200` 2. Use `response.paginationKey` to get the next page of results: `GET api-base-url/visitors/:visitorId?limit=200&paginationKey=1683900801733.Ogvu1j`  Pagination happens during scanning and before filtering, so you can get less visits than the `limit` you specified with more available on the next page. When there are no more results available for scanning, the `paginationKey` attribute is not returned.  | [optional] 
 **before** | **int**| ⚠️ Deprecated pagination method, please use `paginationKey` instead. Timestamp (in milliseconds since epoch) used to paginate results.  | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyQuery](../README.md#ApiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

