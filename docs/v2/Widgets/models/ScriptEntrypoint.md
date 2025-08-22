# ScriptEntrypoint

A script entrypoint to be loaded into the runtime environment.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**file_path** | FilePath | Yes | A relative path from the root to a JavaScript entrypoint. It must satisfy:  - Must contain one or more non-empty segments separated by `/`. - Each segment must only contain the following ASCII characters: a-z, A-Z, 0-9 and -_.. - Must have a maximum length of 100.  |
**script_type** | ScriptType | Yes | Defines HTML "type" attribute to be used for the script entrypoint. The supported values are `DEFAULT` and `MODULE`, where `DEFAULT` maps to "text/javascript" and `MODULE` maps to "module".  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
