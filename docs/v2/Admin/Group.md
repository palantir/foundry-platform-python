# Group

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v2/admin/groups |
[**delete**](#delete) | **DELETE** /v2/admin/groups/{groupId} |
[**get**](#get) | **GET** /v2/admin/groups/{groupId} |
[**get_batch**](#get_batch) | **POST** /v2/admin/groups/getBatch |
[**list**](#list) | **GET** /v2/admin/groups |
[**page**](#page) | **GET** /v2/admin/groups |
[**search**](#search) | **POST** /v2/admin/groups/search |

# **create**
Creates a new Group.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**attributes** | Dict[AttributeName, AttributeValues] | A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change. |  |
**name** | GroupName | The name of the Group. |  |
**organizations** | List[OrganizationRid] | The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.  |  |
**description** | Optional[pydantic.StrictStr] | A description of the Group. | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Group**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Dict[AttributeName, AttributeValues] | A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.
attributes = None
# GroupName | The name of the Group.
name = "Data Source Admins"
# List[OrganizationRid] | The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
organizations = ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]
# Optional[pydantic.StrictStr] | A description of the Group.
description = "Create and modify data sources in the platform"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.create(
        attributes=attributes,
        name=name,
        organizations=organizations,
        description=description,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Group.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Group  | The created Group | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **delete**
Delete the Group with the specified id.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId | groupId |  |
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

# PrincipalId | groupId
group_id = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.delete(
        group_id,
        preview=preview,
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Group.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Group with the specified id.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**group_id** | PrincipalId | groupId |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Group**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# PrincipalId | groupId
group_id = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.get(
        group_id,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Group.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Group  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_batch**
Execute multiple get requests on Group.

The maximum batch size for this endpoint is 500.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | Annotated[List[GetGroupsBatchRequestElementDict], Len(min_length=1, max_length=500)] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**GetGroupsBatchResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Annotated[List[GetGroupsBatchRequestElementDict], Len(min_length=1, max_length=500)] | Body of the request
body = [{"groupId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.get_batch(
        body,
        preview=preview,
    )
    print("The get_batch response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Group.get_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetGroupsBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all Groups.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[Group]**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | pageSize
page_size = None
# Optional[PreviewMode] | preview
preview = None


try:
    for group in foundry_client.admin.Group.list(
        page_size=page_size,
        preview=preview,
    ):
        pprint(group)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Group.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists all Groups.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListGroupsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.page(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Group.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListGroupsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**where** | GroupSearchFilterDict |  |  |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**SearchGroupsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# GroupSearchFilterDict |
where = {"type": "queryString"}
# Optional[PageSize] |
page_size = 100
# Optional[PageToken] |
page_token = "v1.VGhlcmUgaXMgc28gbXVjaCBsZWZ0IHRvIGJ1aWxkIC0gcGFsYW50aXIuY29tL2NhcmVlcnMv"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Group.search(
        where=where,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The search response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Group.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchGroupsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

