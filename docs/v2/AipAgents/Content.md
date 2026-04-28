# Content

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/content | Public Beta |

# **get**
Get the conversation content for a session between the calling user and an Agent.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an Agent created in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/). |  |
**session_rid** | SessionRid | The Resource Identifier (RID) of the conversation session. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Content**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an Agent created in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# SessionRid | The Resource Identifier (RID) of the conversation session.
session_rid = "ri.aip-agents..session.292db3b2-b653-4de6-971c-7e97a7b881d6"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.aip_agents.Agent.Session.Content.get(
        agent_rid, session_rid, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Content.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Content  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

