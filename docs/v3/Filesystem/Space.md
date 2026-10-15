# Space

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**delete**](#delete) | **DELETE** /v3/platform/spaces/{spaceRid} | Private Beta |
[**delete_batch**](#delete_batch) | **POST** /v3/platform/spaces/deleteBatch | Private Beta |
[**get**](#get) | **GET** /v3/platform/spaces/{spaceRid} | Private Beta |
[**get_batch**](#get_batch) | **POST** /v3/platform/spaces/getBatch | Private Beta |
[**list**](#list) | **GET** /v3/platform/spaces | Private Beta |
[**restore**](#restore) | **POST** /v3/platform/spaces/{spaceRid}/restore | Private Beta |

# **delete**
Move the given space to the trash. Following this operation, the space can be restored, using the
`restore` operation, or permanently deleted using the `permanentlyDelete` operation.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**space_rid** | SpaceRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SpaceRid
space_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Space.delete(space_rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.delete: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:space:write:delete]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **delete_batch**
Trash multiple spaces in a single request.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[DeleteSpacesBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[DeleteSpacesBatchRequestElement] | Body of the request
body = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Space.delete_batch(body, preview=preview)
    print("The delete_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.delete_batch: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:space:write:delete]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get**
Get the space with the specified resource identifier (RID).

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**space_rid** | SpaceRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**Space**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SpaceRid
space_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Space.get(space_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:space:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Space  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get_batch**
Fetch multiple spaces in a single request.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetSpacesBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**GetSpacesBatchResponse**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetSpacesBatchRequestElement] | Body of the request
body = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Space.get_batch(body, preview=preview)
    print("The get_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.get_batch: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:space:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetSpacesBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **list**
Lists all spaces.

This is a paginated endpoint. Each page may be smaller or larger than the requested page size.
It is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
To get the next page, make the same request again, but set the value of the `pageToken` query parameter
to be value of the `nextPageToken` value of the previous response. 
If there is no `nextPageToken` field in the response, you are on the last page.

The default page size is 200. The maximum page size is 200. Requests for a larger page size will be
clamped to 200. If pageSize is 0, the default page size is used.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**ListSpacesResponse**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[PageSize]
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode]
preview = None


try:
    for space in client.filesystem.Space.list(
        page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(space)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.list: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:space:read:list]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListSpacesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **restore**
Restore the given space and any directly trashed ancestors from the trash. If the space is not
directly trashed, this operation will return an error.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**space_rid** | SpaceRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SpaceRid
space_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.filesystem.Space.restore(space_rid, preview=preview)
    print("The restore response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Space.restore: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:space:write:restore]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

