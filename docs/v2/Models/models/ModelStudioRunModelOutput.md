# ModelStudioRunModelOutput

Resolved model output details for a Model Studio run.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**model_rid** | ModelRid | Yes | The RID of the model. |
**model_version_rid** | ModelVersionRid | Yes | The RID of the model version created by this run. |
**experiment_rid** | Optional[ExperimentRid] | No | The RID of the experiment associated with this run, if any. |
**type** | Literal["model"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
