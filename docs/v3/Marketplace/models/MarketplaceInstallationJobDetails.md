# MarketplaceInstallationJobDetails

Available preparation results and execution failure diagnostics for an installation job or draft.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**errors** | Optional[InstallationJobErrors] | No | Preparation results for a draft, or execution failure diagnostics for a submitted job, when available. Draft owners receive the full list of preparation and validation errors; other authorized viewers receive a summary of blocking errors, including failures that prevented preparation from reaching a consistent state.  This field is absent when no result is available, for example, while preparation is still running. Absence does not mean preparation passed validation or the job succeeded. An explicitly aborted job may have no diagnostics. Check the job's `status` for its progress and outcome.  An empty preparation error list means a result is available with no preparation or validation errors. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
