# Group

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v2/security/groups |
[**delete**](#delete) | **DELETE** /v2/security/groups/{groupId} |
[**get**](#get) | **GET** /v2/security/groups/{groupId} |
[**list**](#list) | **GET** /v2/security/groups |
[**page**](#page) | **GET** /v2/security/groups |
[**search**](#search) | **POST** /v2/security/groups/search |

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
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[CreateGroupRequest, CreateGroupRequestDict] | Body of the request
create_group_request = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.Group.create(
        create_group_request,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.create: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Group  | The created Group | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

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
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# PrincipalId | groupId
group_id = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.Group.delete(
        group_id,
        preview=preview,
    )
    print("The delete response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.delete: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

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
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# PrincipalId | groupId
group_id = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.Group.get(
        group_id,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Group  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

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
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | pageSize
page_size = None

# Optional[PreviewMode] | preview
preview = None


try:
    for group in foundry_client.security.Group.list(
        page_size=page_size,
        preview=preview,
    ):
        pprint(group)
except PalantirRPCException as e:
    print("HTTP error when calling Group.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

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
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.Group.page(
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

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

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
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[SearchGroupsRequest, SearchGroupsRequestDict] | Body of the request
search_groups_request = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.Group.search(
        search_groups_request,
        preview=preview,
    )
    print("The search response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Group.search: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchGroupsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

