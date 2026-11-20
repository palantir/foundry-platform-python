# ModelApiTabularType

ModelApiTabularType

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**name** | str | Yes |  |
**description** | Optional[str] | No | Explains the purpose of this tabular input or output. Absent when no description is provided. Descriptions longer than 500 Unicode code points are dropped when the model version is created.  |
**required** | Optional[bool] | No | true by default; false if the input or output can be null or omitted |
**columns** | List[ModelApiColumn] | Yes |  |
**format** | Optional[ModelApiTabularFormat] | No | Dataframe format the model will receive or is expected to return for this input or output. PANDAS is the default.  |
**type** | Literal["tabular"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
