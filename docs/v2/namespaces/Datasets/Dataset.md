# Dataset

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v2/datasets |
[**get**](#get) | **GET** /v2/datasets/{datasetRid} |
[**read_table**](#read_table) | **GET** /v2/datasets/{datasetRid}/readTable |

# **create**
Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**create_dataset_request** | Union[CreateDatasetRequest, CreateDatasetRequestDict] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Dataset**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[CreateDatasetRequest, CreateDatasetRequestDict] | Body of the request
create_dataset_request = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.datasets.Dataset.create(
        create_dataset_request,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.create: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  | The created Dataset | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **get**
Get the Dataset with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Dataset**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.datasets.Dataset.get(
        dataset_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.get: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **read_table**
Gets the content of a dataset as a table in the specified format.

This endpoint currently does not support views (Virtual datasets composed of other datasets).


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**format** | TableExportFormat | format |  |
**branch_name** | Optional[BranchName] | branchName | [optional] |
**columns** | Optional[List[StrictStr]] | columns | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**row_limit** | Optional[StrictInt] | rowLimit | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | startTransactionRid | [optional] |

### Return type
**bytes**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None

# TableExportFormat | format
format = None

# Optional[BranchName] | branchName
branch_name = None

# Optional[List[StrictStr]] | columns
columns = None

# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None

# Optional[PreviewMode] | preview
preview = None

# Optional[StrictInt] | rowLimit
row_limit = None

# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.read_table(
        dataset_rid,
        format=format,
        branch_name=branch_name,
        columns=columns,
        end_transaction_rid=end_transaction_rid,
        preview=preview,
        row_limit=row_limit,
        start_transaction_rid=start_transaction_rid,
    )
    print("The read_table response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.read_table: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

