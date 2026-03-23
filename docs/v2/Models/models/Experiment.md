# Experiment

Experiment

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ExperimentRid | Yes |  |
**model_rid** | ModelRid | Yes |  |
**created_time** | CreatedTime | Yes |  |
**created_by** | CreatedBy | Yes |  |
**source** | ExperimentSource | Yes |  |
**status** | ExperimentStatus | Yes |  |
**status_message** | Optional[str] | No |  |
**branch** | ExperimentBranch | Yes |  |
**parameters** | List[Parameter] | Yes |  |
**series** | List[SeriesAggregations] | Yes |  |
**summary_metrics** | List[SummaryMetric] | Yes |  |
**artifacts** | Dict[ExperimentArtifactName, ExperimentArtifactMetadata] | Yes |  |
**tags** | List[ExperimentTagText] | Yes |  |
**linked_model_version** | Optional[ModelVersionRid] | No |  |
**job_rid** | Optional[JobRid] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
