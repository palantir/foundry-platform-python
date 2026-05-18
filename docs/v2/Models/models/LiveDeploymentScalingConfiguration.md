# LiveDeploymentScalingConfiguration

Autoscaling configuration that controls how the deployment scales replicas based on load thresholds and cooldown delays.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**scale_up_load_threshold** | float | Yes | A threshold between 0.0 and 1.0. If the ratio of running jobs to job capacity exceeds this threshold for the duration of the scale-up delay, the deployment will scale up. Job capacity is the number of running replicas multiplied by the thread count (concurrency limit).  |
**scale_up_delay** | Duration | Yes | The duration that load must exceed the scale-up threshold before scaling up.  |
**scale_down_delay** | Duration | Yes | The duration that load must be below the scale-down threshold before scaling down.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
