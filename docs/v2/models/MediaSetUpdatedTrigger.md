# MediaSetUpdatedTrigger

Trigger whenever an update is made to a media set on the target
branch. For transactional media sets, this happens when a transaction
is committed. For non-transactional media sets, this event happens
eventually (but not necessary immediately) after an update.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | Yes |  |
**branch_name** | BranchName | Yes |  |
**type** | Literal["mediaSetUpdated"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
