# BotdResult
Contains all the information from Bot Detection product


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP address of the requesting browser or bot. | 
**time** | **datetime** | Time in UTC when the request from the JS agent was made. We recommend to treat requests that are older than 2 minutes as malicious. Otherwise, request replay attacks are possible | 
**url** | **str** | Page URL from which identification request was sent. | 
**user_agent** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**bot** | [**BotdDetectionResult**](BotdDetectionResult.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

