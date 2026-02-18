# Dataset

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/datasets | Stable |
[**get**](#get) | **GET** /v2/datasets/{datasetRid} | Stable |
[**get_health_check_reports**](#get_health_check_reports) | **GET** /v2/datasets/{datasetRid}/getHealthCheckReports | Public Beta |
[**get_health_checks**](#get_health_checks) | **GET** /v2/datasets/{datasetRid}/getHealthChecks | Public Beta |
[**get_schedules**](#get_schedules) | **GET** /v2/datasets/{datasetRid}/getSchedules | Public Beta |
[**get_schema**](#get_schema) | **GET** /v2/datasets/{datasetRid}/getSchema | Public Beta |
[**get_schema_batch**](#get_schema_batch) | **POST** /v2/datasets/getSchemaBatch | Public Beta |
[**jobs**](#jobs) | **POST** /v2/datasets/{datasetRid}/jobs | Public Beta |
[**put_schema**](#put_schema) | **PUT** /v2/datasets/{datasetRid}/putSchema | Public Beta |
[**read_table**](#read_table) | **GET** /v2/datasets/{datasetRid}/readTable | Stable |
[**transactions**](#transactions) | **GET** /v2/datasets/{datasetRid}/transactions | Public Beta |

# **create**
Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**name** | DatasetName |  |  |
**parent_folder_rid** | FolderRid |  |  |

### Return type
**Dataset**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetName
name = "My Dataset"
# FolderRid
parent_folder_rid = "ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791"


try:
    api_response = client.datasets.Dataset.create(name=name, parent_folder_rid=parent_folder_rid)
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  | The created Dataset | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Dataset with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |

### Return type
**Dataset**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None


try:
    api_response = client.datasets.Dataset.get(dataset_rid)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_health_check_reports**
Get the most recent Data Health Check report for each check configured on the given Dataset.
Returns one report per check, representing the current health status of the dataset.

To get the list of checks configured on a Dataset, use
[Get Dataset Health Checks](https://palantir.com/docs/foundry/api/datasets/get-dataset-health-checks/).
For the full report history of a specific check, use
[Get Latest Check Reports](https://palantir.com/docs/foundry/api/v2/data-health-v2-resources/checks/get-latest-check-reports).


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GetHealthCheckReportsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# Optional[BranchName] | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.
branch_name = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.datasets.Dataset.get_health_check_reports(
        dataset_rid, branch_name=branch_name, preview=preview
    )
    print("The get_health_check_reports response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.get_health_check_reports: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetHealthCheckReportsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_health_checks**
Get the RIDs of the Data Health Checks that are configured for the given Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListHealthChecksResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# Optional[BranchName] | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.
branch_name = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.datasets.Dataset.get_health_checks(
        dataset_rid, branch_name=branch_name, preview=preview
    )
    print("The get_health_checks response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.get_health_checks: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListHealthChecksResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_schedules**
Get the RIDs of the Schedules that target the given Dataset


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListSchedulesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# Optional[BranchName] | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.
branch_name = None
# Optional[PageSize]
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for dataset in client.datasets.Dataset.get_schedules(
        dataset_rid,
        branch_name=branch_name,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(dataset)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.get_schedules: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListSchedulesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_schema**
Gets a dataset's schema. If no `endTransactionRid` is provided, the latest committed version will be used.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**branch_name** | Optional[BranchName] |  | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction. If a user does not provide a value, the RID of the latest committed transaction will be used.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**version_id** | Optional[VersionId] | The schema version that should be used. If none is provided, the latest version will be used.  | [optional] |

### Return type
**GetDatasetSchemaResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# Optional[BranchName]
branch_name = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction. If a user does not provide a value, the RID of the latest committed transaction will be used.
end_transaction_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[VersionId] | The schema version that should be used. If none is provided, the latest version will be used.
version_id = None


try:
    api_response = client.datasets.Dataset.get_schema(
        dataset_rid,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        preview=preview,
        version_id=version_id,
    )
    print("The get_schema response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.get_schema: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetDatasetSchemaResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_schema_batch**
Fetch schemas for multiple datasets in a single request. Datasets not found 
or inaccessible to the user will be omitted from the response.


The maximum batch size for this endpoint is 1000.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetSchemaDatasetsBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GetSchemaDatasetsBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetSchemaDatasetsBatchRequestElement] | Body of the request
body = [
    {
        "endTransactionRid": "ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4",
        "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
        "versionId": "0000000d-2acf-537c-a228-3a9fe3cdc523",
        "branchName": "master",
    }
]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.datasets.Dataset.get_schema_batch(body, preview=preview)
    print("The get_schema_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.get_schema_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetSchemaDatasetsBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **jobs**
Get the RIDs of the Jobs for the given dataset. By default, returned Jobs are sorted in descending order by the Job start time.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**order_by** | List[GetDatasetJobsSort] |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.  | [optional] |
**page_size** | Optional[PageSize] | Max number of results to return. A limit of 1000 on if no limit is supplied in the search request  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**where** | Optional[GetDatasetJobsQuery] |  | [optional] |

### Return type
**GetJobResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# List[GetDatasetJobsSort]
order_by = [{"sortType": "BY_STARTED_TIME", "sortDirection": "DESCENDING"}]
# Optional[BranchName] | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.
branch_name = None
# Optional[PageSize] | Max number of results to return. A limit of 1000 on if no limit is supplied in the search request
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[GetDatasetJobsQuery]
where = {
    "type": "timeFilter",
    "field": "SUBMITTED_TIME",
    "comparisonType": "GTE",
    "value": "2020-09-30T14:30:00Z",
}


try:
    for dataset in client.datasets.Dataset.jobs(
        dataset_rid,
        order_by=order_by,
        branch_name=branch_name,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        where=where,
    ):
        pprint(dataset)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.jobs: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetJobResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **put_schema**
Adds a schema on an existing dataset using a PUT request.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**schema** | DatasetSchema | The schema that will be added.  |  |
**branch_name** | Optional[BranchName] |  | [optional] |
**dataframe_reader** | Optional[DataframeReader] | The dataframe reader used for reading the dataset schema. Defaults to PARQUET. | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GetDatasetSchemaResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# DatasetSchema | The schema that will be added.
schema = {
    "fieldSchemaList": [
        {
            "name": "id",
            "type": "LONG",
            "nullable": False,
            "customMetadata": {"description": "Primary key"},
        },
        {"name": "event_time", "type": "TIMESTAMP", "nullable": False},
        {"name": "price", "type": "DECIMAL", "precision": 10, "scale": 2, "nullable": True},
        {
            "name": "tags",
            "type": "ARRAY",
            "nullable": True,
            "arraySubtype": {"type": "STRING", "nullable": False},
        },
        {
            "name": "metrics",
            "type": "STRUCT",
            "nullable": True,
            "subSchemas": [
                {"name": "temperature", "type": "DOUBLE", "nullable": True},
                {"name": "humidity", "type": "DOUBLE", "nullable": True},
            ],
        },
    ]
}
# Optional[BranchName]
branch_name = "master"
# Optional[DataframeReader] | The dataframe reader used for reading the dataset schema. Defaults to PARQUET.
dataframe_reader = "PARQUET"
# Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.
end_transaction_rid = "ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.datasets.Dataset.put_schema(
        dataset_rid,
        schema=schema,
        branch_name=branch_name,
        dataframe_reader=dataframe_reader,
        end_transaction_rid=end_transaction_rid,
        preview=preview,
    )
    print("The put_schema response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.put_schema: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetDatasetSchemaResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **read_table**
Gets the content of a dataset as a table in the specified format.

This endpoint currently does not support views (virtual datasets composed of other datasets).


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**format** | TableExportFormat | The export format. Must be `ARROW` or `CSV`.  |  |
**branch_name** | Optional[BranchName] | The name of the Branch.  | [optional] |
**columns** | Optional[List[str]] | A subset of the dataset columns to include in the result. Defaults to all columns.  | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.  | [optional] |
**row_limit** | Optional[int] | A limit on the number of rows to return. Note that row ordering is non-deterministic.  | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.  | [optional] |

### Return type
**bytes**

> [!TIP]
> This operation returns tabular data that can be converted to data frame formats:
>
> ```python
> # Get data in Arrow format
> table_data = client.datasets.Dataset.read_table(dataset_rid, format=format, branch_name=branch_name, columns=columns, end_transaction_rid=end_transaction_rid, row_limit=row_limit, start_transaction_rid=start_transaction_rid)
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

# DatasetRid
dataset_rid = None
# TableExportFormat | The export format. Must be `ARROW` or `CSV`.
format = None
# Optional[BranchName] | The name of the Branch.
branch_name = None
# Optional[List[str]] | A subset of the dataset columns to include in the result. Defaults to all columns.
columns = ["id", "firstName", "lastName"]
# Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.
end_transaction_rid = None
# Optional[int] | A limit on the number of rows to return. Note that row ordering is non-deterministic.
row_limit = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.
start_transaction_rid = None


try:
    api_response = client.datasets.Dataset.read_table(
        dataset_rid,
        format=format,
        branch_name=branch_name,
        columns=columns,
        end_transaction_rid=end_transaction_rid,
        row_limit=row_limit,
        start_transaction_rid=start_transaction_rid,
    )
    print("The read_table response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.read_table: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **transactions**
Get the Transaction history for the given Dataset. When requesting all transactions, the endpoint returns them in reverse chronological order.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListTransactionsOfDatasetResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for dataset in client.datasets.Dataset.transactions(
        dataset_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(dataset)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Dataset.transactions: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListTransactionsOfDatasetResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

