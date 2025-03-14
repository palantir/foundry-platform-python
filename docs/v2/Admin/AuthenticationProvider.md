# AuthenticationProvider

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid} | Public Beta |
[**list**](#list) | **GET** /v2/admin/enrollments/{enrollmentRid}/authenticationProviders | Public Beta |
[**preregister_group**](#preregister_group) | **POST** /v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterGroup | Public Beta |
[**preregister_user**](#preregister_user) | **POST** /v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterUser | Public Beta |

# **get**
Get the AuthenticationProvider with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**enrollment_rid** | RID |  |  |
**authentication_provider_rid** | RID |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**AuthenticationProvider**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# RID
enrollment_rid = None
# RID
authentication_provider_rid = "ri.control-panel.main.saml.3faf689c-eaa1-4137-851f-81d58afe4c86"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Enrollment.AuthenticationProvider.get(
        enrollment_rid,
        authentication_provider_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling AuthenticationProvider.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AuthenticationProvider  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all AuthenticationProviders.



### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**enrollment_rid** | RID |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListAuthenticationProvidersResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# RID
enrollment_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Enrollment.AuthenticationProvider.list(
        enrollment_rid,
        preview=preview,
    )
    print("The list response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling AuthenticationProvider.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListAuthenticationProvidersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **preregister_group**
Register a Group with a given name before any users with this group log in through this Authentication Provider.
Preregistered groups can be used anywhere other groups are used in the platform.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**enrollment_rid** | RID |  |  |
**authentication_provider_rid** | RID |  |  |
**name** | str |  |  |
**organizations** | List[OrganizationRid] | The RIDs of the Organizations that can view this group.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**str**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# RID
enrollment_rid = None
# RID
authentication_provider_rid = "ri.control-panel.main.saml.3faf689c-eaa1-4137-851f-81d58afe4c86"
# str
name = "Data Source Admins"
# List[OrganizationRid] | The RIDs of the Organizations that can view this group.
organizations = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Enrollment.AuthenticationProvider.preregister_group(
        enrollment_rid,
        authentication_provider_rid,
        name=name,
        organizations=organizations,
        preview=preview,
    )
    print("The preregister_group response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling AuthenticationProvider.preregister_group: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | str  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **preregister_user**
Register a User with a given username before they log in to the platform for the first time through this
Authentication Provider. Preregistered users can be assigned to groups and roles prior to first login.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**enrollment_rid** | RID |  |  |
**authentication_provider_rid** | RID |  |  |
**organization** | RID | The RID of the user's primary Organization. This may be changed when the user logs in for the first time depending on any configured Organization assignment rules.  |  |
**username** | str | The new user's username. This must match one of the provider's supported username patterns. |  |
**attributes** | Optional[Dict[AttributeName, AttributeValues]] |  | [optional] |
**email** | Optional[str] |  | [optional] |
**family_name** | Optional[str] |  | [optional] |
**given_name** | Optional[str] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**str**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# RID
enrollment_rid = None
# RID
authentication_provider_rid = "ri.control-panel.main.saml.3faf689c-eaa1-4137-851f-81d58afe4c86"
# RID | The RID of the user's primary Organization. This may be changed when the user logs in for the first time depending on any configured Organization assignment rules.
organization = "ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"
# str | The new user's username. This must match one of the provider's supported username patterns.
username = "jsmith"
# Optional[Dict[AttributeName, AttributeValues]]
attributes = {
    "multipass:givenName": ["John"],
    "multipass:familyName": ["Smith"],
    "multipass:email:primary": ["jsmith@example.com"],
    "multipass:realm": ["eab0a251-ca1a-4a84-a482-200edfb8026f"],
    "multipass:organization-rid": [
        "ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"
    ],
    "department": ["Finance"],
    "jobTitle": ["Accountant"],
}
# Optional[str]
email = "jsmith@example.com"
# Optional[str]
family_name = "Smith"
# Optional[str]
given_name = "John"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Enrollment.AuthenticationProvider.preregister_user(
        enrollment_rid,
        authentication_provider_rid,
        organization=organization,
        username=username,
        attributes=attributes,
        email=email,
        family_name=family_name,
        given_name=given_name,
        preview=preview,
    )
    print("The preregister_user response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling AuthenticationProvider.preregister_user: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | str  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

