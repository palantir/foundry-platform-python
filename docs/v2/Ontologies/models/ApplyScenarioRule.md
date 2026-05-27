# ApplyScenarioRule

An Action rule that applies the edits accumulated on a referenced Scenario onto the ontology data context
where the Action is applied. If the Action is applied in the context of main ontology data, the edits are
applied there. If the Action is applied in the context of another Scenario, the edits are applied in that
other Scenario.

The scenario is supplied through the parameter identified by `scenarioParameter` of type
`scenarioReference`. The affected object types and link types are explicitly enumerated in the scope.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**scenario_parameter** | ParameterId | Yes |  |
**object_type_api_names** | List[ObjectTypeApiName] | Yes |  |
**link_types** | List[ObjectTypeLinkTypeApiNameMapping] | Yes |  |
**type** | Literal["applyScenario"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
