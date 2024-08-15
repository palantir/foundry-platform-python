# Group

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v2/admin/groups |
[**delete**](#delete) | **DELETE** /v2/admin/groups/{groupId} |
[**get**](#get) | **GET** /v2/admin/groups/{groupId} |
[**get_batch**](#get_batch) | **POST** /v2/admin/groups/getBatch |
[**list**](#list) | **GET** /v2/admin/groups |
[**page**](#page) | **GET** /v2/admin/groups |
[**search**](#search) | **POST** /v2/admin/groups/search |

# **create**
Creates a new Group

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**create_group_request** | Union[CreateGroupRequest, CreateGroupRequestDict] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Group**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[CreateGroupRequest, CreateGroupRequestDict] | Body of the request
create_group_request = {
    "name": "Data Source Admins",
    "organizations": ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"],
    "description": "Create and modify data sources in the platform",
}

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.create(
        create_group_request,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.create: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Group  | The created Group | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **delete**
Deletes the given Group

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId | groupId |  |
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

# PrincipalId | groupId
group_id = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.delete(
        group_id,
        preview=preview,
    )
    print("The delete response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.delete: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **get**
Get the Group

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId | groupId |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Group**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# PrincipalId | groupId
group_id = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.get(
        group_id,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.get: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Group  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **get_batch**
Execute multiple get requests on Group.

The maximum batch size for this endpoint is 500.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | Union[List[GetGroupsBatchRequestElement], List[GetGroupsBatchRequestElementDict]] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**GetGroupsBatchResponse**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[List[GetGroupsBatchRequestElement], List[GetGroupsBatchRequestElementDict]] | Body of the request
body = {"groupId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.get_batch(
        body,
        preview=preview,
    )
    print("The get_batch response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.get_batch: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetGroupsBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **list**
Lists all Groups

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[Group]**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | pageSize
page_size = None

# Optional[PreviewMode] | preview
preview = None


try:
    for group in foundry_client.admin.Group.list(
        page_size=page_size,
        preview=preview,
    ):
        pprint(group)
except PalantirRPCException as e:
    print("HTTP error when calling Group.list: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **page**
Lists all Groups

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListGroupsResponse**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.page(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.page: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **search**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**search_groups_request** | Union[SearchGroupsRequest, SearchGroupsRequestDict] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**SearchGroupsResponse**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[SearchGroupsRequest, SearchGroupsRequestDict] | Body of the request
search_groups_request = {
    "pageSize": 100,
    "where": {"type": "queryString"},
    "pageToken": "v1.VGhlcmUgaXMgc28gbXVjaCBsZWZ0IHRvIGJ1aWxkIC0gcGFsYW50aXIuY29tL2NhcmVlcnMv",
}

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.search(
        search_groups_request,
        preview=preview,
    )
    print("The search response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.search: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchGroupsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

