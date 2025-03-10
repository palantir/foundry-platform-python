# Marking

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/admin/markings | Public Beta |
[**get**](#get) | **GET** /v2/admin/markings/{markingId} | Public Beta |
[**get_batch**](#get_batch) | **POST** /v2/admin/markings/getBatch | Public Beta |
[**list**](#list) | **GET** /v2/admin/markings | Public Beta |
[**page**](#page) | **GET** /v2/admin/markings | Public Beta |

# **create**
Creates a new Marking.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**category_id** | MarkingCategoryId |  |  |
**initial_members** | typing.List[core_models.PrincipalId] | Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.  |  |
**initial_role_assignments** | typing.List[typing.Union[MarkingRoleUpdate, MarkingRoleUpdateDict]] | The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.  |  |
**name** | MarkingName |  |  |
**description** | typing.Optional[str] |  | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**Marking**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# MarkingCategoryId |
category_id = "0950264e-01c8-4e83-81a9-1a6b7f77621a"
# typing.List[core_models.PrincipalId] | Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
initial_members = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# typing.List[typing.Union[MarkingRoleUpdate, MarkingRoleUpdateDict]] | The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
initial_role_assignments = [
    {"role": "ADMINISTER", "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}
]
# MarkingName |
name = "PII"
# typing.Optional[str] |
description = "Contains personally identifiable information about our customers"
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Marking.create(
        category_id=category_id,
        initial_members=initial_members,
        initial_role_assignments=initial_role_assignments,
        name=name,
        description=description,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Marking.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Marking  | The created Marking | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Marking with the specified id.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | core_models.MarkingId | markingId |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**Marking**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# core_models.MarkingId | markingId
marking_id = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Marking.get(
        marking_id,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Marking.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Marking  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_batch**
Execute multiple get requests on Marking.

The maximum batch size for this endpoint is 500.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | typing_extensions.Annotated[typing.List[typing.Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]], annotated_types.Len(min_length=1, max_length=500)] | Body of the request |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**GetMarkingsBatchResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# typing_extensions.Annotated[typing.List[typing.Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]], annotated_types.Len(min_length=1, max_length=500)] | Body of the request
body = [{"markingId": "18212f9a-0e63-4b79-96a0-aae04df23336"}]
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Marking.get_batch(
        body,
        preview=preview,
    )
    print("The get_batch response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Marking.get_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetMarkingsBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Maximum page size 100.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ListMarkingsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    for marking in foundry_client.admin.Marking.list(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(marking)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Marking.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListMarkingsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Maximum page size 100.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ListMarkingsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Marking.page(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Marking.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListMarkingsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

