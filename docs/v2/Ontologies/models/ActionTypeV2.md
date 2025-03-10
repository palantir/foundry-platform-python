# ActionTypeV2

Represents an action type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | ActionTypeApiName | Yes |  |
**description** | typing.Optional[str] | No |  |
**display_name** | typing.Optional[core_models.DisplayName] | No |  |
**status** | core_models.ReleaseStatus | Yes |  |
**parameters** | typing.Dict[ParameterId, ActionParameterV2] | Yes |  |
**rid** | ActionTypeRid | Yes |  |
**operations** | typing.List[LogicRule] | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
