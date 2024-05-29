# Dataset

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v1/datasets |
[**delete_schema**](#delete_schema) | **DELETE** /v1/datasets/{datasetRid}/schema |
[**get**](#get) | **GET** /v1/datasets/{datasetRid} |
[**get_schema**](#get_schema) | **GET** /v1/datasets/{datasetRid}/schema |
[**read**](#read) | **GET** /v1/datasets/{datasetRid}/readTable |
[**replace_schema**](#replace_schema) | **PUT** /v1/datasets/{datasetRid}/schema |

# **create**
Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**create_dataset_request** | Union[CreateDatasetRequest, CreateDatasetRequestDict] | Body of the request |  |

### Return type
**Dataset**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[CreateDatasetRequest, CreateDatasetRequestDict] | Body of the request
create_dataset_request = {
    "name": "My Dataset",
    "parentFolderRid": "ri.foundry.main.folder.bfe58487-4c56-4c58-aba7-25defd6163c4",
}


try:
    api_response = foundry_client.datasets.Dataset.create(
        create_dataset_request,
    )
    print("The create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.create: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_schema**
Deletes the Schema from a Dataset and Branch.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transaction_rid** | Optional[TransactionRid] | transactionRid | [optional] |

### Return type
**None**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | datasetRid
dataset_rid = None

# Optional[BranchId] | branchId
branch_id = None

# Optional[PreviewMode] | preview
preview = true

# Optional[TransactionRid] | transactionRid
transaction_rid = None



try:
    api_response = foundry_client.datasets.Dataset.delete_schema(dataset_rid,branch_id=branch_idpreview=previewtransaction_rid=transaction_rid)
    print("The delete_schema response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.delete_schema: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  | Schema deleted. | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Gets the Dataset with the given DatasetRid.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |

### Return type
**Dataset**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"


try:
    api_response = foundry_client.datasets.Dataset.get(
        dataset_rid,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_schema**
Retrieves the Schema for a Dataset and Branch, if it exists.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transaction_rid** | Optional[TransactionRid] | transactionRid | [optional] |

### Return type
**Any**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | datasetRid
dataset_rid = None

# Optional[BranchId] | branchId
branch_id = None

# Optional[PreviewMode] | preview
preview = true

# Optional[TransactionRid] | transactionRid
transaction_rid = None



try:
    api_response = foundry_client.datasets.Dataset.get_schema(dataset_rid,branch_id=branch_idpreview=previewtransaction_rid=transaction_rid)
    print("The get_schema response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.get_schema: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Any  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read**
Gets the content of a dataset as a table in the specified format.

This endpoint currently does not support views (Virtual datasets composed of other datasets).

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**columns** | List[StrictStr] | columns |  |
**format** | TableExportFormat | format |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
**row_limit** | Optional[StrictInt] | rowLimit | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | startTransactionRid | [optional] |

### Return type
**bytes**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | datasetRid
dataset_rid = None

# List[StrictStr] | columns
columns = None

# TableExportFormat | format
format = "CSV"

# Optional[BranchId] | branchId
branch_id = None

# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None

# Optional[StrictInt] | rowLimit
row_limit = None

# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None



try:
    api_response = foundry_client.datasets.Dataset.read(dataset_rid,columns=columnsformat=formatbranch_id=branch_idend_transaction_rid=end_transaction_ridrow_limit=row_limitstart_transaction_rid=start_transaction_rid)
    print("The read response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.read: %s\n" % e)

```

### Read a Foundry Dataset as a CSV

```python
import foundry
from foundry.models import TableExportFormat
from foundry import PalantirRPCException

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

try:
    api_response = foundry_client.datasets.Dataset.read(
        dataset_rid="...", format="CSV", columns=[...]
    )

    with open("my_table.csv", "wb") as f:
        f.write(api_response)
except PalantirRPCException as e:
    print("PalantirRPCException when calling DatasetsApiServiceApi -> read: %s\n" % e)
```

### Read a Foundry Dataset into a Pandas DataFrame

> [!IMPORTANT]
> For this example to work, you will need to have `pyarrow` installed in your Python environment.

```python
import foundry
from foundry.models import TableExportFormat
from foundry import PalantirRPCException
import pyarrow as pa

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

try:
    api_response = foundry_client.datasets.Dataset.read(dataset_rid="...", format="ARROW", columns=[...])
    df = pa.ipc.open_stream(api_response).read_all().to_pandas()
    print(df)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> read: %s\n" % e)
```

```
            id        word  length     double boolean
0            0           A     1.0  11.878200       1
1            1           a     1.0  11.578800       0
2            2          aa     2.0  15.738500       1
3            3         aal     3.0   6.643900       0
4            4       aalii     5.0   2.017730       1
...        ...         ...     ...        ...     ...
235881  235881      zythem     6.0  19.427400       1
235882  235882      Zythia     6.0  14.397100       1
235883  235883      zythum     6.0   3.385820       0
235884  235884     Zyzomys     7.0   6.208830       1
235885  235885  Zyzzogeton    10.0   0.947821       0

[235886 rows x 5 columns]
```


### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | The content stream. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_schema**
Puts a Schema on an existing Dataset and Branch.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**body** | Any | Body of the request |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | datasetRid
dataset_rid = None

# Any | Body of the request
body = None

# Optional[BranchId] | branchId
branch_id = None

# Optional[PreviewMode] | preview
preview = true



try:
    api_response = foundry_client.datasets.Dataset.replace_schema(dataset_rid,body,branch_id=branch_idpreview=preview)
    print("The replace_schema response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.replace_schema: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

