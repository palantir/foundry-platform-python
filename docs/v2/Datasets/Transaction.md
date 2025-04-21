# Transaction

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**abort**](#abort) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/abort | Stable |
[**build**](#build) | **GET** /v2/datasets/{datasetRid}/transactions/{transactionRid}/build | Private Beta |
[**commit**](#commit) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/commit | Stable |
[**create**](#create) | **POST** /v2/datasets/{datasetRid}/transactions | Stable |
[**get**](#get) | **GET** /v2/datasets/{datasetRid}/transactions/{transactionRid} | Stable |
[**job**](#job) | **GET** /v2/datasets/{datasetRid}/transactions/{transactionRid}/job | Private Beta |

# **abort**
Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
not updated.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**transaction_rid** | TransactionRid |  |  |

### Return type
**Transaction**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# TransactionRid
transaction_rid = None


try:
    api_response = client.datasets.Dataset.Transaction.abort(dataset_rid, transaction_rid)
    print("The abort response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Transaction.abort: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **build**
Get the [Build](https://palantir.com/docs/foundry/data-integration/builds#builds) that computed the
given Transaction. Not all Transactions have an associated Build. For example, if a Dataset
is updated by a User uploading a CSV file into the browser, no Build will be tied to the Transaction.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**transaction_rid** | TransactionRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Optional[BuildRid]**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# TransactionRid
transaction_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.datasets.Dataset.Transaction.build(
        dataset_rid, transaction_rid, preview=preview
    )
    print("The build response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Transaction.build: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Optional[BuildRid]  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **commit**
Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
updated to point to the Transaction.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**transaction_rid** | TransactionRid |  |  |

### Return type
**Transaction**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# TransactionRid
transaction_rid = None


try:
    api_response = client.datasets.Dataset.Transaction.commit(dataset_rid, transaction_rid)
    print("The commit response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**dataset_rid** | DatasetRid |  |  |
**transaction_type** | TransactionType |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch on which to create the Transaction. Defaults to `master` for most enrollments.  | [optional] |

### Return type
**Transaction**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# TransactionType
transaction_type = "APPEND"
# Optional[BranchName] | The name of the Branch on which to create the Transaction. Defaults to `master` for most enrollments.
branch_name = None


try:
    api_response = client.datasets.Dataset.Transaction.create(
        dataset_rid, transaction_type=transaction_type, branch_name=branch_name
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**dataset_rid** | DatasetRid |  |  |
**transaction_rid** | TransactionRid |  |  |

### Return type
**Transaction**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# TransactionRid
transaction_rid = None


try:
    api_response = client.datasets.Dataset.Transaction.get(dataset_rid, transaction_rid)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Transaction.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Transaction  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **job**
Get the [Job](https://palantir.com/docs/foundry/data-integration/builds#jobs-and-jobspecs) that computed the
given Transaction. Not all Transactions have an associated Job. For example, if a Dataset
is updated by a User uploading a CSV file into the browser, no Job will be tied to the Transaction.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**transaction_rid** | TransactionRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Optional[JobRid]**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# TransactionRid
transaction_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.datasets.Dataset.Transaction.job(
        dataset_rid, transaction_rid, preview=preview
    )
    print("The job response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Transaction.job: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Optional[JobRid]  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

