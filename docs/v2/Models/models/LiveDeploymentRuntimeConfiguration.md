# LiveDeploymentRuntimeConfiguration

The compute resource configuration for a live deployment, controlling replica scaling, CPU, memory, and GPU resources.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**min_replicas** | int | Yes | The minimum number of replicas to keep running. |
**max_replicas** | int | Yes | The maximum number of replicas to scale to under load. |
**cpu** | Optional[float] | No | The number of CPU units requested. This is also set as the limit. |
**memory** | Optional[str] | No | The amount of memory requested in human-readable format (e.g. "256MiB", "1GiB"). This is also set as the limit.  |
**gpu** | Optional[LiveDeploymentGpu] | No | Optional GPU resources for the deployment. |
**thread_count** | Optional[int] | No | The number of threads used for query handling. Defaults to 32 if not specified. Also affects how many concurrent requests will be sent to a single replica.  |
**scaling_configuration** | Optional[LiveDeploymentScalingConfiguration] | No | Autoscaling configuration for the deployment. Controls how the deployment scales replicas up and down based on load.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
