# FileSizeFilter

Only import files whose size is between the specified minimum and maximum values.
At least one of `greaterThan` or `lessThan` should be present.
If both are present, the value specified for `greaterThan` must be strictly less than the value specified for
`lessThan`.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**greater_than** | Optional[SizeBytes] | No | File size must be greater than this number for it to be imported. The value specified cannot be a negative number.  |
**less_than** | Optional[SizeBytes] | No | File size must be less than this number for it to be imported. The value specified must be at least 1 byte.  |
**type** | Literal["fileSizeFilter"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
