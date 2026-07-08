# PropertyTypeMappingInfo

Describes how a single object type property is bound to its backing tabular datasource. A property may be backed
by a single column, by a struct (with nested field mappings), or be edit-only (no backing column even though it
is permissioned to the tabular datasource).


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
StructPropertyMapping | struct
ColumnPropertyMapping | column
EditOnlyPropertyMapping | editOnly


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
