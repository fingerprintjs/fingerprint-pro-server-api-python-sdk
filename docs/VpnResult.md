# VpnResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | VPN or other anonymizing service has been used when sending the request. | 
**origin_timezone** | **str** | Local timezone which is used in timezoneMismatch method. | 
**origin_country** | **str** | Country of the request (only for Android SDK version >= 2.4.0, ISO 3166 format or unknown). | [optional] 
**methods** | [**VpnResultMethods**](VpnResultMethods.md) |  | 
**confidence** | **str** | A confidence rating for the VPN detection result — \"low\", \"medium\", or \"high\". Depends on the combination of results returned from all VPN detection methods. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

