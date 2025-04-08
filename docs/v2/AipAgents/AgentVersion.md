# AgentVersion

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/aipAgents/agents/{agentRid}/agentVersions/{agentVersionString} | Public Beta |
[**list**](#list) | **GET** /v2/aipAgents/agents/{agentRid}/agentVersions | Public Beta |

# **get**
Get version details for an AIP Agent.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/). |  |
**agent_version_string** | AgentVersionString | The semantic version of the Agent, formatted as "majorVersion.minorVersion". |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**AgentVersion**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# AgentVersionString | The semantic version of the Agent, formatted as "majorVersion.minorVersion".
agent_version_string = "1.0"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.aip_agents.Agent.AgentVersion.get(
        agent_rid, agent_version_string, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling AgentVersion.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AgentVersion  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
List all versions for an AIP Agent.
Versions are returned in descending order, by most recent versions first.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/). |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListAgentVersionsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for agent_version in client.aip_agents.Agent.AgentVersion.list(
        agent_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(agent_version)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling AgentVersion.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListAgentVersionsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

