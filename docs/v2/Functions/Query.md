# Query

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**execute**](#execute) | **POST** /v2/functions/queries/{queryApiName}/execute | Private Beta |
[**get**](#get) | **GET** /v2/functions/queries/{queryApiName} | Private Beta |
[**get_by_rid**](#get_by_rid) | **POST** /v2/functions/queries/getByRid | Private Beta |

# **execute**
Executes a Query using the given parameters. By default, this executes the latest version of the query.

Optional parameters do not need to be supplied.


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

