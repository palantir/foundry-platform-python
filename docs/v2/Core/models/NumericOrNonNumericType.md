# NumericOrNonNumericType

The time series property can either contain either numeric or non-numeric data. This enables mixed sensor types
where some sensor time series are numeric and others are categorical. A boolean property reference can be used
to determine if the series is numeric or non-numeric. Without this property, the series type can be either
numeric or non-numeric and must be inferred from the result of a time series query.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**is_non_numeric_property_type_id** | Optional[str] | No | The boolean property type ID specifying whether the series is numeric or non-numeric. If the value is true, the series is non-numeric.  |
**type** | Literal["numericOrNonNumeric"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
