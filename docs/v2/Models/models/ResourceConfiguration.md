# ResourceConfiguration

Compute resource configuration for training runs.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**memory** | str | Yes | Memory allocation (e.g., "4G"). |
**cpu** | str | Yes | CPU allocation (e.g., "2"). |
**gpu** | Optional[GpuType] | No | GPU allocation (must be available in the project's resource queue). |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
