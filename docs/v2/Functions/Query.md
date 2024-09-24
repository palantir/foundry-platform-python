# Query

Method | HTTP request |
------------- | ------------- |

Executes a Query using the given parameters.

Optional parameters do not need to be supplied.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_api_name** | QueryApiName | queryApiName |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ExecuteQueryResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# QueryApiName | queryApiName
query_api_name = None
# Dict[ParameterId, Optional[DataValue]] |
parameters = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.functions.Query.execute(
        query_api_name,
        parameters=parameters,
        preview=preview,
    )
    print("The execute response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Query.execute: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ExecuteQueryResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Gets a specific query type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_api_name** | QueryApiName | queryApiName |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Query**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# QueryApiName | queryApiName
query_api_name = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.functions.Query.get(
        query_api_name,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Query.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Query  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Gets a specific query type with the given RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | FunctionRid |  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Query**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# FunctionRid |
rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.functions.Query.get_by_rid(
        rid=rid,
        preview=preview,
    )
    print("The get_by_rid response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Query.get_by_rid: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Query  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

