# Space

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/filesystem/spaces | Private Beta |
[**delete**](#delete) | **DELETE** /v2/filesystem/spaces/{spaceRid} | Private Beta |
[**get**](#get) | **GET** /v2/filesystem/spaces/{spaceRid} | Private Beta |
[**list**](#list) | **GET** /v2/filesystem/spaces | Stable |
[**replace**](#replace) | **PUT** /v2/filesystem/spaces/{spaceRid} | Private Beta |

# **create**
Creates a new Space.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**deletion_policy_organizations** | List[OrganizationRid] | By default, this Space will use a Last Out deletion policy, meaning that this Space and its projects will be deleted when the last Organization listed here is deleted. Only Organizations in the Space's Enrollment can be included here.  |  |
**display_name** | ResourceDisplayName |  |  |
**enrollment_rid** | EnrollmentRid | The RID of the Enrollment that this Space belongs to.  |  |
**organizations** | List[OrganizationRid] | The list of Organizations that are provisioned access to this Space. In order to access this Space, a user must be a member of at least one of these Organizations.  |  |
**default_role_set_id** | Optional[RoleSetId] | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.  | [optional] |
**description** | Optional[str] | The description of the Space. | [optional] |
**file_system_id** | Optional[FileSystemId] | The ID of the Filesystem for this Space, which is where the contents of the Space are stored. If not provided, the default Filesystem for this Enrollment will be used. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**usage_account_rid** | Optional[UsageAccountRid] | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used. | [optional] |

### Return type
**Space**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[OrganizationRid] | By default, this Space will use a Last Out deletion policy, meaning that this Space and its projects will be deleted when the last Organization listed here is deleted. Only Organizations in the Space's Enrollment can be included here.
deletion_policy_organizations = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# ResourceDisplayName
display_name = "My Space"
# EnrollmentRid | The RID of the Enrollment that this Space belongs to.
enrollment_rid = "ri.control-panel.main.customer.466f812b-f974-4478-9d4f-90402cd3def6"
# List[OrganizationRid] | The list of Organizations that are provisioned access to this Space. In order to access this Space, a user must be a member of at least one of these Organizations.
organizations = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# Optional[RoleSetId] | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.
default_role_set_id = "3181190f-f6b8-4649-90ec-64fa2d847204"
# Optional[str] | The description of the Space.
description = "This space is for xyz"
# Optional[FileSystemId] | The ID of the Filesystem for this Space, which is where the contents of the Space are stored. If not provided, the default Filesystem for this Enrollment will be used.
file_system_id = "hdfs"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[UsageAccountRid] | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used.
usage_account_rid = (
    "ri.resource-policy-manager.global.usage-account.0c91194d-b5e3-4c4f-b96f-7a7f3f50e95c"
)


try:
    api_response = client.filesystem.Space.create(
        deletion_policy_organizations=deletion_policy_organizations,
        display_name=display_name,
        enrollment_rid=enrollment_rid,
        organizations=organizations,
        default_role_set_id=default_role_set_id,
        description=description,
        file_system_id=file_system_id,
        preview=preview,
        usage_account_rid=usage_account_rid,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Space  | The created Space | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **delete**
Delete the space. This will only work if the Space is empty, meaning any Projects or resources have been deleted first.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**space_rid** | SpaceRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SpaceRid
space_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Space.delete(space_rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Space with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**space_rid** | SpaceRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Space**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SpaceRid
space_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Space.get(space_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Space  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all Spaces.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |

### Return type
**ListSpacesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    for space in client.filesystem.Space.list(page_size=page_size, page_token=page_token):
        pprint(space)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListSpacesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the Space with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**space_rid** | SpaceRid |  |  |
**display_name** | ResourceDisplayName |  |  |
**default_role_set_id** | Optional[RoleSetId] | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.  | [optional] |
**description** | Optional[str] | The description of the Space. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**usage_account_rid** | Optional[UsageAccountRid] | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used. | [optional] |

### Return type
**Space**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SpaceRid
space_rid = None
# ResourceDisplayName
display_name = "My Space"
# Optional[RoleSetId] | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.
default_role_set_id = "3181190f-f6b8-4649-90ec-64fa2d847204"
# Optional[str] | The description of the Space.
description = "This space is for xyz"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[UsageAccountRid] | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used.
usage_account_rid = (
    "ri.resource-policy-manager.global.usage-account.0c91194d-b5e3-4c4f-b96f-7a7f3f50e95c"
)


try:
    api_response = client.filesystem.Space.replace(
        space_rid,
        display_name=display_name,
        default_role_set_id=default_role_set_id,
        description=description,
        preview=preview,
        usage_account_rid=usage_account_rid,
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Space  | The replaced Space | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

