# ActionType

Represents an action type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | ActionTypeApiName | Yes |  |
**description** | Optional[pydantic.StrictStr] | No |  |
**display_name** | Optional[DisplayName] | No |  |
**status** | ReleaseStatus | Yes |  |
**parameters** | Dict[ParameterId, Parameter] | Yes |  |
**rid** | ActionTypeRid | Yes |  |
**operations** | List[LogicRule] | Yes |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
