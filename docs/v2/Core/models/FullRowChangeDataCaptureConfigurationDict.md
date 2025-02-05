# FullRowChangeDataCaptureConfigurationDict

Configuration for change data capture which resolves the latest state of the dataset based on new full rows
being pushed to the stream. For example, if a value for a row is updated, it is only sufficient to publish
the entire new state of that row to the stream.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**deletionFieldName** | FieldName | Yes | The name of a boolean field in the schema that indicates whether or not a row has been deleted.  |
**orderingFieldName** | FieldName | Yes | The name of an ordering field that determines the newest state for a row in the dataset.   The ordering field can only be of the following types: - Byte - Date - Decimal - Integer - Long - Short - String - Timestamp  |
**type** | Literal["fullRow"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
