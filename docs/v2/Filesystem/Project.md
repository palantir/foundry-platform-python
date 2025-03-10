# Project

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add_organizations**](#add_organizations) | **POST** /v2/filesystem/projects/{projectRid}/addOrganizations | Public Beta |
[**create**](#create) | **POST** /v2/filesystem/projects/create | Public Beta |
[**create_from_template**](#create_from_template) | **POST** /v2/filesystem/projects/createFromTemplate | Private Beta |
[**get**](#get) | **GET** /v2/filesystem/projects/{projectRid} | Public Beta |
[**organizations**](#organizations) | **GET** /v2/filesystem/projects/{projectRid}/organizations | Public Beta |
[**organizations_page**](#organizations_page) | **GET** /v2/filesystem/projects/{projectRid}/organizations | Public Beta |
[**remove_organizations**](#remove_organizations) | **POST** /v2/filesystem/projects/{projectRid}/removeOrganizations | Public Beta |

# **add_organizations**
Adds a list of Organizations to a Project.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**organization_rids** | typing.List[core_models.OrganizationRid] |  |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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
# typing.List[core_models.OrganizationRid] |
organization_rids = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# typing.Optional[core_models.PreviewMode] | preview
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
**default_roles** | typing.List[core_models.RoleId] |  |  |
**display_name** | ResourceDisplayName |  |  |
**organization_rids** | typing.List[core_models.OrganizationRid] |  |  |
**role_grants** | typing.Dict[core_models.RoleId, typing.List[typing.Union[PrincipalWithId, PrincipalWithIdDict]]] |  |  |
**space_rid** | SpaceRid |  |  |
**description** | typing.Optional[str] |  | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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

# typing.List[core_models.RoleId] |
default_roles = ["8bf49052-dc37-4528-8bf0-b551cfb71268"]
# ResourceDisplayName |
display_name = "My Important Project"
# typing.List[core_models.OrganizationRid] |
organization_rids = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# typing.Dict[core_models.RoleId, typing.List[typing.Union[PrincipalWithId, PrincipalWithIdDict]]] |
role_grants = {
    "8bf49052-dc37-4528-8bf0-b551cfb71268": [
        {"principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de", "principalType": "USER"}
    ]
}
# SpaceRid |
space_rid = "ri.compass.main.folder.a86ad5f5-3db5-48e4-9fdd-00aa3e5731ca"
# typing.Optional[str] |
description = "project description"
# typing.Optional[core_models.PreviewMode] | preview
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

# **create_from_template**
Creates a project from a project template.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**template_rid** | ProjectTemplateRid |  |  |
**variable_values** | typing.Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue] |  |  |
**default_roles** | typing.Optional[typing.List[core_models.RoleId]] |  | [optional] |
**organization_rids** | typing.Optional[typing.List[core_models.OrganizationRid]] |  | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |
**project_description** | typing.Optional[str] |  | [optional] |

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
# typing.Dict[ProjectTemplateVariableId, ProjectTemplateVariableValue] |
variable_values = {"name": "my project name"}
# typing.Optional[typing.List[core_models.RoleId]] |
default_roles = ["8bf49052-dc37-4528-8bf0-b551cfb71268"]
# typing.Optional[typing.List[core_models.OrganizationRid]] |
organization_rids = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# typing.Optional[core_models.PreviewMode] | preview
preview = None
# typing.Optional[str] |
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

# **get**
Get the Project with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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
# typing.Optional[core_models.PreviewMode] | preview
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

# **organizations**
List of Organizations directly applied to a Project. The number of Organizations on a Project is 
typically small so the `pageSize` and `pageToken` parameters are not required.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
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

# **organizations_page**
List of Organizations directly applied to a Project. The number of Organizations on a Project is 
typically small so the `pageSize` and `pageToken` parameters are not required.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
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

# **remove_organizations**
Removes Organizations from a Project.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid | projectRid |  |
**organization_rids** | typing.List[core_models.OrganizationRid] |  |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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
# typing.List[core_models.OrganizationRid] |
organization_rids = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# typing.Optional[core_models.PreviewMode] | preview
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

