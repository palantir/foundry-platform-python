# foundry.DatasetsApiServiceApi

The official Python library for the Foundry API

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_transaction**](<DatasetsApiServiceApi.md#abort_transaction>) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/abort |
[**commit_transaction**](<DatasetsApiServiceApi.md#commit_transaction>) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/commit |
[**create_branch**](<DatasetsApiServiceApi.md#create_branch>) | **POST** /v1/datasets/{datasetRid}/branches |
[**create_dataset**](<DatasetsApiServiceApi.md#create_dataset>) | **POST** /v1/datasets |
[**create_transaction**](<DatasetsApiServiceApi.md#create_transaction>) | **POST** /v1/datasets/{datasetRid}/transactions |
[**delete_branch**](<DatasetsApiServiceApi.md#delete_branch>) | **DELETE** /v1/datasets/{datasetRid}/branches/{branchId} |
[**delete_file**](<DatasetsApiServiceApi.md#delete_file>) | **DELETE** /v1/datasets/{datasetRid}/files/{filePath} |
[**delete_schema**](<DatasetsApiServiceApi.md#delete_schema>) | **DELETE** /v1/datasets/{datasetRid}/schema |
[**get_branch**](<DatasetsApiServiceApi.md#get_branch>) | **GET** /v1/datasets/{datasetRid}/branches/{branchId} |
[**get_dataset**](<DatasetsApiServiceApi.md#get_dataset>) | **GET** /v1/datasets/{datasetRid} |
[**get_file_content**](<DatasetsApiServiceApi.md#get_file_content>) | **GET** /v1/datasets/{datasetRid}/files/{filePath}/content |
[**get_file_metadata**](<DatasetsApiServiceApi.md#get_file_metadata>) | **GET** /v1/datasets/{datasetRid}/files/{filePath} |
[**get_schema**](<DatasetsApiServiceApi.md#get_schema>) | **GET** /v1/datasets/{datasetRid}/schema |
[**get_transaction**](<DatasetsApiServiceApi.md#get_transaction>) | **GET** /v1/datasets/{datasetRid}/transactions/{transactionRid} |
[**list_branches**](<DatasetsApiServiceApi.md#list_branches>) | **GET** /v1/datasets/{datasetRid}/branches |
[**list_files**](<DatasetsApiServiceApi.md#list_files>) | **GET** /v1/datasets/{datasetRid}/files |
[**put_schema**](<DatasetsApiServiceApi.md#put_schema>) | **PUT** /v1/datasets/{datasetRid}/schema |
[**read_table**](<DatasetsApiServiceApi.md#read_table>) | **GET** /v1/datasets/{datasetRid}/readTable |
[**upload_file**](<DatasetsApiServiceApi.md#upload_file>) | **POST** /v1/datasets/{datasetRid}/files:upload |

# **abort_transaction**

> Transaction abort_transaction(dataset_rid, transaction_rid)

Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is not updated.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

### Example

```python
import time
import os
import foundry
from foundry.models.transaction import Transaction
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset that contains the Transaction.
transaction_rid = 'ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496' # str | The Resource Identifier (RID) of the Transaction.

try:
    api_response = foundry_client.datasets.abort_transaction(dataset_rid, transaction_rid)
    print("The response of DatasetsApiServiceApi -> abort_transaction:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> abort_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset that contains the Transaction. |
**transaction_rid** | **str**| The Resource Identifier (RID) of the Transaction. |

### Return type

[**Transaction**](Transaction.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **commit_transaction**

> Transaction commit_transaction(dataset_rid, transaction_rid)

Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is updated to point to the Transaction.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

### Example

```python
import time
import os
import foundry
from foundry.models.transaction import Transaction
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset that contains the Transaction.
transaction_rid = 'ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496' # str | The Resource Identifier (RID) of the Transaction.

try:
    api_response = foundry_client.datasets.commit_transaction(dataset_rid, transaction_rid)
    print("The response of DatasetsApiServiceApi -> commit_transaction:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> commit_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset that contains the Transaction. |
**transaction_rid** | **str**| The Resource Identifier (RID) of the Transaction. |

### Return type

[**Transaction**](Transaction.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **create_branch**

> Branch create_branch(dataset_rid, create_branch_request)

Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

### Example

```python
import time
import os
import foundry
from foundry.models.branch import Branch
from foundry.models.create_branch_request import CreateBranchRequest
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset on which to create the Branch.
create_branch_request = {"branchId":"my-branch"} # CreateBranchRequest | 

try:
    api_response = foundry_client.datasets.create_branch(dataset_rid, create_branch_request)
    print("The response of DatasetsApiServiceApi -> create_branch:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> create_branch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset on which to create the Branch. |
**create_branch_request** | [**CreateBranchRequest**](CreateBranchRequest.md)|  |

### Return type

[**Branch**](Branch.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **create_dataset**

> Dataset create_dataset(create_dataset_request)

Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

### Example

```python
import time
import os
import foundry
from foundry.models.create_dataset_request import CreateDatasetRequest
from foundry.models.dataset import Dataset
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

create_dataset_request = {"name":"My Dataset","parentFolderRid":"ri.foundry.main.folder.bfe58487-4c56-4c58-aba7-25defd6163c4"} # CreateDatasetRequest | 

try:
    api_response = foundry_client.datasets.create_dataset(create_dataset_request)
    print("The response of DatasetsApiServiceApi -> create_dataset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> create_dataset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**create_dataset_request** | [**CreateDatasetRequest**](CreateDatasetRequest.md)|  |

### Return type

[**Dataset**](Dataset.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **create_transaction**

> Transaction create_transaction(dataset_rid, create_transaction_request, branch_id=branch_id)

Creates a Transaction on a Branch of a Dataset.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

### Example

```python
import time
import os
import foundry
from foundry.models.create_transaction_request import CreateTransactionRequest
from foundry.models.transaction import Transaction
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset on which to create the Transaction.
create_transaction_request = {"transactionType":"SNAPSHOT"} # CreateTransactionRequest | 
branch_id = 'branch_id_example' # str | The identifier (name) of the Branch on which to create the Transaction. Defaults to `master` for most enrollments.  (optional)

try:
    api_response = foundry_client.datasets.create_transaction(dataset_rid, create_transaction_request, branch_id=branch_id)
    print("The response of DatasetsApiServiceApi -> create_transaction:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> create_transaction: %s\n" % e)
```


### Manipulate a Dataset within a Transaction

```python
import foundry

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

my_transaction = foundry_client.datasets.create_transaction(
    dataset_rid="...",
    create_transaction_request={},
)

with open("my/path/to/file.txt", 'rb') as f:
    foundry_client.datasets.upload_file(data=f.read(), dataset_rid="....", file_path="...")

foundry_client.datasets.commit_transaction(dataset_rid="...", transaction_rid=my_transaction.rid)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset on which to create the Transaction. |
**create_transaction_request** | [**CreateTransactionRequest**](CreateTransactionRequest.md)|  |
**branch_id** | **str**| The identifier (name) of the Branch on which to create the Transaction. Defaults to \`master\` for most enrollments.  | \[optional\]

### Return type

[**Transaction**](Transaction.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **delete_branch**

> delete_branch(dataset_rid, branch_id)

Deletes the Branch with the given BranchId.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

### Example

```python
import time
import os
import foundry
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset that contains the Branch.
branch_id = 'my-branch' # str | The identifier (name) of the Branch.

try:
    foundry_client.datasets.delete_branch(dataset_rid, branch_id)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> delete_branch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset that contains the Branch. |
**branch_id** | **str**| The identifier (name) of the Branch. |

### Return type

void (empty response body)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Branch deleted. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **delete_file**

> delete_file(dataset_rid, file_path, branch_id=branch_id, transaction_rid=transaction_rid)

Deletes a File from a Dataset. By default the file is deleted in a new transaction on the default  branch - `master` for most enrollments. The file will still be visible on historical views.  #### Advanced Usage               See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.  To **delete a File from a specific Branch** specify the Branch's identifier as `branchId`. A new delete Transaction  will be created and committed on this branch.  To **delete a File using a manually opened Transaction**, specify the Transaction's resource identifier  as `transactionRid`. The transaction must be of type `DELETE`. This is useful for deleting multiple files in a single transaction. See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to  open a transaction.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

### Example

```python
import time
import os
import foundry
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset on which to delete the File.
file_path = 'q3-data%2fmy-file.csv' # str | The File path within the Dataset.
branch_id = 'branch_id_example' # str | The identifier (name) of the Branch on which to delete the File. Defaults to `master` for most enrollments. (optional)
transaction_rid = 'transaction_rid_example' # str | The Resource Identifier (RID) of the open delete Transaction on which to delete the File. (optional)

try:
    foundry_client.datasets.delete_file(dataset_rid, file_path, branch_id=branch_id, transaction_rid=transaction_rid)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> delete_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset on which to delete the File. |
**file_path** | **str**| The File path within the Dataset. |
**branch_id** | **str**| The identifier (name) of the Branch on which to delete the File. Defaults to \`master\` for most enrollments. | \[optional\]
**transaction_rid** | **str**| The Resource Identifier (RID) of the open delete Transaction on which to delete the File. | \[optional\]

### Return type

void (empty response body)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | File deleted. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **delete_schema**

> delete_schema(dataset_rid, branch_id=branch_id, transaction_rid=transaction_rid, preview=preview)

Deletes the Schema from a Dataset and Branch.

### Example

```python
import time
import os
import foundry
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'dataset_rid_example' # str | The RID of the Dataset on which to delete the schema. 
branch_id = 'branch_id_example' # str | The ID of the Branch on which to delete the schema.  (optional)
transaction_rid = 'transaction_rid_example' # str | The RID of the Transaction on which to delete the schema.  (optional)
preview = true # bool |  (optional)

try:
    foundry_client.datasets.delete_schema(dataset_rid, branch_id=branch_id, transaction_rid=transaction_rid, preview=preview)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> delete_schema: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The RID of the Dataset on which to delete the schema.  |
**branch_id** | **str**| The ID of the Branch on which to delete the schema.  | \[optional\]
**transaction_rid** | **str**| The RID of the Transaction on which to delete the schema.  | \[optional\]
**preview** | **bool**|  | \[optional\]

### Return type

void (empty response body)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Schema deleted. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_branch**

> Branch get_branch(dataset_rid, branch_id)

Get a Branch of a Dataset.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

### Example

```python
import time
import os
import foundry
from foundry.models.branch import Branch
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset that contains the Branch.
branch_id = 'master' # str | The identifier (name) of the Branch.

try:
    api_response = foundry_client.datasets.get_branch(dataset_rid, branch_id)
    print("The response of DatasetsApiServiceApi -> get_branch:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> get_branch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset that contains the Branch. |
**branch_id** | **str**| The identifier (name) of the Branch. |

### Return type

[**Branch**](Branch.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_dataset**

> Dataset get_dataset(dataset_rid)

Gets the Dataset with the given DatasetRid.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

### Example

```python
import time
import os
import foundry
from foundry.models.dataset import Dataset
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | 

try:
    api_response = foundry_client.datasets.get_dataset(dataset_rid)
    print("The response of DatasetsApiServiceApi -> get_dataset:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> get_dataset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**|  |

### Return type

[**Dataset**](Dataset.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_file_content**

> bytearray get_file_content(dataset_rid, file_path, branch_id=branch_id, start_transaction_rid=start_transaction_rid, end_transaction_rid=end_transaction_rid)

Gets the content of a File contained in a Dataset. By default this retrieves the file's content from the latest view of the default branch - `master` for most enrollments.  #### Advanced Usage  See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.   To **get a file's content from a specific Branch** specify the Branch's identifier as `branchId`. This will  retrieve the content for the most recent version of the file since the latest snapshot transaction, or the earliest ancestor transaction of the branch if there are no snapshot transactions.  To **get a file's content from the resolved view of a transaction** specify the Transaction's resource identifier as `endTransactionRid`. This will retrieve the content for the most recent version of the file since the latest snapshot transaction, or the earliest ancestor transaction if there are no snapshot transactions.  To **get a file's content from the resolved view of a range of transactions** specify the the start transaction's resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This will retrieve the content for the most recent version of the file since the `startTransactionRid` up to the  `endTransactionRid`. Note that an intermediate snapshot transaction will remove all files from the view. Behavior is undefined when the start and end transactions do not belong to the same root-to-leaf path.  To **get a file's content from a specific transaction** specify the Transaction's resource identifier as both the  `startTransactionRid` and `endTransactionRid`.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

### Example

```python
import time
import os
import foundry
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'dataset_rid_example' # str | The Resource Identifier (RID) of the Dataset that contains the File.
file_path = 'q3-data%2fmy-file.csv' # str | The File's path within the Dataset.
branch_id = 'branch_id_example' # str | The identifier (name) of the Branch that contains the File. Defaults to `master` for most enrollments. (optional)
start_transaction_rid = 'start_transaction_rid_example' # str | The Resource Identifier (RID) of the start Transaction. (optional)
end_transaction_rid = 'end_transaction_rid_example' # str | The Resource Identifier (RID) of the end Transaction. (optional)

try:
    api_response = foundry_client.datasets.get_file_content(dataset_rid, file_path, branch_id=branch_id, start_transaction_rid=start_transaction_rid, end_transaction_rid=end_transaction_rid)
    print("The response of DatasetsApiServiceApi -> get_file_content:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> get_file_content: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset that contains the File. |
**file_path** | **str**| The File's path within the Dataset. |
**branch_id** | **str**| The identifier (name) of the Branch that contains the File. Defaults to \`master\` for most enrollments. | \[optional\]
**start_transaction_rid** | **str**| The Resource Identifier (RID) of the start Transaction. | \[optional\]
**end_transaction_rid** | **str**| The Resource Identifier (RID) of the end Transaction. | \[optional\]

### Return type

**bytearray**

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_file_metadata**

> File get_file_metadata(dataset_rid, file_path, branch_id=branch_id, start_transaction_rid=start_transaction_rid, end_transaction_rid=end_transaction_rid)

Gets metadata about a File contained in a Dataset. By default this retrieves the file's metadata from the latest view of the default branch - `master` for most enrollments.  #### Advanced Usage  See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.   To **get a file's metadata from a specific Branch** specify the Branch's identifier as `branchId`. This will  retrieve metadata for the most recent version of the file since the latest snapshot transaction, or the earliest ancestor transaction of the branch if there are no snapshot transactions.  To **get a file's metadata from the resolved view of a transaction** specify the Transaction's resource identifier as `endTransactionRid`. This will retrieve metadata for the most recent version of the file since the latest snapshot transaction, or the earliest ancestor transaction if there are no snapshot transactions.  To **get a file's metadata from the resolved view of a range of transactions** specify the the start transaction's resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This will retrieve metadata for the most recent version of the file since the `startTransactionRid` up to the  `endTransactionRid`. Behavior is undefined when the start and end transactions do not belong to the same root-to-leaf path.  To **get a file's metadata from a specific transaction** specify the Transaction's resource identifier as both the  `startTransactionRid` and `endTransactionRid`.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

### Example

```python
import time
import os
import foundry
from foundry.models.file import File
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset that contains the File.
file_path = 'q3-data%2fmy-file.csv' # str | The File's path within the Dataset.
branch_id = 'branch_id_example' # str | The identifier (name) of the Branch that contains the File. Defaults to `master` for most enrollments. (optional)
start_transaction_rid = 'start_transaction_rid_example' # str | The Resource Identifier (RID) of the start Transaction. (optional)
end_transaction_rid = 'end_transaction_rid_example' # str | The Resource Identifier (RID) of the end Transaction. (optional)

try:
    api_response = foundry_client.datasets.get_file_metadata(dataset_rid, file_path, branch_id=branch_id, start_transaction_rid=start_transaction_rid, end_transaction_rid=end_transaction_rid)
    print("The response of DatasetsApiServiceApi -> get_file_metadata:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> get_file_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset that contains the File. |
**file_path** | **str**| The File's path within the Dataset. |
**branch_id** | **str**| The identifier (name) of the Branch that contains the File. Defaults to \`master\` for most enrollments. | \[optional\]
**start_transaction_rid** | **str**| The Resource Identifier (RID) of the start Transaction. | \[optional\]
**end_transaction_rid** | **str**| The Resource Identifier (RID) of the end Transaction. | \[optional\]

### Return type

[**File**](File.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_schema**

> object get_schema(dataset_rid, branch_id=branch_id, transaction_rid=transaction_rid, preview=preview)

Retrieves the Schema for a Dataset and Branch, if it exists.

### Example

```python
import time
import os
import foundry
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'dataset_rid_example' # str | The RID of the Dataset. 
branch_id = 'branch_id_example' # str | The ID of the Branch.  (optional)
transaction_rid = 'transaction_rid_example' # str | The TransactionRid that contains the Schema.  (optional)
preview = true # bool |  (optional)

try:
    api_response = foundry_client.datasets.get_schema(dataset_rid, branch_id=branch_id, transaction_rid=transaction_rid, preview=preview)
    print("The response of DatasetsApiServiceApi -> get_schema:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> get_schema: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The RID of the Dataset.  |
**branch_id** | **str**| The ID of the Branch.  | \[optional\]
**transaction_rid** | **str**| The TransactionRid that contains the Schema.  | \[optional\]
**preview** | **bool**|  | \[optional\]

### Return type

**object**

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No Content |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_transaction**

> Transaction get_transaction(dataset_rid, transaction_rid)

Gets a Transaction of a Dataset.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

### Example

```python
import time
import os
import foundry
from foundry.models.transaction import Transaction
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset that contains the Transaction.
transaction_rid = 'ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496' # str | The Resource Identifier (RID) of the Transaction.

try:
    api_response = foundry_client.datasets.get_transaction(dataset_rid, transaction_rid)
    print("The response of DatasetsApiServiceApi -> get_transaction:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> get_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset that contains the Transaction. |
**transaction_rid** | **str**| The Resource Identifier (RID) of the Transaction. |

### Return type

[**Transaction**](Transaction.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **list_branches**

> ListBranchesResponse list_branches(dataset_rid, page_size=page_size, page_token=page_token)

Lists the Branches of a Dataset.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_branches_response import ListBranchesResponse
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset on which to list Branches.
page_size = 56 # int | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    api_response = foundry_client.datasets.list_branches(dataset_rid, page_size=page_size, page_token=page_token)
    print("The response of DatasetsApiServiceApi -> list_branches:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> list_branches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset on which to list Branches. |
**page_size** | **int**| The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | \[optional\]
**page_token** | **str**|  | \[optional\]

### Return type

[**ListBranchesResponse**](ListBranchesResponse.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **list_files**

> ListFilesResponse list_files(dataset_rid, branch_id=branch_id, start_transaction_rid=start_transaction_rid, end_transaction_rid=end_transaction_rid, page_size=page_size, page_token=page_token)

Lists Files contained in a Dataset. By default files are listed on the latest view of the default  branch - `master` for most enrollments.  #### Advanced Usage  See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.  To **list files on a specific Branch** specify the Branch's identifier as `branchId`. This will include the most recent version of all files since the latest snapshot transaction, or the earliest ancestor transaction of the  branch if there are no snapshot transactions.  To **list files on the resolved view of a transaction** specify the Transaction's resource identifier as `endTransactionRid`. This will include the most recent version of all files since the latest snapshot transaction, or the earliest ancestor transaction if there are no snapshot transactions.  To **list files on the resolved view of a range of transactions** specify the the start transaction's resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This will include the most recent version of all files since the `startTransactionRid` up to the `endTransactionRid`. Note that an intermediate snapshot transaction will remove all files from the view. Behavior is undefined when  the start and end transactions do not belong to the same root-to-leaf path.  To **list files on a specific transaction** specify the Transaction's resource identifier as both the  `startTransactionRid` and `endTransactionRid`. This will include only files that were modified as part of that Transaction.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_files_response import ListFilesResponse
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'dataset_rid_example' # str | The Resource Identifier (RID) of the Dataset on which to list Files.
branch_id = 'branch_id_example' # str | The identifier (name) of the Branch on which to list Files. Defaults to `master` for most enrollments. (optional)
start_transaction_rid = 'start_transaction_rid_example' # str | The Resource Identifier (RID) of the start Transaction. (optional)
end_transaction_rid = 'end_transaction_rid_example' # str | The Resource Identifier (RID) of the end Transaction. (optional)
page_size = 56 # int | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    api_response = foundry_client.datasets.list_files(dataset_rid, branch_id=branch_id, start_transaction_rid=start_transaction_rid, end_transaction_rid=end_transaction_rid, page_size=page_size, page_token=page_token)
    print("The response of DatasetsApiServiceApi -> list_files:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> list_files: %s\n" % e)
```


### Read the contents of a file from a dataset (by exploration / listing)

```python
import foundry

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

files = list(foundry_client.datasets.list_files(dataset_rid="..."))

file_path = files[0].path

foundry_client.datasets.File.get_content(dataset_rid = "...", file_path=file_path).read()
```

```
b'Hello!'
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset on which to list Files. |
**branch_id** | **str**| The identifier (name) of the Branch on which to list Files. Defaults to \`master\` for most enrollments. | \[optional\]
**start_transaction_rid** | **str**| The Resource Identifier (RID) of the start Transaction. | \[optional\]
**end_transaction_rid** | **str**| The Resource Identifier (RID) of the end Transaction. | \[optional\]
**page_size** | **int**| The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | \[optional\]
**page_token** | **str**|  | \[optional\]

### Return type

[**ListFilesResponse**](ListFilesResponse.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **put_schema**

> put_schema(dataset_rid, body, branch_id=branch_id, preview=preview)

Puts a Schema on an existing Dataset and Branch.

### Example

```python
import time
import os
import foundry
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'dataset_rid_example' # str | The RID of the Dataset on which to put the Schema. 
body = None # object | 
branch_id = 'branch_id_example' # str | The ID of the Branch on which to put the Schema.  (optional)
preview = true # bool |  (optional)

try:
    foundry_client.datasets.put_schema(dataset_rid, body, branch_id=branch_id, preview=preview)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> put_schema: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The RID of the Dataset on which to put the Schema.  |
**body** | **object**|  |
**branch_id** | **str**| The ID of the Branch on which to put the Schema.  | \[optional\]
**preview** | **bool**|  | \[optional\]

### Return type

void (empty response body)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **read_table**

> bytearray read_table(dataset_rid, format, branch_id=branch_id, start_transaction_rid=start_transaction_rid, end_transaction_rid=end_transaction_rid, columns=columns, row_limit=row_limit, preview=preview)

> [!WARNING]
> This endpoint is in preview and may be modified or removed at any time.   To use this endpoint, add `preview=true` to the request query parameters.   Furthermore, this endpoint currently does not support views (Virtual datasets composed of other datasets). :::  Gets the content of a dataset as a table in the specified format.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

### Example

```python
import time
import os
import foundry
from foundry.models.table_export_format import TableExportFormat
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'dataset_rid_example' # str | The RID of the Dataset. 
format = foundry.TableExportFormat() # TableExportFormat | The export format. Must be `ARROW` or `CSV`. 
branch_id = 'branch_id_example' # str | The identifier (name) of the Branch. (optional)
start_transaction_rid = 'start_transaction_rid_example' # str | The Resource Identifier (RID) of the start Transaction. (optional)
end_transaction_rid = 'end_transaction_rid_example' # str | The Resource Identifier (RID) of the end Transaction. (optional)
columns = ['columns_example'] # List[str] | A subset of the dataset columns to include in the result. Defaults to all columns.  (optional)
row_limit = 56 # int | A limit on the number of rows to return. Note that row ordering is non-deterministic.  (optional)
preview = True # bool | A boolean flag that, when set to true, enables the use of beta features in preview mode.  (optional)

try:
    api_response = foundry_client.datasets.read_table(dataset_rid, format, branch_id=branch_id, start_transaction_rid=start_transaction_rid, end_transaction_rid=end_transaction_rid, columns=columns, row_limit=row_limit, preview=preview)
    print("The response of DatasetsApiServiceApi -> read_table:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> read_table: %s\n" % e)
```


### Read a Foundry Dataset as a CSV

```python
import foundry
from foundry.models import TableExportFormat
from foundry.rest import ApiException

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

try:
    api_response = foundry_client.datasets.read_table(dataset_rid="...", format="CSV", columns=[...])

    with open("my_table.csv", "wb") as f:
        f.write(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> read_table: %s\n" % e)
```

### Read a Foundry Dataset into a Pandas DataFrame

> [!IMPORTANT]
> For this example to work, you will need to have `pyarrow` installed in your Python environment.

```python
import foundry
from foundry.models import TableExportFormat
from foundry.rest import ApiException
import pyarrow as pa

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

try:
    api_response = foundry_client.datasets.read_table(dataset_rid="...", format="ARROW", columns=[...])
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



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The RID of the Dataset.  |
**format** | [**TableExportFormat**](TableExportFormat.md)| The export format. Must be \`ARROW\` or \`CSV\`.  |
**branch_id** | **str**| The identifier (name) of the Branch. | \[optional\]
**start_transaction_rid** | **str**| The Resource Identifier (RID) of the start Transaction. | \[optional\]
**end_transaction_rid** | **str**| The Resource Identifier (RID) of the end Transaction. | \[optional\]
**columns** | [**List\[str\]**](List%5Bstr%5D.md)| A subset of the dataset columns to include in the result. Defaults to all columns.  | \[optional\]
**row_limit** | **int**| A limit on the number of rows to return. Note that row ordering is non-deterministic.  | \[optional\]
**preview** | **bool**| A boolean flag that, when set to true, enables the use of beta features in preview mode.  | \[optional\]

### Return type

**bytearray**

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The content stream. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **upload_file**

> File upload_file(dataset_rid, file_path, body, branch_id=branch_id, transaction_type=transaction_type, transaction_rid=transaction_rid)

Uploads a File to an existing Dataset. The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.  By default the file is uploaded to a new transaction on the default branch - `master` for most enrollments. If the file already exists only the most recent version will be visible in the updated view.  #### Advanced Usage  See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.   To **upload a file to a specific Branch** specify the Branch's identifier as `branchId`. A new transaction will  be created and committed on this branch. By default the TransactionType will be `UPDATE`, to override this default specify `transactionType` in addition to `branchId`.  See [createBranch](/docs/foundry/api/datasets-resources/branches/create-branch/) to create a custom branch.  To **upload a file on a manually opened transaction** specify the Transaction's resource identifier as `transactionRid`. This is useful for uploading multiple files in a single transaction.  See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to open a transaction.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

### Example

```python
import time
import os
import foundry
from foundry.models.file import File
from foundry.models.transaction_type import TransactionType
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth())

dataset_rid = 'dataset_rid_example' # str | The Resource Identifier (RID) of the Dataset on which to upload the File.
file_path = 'q3-data%2fmy-file.csv' # str | The File's path within the Dataset.
body = None # bytearray | 
branch_id = 'branch_id_example' # str | The identifier (name) of the Branch on which to upload the File. Defaults to `master` for most enrollments. (optional)
transaction_type = foundry.TransactionType() # TransactionType | The type of the Transaction to create when using branchId. Defaults to `UPDATE`. (optional)
transaction_rid = 'transaction_rid_example' # str | The Resource Identifier (RID) of the open Transaction on which to upload the File. (optional)

try:
    api_response = foundry_client.datasets.upload_file(dataset_rid, file_path, body, branch_id=branch_id, transaction_type=transaction_type, transaction_rid=transaction_rid)
    print("The response of DatasetsApiServiceApi -> upload_file:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DatasetsApiServiceApi -> upload_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**dataset_rid** | **str**| The Resource Identifier (RID) of the Dataset on which to upload the File. |
**file_path** | **str**| The File's path within the Dataset. |
**body** | **bytearray**|  |
**branch_id** | **str**| The identifier (name) of the Branch on which to upload the File. Defaults to \`master\` for most enrollments. | \[optional\]
**transaction_type** | [**TransactionType**](TransactionType.md)| The type of the Transaction to create when using branchId. Defaults to \`UPDATE\`. | \[optional\]
**transaction_rid** | **str**| The Resource Identifier (RID) of the open Transaction on which to upload the File. | \[optional\]

### Return type

[**File**](File.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)
