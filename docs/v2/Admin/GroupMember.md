# GroupMember

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/admin/groups/{groupId}/groupMembers/add | Stable |
[**list**](#list) | **GET** /v2/admin/groups/{groupId}/groupMembers | Stable |
[**page**](#page) | **GET** /v2/admin/groups/{groupId}/groupMembers | Stable |
[**remove**](#remove) | **POST** /v2/admin/groups/{groupId}/groupMembers/remove | Stable |

# **add**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | core_models.PrincipalId | groupId |  |
**principal_ids** | typing.List[core_models.PrincipalId] |  |  |
**expiration** | typing.Optional[GroupMembershipExpiration] |  | [optional] |

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

# core_models.PrincipalId | groupId
group_id = None
# typing.List[core_models.PrincipalId] |
principal_ids = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# typing.Optional[GroupMembershipExpiration] |
expiration = None


try:
    api_response = foundry_client.admin.Group.GroupMember.add(
        group_id,
        principal_ids=principal_ids,
        expiration=expiration,
    )
    print("The add response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling GroupMember.add: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all members (which can be a User or a Group) of a given Group.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, 
it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. 
To get the next page, make the same request again, but set the value of the `pageToken` query parameter 
to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field 
in the response, you are on the last page.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | core_models.PrincipalId | groupId |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**transitive** | typing.Optional[bool] | transitive | [optional] |

### Return type
**ListGroupMembersResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# core_models.PrincipalId | groupId
group_id = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[bool] | transitive
transitive = None


try:
    for group_member in foundry_client.admin.Group.GroupMember.list(
        group_id,
        page_size=page_size,
        page_token=page_token,
        transitive=transitive,
    ):
        pprint(group_member)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling GroupMember.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupMembersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists all members (which can be a User or a Group) of a given Group.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, 
it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. 
To get the next page, make the same request again, but set the value of the `pageToken` query parameter 
to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field 
in the response, you are on the last page.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | core_models.PrincipalId | groupId |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**transitive** | typing.Optional[bool] | transitive | [optional] |

### Return type
**ListGroupMembersResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# core_models.PrincipalId | groupId
group_id = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[bool] | transitive
transitive = None


try:
    api_response = foundry_client.admin.Group.GroupMember.page(
        group_id,
        page_size=page_size,
        page_token=page_token,
        transitive=transitive,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling GroupMember.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupMembersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **remove**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | core_models.PrincipalId | groupId |  |
**principal_ids** | typing.List[core_models.PrincipalId] |  |  |

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

# core_models.PrincipalId | groupId
group_id = None
# typing.List[core_models.PrincipalId] |
principal_ids = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]


try:
    api_response = foundry_client.admin.Group.GroupMember.remove(
        group_id,
        principal_ids=principal_ids,
    )
    print("The remove response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling GroupMember.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

