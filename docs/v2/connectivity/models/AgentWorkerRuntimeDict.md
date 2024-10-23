# AgentWorkerRuntimeDict

The [agent worker runtime](/docs/foundry/data-connection/core-concepts/#agent-worker-runtime) is used to 
connect to data sources not accessible over the Internet. An agent worker should only be used when the desired 
connector does not support the agent proxy runtime. Agent worker runtimes are associated with a single or 
multiple agents that store the source configuration and credentials locally in an encrypted format, 
and run source capabilities on the agent itself.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**agentRids** | List[AgentRid] | Yes | The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection. These agents are used to provide network connectivity to the external systems or APIs configured on the connection.  |
**type** | Literal["agentWorkerRuntime"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
