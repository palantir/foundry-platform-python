# ObjectContext

Details of relevant retrieved object instances for a user's message to include as
additional context in the prompt to the Agent.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**object_rids** | List[ObjectRid] | Yes | The RIDs of the relevant object instances to include in the prompt. |
**property_type_rids** | List[PropertyTypeRid] | Yes | The RIDs of the property types for the given objects to include in the prompt. |
**type** | Literal["objectContext"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
