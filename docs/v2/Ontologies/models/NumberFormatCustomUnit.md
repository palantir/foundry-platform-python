# NumberFormatCustomUnit

Format numbers with custom units not supported by standard formatting.
Use this for domain-specific units like "requests/sec", "widgets", etc.
Example: 1500 with unit "widgets" displays as "1,500 widgets"


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**base_format_options** | NumberFormatOptions | Yes |  |
**unit** | PropertyTypeReferenceOrStringConstant | Yes |  |
**type** | Literal["customUnit"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
