# File

Method | HTTP request |
------------- | ------------- |
[**delete**](#delete) | **DELETE** /v1/datasets/{datasetRid}/files/{filePath} |
[**get**](#get) | **GET** /v1/datasets/{datasetRid}/files/{filePath} |
[**list**](#list) | **GET** /v1/datasets/{datasetRid}/files |
[**page**](#page) | **GET** /v1/datasets/{datasetRid}/files |
[**read**](#read) | **GET** /v1/datasets/{datasetRid}/files/{filePath}/content |
[**upload**](#upload) | **POST** /v1/datasets/{datasetRid}/files:upload |

# **delete**
Deletes a File from a Dataset. By default the file is deleted in a new transaction on the default 
branch - `master` for most enrollments. The file will still be visible on historical views.

#### Advanced Usage
             
See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

To **delete a File from a specific Branch** specify the Branch's identifier as `branchId`. A new delete Transaction 
will be created and committed on this branch.

To **delete a File using a manually opened Transaction**, specify the Transaction's resource identifier 
as `transactionRid`. The transaction must be of type `DELETE`. This is useful for deleting multiple files in a
single transaction. See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to 
open a transaction.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**file_path** | FilePath | filePath |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
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
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"

# FilePath | filePath
file_path = "q3-data%2fmy-file.csv"

# Optional[BranchId] | branchId
branch_id = None

# Optional[TransactionRid] | transactionRid
transaction_rid = None



try:
    api_response = foundry_client.datasets.File.delete(dataset_rid,file_path, branch_id=branch_idtransaction_rid=transaction_rid)
    print("The File.delete response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling File.delete: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  | File deleted. | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Gets metadata about a File contained in a Dataset. By default this retrieves the file's metadata from the latest
view of the default branch - `master` for most enrollments.

#### Advanced Usage

See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions. 

To **get a file's metadata from a specific Branch** specify the Branch's identifier as `branchId`. This will 
retrieve metadata for the most recent version of the file since the latest snapshot transaction, or the earliest
ancestor transaction of the branch if there are no snapshot transactions.

To **get a file's metadata from the resolved view of a transaction** specify the Transaction's resource identifier
as `endTransactionRid`. This will retrieve metadata for the most recent version of the file since the latest snapshot
transaction, or the earliest ancestor transaction if there are no snapshot transactions.

To **get a file's metadata from the resolved view of a range of transactions** specify the the start transaction's
resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`.
This will retrieve metadata for the most recent version of the file since the `startTransactionRid` up to the 
`endTransactionRid`. Behavior is undefined when the start and end transactions do not belong to the same root-to-leaf path.

To **get a file's metadata from a specific transaction** specify the Transaction's resource identifier as both the 
`startTransactionRid` and `endTransactionRid`.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**file_path** | FilePath | filePath |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | startTransactionRid | [optional] |

### Return type
**File**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"

# FilePath | filePath
file_path = "q3-data%2fmy-file.csv"

# Optional[BranchId] | branchId
branch_id = None

# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None

# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None



try:
    api_response = foundry_client.datasets.File.get(dataset_rid,file_path, branch_id=branch_idend_transaction_rid=end_transaction_ridstart_transaction_rid=start_transaction_rid)
    print("The File.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling File.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | File  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**
Lists Files contained in a Dataset. By default files are listed on the latest view of the default 
branch - `master` for most enrollments.

#### Advanced Usage

See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

To **list files on a specific Branch** specify the Branch's identifier as `branchId`. This will include the most
recent version of all files since the latest snapshot transaction, or the earliest ancestor transaction of the 
branch if there are no snapshot transactions.

To **list files on the resolved view of a transaction** specify the Transaction's resource identifier
as `endTransactionRid`. This will include the most recent version of all files since the latest snapshot
transaction, or the earliest ancestor transaction if there are no snapshot transactions.

To **list files on the resolved view of a range of transactions** specify the the start transaction's resource
identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This
will include the most recent version of all files since the `startTransactionRid` up to the `endTransactionRid`.
Note that an intermediate snapshot transaction will remove all files from the view. Behavior is undefined when 
the start and end transactions do not belong to the same root-to-leaf path.

To **list files on a specific transaction** specify the Transaction's resource identifier as both the 
`startTransactionRid` and `endTransactionRid`. This will include only files that were modified as part of that
Transaction.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | startTransactionRid | [optional] |

### Return type
**ResourceIterator[File]**

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

# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None

# Optional[PageSize] | pageSize
page_size = None

# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None



try:
    for file in foundry_client.datasets.File.list(dataset_rid, branch_id=branch_idend_transaction_rid=end_transaction_ridpage_size=page_sizestart_transaction_rid=start_transaction_rid)
:
        pprint(file)
except PalantirRPCException as e:
    print("HTTP error when calling File.list: %s\n" % e)

```

### Read the contents of a file from a dataset (by exploration / listing)

```python
import foundry

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

result = foundry_client.datasets.File.list(dataset_rid="...")

if result.data:
    file_path = result.data[0].path

    print(foundry_client.datasets.File.read(
        dataset_rid="...", file_path=file_path
    ))
```

```
b'Hello!'
```


### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListFilesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **page**
Lists Files contained in a Dataset. By default files are listed on the latest view of the default 
branch - `master` for most enrollments.

#### Advanced Usage

See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

To **list files on a specific Branch** specify the Branch's identifier as `branchId`. This will include the most
recent version of all files since the latest snapshot transaction, or the earliest ancestor transaction of the 
branch if there are no snapshot transactions.

To **list files on the resolved view of a transaction** specify the Transaction's resource identifier
as `endTransactionRid`. This will include the most recent version of all files since the latest snapshot
transaction, or the earliest ancestor transaction if there are no snapshot transactions.

To **list files on the resolved view of a range of transactions** specify the the start transaction's resource
identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This
will include the most recent version of all files since the `startTransactionRid` up to the `endTransactionRid`.
Note that an intermediate snapshot transaction will remove all files from the view. Behavior is undefined when 
the start and end transactions do not belong to the same root-to-leaf path.

To **list files on a specific transaction** specify the Transaction's resource identifier as both the 
`startTransactionRid` and `endTransactionRid`. This will include only files that were modified as part of that
Transaction.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | startTransactionRid | [optional] |

### Return type
**ListFilesResponse**

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

# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None

# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None



try:
    api_response = foundry_client.datasets.File.page(dataset_rid, branch_id=branch_idend_transaction_rid=end_transaction_ridpage_size=page_sizepage_token=page_tokenstart_transaction_rid=start_transaction_rid)
    print("The File.page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling File.page: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListFilesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read**
Gets the content of a File contained in a Dataset. By default this retrieves the file's content from the latest
view of the default branch - `master` for most enrollments.

#### Advanced Usage

See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions. 

To **get a file's content from a specific Branch** specify the Branch's identifier as `branchId`. This will 
retrieve the content for the most recent version of the file since the latest snapshot transaction, or the
earliest ancestor transaction of the branch if there are no snapshot transactions.

To **get a file's content from the resolved view of a transaction** specify the Transaction's resource identifier
as `endTransactionRid`. This will retrieve the content for the most recent version of the file since the latest
snapshot transaction, or the earliest ancestor transaction if there are no snapshot transactions.

To **get a file's content from the resolved view of a range of transactions** specify the the start transaction's
resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`.
This will retrieve the content for the most recent version of the file since the `startTransactionRid` up to the 
`endTransactionRid`. Note that an intermediate snapshot transaction will remove all files from the view. Behavior
is undefined when the start and end transactions do not belong to the same root-to-leaf path.

To **get a file's content from a specific transaction** specify the Transaction's resource identifier as both the 
`startTransactionRid` and `endTransactionRid`.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**file_path** | FilePath | filePath |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
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

# FilePath | filePath
file_path = "q3-data%2fmy-file.csv"

# Optional[BranchId] | branchId
branch_id = None

# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None

# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None



try:
    api_response = foundry_client.datasets.File.read(dataset_rid,file_path, branch_id=branch_idend_transaction_rid=end_transaction_ridstart_transaction_rid=start_transaction_rid)
    print("The File.read response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling File.read: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload**
Uploads a File to an existing Dataset.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

By default the file is uploaded to a new transaction on the default branch - `master` for most enrollments.
If the file already exists only the most recent version will be visible in the updated view.

#### Advanced Usage

See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions. 

To **upload a file to a specific Branch** specify the Branch's identifier as `branchId`. A new transaction will 
be created and committed on this branch. By default the TransactionType will be `UPDATE`, to override this
default specify `transactionType` in addition to `branchId`. 
See [createBranch](/docs/foundry/api/datasets-resources/branches/create-branch/) to create a custom branch.

To **upload a file on a manually opened transaction** specify the Transaction's resource identifier as
`transactionRid`. This is useful for uploading multiple files in a single transaction. 
See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to open a transaction.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**body** | bytes | Body of the request |  |
**file_path** | FilePath | filePath |  |
**branch_id** | Optional[BranchId] | branchId | [optional] |
**transaction_rid** | Optional[TransactionRid] | transactionRid | [optional] |
**transaction_type** | Optional[TransactionType] | transactionType | [optional] |

### Return type
**File**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | datasetRid
dataset_rid = None

# bytes | Body of the request
body = None

# FilePath | filePath
file_path = "q3-data%2fmy-file.csv"

# Optional[BranchId] | branchId
branch_id = None

# Optional[TransactionRid] | transactionRid
transaction_rid = None

# Optional[TransactionType] | transactionType
transaction_type = None



try:
    api_response = foundry_client.datasets.File.upload(dataset_rid,body, file_path=file_pathbranch_id=branch_idtransaction_rid=transaction_ridtransaction_type=transaction_type)
    print("The File.upload response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling File.upload: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | File  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

