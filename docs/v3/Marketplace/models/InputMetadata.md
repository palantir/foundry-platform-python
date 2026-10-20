# InputMetadata

An input of the target product as it applies to a proposed installation or upgrade.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**input_id** | InputId | Yes |  |
**input_type** | InputType | Yes |  |
**optional** | bool | Yes | Whether the product allows this input to be left unfulfilled. Non-optional inputs may be fulfilled automatically, thus still not requiring manual user intervention. |
**sources** | List[InputSource] | Yes | Available sources to fulfill the value of the input. |
**supported_types** | List[SupportedInputType] | Yes | Accepted representations for supplied values, most preferred first. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
