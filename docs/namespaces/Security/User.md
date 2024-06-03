# User

Method | HTTP request |
------------- | ------------- |
[**delete**](#delete) | **DELETE** /v2/security/users/{userId} |
[**get**](#get) | **GET** /v2/security/users/{userId} |
[**get_current**](#get_current) | **GET** /v2/security/users/getCurrent |
[**list**](#list) | **GET** /v2/security/users |
[**page**](#page) | **GET** /v2/security/users |
[**profile_picture**](#profile_picture) | **GET** /v2/security/users/{userId}/profilePicture |
[**search**](#search) | **POST** /v2/security/users/search |

# **delete**
Deletes the given User

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | PrincipalId | userId |  |
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

# PrincipalId | userId
user_id = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.User.delete(
        user_id,
        preview=preview,
    )
    print("The delete response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling User.delete: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Get the User

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | PrincipalId | userId |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**User**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# PrincipalId | userId
user_id = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.User.get(
        user_id,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling User.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | User  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_current**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**User**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.User.get_current(
        preview=preview,
    )
    print("The get_current response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling User.get_current: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | User  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**
Lists all Users

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[User]**

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
    for user in foundry_client.security.User.list(
        page_size=page_size,
        preview=preview,
    ):
        pprint(user)
except PalantirRPCException as e:
    print("HTTP error when calling User.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListUsersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **page**
Lists all Users

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListUsersResponse**

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
    api_response = foundry_client.security.User.page(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling User.page: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListUsersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **profile_picture**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | PrincipalId | userId |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**bytes**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# PrincipalId | userId
user_id = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.User.profile_picture(
        user_id,
        preview=preview,
    )
    print("The profile_picture response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling User.profile_picture: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**search_users_request** | Union[SearchUsersRequest, SearchUsersRequestDict] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**SearchUsersResponse**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[SearchUsersRequest, SearchUsersRequestDict] | Body of the request
search_users_request = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.security.User.search(
        search_users_request,
        preview=preview,
    )
    print("The search response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling User.search: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchUsersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

