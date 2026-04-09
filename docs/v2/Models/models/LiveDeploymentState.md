# LiveDeploymentState

The operational state of a live deployment.

| Value | Description |
| --- | --- |
| ACTIVE | The deployment is active. It may have zero replicas due to autoscaling and still not be ready. |
| STARTING | The deployment is starting up. |
| DEGRADED | At least one replica is ready, but not all replicas are healthy. |
| DISABLED | The deployment is disabled. |
| FAILED | The deployment has failed. No healthy replicas are available. |


| **Value** |
| --------- |
| `"ACTIVE"` |
| `"STARTING"` |
| `"DEGRADED"` |
| `"DISABLED"` |
| `"FAILED"` |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
