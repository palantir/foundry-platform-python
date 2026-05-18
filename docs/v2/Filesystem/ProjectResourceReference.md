# ProjectResourceReference

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/filesystem/projects/{projectRid}/references/add | Public Beta |
[**list**](#list) | **GET** /v2/filesystem/projects/{projectRid}/references | Public Beta |
[**remove**](#remove) | **POST** /v2/filesystem/projects/{projectRid}/references/remove | Public Beta |

# **add**
Add references to the given project


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid |  |  |
**resources** | List[AddResourceReferenceRequest] |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ProjectRid
project_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# List[AddResourceReferenceRequest]
resources = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Project.Reference.add(
        project_rid, resources=resources, preview=preview
    )
    print("The add response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Reference.add: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
List all references in the given project


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**reference_type** | Optional[ProjectResourceReferenceType] | Filter references by type. If not provided, all references are returned. | [optional] |

### Return type
**ListProjectResourceReferencesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ProjectRid
project_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[ProjectResourceReferenceType] | Filter references by type. If not provided, all references are returned.
reference_type = None


try:
    for project_resource_reference in client.filesystem.Project.Reference.list(
        project_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        reference_type=reference_type,
    ):
        pprint(project_resource_reference)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Reference.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListProjectResourceReferencesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **remove**
Remove references from the given project


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid |  |  |
**resources** | List[RID] | The resource identifiers to remove as references. These may be either filesystem or external resource identifiers. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ProjectRid
project_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# List[RID] | The resource identifiers to remove as references. These may be either filesystem or external resource identifiers.
resources = ["ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Project.Reference.remove(
        project_rid, resources=resources, preview=preview
    )
    print("The remove response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Reference.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

