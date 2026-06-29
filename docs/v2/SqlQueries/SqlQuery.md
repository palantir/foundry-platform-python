# SqlQuery

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**cancel**](#cancel) | **POST** /v2/sqlQueries/{sqlQueryId}/cancel | Stable |
[**execute**](#execute) | **POST** /v2/sqlQueries/execute | Stable |
[**execute_ontology**](#execute_ontology) | **POST** /v2/sqlQueries/executeOntology | Private Beta |
[**get_results**](#get_results) | **GET** /v2/sqlQueries/{sqlQueryId}/getResults | Stable |
[**get_status**](#get_status) | **GET** /v2/sqlQueries/{sqlQueryId}/getStatus | Stable |

# **cancel**
Cancels a query. If the query is no longer running this is effectively a no-op.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**sql_query_id** | SqlQueryId | The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.  |  |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SqlQueryId | The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.
sql_query_id = None


try:
    api_response = client.sql_queries.SqlQuery.cancel(sql_query_id)
    print("The cancel response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling SqlQuery.cancel: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **execute**
Executes a new query. Only the user that invoked the query can operate on the query. The size of query
results are limited by default to 1 million rows. Contact your Palantir representative to discuss limit
increases.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query** | str | The SQL query to execute. Queries should conform to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only. Datasets can be referenced in SQL queries by path or by RID. See the  [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets) for more details.  |  |
**fallback_branch_ids** | Optional[List[BranchName]] | The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.  | [optional] |
**serialization_format** | Optional[SerializationFormat] | The format used to serialize query results. If not specified, defaults to `ARROW`.  | [optional] |

### Return type
**QueryStatus**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# str | The SQL query to execute. Queries should conform to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only. Datasets can be referenced in SQL queries by path or by RID. See the  [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets) for more details.
query = "SELECT * FROM `/Path/To/Dataset`"
# Optional[List[BranchName]] | The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
fallback_branch_ids = ["master"]
# Optional[SerializationFormat] | The format used to serialize query results. If not specified, defaults to `ARROW`.
serialization_format = "CSV"


try:
    api_response = client.sql_queries.SqlQuery.execute(
        query=query,
        fallback_branch_ids=fallback_branch_ids,
        serialization_format=serialization_format,
    )
    print("The execute response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling SqlQuery.execute: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | QueryStatus  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **execute_ontology**
Executes a SQL query against the Ontology. Results are returned synchronously in
[Apache Arrow](https://arrow.apache.org/) format.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**query** | str | The SQL query to execute.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to execute the query against. If not specified, the default (main) branch is used.  | [optional] |
**dry_run** | Optional[bool] | If true, parse and validate the query without executing it. Defaults to false.  | [optional] |
**parameters** | Optional[Parameters] | Parameters for the SQL query. Can be either unnamed positional parameters or a named parameter mapping.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**row_limit** | Optional[int] | Maximum number of rows to return.  | [optional] |
**scenario_rid** | Optional[ScenarioRid] | The scenario to evaluate the query against. If not specified, no scenario is applied.  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# str | The SQL query to execute.
query = "SELECT * FROM ri.ontology.main.object-type.xxx"
# Optional[FoundryBranch] | The Foundry branch to execute the query against. If not specified, the default (main) branch is used.
branch = "ri.branch..branch.d827184f-ee0e-4351-8b70-efbe51e07252"
# Optional[bool] | If true, parse and validate the query without executing it. Defaults to false.
dry_run = None
# Optional[Parameters] | Parameters for the SQL query. Can be either unnamed positional parameters or a named parameter mapping.
parameters = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[int] | Maximum number of rows to return.
row_limit = None
# Optional[ScenarioRid] | The scenario to evaluate the query against. If not specified, no scenario is applied.
scenario_rid = "ri.actions..scenario.0000-0000"


try:
    api_response = client.sql_queries.SqlQuery.execute_ontology(
        query=query,
        branch=branch,
        dry_run=dry_run,
        parameters=parameters,
        preview=preview,
        row_limit=row_limit,
        scenario_rid=scenario_rid,
    )
    print("The execute_ontology response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling SqlQuery.execute_ontology: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_results**
Gets the results of a query. Results are returned in the `serializationFormat` specified at execute time
(defaulting to [Apache Arrow](https://arrow.apache.org/) if no format is provided).

This endpoint implements long polling and requests will time out after one minute. They can be safely
retried while the query is still running.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**sql_query_id** | SqlQueryId | The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.  |  |

### Return type
**bytes**

> [!TIP]
> This operation returns tabular data that can be converted to data frame formats:
>
> ```python
> # Get data in Arrow format
> table_data = client.sql_queries.SqlQuery.get_results(sql_query_id)
>
> # Convert to a PyArrow Table
> arrow_table = table_data.to_pyarrow()
>
> # Convert to a Pandas DataFrame
> pandas_df = table_data.to_pandas()
>
> # Convert to a Polars DataFrame
> polars_df = table_data.to_polars()
>
> # Convert to a DuckDB relation
> duckdb_relation = table_data.to_duckdb()
> ```
>
> For more details, see the [Data Frames section](../../../README.md#data-frames) in the README.

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SqlQueryId | The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.
sql_query_id = None


try:
    api_response = client.sql_queries.SqlQuery.get_results(sql_query_id)
    print("The get_results response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling SqlQuery.get_results: %s\n" % e)

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
**sql_query_id** | SqlQueryId | The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.  |  |

### Return type
**QueryStatus**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SqlQueryId | The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.
sql_query_id = None


try:
    api_response = client.sql_queries.SqlQuery.get_status(sql_query_id)
    print("The get_status response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling SqlQuery.get_status: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | QueryStatus  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

