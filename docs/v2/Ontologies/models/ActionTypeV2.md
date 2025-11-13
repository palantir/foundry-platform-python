# ActionTypeV2

Represents an action type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | ActionTypeApiName | Yes |  |
**description** | Optional[str] | No |  |
**display_name** | Optional[DisplayName] | No |  |
**status** | ReleaseStatus | Yes |  |
**parameters** | Dict[ParameterId, ActionParameterV2] | Yes |  |
**rid** | ActionTypeRid | Yes |  |
**operations** | List[LogicRule] | Yes |  |
**tool_description** | Optional[str] | No | Optional description intended for tool use contexts, such as AI agents. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
