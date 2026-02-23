# ModelStudioConfigVersion

ModelStudioConfigVersion

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**name** | ModelStudioConfigVersionName | Yes | Human readable name of the configuration version and experiment. |
**version** | ModelStudioConfigVersionNumber | Yes | The version number of this configuration. |
**trainer_id** | TrainerId | Yes | The identifier of the trainer to use for this configuration. |
**trainer** | TrainerVersionLocator | Yes | The trainer and version used for this configuration. |
**worker_config** | ModelStudioWorkerConfig | Yes | The worker configuration including inputs, outputs, and custom settings. |
**resources** | ResourceConfiguration | Yes | The compute resources allocated for training runs. |
**changelog** | Optional[str] | No | Changelog describing changes in this version. |
**created_by** | CreatedBy | Yes |  |
**created_time** | CreatedTime | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
