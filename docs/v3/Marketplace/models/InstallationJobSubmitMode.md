# InstallationJobSubmitMode

Submit the job after draft preparation and validation if errors fall within the selected tolerance.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**error_handling** | Optional[InstallationJobErrorHandling] | No | If omitted, uses `ABORT`. |
**error_tolerance** | Optional[InstallationJobValidationErrorTolerance] | No | If omitted, uses `NON_BLOCKING_ERRORS`. |
**type** | Literal["submit"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
