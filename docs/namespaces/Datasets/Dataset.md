# Dataset

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v1/datasets |
[**get**](#get) | **GET** /v1/datasets/{datasetRid} |
[**read_table**](#read_table) | **GET** /v1/datasets/{datasetRid}/readTable |
[**put_schema**](#put_schema) | **PUT** /v1/datasets/{datasetRid}/schema |
[**get_schema**](#get_schema) | **GET** /v1/datasets/{datasetRid}/schema |
[**delete_schema**](#delete_schema) | **DELETE** /v1/datasets/{datasetRid}/schema |

# **create**
Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**create_dataset_request** | CreateDatasetRequest | CreateDatasetRequest |  |

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

create_dataset_request = {
    "name": "My Dataset",
    "parentFolderRid": "ri.foundry.main.folder.bfe58487-4c56-4c58-aba7-25defd6163c4",
}  # CreateDatasetRequest | CreateDatasetRequest


try:
    api_response = foundry_client.datasets.Dataset.create(
        create_dataset_request=create_dataset_request
    )
    print("The Dataset.create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.create: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  | Dataset | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

dataset_rid = (
    "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"  # DatasetRid | datasetRid
)


try:
    api_response = foundry_client.datasets.Dataset.get(
        dataset_rid,
    )
    print("The Dataset.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  | Dataset | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_table**
:::callout{theme=warning title=Warning}
  This endpoint is in preview and may be modified or removed at any time.
  To use this endpoint, add `preview=true` to the request query parameters.
  Furthermore, this endpoint currently does not support views (Virtual datasets composed of other datasets).
:::

Gets the content of a dataset as a table in the specified format.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The RID of the Dataset.  |  |
**branch_id** | Optional[BranchId] | The identifier (name) of the Branch. | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction. | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction. | [optional] |
**format** | TableExportFormat | The export format. Must be `ARROW` or `CSV`.  |  |
**columns** | Optional[List[StrictStr]] | A subset of the dataset columns to include in the result. Defaults to all columns.  | [optional] |
**row_limit** | Optional[StrictInt] | A limit on the number of rows to return. Note that row ordering is non-deterministic.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

dataset_rid = None # DatasetRid | The RID of the Dataset. 
branch_id = None # Optional[BranchId] | The identifier (name) of the Branch.
start_transaction_rid = None # Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.
end_transaction_rid = None # Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.
format = "CSV" # TableExportFormat | The export format. Must be `ARROW` or `CSV`. 
columns = None # Optional[List[StrictStr]] | A subset of the dataset columns to include in the result. Defaults to all columns. 
row_limit = None # Optional[StrictInt] | A limit on the number of rows to return. Note that row ordering is non-deterministic. 
preview = None # Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode. 


try:
    api_response = foundry_client.datasets.Dataset.read_table(
dataset_rid,branch_id=branch_idstart_transaction_rid=start_transaction_ridend_transaction_rid=end_transaction_ridformat=formatcolumns=columnsrow_limit=row_limitpreview=preview    )
    print("The Dataset.read_table response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.read_table: %s\n" % e)

```

### Read a Foundry Dataset as a CSV

```python
import foundry
from foundry.models import TableExportFormat
from foundry import PalantirRPCException

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

try:
    api_response = foundry_client.datasets.Dataset.read_table(
        dataset_rid="...", format="CSV", columns=[...]
    )

    with open("my_table.csv", "wb") as f:
        f.write(api_response)
except PalantirRPCException as e:
    print("PalantirRPCException when calling DatasetsApiServiceApi -> read_table: %s\n" % e)
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
    api_response = foundry_client.datasets.Dataset.read_table(dataset_rid="...", format="ARROW", columns=[...])
    df = pa.ipc.open_stream(api_response).read_all().to_pandas()
    print(df)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> read_table: %s\n" % e)
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
**200** | bytes  | None | */* |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_schema**
Puts a Schema on an existing Dataset and Branch.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The RID of the Dataset on which to put the Schema.  |  |
**branch_id** | Optional[BranchId] | The ID of the Branch on which to put the Schema.  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**body** | object | Body of the request |  |

### Return type
**None**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

dataset_rid = None # DatasetRid | The RID of the Dataset on which to put the Schema. 
branch_id = None # Optional[BranchId] | The ID of the Branch on which to put the Schema. 
preview = True # Optional[PreviewMode] | preview
body = None # object | Body of the request


try:
    api_response = foundry_client.datasets.Dataset.put_schema(
dataset_rid,branch_id=branch_idpreview=previewbody=body    )
    print("The Dataset.put_schema response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.put_schema: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  | No content | None |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema**
Retrieves the Schema for a Dataset and Branch, if it exists.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The RID of the Dataset.  |  |
**branch_id** | Optional[BranchId] | The ID of the Branch.  | [optional] |
**transaction_rid** | Optional[TransactionRid] | The TransactionRid that contains the Schema.  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Union[object, None]**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

dataset_rid = None # DatasetRid | The RID of the Dataset. 
branch_id = None # Optional[BranchId] | The ID of the Branch. 
transaction_rid = None # Optional[TransactionRid] | The TransactionRid that contains the Schema. 
preview = True # Optional[PreviewMode] | preview


try:
    api_response = foundry_client.datasets.Dataset.get_schema(
dataset_rid,branch_id=branch_idtransaction_rid=transaction_ridpreview=preview    )
    print("The Dataset.get_schema response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.get_schema: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | object  | None | application/json |
**204** | None  | No content | None |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schema**
Deletes the Schema from a Dataset and Branch.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The RID of the Dataset on which to delete the schema.  |  |
**branch_id** | Optional[BranchId] | The ID of the Branch on which to delete the schema.  | [optional] |
**transaction_rid** | Optional[TransactionRid] | The RID of the Transaction on which to delete the schema.  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

dataset_rid = None # DatasetRid | The RID of the Dataset on which to delete the schema. 
branch_id = None # Optional[BranchId] | The ID of the Branch on which to delete the schema. 
transaction_rid = None # Optional[TransactionRid] | The RID of the Transaction on which to delete the schema. 
preview = True # Optional[PreviewMode] | preview


try:
    api_response = foundry_client.datasets.Dataset.delete_schema(
dataset_rid,branch_id=branch_idtransaction_rid=transaction_ridpreview=preview    )
    print("The Dataset.delete_schema response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.delete_schema: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  | No content | None |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

