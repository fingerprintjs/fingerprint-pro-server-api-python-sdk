# Identification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visitor_id** | **str** | String of 20 characters that uniquely identifies the visitor's browser or mobile device. | 
**request_id** | **str** | Unique identifier of the user's request. | 
**browser_details** | [**BrowserDetails**](BrowserDetails.md) |  | 
**incognito** | **bool** | Flag if user used incognito session. | 
**ip** | **str** | IP address of the requesting browser or bot. | 
**ip_location** | [**DeprecatedGeolocation**](DeprecatedGeolocation.md) |  | [optional] 
**linked_id** | **str** | A customer-provided id that was sent with the request. | [optional] 
**suspect** | **bool** | Field is `true` if you have previously set the `suspect` flag for this event using the [Server API Update event endpoint](https://dev.fingerprint.com/reference/updateevent). | [optional] 
**timestamp** | **int** | Timestamp of the event with millisecond precision in Unix time. | 
**time** | **datetime** | Time expressed according to ISO 8601 in UTC format, when the request from the JS agent was made. We recommend to treat requests that are older than 2 minutes as malicious. Otherwise, request replay attacks are possible. | 
**url** | **str** | Page URL from which the request was sent. | 
**tag** | [**Tag**](Tag.md) |  | 
**confidence** | [**IdentificationConfidence**](IdentificationConfidence.md) |  | [optional] 
**visitor_found** | **bool** | Attribute represents if a visitor had been identified before. | 
**first_seen_at** | [**IdentificationSeenAt**](IdentificationSeenAt.md) |  | 
**last_seen_at** | [**IdentificationSeenAt**](IdentificationSeenAt.md) |  | 
**components** | [**RawDeviceAttributes**](RawDeviceAttributes.md) |  | [optional] 
**replayed** | **bool** | `true` if we determined that this payload was replayed, `false` otherwise.  | 
**sdk** | [**SDK**](SDK.md) |  | [optional] 
**environment_id** | **str** | Environment ID associated with the event | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

