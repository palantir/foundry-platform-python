# GroupMembershipExpirationPolicy

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/admin/groups/{groupId}/membershipExpirationPolicy | Public Beta |
[**replace**](#replace) | **PUT** /v2/admin/groups/{groupId}/membershipExpirationPolicy | Public Beta |

# **get**
Get the GroupMembershipExpirationPolicy.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | GroupId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GroupMembershipExpirationPolicy**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GroupId
group_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Group.MembershipExpirationPolicy.get(group_id, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MembershipExpirationPolicy.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GroupMembershipExpirationPolicy  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the GroupMembershipExpirationPolicy.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | GroupId |  |  |
**maximum_duration** | Optional[DurationSeconds] | Members in this group must be added with expirations that are less than this duration in seconds into the future from the time they are added.  | [optional] |
**maximum_value** | Optional[GroupMembershipExpiration] | Members in this group must be added with expiration times that occur before this value. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GroupMembershipExpirationPolicy**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GroupId
group_id = None
# Optional[DurationSeconds] | Members in this group must be added with expirations that are less than this duration in seconds into the future from the time they are added.
maximum_duration = 30
# Optional[GroupMembershipExpiration] | Members in this group must be added with expiration times that occur before this value.
maximum_value = "2026-01-31T00:00:00.000Z"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Group.MembershipExpirationPolicy.replace(
        group_id, maximum_duration=maximum_duration, maximum_value=maximum_value, preview=preview
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MembershipExpirationPolicy.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GroupMembershipExpirationPolicy  | The replaced GroupMembershipExpirationPolicy | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

