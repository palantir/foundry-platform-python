# GroupMembership

Method | HTTP request |
------------- | ------------- |
[**list**](#list) | **GET** /v2/security/users/{userId}/groupMemberships |
[**page**](#page) | **GET** /v2/security/users/{userId}/groupMemberships |

# **list**
Lists all GroupMemberships

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | PrincipalId | userId |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transitive** | Optional[StrictBool] | transitive | [optional] |

### Return type
**ResourceIterator[GroupMembership]**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# PrincipalId | userId
user_id = None

# Optional[PageSize] | pageSize
page_size = None

# Optional[PreviewMode] | preview
preview = None

# Optional[StrictBool] | transitive
transitive = None



try:
    for group_membership in foundry_client.security.User.GroupMembership.list(user_id,page_size=page_sizepreview=previewtransitive=transitive):
        pprint(group_membership)
except PalantirRPCException as e:
    print("HTTP error when calling GroupMembership.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupMembershipsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **page**
Lists all GroupMemberships

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | PrincipalId | userId |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transitive** | Optional[StrictBool] | transitive | [optional] |

### Return type
**ListGroupMembershipsResponse**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# PrincipalId | userId
user_id = None

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None

# Optional[PreviewMode] | preview
preview = None

# Optional[StrictBool] | transitive
transitive = None



try:
    api_response = foundry_client.security.User.GroupMembership.page(user_id,page_size=page_sizepage_token=page_tokenpreview=previewtransitive=transitive)
    print("The page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling GroupMembership.page: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupMembershipsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

