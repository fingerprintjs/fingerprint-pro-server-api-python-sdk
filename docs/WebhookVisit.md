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
**root_apps** | [**RootAppsResult**](RootAppsResult.md) |  | [optional] 
**emulator** | [**EmulatorResult**](EmulatorResult.md) |  | [optional] 
**cloned_app** | [**ClonedAppResult**](ClonedAppResult.md) |  | [optional] 
**factory_reset** | [**FactoryResetResult**](FactoryResetResult.md) |  | [optional] 
**jailbroken** | [**JailbrokenResult**](JailbrokenResult.md) |  | [optional] 
**frida** | [**FridaResult**](FridaResult.md) |  | [optional] 
**ip_blocklist** | [**IpBlockListResult**](IpBlockListResult.md) |  | [optional] 
**tor** | [**TorResult**](TorResult.md) |  | [optional] 
**privacy_settings** | [**PrivacySettingsResult**](PrivacySettingsResult.md) |  | [optional] 
**virtual_machine** | [**VirtualMachineResult**](VirtualMachineResult.md) |  | [optional] 
**vpn** | [**VpnResult**](VpnResult.md) |  | [optional] 
**proxy** | [**ProxyResult**](ProxyResult.md) |  | [optional] 
**tampering** | [**TamperingResult**](TamperingResult.md) |  | [optional] 
**raw_device_attributes** | [**RawDeviceAttributesResult**](RawDeviceAttributesResult.md) |  | [optional] 
**high_activity** | [**HighActivityResult**](HighActivityResult.md) |  | [optional] 
**location_spoofing** | [**LocationSpoofingResult**](LocationSpoofingResult.md) |  | [optional] 
**suspect_score** | [**SuspectScoreResult**](SuspectScoreResult.md) |  | [optional] 
**remote_control** | [**RemoteControlResult**](RemoteControlResult.md) |  | [optional] 
**velocity** | [**VelocityResult**](VelocityResult.md) |  | [optional] 
**request_id** | **str** | Unique identifier of the user's identification request. | 
**browser_details** | [**BrowserDetails**](BrowserDetails.md) |  | 
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

