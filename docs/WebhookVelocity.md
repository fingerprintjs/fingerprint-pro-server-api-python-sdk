# WebhookVelocity
Sums key data points for a specific `visitorId`, `ipAddress` and `linkedId` at three distinct time intervals: 5 minutes, 1 hour, and 24 hours as follows:   - Number of distinct IP addresses associated to the visitor ID. - Number of distinct linked IDs associated with the visitor ID. - Number of distinct countries associated with the visitor ID. - Number of identification events associated with the visitor ID. - Number of identification events associated with the detected IP address. - Number of distinct IP addresses associated with the provided linked ID. - Number of distinct visitor IDs associated with the provided linked ID.  The `24h` interval of `distinctIp`, `distinctLinkedId`, `distinctCountry`, `distinctIpByLinkedId` and `distinctVisitorIdByLinkedId` will be omitted  if the number of `events` for the visitor ID in the last 24 hours (`events.intervals.['24h']`) is higher than 20.000. 


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinct_ip** | [**VelocityData**](VelocityData.md) |  | [optional] 
**distinct_linked_id** | [**VelocityData**](VelocityData.md) |  | [optional] 
**distinct_country** | [**VelocityData**](VelocityData.md) |  | [optional] 
**events** | [**VelocityData**](VelocityData.md) |  | [optional] 
**ip_events** | [**VelocityData**](VelocityData.md) |  | [optional] 
**distinct_ip_by_linked_id** | [**VelocityData**](VelocityData.md) |  | [optional] 
**distinct_visitor_id_by_linked_id** | [**VelocityData**](VelocityData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

