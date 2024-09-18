# Transaction

Method | HTTP request |
------------- | ------------- |
[**abort**](#abort) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/abort |
[**commit**](#commit) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/commit |
[**create**](#create) | **POST** /v1/datasets/{datasetRid}/transactions |
[**get**](#get) | **GET** /v1/datasets/{datasetRid}/transactions/{transactionRid} |

# **abort**
Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
not updated.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**transaction_rid** | TransactionRid | transactionRid |  |

### Return type
**Transaction**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# TransactionRid | transactionRid
transaction_rid = "ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496"


try:
    api_response = foundry_client.datasets.Dataset.Transaction.abort(
        dataset_rid,
        transaction_rid,
    )
    print("The abort response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Transaction.abort: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **commit**
Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
updated to point to the Transaction.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**transaction_rid** | TransactionRid | transactionRid |  |

### Return type
**Transaction**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# TransactionRid | transactionRid
transaction_rid = "ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496"


try:
    api_response = foundry_client.datasets.Dataset.Transaction.commit(
        dataset_rid,
        transaction_rid,
    )
    print("The commit response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Transaction.commit: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **create**
Creates a Transaction on a Branch of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**transaction_type** | Optional[TransactionType] |  | [optional] |

### Return type
**Transaction**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[BranchId] | branchId
branch_id = None
# Optional[TransactionType] |
transaction_type = "SNAPSHOT"


try:
    api_response = foundry_client.datasets.Dataset.Transaction.create(
        dataset_rid,
        branch_id=branch_id,
        transaction_type=transaction_type,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Transaction.create: %s\n" % e)

```

### Manipulate a Dataset within a Transaction

```python
import foundry

foundry_client = foundry.FoundryV1Client(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

transaction = foundry_client.datasets.Dataset.Transaction.create(
    dataset_rid="...",
    create_transaction_request={},
)

with open("my/path/to/file.txt", 'rb') as f:
    foundry_client.datasets.Dataset.File.upload(
        body=f.read(),
        dataset_rid="....",
        file_path="...",
        transaction_rid=transaction.rid,
    )

foundry_client.datasets.Dataset.Transaction.commit(dataset_rid="...", transaction_rid=transaction.rid)
```


### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **get**
Gets a Transaction of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**transaction_rid** | TransactionRid | transactionRid |  |

### Return type
**Transaction**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# TransactionRid | transactionRid
transaction_rid = "ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496"


try:
    api_response = foundry_client.datasets.Dataset.Transaction.get(
        dataset_rid,
        transaction_rid,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Transaction.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

