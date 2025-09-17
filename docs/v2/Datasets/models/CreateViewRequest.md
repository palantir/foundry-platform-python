# CreateViewRequest

CreateViewRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**parent_folder_rid** | FolderRid | Yes |  |
**view_name** | DatasetName | Yes |  |
**backing_datasets** | List[ViewBackingDataset] | Yes |  |
**branch** | Optional[BranchName] | No | The branch name of the View. If not specified, defaults to `master` for most enrollments. |
**primary_key** | Optional[ViewPrimaryKey] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
