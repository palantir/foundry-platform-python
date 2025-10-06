# ResourceRole

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/filesystem/resources/{resourceRid}/roles/add | Stable |
[**list**](#list) | **GET** /v2/filesystem/resources/{resourceRid}/roles | Stable |
[**remove**](#remove) | **POST** /v2/filesystem/resources/{resourceRid}/roles/remove | Stable |

# **add**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rid** | ResourceRid |  |  |
**roles** | List[ResourceRoleIdentifier] |  |  |

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
# List[ResourceRoleIdentifier]
roles = [
    {
        "resourceRolePrincipal": {
            "type": "principalIdOnly",
            "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de",
        },
        "roleId": "8bf49052-dc37-4528-8bf0-b551cfb71268",
    }
]


try:
    api_response = client.filesystem.Resource.Role.add(resource_rid, roles=roles)
    print("The add response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**resource_rid** | ResourceRid |  |  |
**include_inherited** | Optional[bool] | Whether to include inherited roles on the resource. | [optional] |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |

### Return type
**ListResourceRolesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ResourceRid
resource_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# Optional[bool] | Whether to include inherited roles on the resource.
include_inherited = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    for resource_role in client.filesystem.Resource.Role.list(
        resource_rid,
        include_inherited=include_inherited,
        page_size=page_size,
        page_token=page_token,
    ):
        pprint(resource_role)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Role.list: %s\n" % e)

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
**resource_rid** | ResourceRid |  |  |
**roles** | List[ResourceRoleIdentifier] |  |  |

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
# List[ResourceRoleIdentifier]
roles = [
    {
        "resourceRolePrincipal": {
            "type": "principalIdOnly",
            "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de",
        },
        "roleId": "8bf49052-dc37-4528-8bf0-b551cfb71268",
    }
]


try:
    api_response = client.filesystem.Resource.Role.remove(resource_rid, roles=roles)
    print("The remove response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Role.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

