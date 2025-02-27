# Resource

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add_markings**](#add_markings) | **POST** /v2/filesystem/resources/{resourceRid}/addMarkings | Private Beta |
[**delete**](#delete) | **DELETE** /v2/filesystem/resources/{resourceRid} | Private Beta |
[**get**](#get) | **GET** /v2/filesystem/resources/{resourceRid} | Private Beta |
[**get_access_requirements**](#get_access_requirements) | **GET** /v2/filesystem/resources/{resourceRid}/getAccessRequirements | Private Beta |
[**get_by_path**](#get_by_path) | **GET** /v2/filesystem/resources/getByPath | Private Beta |
[**markings**](#markings) | **GET** /v2/filesystem/resources/{resourceRid}/markings | Private Beta |
[**markings_page**](#markings_page) | **GET** /v2/filesystem/resources/{resourceRid}/markings | Private Beta |
[**permanently_delete**](#permanently_delete) | **POST** /v2/filesystem/resources/{resourceRid}/permanentlyDelete | Private Beta |
[**remove_markings**](#remove_markings) | **POST** /v2/filesystem/resources/{resourceRid}/removeMarkings | Private Beta |
[**restore**](#restore) | **POST** /v2/filesystem/resources/{resourceRid}/restore | Private Beta |

# **add_markings**
Adds a list of Markings to a resource.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid | resourceRid |  |
**marking_ids** | List[MarkingId] |  |  |
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

# ResourceRid | resourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# List[MarkingId] |
marking_ids = ["18212f9a-0e63-4b79-96a0-aae04df23336"]
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.add_markings(
        resource_rid,
        marking_ids=marking_ids,
        preview=preview,
    )
    print("The add_markings response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
**resource_rid** | ResourceRid | resourceRid |  |
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

# ResourceRid | resourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.delete(
        resource_rid,
        preview=preview,
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
**resource_rid** | ResourceRid | resourceRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Resource**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ResourceRid | resourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.get(
        resource_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
**resource_rid** | ResourceRid | resourceRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**AccessRequirements**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ResourceRid | resourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.get_access_requirements(
        resource_rid,
        preview=preview,
    )
    print("The get_access_requirements response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Resource.get_access_requirements: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AccessRequirements  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_by_path**
Get a Resource by its absolute path.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**path** | ResourcePath | path |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Resource**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ResourcePath | path
path = "/My Organization-abcd/My Important Project/My Dataset"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.get_by_path(
        path=path,
        preview=preview,
    )
    print("The get_by_path response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
**resource_rid** | ResourceRid | resourceRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[MarkingId]**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ResourceRid | resourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    for resource in foundry_client.filesystem.Resource.markings(
        resource_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(resource)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Resource.markings: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListMarkingsOfResourceResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **markings_page**
List of Markings directly applied to a resource. The number of Markings on a resource is typically small 
so the `pageSize` and `pageToken` parameters are not required.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid | resourceRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListMarkingsOfResourceResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ResourceRid | resourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.markings_page(
        resource_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The markings_page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Resource.markings_page: %s\n" % e)

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
**resource_rid** | ResourceRid | resourceRid |  |
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

# ResourceRid | resourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.permanently_delete(
        resource_rid,
        preview=preview,
    )
    print("The permanently_delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
**resource_rid** | ResourceRid | resourceRid |  |
**marking_ids** | List[MarkingId] |  |  |
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

# ResourceRid | resourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# List[MarkingId] |
marking_ids = ["18212f9a-0e63-4b79-96a0-aae04df23336"]
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.remove_markings(
        resource_rid,
        marking_ids=marking_ids,
        preview=preview,
    )
    print("The remove_markings response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
**resource_rid** | ResourceRid | resourceRid |  |
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

# ResourceRid | resourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.restore(
        resource_rid,
        preview=preview,
    )
    print("The restore response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Resource.restore: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

