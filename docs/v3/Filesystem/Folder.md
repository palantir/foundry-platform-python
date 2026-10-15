# Folder

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v3/platform/folders | Private Beta |
[**delete**](#delete) | **DELETE** /v3/platform/folders/{folderRid} | Private Beta |
[**delete_batch**](#delete_batch) | **POST** /v3/platform/folders/deleteBatch | Private Beta |
[**get**](#get) | **GET** /v3/platform/folders/{folderRid} | Private Beta |
[**get_batch**](#get_batch) | **POST** /v3/platform/folders/getBatch | Private Beta |
[**restore**](#restore) | **POST** /v3/platform/folders/{folderRid}/restore | Private Beta |

# **create**
Create a new folder in the given parent folder.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**display_name** | DisplayName | The display name of the folder. |  |
**parent_folder_rid** | FolderRid | The RID of the existing project or folder in which to create the new folder. The parent must be inside a project. |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**Folder**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DisplayName | The display name of the folder.
display_name = None
# FolderRid | The RID of the existing project or folder in which to create the new folder. The parent must be inside a project.
parent_folder_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Folder.create(
        display_name=display_name, parent_folder_rid=parent_folder_rid, preview=preview
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Folder.create: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:folder:write:create]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Folder  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **delete**
Move the given folder to the trash. Following this operation, the folder can be restored, using the
`restore` operation, or permanently deleted using the `permanentlyDelete` operation.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**folder_rid** | FolderRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# FolderRid
folder_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Folder.delete(folder_rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Folder.delete: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:folder:write:delete]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **delete_batch**
Trash multiple folders in a single request.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[DeleteFoldersBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[DeleteFoldersBatchRequestElement] | Body of the request
body = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Folder.delete_batch(body, preview=preview)
    print("The delete_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Folder.delete_batch: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:folder:write:delete]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get**
Get the folder with the specified resource identifier (RID).

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**folder_rid** | FolderRid |  |  |
**include** | Optional[List[AdditionalField]] |  | [optional] |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**Folder**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# FolderRid
folder_rid = None
# Optional[List[AdditionalField]]
include = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Folder.get(folder_rid, include=include, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Folder.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:folder:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Folder  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get_batch**
Fetch multiple folders in a single request.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetFoldersBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**GetFoldersBatchResponse**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetFoldersBatchRequestElement] | Body of the request
body = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Folder.get_batch(body, preview=preview)
    print("The get_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Folder.get_batch: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:folder:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetFoldersBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **restore**
Restore the given folder and any directly trashed ancestors from the trash. If the folder is not
directly trashed, this operation will return an error.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**folder_rid** | FolderRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# FolderRid
folder_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Folder.restore(folder_rid, preview=preview)
    print("The restore response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Folder.restore: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:folder:write:restore]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

