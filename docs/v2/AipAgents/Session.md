# Session

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**blocking_continue**](#blocking_continue) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/blockingContinue | Public Beta |
[**cancel**](#cancel) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/cancel | Public Beta |
[**create**](#create) | **POST** /v2/aipAgents/agents/{agentRid}/sessions | Public Beta |
[**get**](#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid} | Public Beta |
[**list**](#list) | **GET** /v2/aipAgents/agents/{agentRid}/sessions | Public Beta |
[**rag_context**](#rag_context) | **PUT** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/ragContext | Public Beta |
[**streaming_continue**](#streaming_continue) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/streamingContinue | Public Beta |
[**update_title**](#update_title) | **PUT** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/updateTitle | Public Beta |

# **blocking_continue**
Continue a conversation session with an Agent, or add the first exchange to a session after creation.
Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
Blocks on returning the result of the added exchange until the response is fully generated.
Streamed responses are also supported; see `streamingContinue` for details.
Concurrent requests to continue the same session are not supported.
Clients should wait to receive a response before sending the next message.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/). |  |
**session_rid** | SessionRid | The Resource Identifier (RID) of the conversation session. |  |
**parameter_inputs** | Dict[ParameterId, ParameterValue] | Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.  |  |
**user_input** | UserTextInput | The user message for the Agent to respond to. |  |
**contexts_override** | Optional[List[InputContext]] | If set, automatic [context retrieval](/docs/foundry/agent-studio/retrieval-context/) is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**SessionExchangeResult**

### Example

```python
from foundry_sdk.v2 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# SessionRid | The Resource Identifier (RID) of the conversation session.
session_rid = "ri.aip-agents..session.292db3b2-b653-4de6-971c-7e97a7b881d6"
# Dict[ParameterId, ParameterValue] | Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
parameter_inputs = {
    "currentCustomerOrders": {
        "type": "objectSet",
        "ontology": "example-ontology",
        "objectSet": {
            "type": "filter",
            "objectSet": {"type": "base", "objectType": "customerOrder"},
            "where": {"type": "eq", "field": "customerId", "value": "123abc"},
        },
    }
}
# UserTextInput | The user message for the Agent to respond to.
user_input = {"text": "What is the status of my order?"}
# Optional[List[InputContext]] | If set, automatic [context retrieval](/docs/foundry/agent-studio/retrieval-context/) is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
contexts_override = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.aip_agents.Agent.Session.blocking_continue(
        agent_rid,
        session_rid,
        parameter_inputs=parameter_inputs,
        user_input=user_input,
        contexts_override=contexts_override,
        preview=preview,
    )
    print("The blocking_continue response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Session.blocking_continue: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SessionExchangeResult  | The result of the added exchange for the session.  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **cancel**
Cancel an in-progress streamed exchange with an Agent which was initiated with `streamingContinue`.
Canceling an exchange allows clients to prevent the exchange from being added to the session, or to provide a response to replace the Agent-generated response.
Note that canceling an exchange does not terminate the stream returned by `streamingContinue`; clients should close the stream on triggering the cancellation request to stop reading from the stream.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/). |  |
**session_rid** | SessionRid | The Resource Identifier (RID) of the conversation session. |  |
**message_id** | MessageId | The identifier for the in-progress exchange to cancel. This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**response** | Optional[AgentMarkdownResponse] | When specified, the exchange is added to the session with the client-provided response as the result. When omitted, the exchange is not added to the session.  | [optional] |

### Return type
**CancelSessionResponse**

### Example

```python
from foundry_sdk.v2 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# SessionRid | The Resource Identifier (RID) of the conversation session.
session_rid = "ri.aip-agents..session.292db3b2-b653-4de6-971c-7e97a7b881d6"
# MessageId | The identifier for the in-progress exchange to cancel. This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`.
message_id = "00f8412a-c29d-4063-a417-8052825285a5"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[AgentMarkdownResponse] | When specified, the exchange is added to the session with the client-provided response as the result. When omitted, the exchange is not added to the session.
response = "The status of your order is **In Transit**."


try:
    api_response = foundry_client.aip_agents.Agent.Session.cancel(
        agent_rid, session_rid, message_id=message_id, preview=preview, response=response
    )
    print("The cancel response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Session.cancel: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CancelSessionResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create**
Create a new conversation session between the calling user and an Agent.
Use `blockingContinue` or `streamingContinue` to start adding exchanges to the session.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/). |  |
**agent_version** | Optional[AgentVersionString] | The version of the Agent associated with the session. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Session**

### Example

```python
from foundry_sdk.v2 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# Optional[AgentVersionString] | The version of the Agent associated with the session. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.
agent_version = "1.0"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.aip_agents.Agent.Session.create(
        agent_rid, agent_version=agent_version, preview=preview
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Session.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Session  | The created Session | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the details of a conversation session between the calling user and an Agent.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/). |  |
**session_rid** | SessionRid | The Resource Identifier (RID) of the conversation session. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Session**

### Example

```python
from foundry_sdk.v2 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# SessionRid | The Resource Identifier (RID) of the conversation session.
session_rid = "ri.aip-agents..session.292db3b2-b653-4de6-971c-7e97a7b881d6"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.aip_agents.Agent.Session.get(
        agent_rid, session_rid, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Session.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Session  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
List all conversation sessions between the calling user and an Agent that was created by this client.
This does not list sessions for the user created by other clients.
For example, any sessions created by the user in AIP Agent Studio will not be listed here.
Sessions are returned in order of most recently updated first.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/). |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListSessionsResponse**

### Example

```python
from foundry_sdk.v2 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for session in client.aip_agents.Agent.Session.list(
        agent_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(session)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Session.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListSessionsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **rag_context**
Retrieve relevant [context](/docs/foundry/agent-studio/core-concepts/#retrieval-context) for a user message from the data sources configured for the session.
This allows clients to pre-retrieve context for a user message before sending it to the Agent with the `contextsOverride` option when continuing a session, to allow any pre-processing of the context before sending it to the Agent.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/). |  |
**session_rid** | SessionRid | The Resource Identifier (RID) of the conversation session. |  |
**parameter_inputs** | Dict[ParameterId, ParameterValue] | Any values for [application variables](/docs/foundry/agent-studio/application-state/) to use for the context retrieval.  |  |
**user_input** | UserTextInput | The user message to retrieve relevant context for from the configured Agent data sources. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**AgentSessionRagContextResponse**

### Example

```python
from foundry_sdk.v2 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# SessionRid | The Resource Identifier (RID) of the conversation session.
session_rid = "ri.aip-agents..session.292db3b2-b653-4de6-971c-7e97a7b881d6"
# Dict[ParameterId, ParameterValue] | Any values for [application variables](/docs/foundry/agent-studio/application-state/) to use for the context retrieval.
parameter_inputs = {"customerName": {"type": "string", "value": "Titan Technologies"}}
# UserTextInput | The user message to retrieve relevant context for from the configured Agent data sources.
user_input = {"text": "What is the status of my order?"}
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.aip_agents.Agent.Session.rag_context(
        agent_rid,
        session_rid,
        parameter_inputs=parameter_inputs,
        user_input=user_input,
        preview=preview,
    )
    print("The rag_context response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Session.rag_context: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AgentSessionRagContextResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **streaming_continue**
Continue a conversation session with an Agent, or add the first exchange to a session after creation.
Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
Streamed exchanges also support cancellation; see `cancel` for details.
Concurrent requests to continue the same session are not supported.
Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/). |  |
**session_rid** | SessionRid | The Resource Identifier (RID) of the conversation session. |  |
**parameter_inputs** | Dict[ParameterId, ParameterValue] | Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.  |  |
**user_input** | UserTextInput | The user message for the Agent to respond to. |  |
**contexts_override** | Optional[List[InputContext]] | If set, automatic [context](/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.  | [optional] |
**message_id** | Optional[MessageId] | A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk.v2 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# SessionRid | The Resource Identifier (RID) of the conversation session.
session_rid = "ri.aip-agents..session.292db3b2-b653-4de6-971c-7e97a7b881d6"
# Dict[ParameterId, ParameterValue] | Any supplied values for [application variables](/docs/foundry/agent-studio/application-state/) to pass to the Agent for the exchange.
parameter_inputs = {
    "currentCustomerOrders": {
        "type": "objectSet",
        "ontology": "example-ontology",
        "objectSet": {
            "type": "filter",
            "objectSet": {"type": "base", "objectType": "customerOrder"},
            "where": {"type": "eq", "field": "customerId", "value": "123abc"},
        },
    }
}
# UserTextInput | The user message for the Agent to respond to.
user_input = {"text": "What is the status of my order?"}
# Optional[List[InputContext]] | If set, automatic [context](/docs/foundry/agent-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
contexts_override = None
# Optional[MessageId] | A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete.
message_id = "00f8412a-c29d-4063-a417-8052825285a5"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.aip_agents.Agent.Session.streaming_continue(
        agent_rid,
        session_rid,
        parameter_inputs=parameter_inputs,
        user_input=user_input,
        contexts_override=contexts_override,
        message_id=message_id,
        preview=preview,
    )
    print("The streaming_continue response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Session.streaming_continue: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **update_title**
Update the title for a session.
Use this to set a custom title for a session to help identify it in the list of sessions with an Agent.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**agent_rid** | AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/). |  |
**session_rid** | SessionRid | The Resource Identifier (RID) of the conversation session. |  |
**title** | str | The new title for the session. The maximum title length is 200 characters. Titles are truncated if they exceed this length.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v2 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AgentRid | An RID identifying an AIP Agent created in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).
agent_rid = "ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1"
# SessionRid | The Resource Identifier (RID) of the conversation session.
session_rid = "ri.aip-agents..session.292db3b2-b653-4de6-971c-7e97a7b881d6"
# str | The new title for the session. The maximum title length is 200 characters. Titles are truncated if they exceed this length.
title = "Order status 02/01"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.aip_agents.Agent.Session.update_title(
        agent_rid, session_rid, title=title, preview=preview
    )
    print("The update_title response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Session.update_title: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

