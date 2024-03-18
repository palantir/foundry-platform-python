# ActionTypeV2

Represents an action type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | ActionTypeApiName | Yes | The name of the action type in the API. To find the API name for your Action Type, use the `List action types` endpoint or check the **Ontology Manager**.  |
**description** | StrictStr | No | None |
**display_name** | DisplayName | No | The display name of the entity. |
**status** | ReleaseStatus | Yes | The release status of the entity. |
**parameters** | Dict[str, ActionParameterV2] | No | None |
**rid** | ActionTypeRid | Yes | The unique resource identifier of an action type, useful for interacting with other Foundry APIs.  |
**operations** | List[LogicRule] | No | None |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
