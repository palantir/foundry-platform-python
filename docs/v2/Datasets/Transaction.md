# Transaction

Method | HTTP request |
------------- | ------------- |
[**abort**](#abort) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/abort |
[**commit**](#commit) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/commit |
[**create**](#create) | **POST** /v2/datasets/{datasetRid}/transactions |
[**get**](#get) | **GET** /v2/datasets/{datasetRid}/transactions/{transactionRid} |

# **abort**
Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
not updated.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**transaction_rid** | TransactionRid | transactionRid |  |

### Return type
**Transaction**

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
# TransactionRid | transactionRid
transaction_rid = None


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

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Get the [Build](/docs/foundry/data-integration/builds#builds) that computed the
given Transaction. Not all Transactions have an associated Build. For example, if a Dataset
is updated by a User uploading a CSV file into the browser, no Build will be tied to the Transaction.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**transaction_rid** | TransactionRid | transactionRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Build**

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
# TransactionRid | transactionRid
transaction_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.datasets.Dataset.Transaction.build(
        dataset_rid,
        transaction_rid,
        preview=preview,
    )
    print("The build response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Transaction.build: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Build  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **commit**
Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
updated to point to the Transaction.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**transaction_rid** | TransactionRid | transactionRid |  |

### Return type
**Transaction**

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
# TransactionRid | transactionRid
transaction_rid = None


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

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create**
Creates a Transaction on a Branch of a Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**transaction_type** | TransactionType |  |  |
**branch_name** | Optional[BranchName] | branchName | [optional] |

### Return type
**Transaction**

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
# TransactionType |
transaction_type = "APPEND"
# Optional[BranchName] | branchName
branch_name = None


try:
    api_response = foundry_client.datasets.Dataset.Transaction.create(
        dataset_rid,
        transaction_type=transaction_type,
        branch_name=branch_name,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Transaction.create: %s\n" % e)

```

### Manipulate a Dataset within a Transaction

```python
import foundry

foundry_client = foundry.FoundryV2Client(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

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
**200** | Transaction  | The created Transaction | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Gets a Transaction of a Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**transaction_rid** | TransactionRid | transactionRid |  |

### Return type
**Transaction**

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
# TransactionRid | transactionRid
transaction_rid = None


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

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

