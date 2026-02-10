# Organization

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/admin/organizations | Private Beta |
[**get**](#get) | **GET** /v2/admin/organizations/{organizationRid} | Public Beta |
[**list_available_roles**](#list_available_roles) | **GET** /v2/admin/organizations/{organizationRid}/listAvailableRoles | Public Beta |
[**replace**](#replace) | **PUT** /v2/admin/organizations/{organizationRid} | Public Beta |

# **create**
Creates a new Organization.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**administrators** | List[PrincipalId] | The initial administrators of the Organization. At least one principal must be provided.  |  |
**enrollment_rid** | EnrollmentRid | The RID of the Enrollment that this Organization belongs to. This must be provided.  |  |
**name** | OrganizationName |  |  |
**description** | Optional[str] |  | [optional] |
**host** | Optional[HostName] | The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Organization**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[PrincipalId] | The initial administrators of the Organization. At least one principal must be provided.
administrators = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# EnrollmentRid | The RID of the Enrollment that this Organization belongs to. This must be provided.
enrollment_rid = "ri.control-panel.main.customer.466f812b-f974-4478-9d4f-90402cd3def6"
# OrganizationName
name = "Example Organization"
# Optional[str]
description = None
# Optional[HostName] | The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.
host = "example.palantirfoundry.com"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Organization.create(
        administrators=administrators,
        enrollment_rid=enrollment_rid,
        name=name,
        description=description,
        host=host,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Organization.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Organization  | The created Organization | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Organization with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Organization**

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
    api_response = client.admin.Organization.get(organization_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Organization.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Organization  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_available_roles**
List all roles that can be assigned to a principal for the given Organization.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListAvailableOrganizationRolesResponse**

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
    api_response = client.admin.Organization.list_available_roles(organization_rid, preview=preview)
    print("The list_available_roles response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Organization.list_available_roles: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListAvailableOrganizationRolesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the Organization with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**name** | OrganizationName |  |  |
**description** | Optional[str] |  | [optional] |
**host** | Optional[HostName] | The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Organization**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OrganizationRid
organization_rid = None
# OrganizationName
name = "Example Organization"
# Optional[str]
description = None
# Optional[HostName] | The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.
host = "example.palantirfoundry.com"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Organization.replace(
        organization_rid, name=name, description=description, host=host, preview=preview
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Organization.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Organization  | The replaced Organization | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

