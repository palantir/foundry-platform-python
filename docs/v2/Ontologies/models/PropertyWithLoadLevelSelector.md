# PropertyWithLoadLevelSelector

A combination of a property identifier and the load level to apply to the property. You can select a reduced
value for arrays and the main value for structs. If the provided load level cannot be applied to the property
type, then it will be ignored. This selector is experimental and may not work in filters or sorts.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**property_identifier** | PropertyIdentifier | Yes |  |
**load_level** | PropertyLoadLevel | Yes |  |
**type** | Literal["propertyWithLoadLevel"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
