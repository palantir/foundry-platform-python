# OrganizationGuestMember

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/admin/organizations/{organizationRid}/guestMembers/add | Private Beta |
[**list**](#list) | **GET** /v2/admin/organizations/{organizationRid}/guestMembers | Private Beta |
[**remove**](#remove) | **POST** /v2/admin/organizations/{organizationRid}/guestMembers/remove | Private Beta |

# **add**
Adds principals as guest members of an Organization. Attempting to add a primary member through this endpoint will not add the principal as a guest, but will still return a successful response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**principal_ids** | List[PrincipalId] |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OrganizationRid
organization_rid = None
# List[PrincipalId]
principal_ids = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Organization.OrganizationGuestMember.add(
        organization_rid, principal_ids=principal_ids, preview=preview
    )
    print("The add response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OrganizationGuestMember.add: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

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

# **remove**
Removes principals from being guest members of an Organization. Attempting to remove a primary member through this endpoint will not remove the primary member, but will still return a successful response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**principal_ids** | List[PrincipalId] |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OrganizationRid
organization_rid = None
# List[PrincipalId]
principal_ids = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Organization.OrganizationGuestMember.remove(
        organization_rid, principal_ids=principal_ids, preview=preview
    )
    print("The remove response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OrganizationGuestMember.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

