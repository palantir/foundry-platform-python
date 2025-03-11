# FileSizeFilterDict

Only import files whose size is between the specified minimum and maximum values.
At least one of `gt` or `lt` should be present.
If both are present, the value specified for `gt` must be strictly less than `lt - 1`.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**gt** | NotRequired[SizeBytes] | No | File size must be greater than this number for it to be imported. The value specified cannot be a negative number.  |
**lt** | NotRequired[SizeBytes] | No | File size must be less than this number for it to be imported. The value specified must be at least 1 byte.  |
**type** | Literal["fileSizeFilter"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
