# ListScenarioEditedObjectsResponse

The objects that have been edited within a scenario for a given object type.

The Ontology Objects in this response will only ever have the `__primaryKey` and `__apiName`
fields present, thus functioning as object locators rather than full objects.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**data** | List[OntologyObjectV2] | Yes | The list of objects that have been edited within the scenario. |
**next_page_token** | Optional[PageToken] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
