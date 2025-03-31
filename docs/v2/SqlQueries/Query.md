# Query

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**cancel**](#cancel) | **POST** /v2/sqlQueries/queries/{queryId}/cancel | Private Beta |
[**execute**](#execute) | **POST** /v2/sqlQueries/queries/execute | Private Beta |
[**get_results**](#get_results) | **GET** /v2/sqlQueries/queries/{queryId}/getResults | Private Beta |
[**get_status**](#get_status) | **GET** /v2/sqlQueries/queries/{queryId}/getStatus | Private Beta |

# **cancel**
Cancels a query. If the query is no longer running this is effectively a no-op.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_id** | QueryId | The id of a query.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# QueryId | The id of a query.
query_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.sql_queries.Query.cancel(query_id, preview=preview)
    print("The cancel response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Query.cancel: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **execute**
Executes a new query. Only the user that invoked the query can operate on the query.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query** | str | The SQL query to execute. Queries should confirm to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only.  |  |
**fallback_branch_ids** | Optional[List[BranchName]] | The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**QueryStatus**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# str | The SQL query to execute. Queries should confirm to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only.
query = None
# Optional[List[BranchName]] | The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
fallback_branch_ids = ["master"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.sql_queries.Query.execute(
        query=query, fallback_branch_ids=fallback_branch_ids, preview=preview
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
**200** | QueryStatus  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_results**
Gets the results of a query. This endpoint implements long polling and requests will time out after
one minute.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_id** | QueryId | The id of a query.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**bytes**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# QueryId | The id of a query.
query_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.sql_queries.Query.get_results(query_id, preview=preview)
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

# **get_status**
Gets the status of a query.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query_id** | QueryId | The id of a query.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**QueryStatus**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# QueryId | The id of a query.
query_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.sql_queries.Query.get_status(query_id, preview=preview)
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

