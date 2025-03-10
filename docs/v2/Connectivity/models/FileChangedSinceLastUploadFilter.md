# FileChangedSinceLastUploadFilter

Only import files that have changed or been added since the last import run. Whether or not a file is considered to be changed is determined by the specified file properties.
This will exclude files uploaded in any previous imports, regardless of the file import mode used. A SNAPSHOT file import mode does not reset the filter.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**file_properties** | typing.List[FileProperty] | Yes | The criteria on which to determine whether a file has been changed or not since the last import.  If any of the specified criteria have changed, the file is consider changed. The criteria include:  LAST_MODIFIED: The file's last modified timestamp has changed since the last import. SIZE: The file's size has changed since the last import.  If no criteria are specified, only newly added files will be imported.  |
**type** | typing.Literal["changedSinceLastUploadFilter"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
