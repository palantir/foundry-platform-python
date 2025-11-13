# Query

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**execute**](#execute) | **POST** /v2/functions/queries/{queryApiName}/execute | Private Beta |
[**get**](#get) | **GET** /v2/functions/queries/{queryApiName} | Private Beta |
[**get_by_rid**](#get_by_rid) | **POST** /v2/functions/queries/getByRid | Private Beta |
[**streaming_execute**](#streaming_execute) | **POST** /v2/functions/queries/{queryApiName}/streamingExecute | Private Beta |

# **execute**
Executes a Query using the given parameters. By default, this executes the latest version of the query.

This endpoint is maintained for backward compatibility only.

For all new implementations, use the `streamingExecute` endpoint, which supports all function types 
and provides enhanced functionality.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_api_name** | QueryApiName |  |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |
**attribution** | Optional[Attribution] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**trace_parent** | Optional[TraceParent] |  | [optional] |
**trace_state** | Optional[TraceState] |  | [optional] |
**version** | Optional[FunctionVersion] |  | [optional] |

### Return type
**ExecuteQueryResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# QueryApiName
query_api_name = None
# Dict[ParameterId, Optional[DataValue]]
parameters = None
# Optional[Attribution]
attribution = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[TraceParent]
trace_parent = None
# Optional[TraceState]
trace_state = None
# Optional[FunctionVersion]
version = None


try:
    api_response = client.functions.Query.execute(
        query_api_name,
        parameters=parameters,
        attribution=attribution,
        preview=preview,
        trace_parent=trace_parent,
        trace_state=trace_state,
        version=version,
    )
    print("The execute response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Query.execute: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ExecuteQueryResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Gets a specific query type with the given API name. By default, this gets the latest version of the query.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_api_name** | QueryApiName |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**version** | Optional[FunctionVersion] |  | [optional] |

### Return type
**Query**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# QueryApiName
query_api_name = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[FunctionVersion]
version = None


try:
    api_response = client.functions.Query.get(query_api_name, preview=preview, version=version)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Query.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Query  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_by_rid**
Gets a specific query type with the given RID.By default, this gets the latest version of the query.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | FunctionRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**version** | Optional[FunctionVersion] |  | [optional] |

### Return type
**Query**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# FunctionRid
rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[FunctionVersion]
version = None


try:
    api_response = client.functions.Query.get_by_rid(rid=rid, preview=preview, version=version)
    print("The get_by_rid response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Query.get_by_rid: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Query  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **streaming_execute**
Executes a Query using the given parameters, returning results as an NDJSON stream. By default, this executes the latest version of the query.

This endpoint supports all Query functions. The endpoint name 'streamingExecute' refers to the NDJSON
streaming response format. Both streaming and non-streaming functions can use this endpoint.
Non-streaming functions return a single-line NDJSON response, while streaming functions return multi-line NDJSON responses.
This is the recommended endpoint for all query execution.

The response is returned as a binary stream in NDJSON (Newline Delimited JSON) format, where each line
is a StreamingExecuteQueryResponse containing either a data batch or an error.

For a function returning a list of 5 records with a batch size of 3, the response stream would contain
two lines. The first line contains the first 3 items, and the second line contains the remaining 2 items:

```
{"type":"data","value":[{"productId":"SKU-001","price":29.99},{"productId":"SKU-002","price":49.99},{"productId":"SKU-003","price":19.99}]}
{"type":"data","value":[{"productId":"SKU-004","price":39.99},{"productId":"SKU-005","price":59.99}]}
```

Each line is a separate JSON object followed by a newline character. Clients should parse the stream
line-by-line to process results as they arrive. If an error occurs during execution, the stream will
contain an error line:

```
{"type":"error","errorCode":"INVALID_ARGUMENT","errorName":"QueryRuntimeError","errorInstanceId":"3f8a9c7b-2e4d-4a1f-9b8c-7d6e5f4a3b2c","errorDescription":"Division by zero","parameters":{}}
```


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_api_name** | QueryApiName |  |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |
**attribution** | Optional[Attribution] |  | [optional] |
**ontology** | Optional[OntologyIdentifier] | Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**trace_parent** | Optional[TraceParent] |  | [optional] |
**trace_state** | Optional[TraceState] |  | [optional] |
**version** | Optional[FunctionVersion] |  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# QueryApiName
query_api_name = None
# Dict[ParameterId, Optional[DataValue]]
parameters = None
# Optional[Attribution]
attribution = None
# Optional[OntologyIdentifier] | Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
ontology = "example-ontology"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[TraceParent]
trace_parent = None
# Optional[TraceState]
trace_state = None
# Optional[FunctionVersion]
version = None


try:
    api_response = client.functions.Query.streaming_execute(
        query_api_name,
        parameters=parameters,
        attribution=attribution,
        ontology=ontology,
        preview=preview,
        trace_parent=trace_parent,
        trace_state=trace_state,
        version=version,
    )
    print("The streaming_execute response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Query.streaming_execute: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

