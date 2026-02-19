# ObjectEditHistoryEntry

Represents a single object edit operation in the history. This captures when an object was
created, modified, or deleted as part of an action execution.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**object_primary_key** | ObjectPrimaryKeyV2 | Yes |  |
**operation_id** | ActionRid | Yes |  |
**action_type_rid** | ActionTypeRid | Yes |  |
**user_id** | str | Yes | The user ID or principal that performed the action |
**timestamp** | datetime | Yes | When this edit occurred (ISO 8601 format) |
**edit** | EditHistoryEdit | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
