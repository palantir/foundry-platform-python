# GroupMembership

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**list**](#list) | **GET** /v2/admin/users/{userId}/groupMemberships | Stable |
[**page**](#page) | **GET** /v2/admin/users/{userId}/groupMemberships | Stable |

# **list**
Lists all Groups a given User is a member of.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, 
it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. 
To get the next page, make the same request again, but set the value of the `pageToken` query parameter 
to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field 
in the response, you are on the last page.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | core_models.PrincipalId | userId |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**transitive** | typing.Optional[bool] | transitive | [optional] |

### Return type
**ListGroupMembershipsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# core_models.PrincipalId | userId
user_id = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[bool] | transitive
transitive = None


try:
    for group_membership in foundry_client.admin.User.GroupMembership.list(
        user_id,
        page_size=page_size,
        page_token=page_token,
        transitive=transitive,
    ):
        pprint(group_membership)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling GroupMembership.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupMembershipsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists all Groups a given User is a member of.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, 
it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. 
To get the next page, make the same request again, but set the value of the `pageToken` query parameter 
to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field 
in the response, you are on the last page.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | core_models.PrincipalId | userId |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**transitive** | typing.Optional[bool] | transitive | [optional] |

### Return type
**ListGroupMembershipsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# core_models.PrincipalId | userId
user_id = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[bool] | transitive
transitive = None


try:
    api_response = foundry_client.admin.User.GroupMembership.page(
        user_id,
        page_size=page_size,
        page_token=page_token,
        transitive=transitive,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling GroupMembership.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupMembershipsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

