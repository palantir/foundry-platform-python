# FilesCountLimitFilter

Only retain `filesCount` number of files in each transaction.
The choice of files to retain is made without any guarantee of order.
This option can increase the reliability of incremental syncs.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**files_count** | pydantic.StrictInt | Yes | The number of files to import in the transaction. The value specified must be positive. |
**type** | Literal["filesCountLimitFilter"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
