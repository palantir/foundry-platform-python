# ActionTypeDict

Represents an action type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ActionTypeApiName | Yes |  |
**description** | NotRequired[StrictStr] | No |  |
**displayName** | NotRequired[DisplayName] | No |  |
**status** | ReleaseStatus | Yes |  |
**parameters** | Dict[ParameterId, ParameterDict] | Yes |  |
**rid** | ActionTypeRid | Yes |  |
**operations** | List[LogicRuleDict] | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)