# Agent

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**all_sessions**](#all_sessions) | **GET** /v2/aipAgents/agents/allSessions | Public Beta |
[**get**](#get) | **GET** /v2/aipAgents/agents/{agentRid} | Public Beta |

# **all_sessions**
List all conversation sessions between the calling user and all accessible Agents that were created by this client.
Sessions are returned in order of most recently updated first.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | The maximum number of sessions to return in a single page. The maximum allowed value is 100. Defaults to 100 if not specified.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**AgentsSessionsPage**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[PageSize] | The maximum number of sessions to return in a single page. The maximum allowed value is 100. Defaults to 100 if not specified.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for agent in client.aip_agents.Agent.all_sessions(
        page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(agent)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Agent.all_sessions: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AgentsSessionsPage  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get details for an AIP Agent.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/). |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**version** | Optional[AgentVersionString] | The version of the Agent to retrieve. If not specified, the latest published version will be returned.  | [optional] |

### Return type
**Agent**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[AgentVersionString] | The version of the Agent to retrieve. If not specified, the latest published version will be returned.
version = None


try:
    api_response = client.aip_agents.Agent.get(agent_rid, preview=preview, version=version)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Agent.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Agent  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

