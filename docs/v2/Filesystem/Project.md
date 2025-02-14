# Project

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v2/filesystem/projects/create |

Adds a list of Organizations to a Project.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**organization_rids** | List[OrganizationRid] |  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ProjectRid | projectRid
project_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# List[OrganizationRid] |
organization_rids = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Project.add_organizations(
        project_rid,
        organization_rids=organization_rids,
        preview=preview,
    )
    print("The add_organizations response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Project.add_organizations: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create**
Creates a new Project.

Note that third-party applications using this endpoint via OAuth2 cannot be associated with an
Ontology SDK as this will reduce the scope of operations to only those within specified projects.
When creating the application, select "No, I won't use an Ontology SDK" on the Resources page.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**default_roles** | List[RoleId] |  |  |
**display_name** | ResourceDisplayName |  |  |
**organization_rids** | List[OrganizationRid] |  |  |
**role_grants** | Dict[RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]] |  |  |
**space_rid** | SpaceRid |  |  |
**description** | Optional[str] |  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Project**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# List[RoleId] |
default_roles = ["8bf49052-dc37-4528-8bf0-b551cfb71268"]
# ResourceDisplayName |
display_name = "My Important Project"
# List[OrganizationRid] |
organization_rids = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# Dict[RoleId, List[Union[PrincipalWithId, PrincipalWithIdDict]]] |
role_grants = {
    "8bf49052-dc37-4528-8bf0-b551cfb71268": [
        {"principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de", "principalType": "USER"}
    ]
}
# SpaceRid |
space_rid = "ri.compass.main.folder.a86ad5f5-3db5-48e4-9fdd-00aa3e5731ca"
# Optional[str] |
description = "project description"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Project.create(
        default_roles=default_roles,
        display_name=display_name,
        organization_rids=organization_rids,
        role_grants=role_grants,
        space_rid=space_rid,
        description=description,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Project.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Project  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Creates a project from a project template.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**template_rid** | ProjectTemplateRid |  |  |
**variable_values** | Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue] |  |  |
**default_roles** | Optional[List[RoleId]] |  | [optional] |
**organization_rids** | Optional[List[OrganizationRid]] |  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**project_description** | Optional[str] |  | [optional] |

### Return type
**Project**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ProjectTemplateRid |
template_rid = "ri.compass.main.template.c410f510-2937-420e-8ea3-8c9bcb3c1791"
# Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue] |
variable_values = {"name": "my project name"}
# Optional[List[RoleId]] |
default_roles = ["8bf49052-dc37-4528-8bf0-b551cfb71268"]
# Optional[List[OrganizationRid]] |
organization_rids = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# Optional[PreviewMode] | preview
preview = None
# Optional[str] |
project_description = None


try:
    api_response = foundry_client.filesystem.Project.create_from_template(
        template_rid=template_rid,
        variable_values=variable_values,
        default_roles=default_roles,
        organization_rids=organization_rids,
        preview=preview,
        project_description=project_description,
    )
    print("The create_from_template response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Project.create_from_template: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Project  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Get the Project with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Project**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ProjectRid | projectRid
project_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Project.get(
        project_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Project.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Project  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

List of Organizations directly applied to a Project. The number of Organizations on a Project is 
typically small so the `pageSize` and `pageToken` parameters are not required.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[OrganizationRid]**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ProjectRid | projectRid
project_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    for project in foundry_client.filesystem.Project.organizations(
        project_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(project)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Project.organizations: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOrganizationsOfProjectResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

List of Organizations directly applied to a Project. The number of Organizations on a Project is 
typically small so the `pageSize` and `pageToken` parameters are not required.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListOrganizationsOfProjectResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ProjectRid | projectRid
project_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Project.organizations_page(
        project_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The organizations_page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Project.organizations_page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOrganizationsOfProjectResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Removes Organizations from a Project.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**organization_rids** | List[OrganizationRid] |  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ProjectRid | projectRid
project_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# List[OrganizationRid] |
organization_rids = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Project.remove_organizations(
        project_rid,
        organization_rids=organization_rids,
        preview=preview,
    )
    print("The remove_organizations response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Project.remove_organizations: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

