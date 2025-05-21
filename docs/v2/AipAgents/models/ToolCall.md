# ToolCall

A tool call with its input and output.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**tool_metadata** | ToolMetadata | Yes | Details about the tool that was called, including the name and type of the tool.  |
**input** | ToolCallInput | Yes |  |
**output** | Optional[ToolCallOutput] | No | Empty if the tool call is in progress. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
