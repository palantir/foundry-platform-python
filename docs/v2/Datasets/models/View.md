# View

View

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**view_name** | DatasetName | Yes |  |
**dataset_rid** | DatasetRid | Yes | The rid of the View. |
**parent_folder_rid** | FolderRid | Yes |  |
**branch** | Optional[BranchName] | No | The branch name of the View. If not specified, defaults to `master` for most enrollments. |
**backing_datasets** | List[ViewBackingDataset] | Yes |  |
**primary_key** | Optional[ViewPrimaryKey] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
