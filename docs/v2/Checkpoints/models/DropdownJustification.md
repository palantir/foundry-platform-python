# DropdownJustification

Checkpoint justification where the user selects one or more options from a dropdown.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**selected_options** | List[DropdownSelection] | Yes | Options the user selected in the dropdown. |
**prompt** | str | Yes | Prompt to which the user-selected options respond. |
**description** | Optional[str] | No | Supplemental information that helps users understand the prompt. |
**title** | str | Yes | Title of the checkpoint to which the user is responding. |
**type** | Literal["dropdownJustification"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
