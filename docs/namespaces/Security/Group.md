# Group

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v2/security/groups |
[**delete**](#delete) | **DELETE** /v2/security/groups/{groupId} |
[**get**](#get) | **GET** /v2/security/groups/{groupId} |

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
    api_response = foundry_client.security.Group.create(create_group_request, preview=preview)
    print("The Group.create response:\n")
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
    api_response = foundry_client.security.Group.delete(group_id, preview=preview)
    print("The Group.delete response:\n")
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
    api_response = foundry_client.security.Group.get(group_id, preview=preview)
    print("The Group.get response:\n")
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

