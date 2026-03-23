# OrganizationRoleAssignment

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/admin/organizations/{organizationRid}/roleAssignments/add | Stable |
[**list**](#list) | **GET** /v2/admin/organizations/{organizationRid}/roleAssignments | Stable |
[**remove**](#remove) | **POST** /v2/admin/organizations/{organizationRid}/roleAssignments/remove | Stable |

# **add**
Assign roles to principals for the given Organization. At most 100 role assignments can be added in a single request.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**role_assignments** | List[RoleAssignmentUpdate] |  |  |

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
# List[RoleAssignmentUpdate]
role_assignments = [
    {
        "roleId": "8bf49052-dc37-4528-8bf0-b551cfb71268",
        "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de",
    }
]


try:
    api_response = client.admin.Organization.OrganizationRoleAssignment.add(
        organization_rid, role_assignments=role_assignments
    )
    print("The add response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OrganizationRoleAssignment.add: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
List all principals who are assigned a role for the given Organization.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |

### Return type
**ListOrganizationRoleAssignmentsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OrganizationRid
organization_rid = None


try:
    api_response = client.admin.Organization.OrganizationRoleAssignment.list(organization_rid)
    print("The list response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OrganizationRoleAssignment.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOrganizationRoleAssignmentsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **remove**
Remove roles from principals for the given Organization. At most 100 role assignments can be removed in a single request.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**role_assignments** | List[RoleAssignmentUpdate] |  |  |

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
# List[RoleAssignmentUpdate]
role_assignments = [
    {
        "roleId": "8bf49052-dc37-4528-8bf0-b551cfb71268",
        "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de",
    }
]


try:
    api_response = client.admin.Organization.OrganizationRoleAssignment.remove(
        organization_rid, role_assignments=role_assignments
    )
    print("The remove response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OrganizationRoleAssignment.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

