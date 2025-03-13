# File

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**content**](#content) | **GET** /v2/datasets/{datasetRid}/files/{filePath}/content | Stable |
[**delete**](#delete) | **DELETE** /v2/datasets/{datasetRid}/files/{filePath} | Stable |
[**get**](#get) | **GET** /v2/datasets/{datasetRid}/files/{filePath} | Stable |
[**list**](#list) | **GET** /v2/datasets/{datasetRid}/files | Stable |
[**page**](#page) | **GET** /v2/datasets/{datasetRid}/files | Stable |
[**upload**](#upload) | **POST** /v2/datasets/{datasetRid}/files/{filePath}/upload | Stable |

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
**dataset_rid** | DatasetRid |  |  |
**file_path** | FilePath |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch that contains the File. Defaults to `master` for most enrollments.  | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.  | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.  | [optional] |

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

# DatasetRid
dataset_rid = None
# FilePath
file_path = None
# Optional[BranchName] | The name of the Branch that contains the File. Defaults to `master` for most enrollments.
branch_name = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.
end_transaction_rid = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.
start_transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.File.content(
        dataset_rid,
        file_path,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
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
**dataset_rid** | DatasetRid |  |  |
**file_path** | FilePath |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch on which to delete the File. Defaults to `master` for most enrollments.  | [optional] |
**transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the open delete Transaction on which to delete the File.  | [optional] |

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

# DatasetRid
dataset_rid = None
# FilePath
file_path = None
# Optional[BranchName] | The name of the Branch on which to delete the File. Defaults to `master` for most enrollments.
branch_name = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the open delete Transaction on which to delete the File.
transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.File.delete(
        dataset_rid,
        file_path,
        branch_name=branch_name,
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
**dataset_rid** | DatasetRid |  |  |
**file_path** | FilePath |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch that contains the File. Defaults to `master` for most enrollments.  | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.  | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.  | [optional] |

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

# DatasetRid
dataset_rid = None
# FilePath
file_path = None
# Optional[BranchName] | The name of the Branch that contains the File. Defaults to `master` for most enrollments.
branch_name = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.
end_transaction_rid = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.
start_transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.File.get(
        dataset_rid,
        file_path,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
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
**dataset_rid** | DatasetRid |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch on which to list Files. Defaults to `master` for most enrollments.  | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.  | [optional] |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.  | [optional] |

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

# DatasetRid
dataset_rid = None
# Optional[BranchName] | The name of the Branch on which to list Files. Defaults to `master` for most enrollments.
branch_name = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.
end_transaction_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.
start_transaction_rid = None


try:
    for file in foundry_client.datasets.Dataset.File.list(
        dataset_rid,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        page_size=page_size,
        page_token=page_token,
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
**dataset_rid** | DatasetRid |  |  |
**branch_name** | Optional[BranchName] | The name of the Branch on which to list Files. Defaults to `master` for most enrollments.  | [optional] |
**end_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.  | [optional] |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**start_transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.  | [optional] |

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

# DatasetRid
dataset_rid = None
# Optional[BranchName] | The name of the Branch on which to list Files. Defaults to `master` for most enrollments.
branch_name = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the end Transaction.
end_transaction_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the start Transaction.
start_transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.File.page(
        dataset_rid,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        page_size=page_size,
        page_token=page_token,
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
**dataset_rid** | DatasetRid |  |  |
**file_path** | FilePath |  |  |
**body** | bytes | Body of the request |  |
**branch_name** | Optional[BranchName] | The name of the Branch on which to upload the File. Defaults to `master` for most enrollments.  | [optional] |
**transaction_rid** | Optional[TransactionRid] | The Resource Identifier (RID) of the open Transaction on which to upload the File.  | [optional] |
**transaction_type** | Optional[TransactionType] | The type of the Transaction to create when using branchName. Defaults to `UPDATE`.  | [optional] |

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

# DatasetRid
dataset_rid = None
# FilePath
file_path = None
# bytes | Body of the request
body = None
# Optional[BranchName] | The name of the Branch on which to upload the File. Defaults to `master` for most enrollments.
branch_name = None
# Optional[TransactionRid] | The Resource Identifier (RID) of the open Transaction on which to upload the File.
transaction_rid = None
# Optional[TransactionType] | The type of the Transaction to create when using branchName. Defaults to `UPDATE`.
transaction_type = None


try:
    api_response = foundry_client.datasets.Dataset.File.upload(
        dataset_rid,
        file_path,
        body,
        branch_name=branch_name,
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

