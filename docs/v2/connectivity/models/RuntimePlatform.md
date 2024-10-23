# RuntimePlatform

[The runtime of a Connection](/docs/foundry/data-connection/core-concepts/#runtimes), which defines the
networking configuration and where capabilities are executed.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
DirectConnectionRuntime | directConnectionRuntime
AgentProxyRuntime | agentProxyRuntime
AgentWorkerRuntime | agentWorkerRuntime


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
