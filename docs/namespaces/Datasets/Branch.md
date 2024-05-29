# Branch

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v1/datasets/{datasetRid}/branches |
[**delete**](#delete) | **DELETE** /v1/datasets/{datasetRid}/branches/{branchId} |
[**get**](#get) | **GET** /v1/datasets/{datasetRid}/branches/{branchId} |
[**list**](#list) | **GET** /v1/datasets/{datasetRid}/branches |
[**page**](#page) | **GET** /v1/datasets/{datasetRid}/branches |

# **create**
Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**create_branch_request** | Union[CreateBranchRequest, CreateBranchRequestDict] | Body of the request |  |

### Return type
**Branch**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"

# Union[CreateBranchRequest, CreateBranchRequestDict] | Body of the request
create_branch_request = {"branchId": "my-branch"}


try:
    api_response = foundry_client.datasets.Dataset.Branch.create(
        dataset_rid,
        create_branch_request,
    )
    print("The create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.create: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Branch  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete**
Deletes the Branch with the given BranchId.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_id** | BranchId | branchId |  |

### Return type
**None**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"

# BranchId | branchId
branch_id = "my-branch"


try:
    api_response = foundry_client.datasets.Dataset.Branch.delete(
        dataset_rid,
        branch_id,
    )
    print("The delete response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.delete: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  | Branch deleted. | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Get a Branch of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_id** | BranchId | branchId |  |

### Return type
**Branch**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"

# BranchId | branchId
branch_id = "master"


try:
    api_response = foundry_client.datasets.Dataset.Branch.get(
        dataset_rid,
        branch_id,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Branch  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**
Lists the Branches of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |

### Return type
**ResourceIterator[Branch]**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"

# Optional[PageSize] | pageSize
page_size = None


try:
    for branch in foundry_client.datasets.Dataset.Branch.list(dataset_rid, page_size=page_size):
        pprint(branch)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListBranchesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **page**
Lists the Branches of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListBranchesResponse**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None



try:
    api_response = foundry_client.datasets.Dataset.Branch.page(dataset_rid,page_size=page_sizepage_token=page_token)
    print("The page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.page: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListBranchesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

