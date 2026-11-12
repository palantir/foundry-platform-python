# ModelApiColumn

ModelApiColumn

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**name** | str | Yes |  |
**description** | Optional[str] | No | Explains the meaning of the values in this column. Absent when no description is provided. Descriptions longer than 500 Unicode code points are dropped when the model version is created.  |
**required** | Optional[bool] | No | true by default; false if the column can be null or omitted |
**data_type** | ModelApiDataType | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
