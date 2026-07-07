# ObjectTypeRestrictedViewDatasource

An object type datasource backed by a Foundry restricted view.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**restricted_view_rid** | RestrictedViewRid | Yes |  |
**property_mapping** | Dict[PropertyApiName, PropertyTypeMappingInfo] | Yes | A mapping from property API name to a description of how that property is bound to the restricted view. Properties whose mapping info cannot be modeled are omitted.  |
**type** | Literal["restrictedView"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
