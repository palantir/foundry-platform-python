# Resource

Method | HTTP request |
------------- | ------------- |

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
path = "/My Organization/My Important Project/My Dataset"
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

