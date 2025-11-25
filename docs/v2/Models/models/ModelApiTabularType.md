# ModelApiTabularType

ModelApiTabularType

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**name** | str | Yes |  |
**required** | Optional[bool] | No | true by default; false if the input or output can be null or omitted |
**columns** | List[ModelApiColumn] | Yes |  |
**format** | Optional[ModelApiTabularFormat] | No | Dataframe format the model will receive or is expected to return for this input or output. PANDAS is the default.  |
**type** | Literal["tabular"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
