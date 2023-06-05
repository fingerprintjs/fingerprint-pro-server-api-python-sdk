# WebhookVisit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visitor_id** | **str** |  | 
**client_referrer** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**bot** | [**BotdDetectionResult**](BotdDetectionResult.md) |  | [optional] 
**ip_info** | [**IpInfoResult**](IpInfoResult.md) |  | [optional] 
**incognito** | **bool** | Flag if user used incognito session. | 
**root_apps** | [**WebhookSignalResponseRootApps**](WebhookSignalResponseRootApps.md) |  | [optional] 
**emulator** | [**WebhookSignalResponseEmulator**](WebhookSignalResponseEmulator.md) |  | [optional] 
**ip_blocklist** | [**IpBlockListResult**](IpBlockListResult.md) |  | [optional] 
**tor** | [**WebhookSignalResponseTor**](WebhookSignalResponseTor.md) |  | [optional] 
**vpn** | [**VpnResult**](VpnResult.md) |  | [optional] 
**proxy** | [**WebhookSignalResponseProxy**](WebhookSignalResponseProxy.md) |  | [optional] 
**tampering** | [**TamperingResult**](TamperingResult.md) |  | [optional] 
**request_id** | **str** | Unique identifier of the user's identification request. | 
**browser_details** | [**BrowserDetails**](BrowserDetails.md) |  | 
**ip** | **str** |  | 
**ip_location** | [**IPLocation**](IPLocation.md) |  | [optional] 
**timestamp** | **int** | Timestamp of the event with millisecond precision in Unix time. | 
**time** | **datetime** | Time expressed according to ISO 8601 in UTC format. | 
**url** | **str** | Page URL from which identification request was sent. | 
**tag** | **dict(str, object)** | A customer-provided value or an object that was sent with identification request. | [optional] 
**linked_id** | **str** | A customer-provided id that was sent with identification request. | [optional] 
**confidence** | [**Confidence**](Confidence.md) |  | 
**visitor_found** | **bool** | Attribute represents if a visitor had been identified before. | 
**first_seen_at** | [**SeenAt**](SeenAt.md) |  | 
**last_seen_at** | [**SeenAt**](SeenAt.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

