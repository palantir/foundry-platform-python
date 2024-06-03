# GroupMember

Method | HTTP request |
------------- | ------------- |
[**add**](#add) | **POST** /v2/security/groups/{groupId}/groupMembers/add |
[**list**](#list) | **GET** /v2/security/groups/{groupId}/groupMembers |
[**page**](#page) | **GET** /v2/security/groups/{groupId}/groupMembers |
[**remove**](#remove) | **POST** /v2/security/groups/{groupId}/groupMembers/remove |

# **add**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId | groupId |  |
**add_group_members_request** | Union[AddGroupMembersRequest, AddGroupMembersRequestDict] | Body of the request |  |
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

# Union[AddGroupMembersRequest, AddGroupMembersRequestDict] | Body of the request
add_group_members_request = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.Group.GroupMember.add(
        group_id,
        add_group_members_request,
        preview=preview,
    )
    print("The add response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling GroupMember.add: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**
Lists all GroupMembers

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId | groupId |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transitive** | Optional[StrictBool] | transitive | [optional] |

### Return type
**ResourceIterator[GroupMember]**

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

# Optional[PageSize] | pageSize
page_size = None

# Optional[PreviewMode] | preview
preview = None

# Optional[StrictBool] | transitive
transitive = None


try:
    for group_member in foundry_client.security.Group.GroupMember.list(
        group_id,
        page_size=page_size,
        preview=preview,
        transitive=transitive,
    ):
        pprint(group_member)
except PalantirRPCException as e:
    print("HTTP error when calling GroupMember.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupMembersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **page**
Lists all GroupMembers

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId | groupId |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transitive** | Optional[StrictBool] | transitive | [optional] |

### Return type
**ListGroupMembersResponse**

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

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None

# Optional[PreviewMode] | preview
preview = None

# Optional[StrictBool] | transitive
transitive = None


try:
    api_response = foundry_client.security.Group.GroupMember.page(
        group_id,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        transitive=transitive,
    )
    print("The page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling GroupMember.page: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupMembersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId | groupId |  |
**remove_group_members_request** | Union[RemoveGroupMembersRequest, RemoveGroupMembersRequestDict] | Body of the request |  |
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

# Union[RemoveGroupMembersRequest, RemoveGroupMembersRequestDict] | Body of the request
remove_group_members_request = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.Group.GroupMember.remove(
        group_id,
        remove_group_members_request,
        preview=preview,
    )
    print("The remove response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling GroupMember.remove: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

