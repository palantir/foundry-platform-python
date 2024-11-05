# Content

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/content |

# **get**
Get the conversation content for a session between the calling user and an Agent.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | agentRid |  |
**session_rid** | SessionRid | sessionRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Content**

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
# SessionRid | sessionRid
session_rid = "ri.aip-agents..session.292db3b2-b653-4de6-971c-7e97a7b881d6"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.aip_agents.Agent.Session.Content.get(
        agent_rid,
        session_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Content.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Content  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

