# ActionTypeV2Dict

Represents an action type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ActionTypeApiName | Yes |  |
**description** | NotRequired[StrictStr] | No |  |
**displayName** | NotRequired[DisplayName] | No |  |
**status** | ReleaseStatus | Yes |  |
**parameters** | Dict[ParameterId, ActionParameterV2Dict] | Yes |  |
**rid** | ActionTypeRid | Yes |  |
**operations** | List[LogicRuleDict] | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
