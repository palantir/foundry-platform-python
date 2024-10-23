# AgentProxyRuntime

The [agent proxy runtime](/docs/foundry/data-connection/core-concepts/#agent-proxy-runtime) is used to connect
to data sources not accessible over the Internet. The agent acts as an inverting network proxy, forwarding
network traffic originating in Foundry into the network where the agent is deployed, and relaying traffic
back to Foundry. This allows capabilities in Foundry to work almost exactly the same as when using a
direct connection but without requiring you to allow inbound network traffic to your systems originating
from Foundry's IP addresses.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**agent_rids** | List[AgentRid] | Yes | The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection. These agents are used to provide network connectivity to the external systems or APIs configured on the connection.  |
**type** | Literal["agentProxyRuntime"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
