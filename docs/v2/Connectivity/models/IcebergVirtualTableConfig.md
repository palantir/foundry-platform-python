# IcebergVirtualTableConfig

Pointer to the Iceberg table.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**table_identifier** | str | Yes | The identifier of the Iceberg table. |
**warehouse_path** | Optional[str] | No | The path to the folder in the file system containing the Iceberg table. Can be omitted when the connection is configured with a catalog that does not rely on warehouse path.  |
**type** | Literal["iceberg"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
