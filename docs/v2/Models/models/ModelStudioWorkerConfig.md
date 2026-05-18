# ModelStudioWorkerConfig

Configuration for the Model Studio worker.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**custom_config** | Optional[Dict[str, Any]] | No | Custom configuration matching the trainer's JSON schema. |
**inputs** | Dict[InputAlias, ModelStudioInput] | Yes | Input configurations keyed by alias. |
**outputs** | Dict[OutputAlias, ModelStudioOutput] | Yes | Output configurations keyed by alias. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
