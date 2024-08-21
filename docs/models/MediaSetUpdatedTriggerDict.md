# MediaSetUpdatedTriggerDict

Trigger whenever an update is made to a media set on the target
branch. For transactional media sets, this happens when a transaction
is committed. For non-transactional media sets, this event happens
eventually (but not necessary immediately) after an update.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**mediaSetRid** | MediaSetRid | Yes |  |
**branchName** | BranchName | Yes |  |
**type** | Literal["mediaSetUpdated"] | Yes | None |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
