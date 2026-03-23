# OrganizationGuestMember

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**list**](#list) | **GET** /v2/admin/organizations/{organizationRid}/guestMembers | Private Beta |

# **list**
Lists all guest members of an Organization.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListOrganizationGuestMembersResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OrganizationRid
organization_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Organization.OrganizationGuestMember.list(
        organization_rid, preview=preview
    )
    print("The list response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OrganizationGuestMember.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOrganizationGuestMembersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

