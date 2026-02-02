# FilesVirtualTableConfig

Pointer to the table in cloud object storage (e.g., Azure Data Lake Storage, Google Cloud Storage, S3).

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | FileFormat | Yes |  |
**path** | str | Yes | Storage path for the data in the underlying file system, i.e. paths like `/foo/bar`. The scheme is not  included. May be either a folder or file. A non-partitioned table will have a single location. A  partitioned table can have multiple locations, one for each partition.  |
**type** | Literal["files"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
