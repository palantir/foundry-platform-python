# Branch

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v2/datasets/{datasetRid}/branches |
[**delete**](#delete) | **DELETE** /v2/datasets/{datasetRid}/branches/{branchName} |
[**get**](#get) | **GET** /v2/datasets/{datasetRid}/branches/{branchName} |
[**list**](#list) | **GET** /v2/datasets/{datasetRid}/branches |
[**page**](#page) | **GET** /v2/datasets/{datasetRid}/branches |

# **create**
Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**create_branch_request** | Union[CreateBranchRequest, CreateBranchRequestDict] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Branch**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None

# Union[CreateBranchRequest, CreateBranchRequestDict] | Body of the request
create_branch_request = {
    "transactionRid": "ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4",
    "name": "master",
}

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.datasets.Dataset.Branch.create(
        dataset_rid,
        create_branch_request,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.create: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Branch  | The created Branch | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **delete**
Deletes the Branch with the given BranchName.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_name** | BranchName | branchName |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None

# BranchName | branchName
branch_name = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.datasets.Dataset.Branch.delete(
        dataset_rid,
        branch_name,
        preview=preview,
    )
    print("The delete response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.delete: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **get**
Get a Branch of a Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_name** | BranchName | branchName |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Branch**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None

# BranchName | branchName
branch_name = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.datasets.Dataset.Branch.get(
        dataset_rid,
        branch_name,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.get: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Branch  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **list**
Lists the Branches of a Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[Branch]**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None

# Optional[PageSize] | pageSize
page_size = None

# Optional[PreviewMode] | preview
preview = None


try:
    for branch in foundry_client.datasets.Dataset.Branch.list(
        dataset_rid,
        page_size=page_size,
        preview=preview,
    ):
        pprint(branch)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.list: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListBranchesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **page**
Lists the Branches of a Dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListBranchesResponse**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.datasets.Dataset.Branch.page(
        dataset_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.page: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListBranchesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

