# IPLocation
This field is **deprecated** and will not return a result for **accounts created after December 18th, 2023**. Please use the [`ipInfo` Smart signal](https://dev.fingerprint.com/docs/smart-signals-overview#ip-geolocation) for geolocation information.


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accuracy_radius** | **int** | The IP address is likely to be within this radius (in km) of the specified location. | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**city** | [**IPLocationCity**](IPLocationCity.md) |  | [optional] 
**country** | [**Location**](Location.md) |  | [optional] 
**continent** | [**Location**](Location.md) |  | [optional] 
**subdivisions** | [**list[Subdivision]**](Subdivision.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

