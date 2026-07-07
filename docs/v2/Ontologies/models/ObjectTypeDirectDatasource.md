# ObjectTypeDirectDatasource

An object type datasource backed by a direct-write source. Property values are written directly to the
datasource rather than being read from a separate Foundry resource. Unlike an edits-only datasource, a direct
datasource has a backing source that values are written to by some writer. An edits-only datasource has no
backing source at all and its properties are populated solely via Actions.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**direct_source_rid** | DirectSourceRid | Yes |  |
**property_mapping** | Dict[PropertyApiName, PropertyTypeMappingInfo] | Yes | A mapping from property API name to a description of how that property is bound to the direct datasource. Properties whose mapping info cannot be modeled are omitted.  |
**type** | Literal["direct"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
