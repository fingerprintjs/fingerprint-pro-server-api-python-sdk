# ResponseVisits

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique identifier of the user's identification request. | 
**browser_details** | [**BrowserDetails**](BrowserDetails.md) |  | 
**incognito** | **bool** | Flag if user used incognito session. | 
**ip** | **str** |  | 
**ip_location** | [**DeprecatedIPLocation**](DeprecatedIPLocation.md) |  | [optional] 
**timestamp** | **int** | Timestamp of the event with millisecond precision in Unix time. | 
**time** | **datetime** | Time expressed according to ISO 8601 in UTC format. | 
**url** | **str** | Page URL from which the identification request was sent. | 
**tag** | **dict(str, object)** | A customer-provided value or an object that was sent with identification request. | 
**linked_id** | **str** | A customer-provided id that was sent with identification request. | [optional] 
**confidence** | [**Confidence**](Confidence.md) |  | [optional] 
**visitor_found** | **bool** | Attribute represents if a visitor had been identified before. | 
**first_seen_at** | [**SeenAt**](SeenAt.md) |  | 
**last_seen_at** | [**SeenAt**](SeenAt.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

