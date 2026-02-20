# ModelStudioRun

ModelStudioRun

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**run_id** | RunId | Yes | A unique identifier for this run, derived from the studio, config, and build. |
**build_rid** | ModelStudioRunBuildRid | Yes | The RID of the build associated with this run. |
**job_rid** | ModelStudioRunJobRid | Yes | The RID of the job associated with this run. |
**config_version** | ModelStudioConfigVersionNumber | Yes | The configuration version used for this run. |
**started_by** | CreatedBy | Yes | The user who started this run. |
**started_time** | CreatedTime | Yes | When this run was started. |
**resolved_outputs** | Dict[OutputAlias, ModelStudioRunOutput] | Yes | Map of alias to resolved output details (e.g., for models, contains the version RID and experiment). |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
