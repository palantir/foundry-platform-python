# EnrollmentRoleAssignment

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/admin/enrollments/{enrollmentRid}/roleAssignments/add | Public Beta |
[**list**](#list) | **GET** /v2/admin/enrollments/{enrollmentRid}/roleAssignments | Public Beta |
[**remove**](#remove) | **POST** /v2/admin/enrollments/{enrollmentRid}/roleAssignments/remove | Public Beta |

# **add**
Assign roles to principals for the given Enrollment. At most 100 role assignments can be added in a single request.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**enrollment_rid** | EnrollmentRid |  |  |
**role_assignments** | List[RoleAssignmentUpdate] |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# EnrollmentRid
enrollment_rid = None
# List[RoleAssignmentUpdate]
role_assignments = [
    {
        "roleId": "8bf49052-dc37-4528-8bf0-b551cfb71268",
        "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de",
    }
]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Enrollment.EnrollmentRoleAssignment.add(
        enrollment_rid, role_assignments=role_assignments, preview=preview
    )
    print("The add response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling EnrollmentRoleAssignment.add: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
List all principals who are assigned a role for the given Enrollment.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**enrollment_rid** | EnrollmentRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListEnrollmentRoleAssignmentsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# EnrollmentRid
enrollment_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Enrollment.EnrollmentRoleAssignment.list(
        enrollment_rid, preview=preview
    )
    print("The list response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling EnrollmentRoleAssignment.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListEnrollmentRoleAssignmentsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **remove**
Remove roles from principals for the given Enrollment. At most 100 role assignments can be removed in a single request.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**enrollment_rid** | EnrollmentRid |  |  |
**role_assignments** | List[RoleAssignmentUpdate] |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# EnrollmentRid
enrollment_rid = None
# List[RoleAssignmentUpdate]
role_assignments = [
    {
        "roleId": "8bf49052-dc37-4528-8bf0-b551cfb71268",
        "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de",
    }
]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Enrollment.EnrollmentRoleAssignment.remove(
        enrollment_rid, role_assignments=role_assignments, preview=preview
    )
    print("The remove response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling EnrollmentRoleAssignment.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

