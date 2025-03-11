# CreateStreamRequestStreamSchemaDict

CreateStreamRequestStreamSchema

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**keyFieldNames** | NotRequired[List[FieldName]] | No | The names of the fields to be used as keys for partitioning records. These key fields are used to group all records with the same key into the same partition, to guarantee processing order of grouped records. These keys are not meant to uniquely identify records, and do not by themselves deduplicate records. To deduplicate records, provide a change data capture configuration for the schema.  Key fields can only be of the following types: - Boolean - Byte - Date - Decimal - Integer - Long - Short - String - Timestamp  For additional information on keys for Foundry streams, see the [streaming keys](/docs/foundry/building-pipelines/streaming-keys/) user documentation.  |
**fields** | List[FieldDict] | Yes |  |
**changeDataCapture** | NotRequired[ChangeDataCaptureConfigurationDict] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
