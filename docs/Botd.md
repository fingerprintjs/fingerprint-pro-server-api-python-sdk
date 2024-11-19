# Botd
Contains all the information from Bot Detection product


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot** | [**BotdBot**](BotdBot.md) |  | 
**meta** | [**Tag**](Tag.md) |  | [optional] 
**linked_id** | **str** | A customer-provided id that was sent with the request. | [optional] 
**url** | **str** | Page URL from which the request was sent. | 
**ip** | **str** | IP address of the requesting browser or bot. | 
**time** | **datetime** | Time in UTC when the request from the JS agent was made. We recommend to treat requests that are older than 2 minutes as malicious. Otherwise, request replay attacks are possible. | 
**user_agent** | **str** |  | 
**request_id** | **str** | Unique identifier of the user's request. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

