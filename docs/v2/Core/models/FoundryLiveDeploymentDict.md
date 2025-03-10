# FoundryLiveDeploymentDict

FoundryLiveDeployment

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | typing_extensions.NotRequired[core.RID] | No | The live deployment identifier. This rid is of the format 'ri.foundry-ml-live.main.live-deployment.<uuid>'.  |
**inputParamName** | typing_extensions.NotRequired[str] | No | The name of the input parameter to the model which should contain the query string. |
**outputParamName** | typing_extensions.NotRequired[str] | No | The name of the output parameter to the model which should contain the computed embedding. |
**type** | typing.Literal["foundryLiveDeployment"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
