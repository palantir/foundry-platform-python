# Resource

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add_markings**](#add_markings) | **POST** /v2/filesystem/resources/{resourceRid}/addMarkings | Public Beta |
[**delete**](#delete) | **DELETE** /v2/filesystem/resources/{resourceRid} | Public Beta |
[**get**](#get) | **GET** /v2/filesystem/resources/{resourceRid} | Public Beta |
[**get_access_requirements**](#get_access_requirements) | **GET** /v2/filesystem/resources/{resourceRid}/getAccessRequirements | Public Beta |
[**get_batch**](#get_batch) | **POST** /v2/filesystem/resources/getBatch | Public Beta |
[**get_by_path**](#get_by_path) | **GET** /v2/filesystem/resources/getByPath | Public Beta |
[**markings**](#markings) | **GET** /v2/filesystem/resources/{resourceRid}/markings | Public Beta |
[**permanently_delete**](#permanently_delete) | **POST** /v2/filesystem/resources/{resourceRid}/permanentlyDelete | Public Beta |
[**remove_markings**](#remove_markings) | **POST** /v2/filesystem/resources/{resourceRid}/removeMarkings | Public Beta |
[**restore**](#restore) | **POST** /v2/filesystem/resources/{resourceRid}/restore | Public Beta |

# **add_markings**
Adds a list of Markings to a resource.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**marking_ids** | List[MarkingId] |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# List[MarkingId]
marking_ids = ["18212f9a-0e63-4b79-96a0-aae04df23336"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Resource.add_markings(
        resource_rid, marking_ids=marking_ids, preview=preview
    )
    print("The add_markings response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.add_markings: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **delete**
Move the given resource to the trash. Following this operation, the resource can be restored, using the
`restore` operation, or permanently deleted using the `permanentlyDelete` operation.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Resource.delete(resource_rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Resource with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Resource**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Resource.get(resource_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Resource  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_access_requirements**
Returns a list of access requirements a user needs in order to view a resource. Access requirements are
composed of Organizations and Markings, and can either be applied directly to the resource or inherited.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**AccessRequirements**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Resource.get_access_requirements(resource_rid, preview=preview)
    print("The get_access_requirements response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.get_access_requirements: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AccessRequirements  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_batch**
Fetches multiple resources in a single request.
Returns a map from RID to the corresponding resource. If a resource does not exist, or if it is a root folder or space, its RID will not be included in the map.
At most 1,000 resources should be requested at once.


The maximum batch size for this endpoint is 1000.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetResourcesBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GetResourcesBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetResourcesBatchRequestElement] | Body of the request
body = [{"resourceRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"}]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Resource.get_batch(body, preview=preview)
    print("The get_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.get_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetResourcesBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_by_path**
Get a Resource by its absolute path.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**path** | ResourcePath | The path to the Resource. The leading slash is optional. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Resource**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourcePath | The path to the Resource. The leading slash is optional.
path = "/My Organization-abcd/My Important Project/My Dataset"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Resource.get_by_path(path=path, preview=preview)
    print("The get_by_path response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.get_by_path: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Resource  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **markings**
List of Markings directly applied to a resource. The number of Markings on a resource is typically small 
so the `pageSize` and `pageToken` parameters are not required.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListMarkingsOfResourceResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for resource in client.filesystem.Resource.markings(
        resource_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(resource)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.markings: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListMarkingsOfResourceResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **permanently_delete**
Permanently delete the given resource from the trash. If the Resource is not directly trashed, a
`ResourceNotTrashed` error will be thrown.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Resource.permanently_delete(resource_rid, preview=preview)
    print("The permanently_delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.permanently_delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **remove_markings**
Removes Markings from a resource.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**marking_ids** | List[MarkingId] |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# List[MarkingId]
marking_ids = ["18212f9a-0e63-4b79-96a0-aae04df23336"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Resource.remove_markings(
        resource_rid, marking_ids=marking_ids, preview=preview
    )
    print("The remove_markings response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.remove_markings: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **restore**
Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
trashed, this operation will be ignored.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.filesystem.Resource.restore(resource_rid, preview=preview)
    print("The restore response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Resource.restore: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

