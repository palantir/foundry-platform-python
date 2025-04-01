# Branch

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/datasets/{datasetRid}/branches | Stable |
[**delete**](#delete) | **DELETE** /v2/datasets/{datasetRid}/branches/{branchName} | Stable |
[**get**](#get) | **GET** /v2/datasets/{datasetRid}/branches/{branchName} | Stable |
[**list**](#list) | **GET** /v2/datasets/{datasetRid}/branches | Stable |

# **create**
Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**name** | BranchName |  |  |
**transaction_rid** | Optional[TransactionRid] | The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction. | [optional] |

### Return type
**Branch**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
name = "master"
# Optional[TransactionRid] | The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction.
transaction_rid = "ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4"


try:
    api_response = foundry_client.datasets.Dataset.Branch.create(
        dataset_rid, name=name, transaction_rid=transaction_rid
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Branch.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Branch  | The created Branch | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **delete**
Deletes the Branch with the given BranchName.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**branch_name** | BranchName |  |  |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
branch_name = None


try:
    api_response = foundry_client.datasets.Dataset.Branch.delete(dataset_rid, branch_name)
    print("The delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Branch.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get a Branch of a Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**branch_name** | BranchName |  |  |

### Return type
**Branch**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
branch_name = None


try:
    api_response = foundry_client.datasets.Dataset.Branch.get(dataset_rid, branch_name)
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Branch.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Branch  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the Branches of a Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |

### Return type
**ListBranchesResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    for branch in client.datasets.Dataset.Branch.list(
        dataset_rid, page_size=page_size, page_token=page_token
    ):
        pprint(branch)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Branch.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListBranchesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

