# MarkingMember

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/admin/markings/{markingId}/markingMembers/add | Public Beta |
[**list**](#list) | **GET** /v2/admin/markings/{markingId}/markingMembers | Public Beta |
[**page**](#page) | **GET** /v2/admin/markings/{markingId}/markingMembers | Public Beta |
[**remove**](#remove) | **POST** /v2/admin/markings/{markingId}/markingMembers/remove | Public Beta |

# **add**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**principal_ids** | List[PrincipalId] |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingId
marking_id = None
# List[PrincipalId]
principal_ids = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Marking.MarkingMember.add(
        marking_id, principal_ids=principal_ids, preview=preview
    )
    print("The add response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MarkingMember.add: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
Requires `api:admin-write` because only marking administrators can view marking members.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**transitive** | Optional[bool] | When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.  | [optional] |

### Return type
**ListMarkingMembersResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingId
marking_id = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[bool] | When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
transitive = None


try:
    for marking_member in client.admin.Marking.MarkingMember.list(
        marking_id,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        transitive=transitive,
    ):
        pprint(marking_member)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MarkingMember.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListMarkingMembersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
Requires `api:admin-write` because only marking administrators can view marking members.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**transitive** | Optional[bool] | When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.  | [optional] |

### Return type
**ListMarkingMembersResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingId
marking_id = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[bool] | When true, includes the transitive members of groups contained within groups that are members of this  Marking. For example, say the Marking has member Group A, and Group A has member User B. If  `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B  will be returned. This will recursively resolve Groups through all layers of nesting.  Defaults to false.
transitive = None


try:
    api_response = foundry_client.admin.Marking.MarkingMember.page(
        marking_id,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        transitive=transitive,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MarkingMember.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListMarkingMembersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **remove**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**principal_ids** | List[PrincipalId] |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingId
marking_id = None
# List[PrincipalId]
principal_ids = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Marking.MarkingMember.remove(
        marking_id, principal_ids=principal_ids, preview=preview
    )
    print("The remove response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MarkingMember.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

