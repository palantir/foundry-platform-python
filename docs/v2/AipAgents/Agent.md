# Agent

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**all_sessions**](#all_sessions) | **GET** /v2/aipAgents/agents/allSessions | Public Beta |
[**all_sessions_page**](#all_sessions_page) | **GET** /v2/aipAgents/agents/allSessions | Public Beta |
[**get**](#get) | **GET** /v2/aipAgents/agents/{agentRid} | Public Beta |

# **all_sessions**
List all conversation sessions between the calling user and all accessible Agents that were created by this client.
Sessions are returned in order of most recently updated first.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[Session]**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    for agent in foundry_client.aip_agents.Agent.all_sessions(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(agent)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Agent.all_sessions: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AgentsSessionsPage  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **all_sessions_page**
List all conversation sessions between the calling user and all accessible Agents that were created by this client.
Sessions are returned in order of most recently updated first.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**AgentsSessionsPage**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.aip_agents.Agent.all_sessions_page(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The all_sessions_page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Agent.all_sessions_page: %s\n" % e)

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
**agent_rid** | AgentRid | agentRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |
**version** | Optional[AgentVersionString] | version | [optional] |

### Return type
**Agent**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# AgentRid | agentRid
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# Optional[PreviewMode] | preview
preview = None
# Optional[AgentVersionString] | version
version = None


try:
    api_response = foundry_client.aip_agents.Agent.get(
        agent_rid,
        preview=preview,
        version=version,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Agent.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Agent  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

