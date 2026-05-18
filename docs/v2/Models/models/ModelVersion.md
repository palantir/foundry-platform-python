# ModelVersion

ModelVersion

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ModelVersionRid | Yes |  |
**model_api** | ModelApi | Yes |  |
**conda_requirements** | List[str] | Yes |  |
**backing_repositories** | List[RID] | Yes |  |
**created_time** | CreatedTime | Yes |  |
**source** | Optional[ModelVersionSource] | No |  |
**linked_experiment** | Optional[ExperimentRid] | No | The Experiment linked to this Model Version, if one exists. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
