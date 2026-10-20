# InstallationJobExecutionFailure

Errors from a submitted installation job.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**errors** | List[ErrorValue] | Yes | Errors recorded during job, integration, and build execution. Each error has an `errorType` parameter containing `kind` (`installJob`, `integration`, or `build`) and, for integration and build errors, `integrationType`. |
**stage** | InstallationJobFailureStage | Yes |  |
**type** | Literal["execution"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
