# ReauthenticationJustification

Checkpoint justification that requires the user to reauthenticate with the platform.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**reauthentication_id** | UUID | Yes | Identifier for the reauthentication instance. |
**prompt** | str | Yes | Prompt shown to the user during reauthentication. |
**description** | Optional[str] | No | Supplemental information that helps users understand the prompt. |
**title** | str | Yes | Title of the checkpoint that the user is acknowledging. |
**type** | Literal["reauthenticationJustification"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
