# FoundryWorker

The [Foundry worker](https://palantir.com/docs/foundry/data-connection/core-concepts/#foundry-worker) is used to run capabilities 
in Foundry.
This is the preferred method for connections, as these connections benefit from Foundry's containerized 
and scalable job execution, improved stability and do not incur the maintenance overhead associated with agents.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**network_egress_policy_rids** | List[NetworkEgressPolicyRid] | Yes |  |
**type** | Literal["foundryWorker"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
