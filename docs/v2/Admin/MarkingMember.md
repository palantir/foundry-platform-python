# MarkingMember

Method | HTTP request |
------------- | ------------- |
[**add**](#add) | **POST** /v2/admin/markings/{markingId}/markingMembers/add |
[**list**](#list) | **GET** /v2/admin/markings/{markingId}/markingMembers |
[**page**](#page) | **GET** /v2/admin/markings/{markingId}/markingMembers |
[**remove**](#remove) | **POST** /v2/admin/markings/{markingId}/markingMembers/remove |

# **add**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId | markingId |  |
**principal_ids** | List[PrincipalId] |  |  |
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

# MarkingId | markingId
marking_id = None
# List[PrincipalId] |
principal_ids = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Marking.MarkingMember.add(
        marking_id,
        principal_ids=principal_ids,
        preview=preview,
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
**marking_id** | MarkingId | markingId |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transitive** | Optional[pydantic.StrictBool] | transitive | [optional] |

### Return type
**ResourceIterator[MarkingMember]**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# MarkingId | markingId
marking_id = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[PreviewMode] | preview
preview = None
# Optional[pydantic.StrictBool] | transitive
transitive = None


try:
    for marking_member in foundry_client.admin.Marking.MarkingMember.list(
        marking_id,
        page_size=page_size,
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
**marking_id** | MarkingId | markingId |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**transitive** | Optional[pydantic.StrictBool] | transitive | [optional] |

### Return type
**ListMarkingMembersResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# MarkingId | markingId
marking_id = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None
# Optional[pydantic.StrictBool] | transitive
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
**marking_id** | MarkingId | markingId |  |
**principal_ids** | List[PrincipalId] |  |  |
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

# MarkingId | markingId
marking_id = None
# List[PrincipalId] |
principal_ids = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Marking.MarkingMember.remove(
        marking_id,
        principal_ids=principal_ids,
        preview=preview,
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

