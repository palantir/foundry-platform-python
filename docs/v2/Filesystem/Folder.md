# Folder

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**children**](#children) | **GET** /v2/filesystem/folders/{folderRid}/children | Public Beta |
[**create**](#create) | **POST** /v2/filesystem/folders | Public Beta |
[**get**](#get) | **GET** /v2/filesystem/folders/{folderRid} | Public Beta |

# **children**
List all child Resources of the Folder.

This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
provided, this page size will also be used as the default.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**folder_rid** | FolderRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListChildrenOfFolderResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# FolderRid
folder_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for folder in client.filesystem.Folder.children(
        folder_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(folder)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Folder.children: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListChildrenOfFolderResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create**
Creates a new Folder.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**display_name** | ResourceDisplayName |  |  |
**parent_folder_rid** | FolderRid | The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Folder**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceDisplayName
display_name = "My Folder"
# FolderRid | The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).
parent_folder_rid = "ri.compass.main.folder.4cae7c13-b59f-48f6-9ef2-dbde603e4e33"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.filesystem.Folder.create(
        display_name=display_name, parent_folder_rid=parent_folder_rid, preview=preview
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Folder.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Folder  | The created Folder | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Folder with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**folder_rid** | FolderRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Folder**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# FolderRid
folder_rid = "ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.filesystem.Folder.get(folder_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Folder.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Folder  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

