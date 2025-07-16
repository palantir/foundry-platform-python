# DatasetFieldSchema

A field in a Foundry dataset.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**type** | str | Yes |  |
**name** | FieldName | Yes | The name of a column. May be absent in nested schema objects.  |
**nullable** | bool | Yes | Indicates whether values of this field may be null.  |
**user_defined_type_class** | Optional[str] | No | Canonical classname of the user-defined type for this field. This should be a subclass of Spark's `UserDefinedType`.  |
**custom_metadata** | Optional[CustomMetadata] | No | User-supplied custom metadata about the column, such as Foundry web archetypes, descriptions, etc.  |
**array_subtype** | Optional[DatasetFieldSchema] | No | Only used with {@link FieldDataType#ARRAY}.  |
**precision** | Optional[int] | No | Only used with {@link FieldDataType#DECIMAL}.  |
**scale** | Optional[int] | No | Only used with {@link FieldDataType#DECIMAL}.  |
**map_key_type** | Optional[DatasetFieldSchema] | No | Only used with {@link FieldDataType#MAP}.  |
**map_value_type** | Optional[DatasetFieldSchema] | No | Only used with {@link FieldDataType#MAP}.  |
**sub_schemas** | Optional[List[DatasetFieldSchema]] | No | Only used with {@link FieldDataType#STRUCT}.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
