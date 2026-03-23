# MarkingRoleAssignment

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add**](#add) | **POST** /v2/admin/markings/{markingId}/roleAssignments/add | Stable |
[**list**](#list) | **GET** /v2/admin/markings/{markingId}/roleAssignments | Stable |
[**remove**](#remove) | **POST** /v2/admin/markings/{markingId}/roleAssignments/remove | Stable |

# **add**
Adds role assignments for the given Marking. For Organization markings, only the USE and DECLASSIFY
roles are supported; the ADMINISTER role must be managed via the Organization Role Assignment endpoints.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**role_assignments** | List[MarkingRoleUpdate] |  |  |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingId
marking_id = None
# List[MarkingRoleUpdate]
role_assignments = [{"role": "ADMINISTER", "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]


try:
    api_response = client.admin.Marking.MarkingRoleAssignment.add(
        marking_id, role_assignments=role_assignments
    )
    print("The add response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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

### Return type
**ListMarkingRoleAssignmentsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingId
marking_id = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    for marking_role_assignment in client.admin.Marking.MarkingRoleAssignment.list(
        marking_id, page_size=page_size, page_token=page_token
    ):
        pprint(marking_role_assignment)
except foundry_sdk.PalantirRPCException as e:
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
Removes role assignments for the given Marking. For Organization markings, only the USE and DECLASSIFY
roles are supported; the ADMINISTER role must be managed via the Organization Role Assignment endpoints.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**role_assignments** | List[MarkingRoleUpdate] |  |  |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingId
marking_id = None
# List[MarkingRoleUpdate]
role_assignments = [{"role": "ADMINISTER", "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]


try:
    api_response = client.admin.Marking.MarkingRoleAssignment.remove(
        marking_id, role_assignments=role_assignments
    )
    print("The remove response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarkingRoleAssignment.remove: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

