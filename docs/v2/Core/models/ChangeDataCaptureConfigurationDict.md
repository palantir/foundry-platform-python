# ChangeDataCaptureConfigurationDict

Configuration for utilizing the stream as a change data capture (CDC) dataset. To configure CDC on a stream, at
least one key needs to be provided.

For more information on CDC in
Foundry, see the [Change Data Capture](/docs/foundry/data-integration/change-data-capture/) user documentation.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**deletionFieldName** | FieldName | Yes | The name of a boolean field in the schema that indicates whether or not a row has been deleted.  |
**orderingFieldName** | FieldName | Yes | The name of an ordering field that determines the newest state for a row in the dataset.   The ordering field can only be of the following types: - Byte - Date - Decimal - Integer - Long - Short - String - Timestamp  |
**type** | typing.Literal["fullRow"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
