# Resource

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**delete**](#delete) | **DELETE** /v3/platform/resources/{resourceRid} | Private Beta |
[**delete_batch**](#delete_batch) | **POST** /v3/platform/resources/deleteBatch | Private Beta |
[**get**](#get) | **GET** /v3/platform/resources/{resourceRid} | Private Beta |
[**get_batch**](#get_batch) | **POST** /v3/platform/resources/getBatch | Private Beta |
[**get_by_path**](#get_by_path) | **GET** /v3/platform/resources/getByPath | Private Beta |
[**restore**](#restore) | **POST** /v3/platform/resources/{resourceRid}/restore | Private Beta |

# **delete**
Move the given resource to the trash. Following this operation, the resource can be restored, using the
`restore` operation, or permanently deleted using the `permanentlyDelete` operation.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Resource.delete(resource_rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.delete: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:resource:write:delete]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **delete_batch**
Trash multiple resources in a single request.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[DeleteResourcesBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[DeleteResourcesBatchRequestElement] | Body of the request
body = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Resource.delete_batch(body, preview=preview)
    print("The delete_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.delete_batch: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:resource:write:delete]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get**
Get the resource with the specified resource identifier (RID).

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**include** | Optional[List[AdditionalField]] |  | [optional] |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**Resource**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = None
# Optional[List[AdditionalField]]
include = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Resource.get(resource_rid, include=include, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:resource:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Resource  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get_batch**
Fetch multiple resources in a single request.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetResourcesBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**GetResourcesBatchResponse**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetResourcesBatchRequestElement] | Body of the request
body = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Resource.get_batch(body, preview=preview)
    print("The get_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.get_batch: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:resource:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetResourcesBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get_by_path**
Get a resource by its absolute path. The leading slash is optional.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**path** | ResourcePath |  |  |
**include** | Optional[List[AdditionalField]] |  | [optional] |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**Resource**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourcePath
path = None
# Optional[List[AdditionalField]]
include = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Resource.get_by_path(
        path=path, include=include, preview=preview
    )
    print("The get_by_path response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.get_by_path: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:resource:read:get-by-path]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Resource  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **restore**
Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
directly trashed, this operation will return an error.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Resource.restore(resource_rid, preview=preview)
    print("The restore response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.restore: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:resource:write:restore]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

