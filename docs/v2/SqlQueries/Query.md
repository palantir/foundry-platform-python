# Query

Method | HTTP request |
------------- | ------------- |

Cancels a query. If the query is no longer running this is effectively a no-op.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_id** | QueryId | queryId |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# QueryId | queryId
query_id = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.sql_queries.Query.cancel_query(
        query_id,
        preview=preview,
    )
    print("The cancel_query response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Query.cancel_query: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Executes a new query. Only the user that invoked the query can operate on the query.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query** | str | The SQL query to execute. Queries should confirm to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only.  |  |
**fallback_branch_ids** | Optional[List[BranchName]] | The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**QueryStatus**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# str | The SQL query to execute. Queries should confirm to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only.
query = None
# Optional[List[BranchName]] | The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
fallback_branch_ids = ["master"]
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.sql_queries.Query.execute_query(
        query=query,
        fallback_branch_ids=fallback_branch_ids,
        preview=preview,
    )
    print("The execute_query response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Query.execute_query: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | QueryStatus  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Gets the results of a query. This endpoint implements long polling and requests will time out after
one minute.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_id** | QueryId | queryId |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**bytes**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# QueryId | queryId
query_id = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.sql_queries.Query.get_results(
        query_id,
        preview=preview,
    )
    print("The get_results response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Query.get_results: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Gets the status of a query.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_id** | QueryId | queryId |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**QueryStatus**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# QueryId | queryId
query_id = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.sql_queries.Query.get_status(
        query_id,
        preview=preview,
    )
    print("The get_status response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Query.get_status: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | QueryStatus  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

