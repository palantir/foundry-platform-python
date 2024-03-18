# Transaction

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v1/datasets/{datasetRid}/transactions |
[**get**](#get) | **GET** /v1/datasets/{datasetRid}/transactions/{transactionRid} |
[**commit**](#commit) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/commit |
[**abort**](#abort) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/abort |

# **create**
Creates a Transaction on a Branch of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset on which to create the Transaction. |  |
**branch_id** | Optional[BranchId] | The identifier (name) of the Branch on which to create the Transaction. Defaults to `master` for most enrollments.
 | [optional] |
**create_transaction_request** | CreateTransactionRequest | CreateTransactionRequest |  |

### Return type
**Transaction**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da" # DatasetRid | The Resource Identifier (RID) of the Dataset on which to create the Transaction.
branch_id = None # Optional[BranchId] | The identifier (name) of the Branch on which to create the Transaction. Defaults to `master` for most enrollments. 
create_transaction_request = {'transactionType': 'SNAPSHOT'} # CreateTransactionRequest | CreateTransactionRequest


try:
    api_response = foundry_client.datasets.Transaction.create(
dataset_rid,branch_id=branch_idcreate_transaction_request=create_transaction_request    )
    print("The Transaction.create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Transaction.create: %s\n" % e)

```

### Manipulate a Dataset within a Transaction

```python
import foundry

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

my_transaction = foundry_client.datasets.Transaction.create(
    dataset_rid="...",
    create_transaction_request={},
)

with open("my/path/to/file.txt", 'rb') as f:
    foundry_client.datasets.File.upload(body=f.read(), dataset_rid="....", file_path="...")

foundry_client.datasets.Transaction.commit(dataset_rid="...", transaction_rid=my_transaction.rid)
```


### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  | An operation that modifies the files within a dataset.  | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
Gets a Transaction of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Transaction. |  |
**transaction_rid** | TransactionRid | The Resource Identifier (RID) of the Transaction. |  |

### Return type
**Transaction**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"  # DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Transaction.
transaction_rid = "ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496"  # TransactionRid | The Resource Identifier (RID) of the Transaction.


try:
    api_response = foundry_client.datasets.Transaction.get(
        dataset_rid,
        transaction_rid,
    )
    print("The Transaction.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Transaction.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  | An operation that modifies the files within a dataset.  | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commit**
Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
updated to point to the Transaction.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Transaction. |  |
**transaction_rid** | TransactionRid | The Resource Identifier (RID) of the Transaction. |  |

### Return type
**Transaction**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"  # DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Transaction.
transaction_rid = "ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496"  # TransactionRid | The Resource Identifier (RID) of the Transaction.


try:
    api_response = foundry_client.datasets.Transaction.commit(
        dataset_rid,
        transaction_rid,
    )
    print("The Transaction.commit response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Transaction.commit: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  | An operation that modifies the files within a dataset.  | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abort**
Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
not updated.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Transaction. |  |
**transaction_rid** | TransactionRid | The Resource Identifier (RID) of the Transaction. |  |

### Return type
**Transaction**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"  # DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Transaction.
transaction_rid = "ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496"  # TransactionRid | The Resource Identifier (RID) of the Transaction.


try:
    api_response = foundry_client.datasets.Transaction.abort(
        dataset_rid,
        transaction_rid,
    )
    print("The Transaction.abort response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Transaction.abort: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  | An operation that modifies the files within a dataset.  | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

