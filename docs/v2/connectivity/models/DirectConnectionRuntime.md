# DirectConnectionRuntime

[Direct connections](/docs/foundry/data-connection/core-concepts/#direct-connection) enable users to connect
to data sources accessible over the Internet without needing to set up an agent. If your Foundry stack is
hosted on-premises, you can also connect to data sources within your on-premises network.

This is the preferred source connection method if the data source is accessible over the Internet.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**network_egress_policy_rids** | List[NetworkEgressPolicyRid] | Yes | The RIDs of the [network egress policies](/docs/foundry/administration/configure-egress/#network-egress-policies)  configured on the connection. These network egress policies represent the set of external destinations that the connection is allowed to egress to from a Foundry enrollment  |
**type** | Literal["directConnectionRuntime"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
