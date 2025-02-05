# SessionMetadataDict

Metadata for a conversation session with an Agent.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**title** | str | Yes | The title of the session. |
**createdTime** | datetime | Yes | The time the session was created. |
**updatedTime** | datetime | Yes | The time the session was last updated. |
**messageCount** | int | Yes | The count of messages in the session. Includes both user messages and Agent replies, so each complete exchange counts as two messages.  |
**estimatedExpiresTime** | datetime | Yes | The estimated time at which the session is due to expire. Once a session has expired, it can no longer be accessed and a new session must be created. The expiry time is automatically extended when new exchanges are added to the session.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
