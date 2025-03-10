# Dataset

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/datasets | Stable |
[**get**](#get) | **GET** /v2/datasets/{datasetRid} | Stable |
[**read_table**](#read_table) | **GET** /v2/datasets/{datasetRid}/readTable | Stable |

# **create**
Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**name** | DatasetName |  |  |
**parent_folder_rid** | filesystem_models.FolderRid |  |  |

### Return type
**Dataset**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetName |
name = "My Dataset"
# filesystem_models.FolderRid |
parent_folder_rid = "ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791"


try:
    api_response = foundry_client.datasets.Dataset.create(
        name=name,
        parent_folder_rid=parent_folder_rid,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
**dataset_rid** | DatasetRid | datasetRid |  |

### Return type
**Dataset**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None


try:
    api_response = foundry_client.datasets.Dataset.get(
        dataset_rid,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Dataset.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **read_table**
Gets the content of a dataset as a table in the specified format.

This endpoint currently does not support views (virtual datasets composed of other datasets).


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**format** | TableExportFormat | format |  |
**branch_name** | typing.Optional[BranchName] | branchName | [optional] |
**columns** | typing.Optional[typing.List[str]] | columns | [optional] |
**end_transaction_rid** | typing.Optional[TransactionRid] | endTransactionRid | [optional] |
**row_limit** | typing.Optional[int] | rowLimit | [optional] |
**start_transaction_rid** | typing.Optional[TransactionRid] | startTransactionRid | [optional] |

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

# DatasetRid | datasetRid
dataset_rid = None
# TableExportFormat | format
format = None
# typing.Optional[BranchName] | branchName
branch_name = None
# typing.Optional[typing.List[str]] | columns
columns = ["id", "firstName", "lastName"]
# typing.Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None
# typing.Optional[int] | rowLimit
row_limit = None
# typing.Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.read_table(
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
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Dataset.read_table: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

