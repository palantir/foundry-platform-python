# MarketplaceInstallationJobDetails

Available validation and failure diagnostics for an installation job or draft.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**failure** | Optional[InstallationJobFailure] | No | Diagnostics for a draft preparation or submitted-job execution failure, when available. A draft preparation failure can appear alongside validation. Absence does not mean the job succeeded; for example, an explicitly aborted job may have no failure diagnostics. Check the job's `status` for its outcome. |
**validation** | Optional[InstallationJobValidation] | No | Draft validation results, when available. The draft owner receives the full list of errors; other authorized viewers receive a summary of blocking errors. An empty error list or a summary count of zero is a validation result, not an absence of validation. This field is absent when no draft validation result is available. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
