# Branch

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v1/datasets/{datasetRid}/branches | Stable |
[**delete**](#delete) | **DELETE** /v1/datasets/{datasetRid}/branches/{branchId} | Stable |
[**get**](#get) | **GET** /v1/datasets/{datasetRid}/branches/{branchId} | Stable |
[**list**](#list) | **GET** /v1/datasets/{datasetRid}/branches | Stable |
[**page**](#page) | **GET** /v1/datasets/{datasetRid}/branches | Stable |

# **create**
Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset on which to create the Branch. |  |
**branch_id** | BranchId |  |  |
**transaction_rid** | Optional[TransactionRid] |  | [optional] |

### Return type
**Branch**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | The Resource Identifier (RID) of the Dataset on which to create the Branch.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# BranchId
branch_id = "my-branch"
# Optional[TransactionRid]
transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.Branch.create(
        dataset_rid,
        branch_id=branch_id,
        transaction_rid=transaction_rid,
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
**200** | Branch  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

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
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Branch.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# BranchId | The identifier (name) of the Branch.
branch_id = "my-branch"


try:
    api_response = foundry_client.datasets.Dataset.Branch.delete(
        dataset_rid,
        branch_id,
    )
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
**204** | None  | Branch deleted. | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

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
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | The Resource Identifier (RID) of the Dataset that contains the Branch.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# BranchId | The identifier (name) of the Branch.
branch_id = "master"


try:
    api_response = foundry_client.datasets.Dataset.Branch.get(
        dataset_rid,
        branch_id,
    )
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

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **list**
Lists the Branches of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset on which to list Branches. |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListBranchesResponse**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | The Resource Identifier (RID) of the Dataset on which to list Branches.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for branch in foundry_client.datasets.Dataset.Branch.list(
        dataset_rid,
        page_size=page_size,
        page_token=page_token,
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

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **page**
Lists the Branches of a Dataset.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | The Resource Identifier (RID) of the Dataset on which to list Branches. |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListBranchesResponse**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | The Resource Identifier (RID) of the Dataset on which to list Branches.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None


try:
    api_response = foundry_client.datasets.Dataset.Branch.page(
        dataset_rid,
        page_size=page_size,
        page_token=page_token,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Branch.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListBranchesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

