# ListScenarioEditedEntityTypesResponse

The object types and link types that have been modified within a scenario.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**object_types** | List[ObjectTypeApiName] | Yes | The list of object type API names that have been modified within the scenario. |
**link_types** | List[ObjectTypeLinkTypeApiNameMapping] | Yes | The list of edited link types grouped by source object type.  Note that only many-to-many link types are returned. One-to-many link type edits are surfaced as object edits on the object type that owns the foreign key property.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
