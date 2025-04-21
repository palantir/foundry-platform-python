# UserProviderInfo

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/admin/users/{userId}/providerInfo | Public Beta |
[**replace**](#replace) | **PUT** /v2/admin/users/{userId}/providerInfo | Public Beta |

# **get**
Get the UserProviderInfo.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | PrincipalId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**UserProviderInfo**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# PrincipalId
user_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.User.ProviderInfo.get(user_id, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ProviderInfo.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | UserProviderInfo  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the UserProviderInfo.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | PrincipalId |  |  |
**provider_id** | ProviderId | The ID of the User in the external authentication provider. This value is determined by the authentication provider. At most one User can have a given provider ID in a given Realm.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**UserProviderInfo**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# PrincipalId
user_id = None
# ProviderId | The ID of the User in the external authentication provider. This value is determined by the authentication provider. At most one User can have a given provider ID in a given Realm.
provider_id = "2838c8f3-d76a-4e99-acf1-1dee537e4c48"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.User.ProviderInfo.replace(
        user_id, provider_id=provider_id, preview=preview
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ProviderInfo.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | UserProviderInfo  | The replaced UserProviderInfo | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

