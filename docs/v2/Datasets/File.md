# File

Method | HTTP request |
------------- | ------------- |
[**content**](#content) | **GET** /v2/datasets/{datasetRid}/files/{filePath}/content |
[**delete**](#delete) | **DELETE** /v2/datasets/{datasetRid}/files/{filePath} |
[**get**](#get) | **GET** /v2/datasets/{datasetRid}/files/{filePath} |
[**list**](#list) | **GET** /v2/datasets/{datasetRid}/files |
[**page**](#page) | **GET** /v2/datasets/{datasetRid}/files |
[**upload**](#upload) | **POST** /v2/datasets/{datasetRid}/files/{filePath}/upload |

# **content**
Gets the content of a File contained in a Dataset. By default this retrieves the file's content from the latest
view of the default branch - `master` for most enrollments.
#### Advanced Usage
See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions. 
To **get a file's content from a specific Branch** specify the Branch's name as `branchName`. This will 
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


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**file_path** | FilePath | filePath |  |
**branch_name** | Optional[BranchName] | branchName | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | startTransactionRid | [optional] |

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
# FilePath | filePath
file_path = None
# Optional[BranchName] | branchName
branch_name = None
# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None
# Optional[PreviewMode] | preview
preview = None
# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.File.content(
        dataset_rid,
        file_path,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        preview=preview,
        start_transaction_rid=start_transaction_rid,
    )
    print("The content response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling File.content: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **delete**
Deletes a File from a Dataset. By default the file is deleted in a new transaction on the default 
branch - `master` for most enrollments. The file will still be visible on historical views.
#### Advanced Usage
See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
To **delete a File from a specific Branch** specify the Branch's name as `branchName`. A new delete Transaction 
will be created and committed on this branch.
To **delete a File using a manually opened Transaction**, specify the Transaction's resource identifier 
as `transactionRid`. The transaction must be of type `DELETE`. This is useful for deleting multiple files in a
single transaction. See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to 
open a transaction.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**file_path** | FilePath | filePath |  |
**branch_name** | Optional[BranchName] | branchName | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transaction_rid** | Optional[TransactionRid] | transactionRid | [optional] |

### Return type
**None**

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
# FilePath | filePath
file_path = None
# Optional[BranchName] | branchName
branch_name = None
# Optional[PreviewMode] | preview
preview = None
# Optional[TransactionRid] | transactionRid
transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.File.delete(
        dataset_rid,
        file_path,
        branch_name=branch_name,
        preview=preview,
        transaction_rid=transaction_rid,
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling File.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Gets metadata about a File contained in a Dataset. By default this retrieves the file's metadata from the latest
view of the default branch - `master` for most enrollments.
#### Advanced Usage
See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions. 
To **get a file's metadata from a specific Branch** specify the Branch's name as `branchName`. This will 
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


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**file_path** | FilePath | filePath |  |
**branch_name** | Optional[BranchName] | branchName | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | startTransactionRid | [optional] |

### Return type
**File**

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
# FilePath | filePath
file_path = None
# Optional[BranchName] | branchName
branch_name = None
# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None
# Optional[PreviewMode] | preview
preview = None
# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.File.get(
        dataset_rid,
        file_path,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        preview=preview,
        start_transaction_rid=start_transaction_rid,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling File.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | File  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists Files contained in a Dataset. By default files are listed on the latest view of the default 
branch - `master` for most enrollments.
#### Advanced Usage
See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
To **list files on a specific Branch** specify the Branch's name as `branchName`. This will include the most
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


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_name** | Optional[BranchName] | branchName | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | startTransactionRid | [optional] |

### Return type
**ResourceIterator[File]**

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
# Optional[BranchName] | branchName
branch_name = None
# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[PreviewMode] | preview
preview = None
# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None


try:
    for file in foundry_client.datasets.Dataset.File.list(
        dataset_rid,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        page_size=page_size,
        preview=preview,
        start_transaction_rid=start_transaction_rid,
    ):
        pprint(file)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling File.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListFilesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists Files contained in a Dataset. By default files are listed on the latest view of the default 
branch - `master` for most enrollments.
#### Advanced Usage
See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
To **list files on a specific Branch** specify the Branch's name as `branchName`. This will include the most
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


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_name** | Optional[BranchName] | branchName | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | endTransactionRid | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | startTransactionRid | [optional] |

### Return type
**ListFilesResponse**

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
# Optional[BranchName] | branchName
branch_name = None
# Optional[TransactionRid] | endTransactionRid
end_transaction_rid = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None
# Optional[TransactionRid] | startTransactionRid
start_transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.File.page(
        dataset_rid,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        start_transaction_rid=start_transaction_rid,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling File.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListFilesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload**
Uploads a File to an existing Dataset.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
By default the file is uploaded to a new transaction on the default branch - `master` for most enrollments.
If the file already exists only the most recent version will be visible in the updated view.
#### Advanced Usage
See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions. 
To **upload a file to a specific Branch** specify the Branch's name as `branchName`. A new transaction will 
be created and committed on this branch. By default the TransactionType will be `UPDATE`, to override this
default specify `transactionType` in addition to `branchName`. 
See [createBranch](/docs/foundry/api/datasets-resources/branches/create-branch/) to create a custom branch.
To **upload a file on a manually opened transaction** specify the Transaction's resource identifier as
`transactionRid`. This is useful for uploading multiple files in a single transaction. 
See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to open a transaction.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**file_path** | FilePath | filePath |  |
**body** | bytes | Body of the request |  |
**branch_name** | Optional[BranchName] | branchName | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transaction_rid** | Optional[TransactionRid] | transactionRid | [optional] |
**transaction_type** | Optional[TransactionType] | transactionType | [optional] |

### Return type
**File**

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
# FilePath | filePath
file_path = None
# bytes | Body of the request
body = None
# Optional[BranchName] | branchName
branch_name = None
# Optional[PreviewMode] | preview
preview = None
# Optional[TransactionRid] | transactionRid
transaction_rid = None
# Optional[TransactionType] | transactionType
transaction_type = None


try:
    api_response = foundry_client.datasets.Dataset.File.upload(
        dataset_rid,
        file_path,
        body,
        branch_name=branch_name,
        preview=preview,
        transaction_rid=transaction_rid,
        transaction_type=transaction_type,
    )
    print("The upload response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling File.upload: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | File  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

