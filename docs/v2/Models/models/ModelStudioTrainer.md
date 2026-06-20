# ModelStudioTrainer

ModelStudioTrainer

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**trainer_id** | TrainerId | Yes |  |
**version** | TrainerVersion | Yes | The version of this trainer. |
**name** | TrainerName | Yes | Human-readable name of the trainer. |
**type** | TrainerType | Yes | The category of machine learning task this trainer is designed to solve. |
**description** | TrainerDescription | Yes | Description of what this trainer does and its capabilities. |
**custom_config_schema** | TrainerSchemaDefinition | Yes | JSON schema defining the custom configuration parameters for this trainer. |
**inputs** | TrainerInputsSpecification | Yes | Input specifications for this trainer. |
**outputs** | TrainerOutputsSpecification | Yes | Output specifications for this trainer. |
**experimental** | ModelStudioTrainerExperimental | Yes | Whether this trainer is experimental and may have breaking changes. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
