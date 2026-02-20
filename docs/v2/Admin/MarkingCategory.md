# MarkingCategory

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/admin/markingCategories | Private Beta |
[**get**](#get) | **GET** /v2/admin/markingCategories/{markingCategoryId} | Public Beta |
[**list**](#list) | **GET** /v2/admin/markingCategories | Public Beta |

# **create**
Creates a new MarkingCategory.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**description** | MarkingCategoryDescription |  |  |
**initial_permissions** | MarkingCategoryPermissions | The initial permissions for the Marking Category. This can be changed later through MarkingCategoryPermission operations. The provided permissions must include at least one ADMINISTER role assignment.  WARNING: If you do not list your own principal ID or the ID of a Group that you are a member of as an ADMINISTER, you will create a Marking Category that you cannot administer.  |  |
**name** | MarkingCategoryName |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**MarkingCategory**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingCategoryDescription
description = "Markings related to data about our customers"
# MarkingCategoryPermissions | The initial permissions for the Marking Category. This can be changed later through MarkingCategoryPermission operations. The provided permissions must include at least one ADMINISTER role assignment.  WARNING: If you do not list your own principal ID or the ID of a Group that you are a member of as an ADMINISTER, you will create a Marking Category that you cannot administer.
initial_permissions = {
    "organizationRids": ["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"],
    "roles": [{"role": "ADMINISTER", "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}],
}
# MarkingCategoryName
name = "Customer Data"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.MarkingCategory.create(
        description=description, initial_permissions=initial_permissions, name=name, preview=preview
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarkingCategory.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MarkingCategory  | The created MarkingCategory | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the MarkingCategory with the specified id.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_category_id** | MarkingCategoryId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**MarkingCategory**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingCategoryId
marking_category_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.MarkingCategory.get(marking_category_id, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarkingCategory.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MarkingCategory  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Maximum page size 100.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListMarkingCategoriesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for marking_category in client.admin.MarkingCategory.list(
        page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(marking_category)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarkingCategory.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListMarkingCategoriesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

