# ApplyScenarioLogicRule

An Action rule that merges the edits accumulated on a referenced Scenario into the ontology data context
where the Action is applied. If the Action is applied against another Scenario, the edits are merged into
that target Scenario.

The scenario is supplied through the parameter identified by `scenarioParameter`, whose value type is
`scenarioReference`. The affected object types and link types are explicitly enumerated in the scope.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**scenario_parameter** | ParameterId | Yes |  |
**object_type_api_names** | List[ObjectTypeApiName] | Yes |  |
**link_types** | List[ObjectTypeLinkTypeApiNameMapping] | Yes |  |
**type** | Literal["applyScenario"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
