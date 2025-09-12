# PrimaryKeyResolutionDuplicate

Duplicate primary key values may exist within the dataset – resolution required.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**deletion_column** | Optional[str] | No | The name of the boolean column that indicates whether a row should be considered deleted. Based on the `resolutionStrategy`, if the final row selected for a given primary key has `true` in this column, that row will be excluded from the results. Otherwise, it will be included.  |
**resolution_strategy** | PrimaryKeyResolutionStrategy | Yes |  |
**type** | Literal["duplicate"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
