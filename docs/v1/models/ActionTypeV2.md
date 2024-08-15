# ActionTypeV2

Represents an action type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | ActionTypeApiName | Yes |  |
**description** | Optional[StrictStr] | No |  |
**display_name** | Optional[DisplayName] | No |  |
**status** | ReleaseStatus | Yes |  |
**parameters** | Dict[ParameterId, ActionParameterV2] | Yes |  |
**rid** | ActionTypeRid | Yes |  |
**operations** | List[LogicRule] | Yes |  |


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
