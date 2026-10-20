# MarketplaceInstallationJobStatus

Values:
- **ABORTED**: The draft or running job was aborted. This can happen either via an explicit abort call or from a job submission failure. An aborted draft remains queryable until automatic cleanup, after which it is no longer found. Terminal status.
- **ABORTING**: Cancellation has been requested for the submitted installation job, but it has not yet reached a terminal state. Continue polling.
- **BUILDING**: Resources have been installed and dataset builds are being submitted or awaited. Continue polling.
- **FAILED**: The installation job failed. Terminal.
- **IDLE_DRAFT**: The draft is retained without running an installation job, either by request or because submission was prevented. Further action is required to submit it; polling alone will not advance it.
- **IN_PROGRESS**: The installation job is executing. Continue polling.
- **PREPARING**: The draft is resolving inputs, validating, or being submitted. Continue polling.
- **SUCCEEDED**: The installation job completed successfully. Terminal.

| **Value** |
| --------- |
| `"PREPARING"` |
| `"IDLE_DRAFT"` |
| `"ABORTING"` |
| `"IN_PROGRESS"` |
| `"BUILDING"` |
| `"ABORTED"` |
| `"SUCCEEDED"` |
| `"FAILED"` |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
