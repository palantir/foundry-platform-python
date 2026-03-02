# Query

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**execute**](#execute) | **POST** /v2/functions/queries/{queryApiName}/execute | Private Beta |
[**get**](#get) | **GET** /v2/functions/queries/{queryApiName} | Private Beta |
[**get_by_rid**](#get_by_rid) | **GET** /v2/functions/queries/getByRid | Private Beta |
[**get_by_rid_batch**](#get_by_rid_batch) | **POST** /v2/functions/queries/getByRidBatch | Private Beta |
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
**branch** | Optional[FoundryBranch] | The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**trace_parent** | Optional[TraceParent] |  | [optional] |
**trace_state** | Optional[TraceState] |  | [optional] |
**transaction_id** | Optional[TransactionId] | The ID of a transaction to read from. Transactions are an experimental feature and all workflows may not be supported. | [optional] |
**version** | Optional[FunctionVersion] | The version of the query to execute. When used with `branch`, the specified version must exist on the branch.  | [optional] |

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
# Optional[FoundryBranch] | The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
branch = "ri.branch..branch.d827184f-ee0e-4351-8b70-efbe51e07252"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[TraceParent]
trace_parent = None
# Optional[TraceState]
trace_state = None
# Optional[TransactionId] | The ID of a transaction to read from. Transactions are an experimental feature and all workflows may not be supported.
transaction_id = None
# Optional[FunctionVersion] | The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
version = None


try:
    api_response = client.functions.Query.execute(
        query_api_name,
        parameters=parameters,
        attribution=attribution,
        branch=branch,
        preview=preview,
        trace_parent=trace_parent,
        trace_state=trace_state,
        transaction_id=transaction_id,
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
Gets a specific query type with the given RID. By default, this gets the latest version of the query.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | FunctionRid |  |  |
**include_prerelease** | Optional[bool] | When no version is specified and this flag is set to true, the latest version resolution will consider prerelease versions (e.g., 1.2.3-beta could be returned as the latest). When false, only stable versions are considered when determining the latest version.  Defaults to false.  | [optional] |
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
# Optional[bool] | When no version is specified and this flag is set to true, the latest version resolution will consider prerelease versions (e.g., 1.2.3-beta could be returned as the latest). When false, only stable versions are considered when determining the latest version.  Defaults to false.
include_prerelease = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[FunctionVersion]
version = None


try:
    api_response = client.functions.Query.get_by_rid(
        rid=rid, include_prerelease=include_prerelease, preview=preview, version=version
    )
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

# **get_by_rid_batch**
Gets a list of query types by RID in bulk. By default, this gets the latest version of each query.

Queries are filtered from the response if they don't exist or the requesting token lacks the required 
permissions.

The maximum batch size for this endpoint is 100.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetByRidQueriesBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GetByRidQueriesBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetByRidQueriesBatchRequestElement] | Body of the request
body = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.functions.Query.get_by_rid_batch(body, preview=preview)
    print("The get_by_rid_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Query.get_by_rid_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetByRidQueriesBatchResponse  |  | application/json |

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
**branch** | Optional[FoundryBranch] | The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.  | [optional] |
**ontology** | Optional[OntologyIdentifier] | Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**trace_parent** | Optional[TraceParent] |  | [optional] |
**trace_state** | Optional[TraceState] |  | [optional] |
**transaction_id** | Optional[TransactionId] | The ID of a transaction to read from. Transactions are an experimental feature and all workflows may not be supported. | [optional] |
**version** | Optional[FunctionVersion] | The version of the query to execute. When used with `branch`, the specified version must exist on the branch.  | [optional] |

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
# Optional[FoundryBranch] | The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
branch = "ri.branch..branch.d827184f-ee0e-4351-8b70-efbe51e07252"
# Optional[OntologyIdentifier] | Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
ontology = "example-ontology"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[TraceParent]
trace_parent = None
# Optional[TraceState]
trace_state = None
# Optional[TransactionId] | The ID of a transaction to read from. Transactions are an experimental feature and all workflows may not be supported.
transaction_id = None
# Optional[FunctionVersion] | The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
version = None


try:
    api_response = client.functions.Query.streaming_execute(
        query_api_name,
        parameters=parameters,
        attribution=attribution,
        branch=branch,
        ontology=ontology,
        preview=preview,
        trace_parent=trace_parent,
        trace_state=trace_state,
        transaction_id=transaction_id,
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

