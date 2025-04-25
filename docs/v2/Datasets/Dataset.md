# Dataset

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/datasets | Stable |
[**get**](#get) | **GET** /v2/datasets/{datasetRid} | Stable |
[**get_schedules**](#get_schedules) | **GET** /v2/datasets/{datasetRid}/getSchedules | Public Beta |
[**read_table**](#read_table) | **GET** /v2/datasets/{datasetRid}/readTable | Stable |

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

