# CreateFileImportRequest

CreateFileImportRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | Yes | The RID of the output dataset. Can not be modified after the file import is created. |
**import_mode** | FileImportMode | Yes |  |
**display_name** | FileImportDisplayName | Yes |  |
**branch_name** | Optional[BranchName] | No | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. Can not be modified after the file import is created. |
**subfolder** | Optional[str] | No | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system. |
**file_import_filters** | List[FileImportFilter] | Yes | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](https://palantir.com/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs) |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
