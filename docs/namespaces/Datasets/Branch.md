# Branch

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v1/datasets/{datasetRid}/branches |
[**get**](#get) | **GET** /v1/datasets/{datasetRid}/branches/{branchId} |
[**delete**](#delete) | **DELETE** /v1/datasets/{datasetRid}/branches/{branchId} |
[**iterator**](#iterator) | **GET** /v1/datasets/{datasetRid}/branches |

# **create**
Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset on which to create the Branch. |  |
**create_branch_request** | CreateBranchRequest | CreateBranchRequest |  |

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

dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"  # DatasetRid | The Resource Identifier (RID) of the Dataset on which to create the Branch.
create_branch_request = {"branchId": "my-branch"}  # CreateBranchRequest | CreateBranchRequest


try:
    api_response = foundry_client.datasets.Branch.create(
        dataset_rid, create_branch_request=create_branch_request
    )
    print("The Branch.create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.create: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Branch  | A Branch of a Dataset.  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Get a Branch of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Branch. |  |
**branch_id** | BranchId | The identifier (name) of the Branch. |  |

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

dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"  # DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Branch.
branch_id = "master"  # BranchId | The identifier (name) of the Branch.


try:
    api_response = foundry_client.datasets.Branch.get(
        dataset_rid,
        branch_id,
    )
    print("The Branch.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Branch  | A Branch of a Dataset.  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete**
Deletes the Branch with the given BranchId.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Branch. |  |
**branch_id** | BranchId | The identifier (name) of the Branch. |  |

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

dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"  # DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Branch.
branch_id = "my-branch"  # BranchId | The identifier (name) of the Branch.


try:
    api_response = foundry_client.datasets.Branch.delete(
        dataset_rid,
        branch_id,
    )
    print("The Branch.delete response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.delete: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  | No content | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **iterator**
Lists the Branches of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset on which to list Branches. |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListBranchesResponse**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da" # DatasetRid | The Resource Identifier (RID) of the Dataset on which to list Branches.
page_size = None # Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details. 
page_token = None # Optional[PageToken] | pageToken


try:
    api_response = foundry_client.datasets.Branch.iterator(
dataset_rid,page_size=page_sizepage_token=page_token    )
    print("The Branch.iterator response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.iterator: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListBranchesResponse  | ListBranchesResponse | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

