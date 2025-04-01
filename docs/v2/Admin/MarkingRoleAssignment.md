# MarkingRoleAssignment

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/admin/markings/{markingId}/roleAssignments/add | Public Beta |
[**list**](#list) | **GET** /v2/admin/markings/{markingId}/roleAssignments | Public Beta |
[**remove**](#remove) | **POST** /v2/admin/markings/{markingId}/roleAssignments/remove | Public Beta |

# **add**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**role_assignments** | List[MarkingRoleUpdate] |  |  |
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
# List[MarkingRoleUpdate]
role_assignments = [{"role": "ADMINISTER", "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Marking.MarkingRoleAssignment.add(
        marking_id, role_assignments=role_assignments, preview=preview
    )
    print("The add response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MarkingRoleAssignment.add: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListMarkingRoleAssignmentsResponse**

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


try:
    for marking_role_assignment in client.admin.Marking.MarkingRoleAssignment.list(
        marking_id, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(marking_role_assignment)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MarkingRoleAssignment.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListMarkingRoleAssignmentsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **remove**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**role_assignments** | List[MarkingRoleUpdate] |  |  |
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
# List[MarkingRoleUpdate]
role_assignments = [{"role": "ADMINISTER", "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.Marking.MarkingRoleAssignment.remove(
        marking_id, role_assignments=role_assignments, preview=preview
    )
    print("The remove response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MarkingRoleAssignment.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

