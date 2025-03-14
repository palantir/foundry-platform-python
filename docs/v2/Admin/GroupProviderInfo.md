# GroupProviderInfo

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/admin/groups/{groupId}/providerInfo | Public Beta |
[**replace**](#replace) | **PUT** /v2/admin/groups/{groupId}/providerInfo | Public Beta |

# **get**
Get the GroupProviderInfo.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GroupProviderInfo**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# PrincipalId
group_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Group.ProviderInfo.get(
        group_id,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling ProviderInfo.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GroupProviderInfo  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the GroupProviderInfo.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId |  |  |
**provider_id** | str | The ID of the Group in the external authentication provider. This value is determined by the authentication provider. At most one Group can have a given provider ID in a given Realm.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GroupProviderInfo**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# PrincipalId
group_id = None
# str | The ID of the Group in the external authentication provider. This value is determined by the authentication provider. At most one Group can have a given provider ID in a given Realm.
provider_id = "2838c8f3-d76a-4e99-acf1-1dee537e4c48"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Group.ProviderInfo.replace(
        group_id,
        provider_id=provider_id,
        preview=preview,
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling ProviderInfo.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GroupProviderInfo  | The replaced GroupProviderInfo | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

