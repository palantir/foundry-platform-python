# ActionTypeV2Dict

Represents an action type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ActionTypeApiName | Yes |  |
**description** | typing_extensions.NotRequired[str] | No |  |
**displayName** | typing_extensions.NotRequired[core_models.DisplayName] | No |  |
**status** | core_models.ReleaseStatus | Yes |  |
**parameters** | typing.Dict[ParameterId, ActionParameterV2Dict] | Yes |  |
**rid** | ActionTypeRid | Yes |  |
**operations** | typing.List[LogicRuleDict] | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
