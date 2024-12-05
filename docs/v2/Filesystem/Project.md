# Project

Method | HTTP request |
------------- | ------------- |

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
project_rid = None
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
project_rid = None
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
project_rid = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[PreviewMode] | preview
preview = None


try:
    for project in foundry_client.filesystem.Project.organizations(
        project_rid,
        page_size=page_size,
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
project_rid = None
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
project_rid = None
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

