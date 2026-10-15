# Project

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**delete**](#delete) | **DELETE** /v3/platform/projects/{projectRid} | Private Beta |
[**delete_batch**](#delete_batch) | **POST** /v3/platform/projects/deleteBatch | Private Beta |
[**get**](#get) | **GET** /v3/platform/projects/{projectRid} | Private Beta |
[**get_batch**](#get_batch) | **POST** /v3/platform/projects/getBatch | Private Beta |
[**restore**](#restore) | **POST** /v3/platform/projects/{projectRid}/restore | Private Beta |

# **delete**
Move the given project to the trash. Following this operation, the project can be restored, using the
`restore` operation, or permanently deleted using the `permanentlyDelete` operation.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ProjectRid
project_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Project.delete(project_rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Project.delete: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:project:write:delete]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **delete_batch**
Trash multiple projects in a single request.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[DeleteProjectsBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[DeleteProjectsBatchRequestElement] | Body of the request
body = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Project.delete_batch(body, preview=preview)
    print("The delete_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Project.delete_batch: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:project:write:delete]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get**
Get the project with the specified resource identifier (RID).

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**Project**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ProjectRid
project_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Project.get(project_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Project.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:project:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Project  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get_batch**
Fetch multiple projects in a single request.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetProjectsBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**GetProjectsBatchResponse**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetProjectsBatchRequestElement] | Body of the request
body = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Project.get_batch(body, preview=preview)
    print("The get_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Project.get_batch: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:project:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetProjectsBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **restore**
Restore the given project and any directly trashed ancestors from the trash. If the project is not
directly trashed, this operation will return an error.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**project_rid** | ProjectRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ProjectRid
project_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Project.restore(project_rid, preview=preview)
    print("The restore response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Project.restore: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:project:write:restore]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

