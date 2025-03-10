# ResourceRole

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/filesystem/resources/{resourceRid}/roles/add | Public Beta |
[**list**](#list) | **GET** /v2/filesystem/resources/{resourceRid}/roles | Public Beta |
[**page**](#page) | **GET** /v2/filesystem/resources/{resourceRid}/roles | Public Beta |
[**remove**](#remove) | **POST** /v2/filesystem/resources/{resourceRid}/roles/remove | Public Beta |

# **add**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid | resourceRid |  |
**roles** | typing.List[typing.Union[ResourceRole, ResourceRoleDict]] |  |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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
# typing.List[typing.Union[ResourceRole, ResourceRoleDict]] |
roles = [{"roleId": "8bf49052-dc37-4528-8bf0-b551cfb71268"}]
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.Role.add(
        resource_rid,
        roles=roles,
        preview=preview,
    )
    print("The add response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Role.add: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
List the roles on a resource.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid | resourceRid |  |
**include_inherited** | typing.Optional[bool] | includeInherited | [optional] |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ListResourceRolesResponse**

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
# typing.Optional[bool] | includeInherited
include_inherited = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    for resource_role in foundry_client.filesystem.Resource.Role.list(
        resource_rid,
        include_inherited=include_inherited,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(resource_role)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Role.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListResourceRolesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
List the roles on a resource.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid | resourceRid |  |
**include_inherited** | typing.Optional[bool] | includeInherited | [optional] |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ListResourceRolesResponse**

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
# typing.Optional[bool] | includeInherited
include_inherited = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.Role.page(
        resource_rid,
        include_inherited=include_inherited,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Role.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListResourceRolesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **remove**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid | resourceRid |  |
**roles** | typing.List[typing.Union[ResourceRole, ResourceRoleDict]] |  |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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
# typing.List[typing.Union[ResourceRole, ResourceRoleDict]] |
roles = [{"roleId": "8bf49052-dc37-4528-8bf0-b551cfb71268"}]
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.filesystem.Resource.Role.remove(
        resource_rid,
        roles=roles,
        preview=preview,
    )
    print("The remove response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Role.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

