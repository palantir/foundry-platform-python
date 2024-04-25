# User

Method | HTTP request |
------------- | ------------- |
[**delete**](#delete) | **DELETE** /v2/security/users/{userId} |
[**get**](#get) | **GET** /v2/security/users/{userId} |
[**me**](#me) | **GET** /v2/security/users/me |
[**profile_picture**](#profile_picture) | **GET** /v2/security/users/{userId}/profilePicture |

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
    api_response = foundry_client.security.User.delete(user_id, preview=preview)
    print("The User.delete response:\n")
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
    api_response = foundry_client.security.User.get(user_id, preview=preview)
    print("The User.get response:\n")
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

# **me**


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
    api_response = foundry_client.security.User.me(preview=preview)
    print("The User.me response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling User.me: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | User  |  | application/json |

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
    api_response = foundry_client.security.User.profile_picture(user_id, preview=preview)
    print("The User.profile_picture response:\n")
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

