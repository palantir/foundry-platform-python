# FileImportDict

FileImport

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | FileImportRid | Yes |  |
**connectionRid** | ConnectionRid | Yes | The RID of the Connection (formerly known as a source) that the File Import uses to import data. |
**datasetRid** | DatasetRid | Yes | The RID of the output dataset. |
**branchName** | NotRequired[BranchName] | No | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. |
**displayName** | FileImportDisplayName | Yes |  |
**fileImportFilters** | List[FileImportFilterDict] | Yes | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs) |
**importMode** | FileImportMode | Yes |  |
**subfolder** | NotRequired[StrictStr] | No | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
