# Marking

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**canonicalize**](#canonicalize) | **POST** /v2/admin/markings/canonicalize | Private Beta |
[**create**](#create) | **POST** /v2/admin/markings | Stable |
[**flatten**](#flatten) | **POST** /v2/admin/markings/flatten | Private Beta |
[**get**](#get) | **GET** /v2/admin/markings/{markingId} | Stable |
[**get_batch**](#get_batch) | **POST** /v2/admin/markings/getBatch | Stable |
[**list**](#list) | **GET** /v2/admin/markings | Stable |
[**parse_classifications**](#parse_classifications) | **POST** /v2/admin/markings/parseClassifications | Stable |
[**replace**](#replace) | **PUT** /v2/admin/markings/{markingId} | Stable |

# **canonicalize**
Returns a canonical set of CBAC marking IDs for the supplied markings. Requires permission to view
classification markings.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_ids** | List[MarkingId] | The marking IDs to canonicalize. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**CanonicalizeMarkingsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[MarkingId] | The marking IDs to canonicalize.
marking_ids = ["18212f9a-0e63-4b79-96a0-aae04df23336"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Marking.canonicalize(marking_ids=marking_ids, preview=preview)
    print("The canonicalize response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Marking.canonicalize: %s\n" % e)

```



### Authorization

Required scopes: [api:admin-read]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CanonicalizeMarkingsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create**
Creates a new Marking.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**category_id** | MarkingCategoryId |  |  |
**initial_members** | List[PrincipalId] | Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.  |  |
**initial_role_assignments** | List[MarkingRoleUpdate] | The initial roles that will be assigned when the Marking is created. At least one ADMINISTER role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.  |  |
**name** | MarkingName |  |  |
**description** | Optional[str] |  | [optional] |

### Return type
**Marking**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingCategoryId
category_id = "0950264e-01c8-4e83-81a9-1a6b7f77621a"
# List[PrincipalId] | Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
initial_members = ["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]
# List[MarkingRoleUpdate] | The initial roles that will be assigned when the Marking is created. At least one ADMINISTER role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
initial_role_assignments = [
    {"role": "ADMINISTER", "principalId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}
]
# MarkingName
name = "PII"
# Optional[str]
description = "Contains personally identifiable information about our customers"


try:
    api_response = client.admin.Marking.create(
        category_id=category_id,
        initial_members=initial_members,
        initial_role_assignments=initial_role_assignments,
        name=name,
        description=description,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Marking.create: %s\n" % e)

```



### Authorization

Required scopes: [api:admin-write]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Marking  | The created Marking | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **flatten**
Flattens up to 1,000 marking expressions. For each expression, returns a set of markings with the same
access requirement, or a stricter one if an exact flat representation is unavailable. You must have
permission to view every input marking. Each clause must contain markings from one category; a clause
in a conjunctive category must contain exactly one marking.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_expressions** | List[MarkingExpression] | The expressions to flatten, in result order. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**FlattenMarkingExpressionsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[MarkingExpression] | The expressions to flatten, in result order.
marking_expressions = [{"and": [{"or": ["18212f9a-0e63-4b79-96a0-aae04df23336"]}]}]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.Marking.flatten(
        marking_expressions=marking_expressions, preview=preview
    )
    print("The flatten response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Marking.flatten: %s\n" % e)

```



### Authorization

Required scopes: [api:admin-read]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | FlattenMarkingExpressionsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Marking with the specified id.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |

### Return type
**Marking**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingId
marking_id = None


try:
    api_response = client.admin.Marking.get(marking_id)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Marking.get: %s\n" % e)

```



### Authorization

Required scopes: [api:admin-read]

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
**body** | List[GetMarkingsBatchRequestElement] | Body of the request |  |

### Return type
**GetMarkingsBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetMarkingsBatchRequestElement] | Body of the request
body = [{"markingId": "18212f9a-0e63-4b79-96a0-aae04df23336"}]


try:
    api_response = client.admin.Marking.get_batch(body)
    print("The get_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Marking.get_batch: %s\n" % e)

```



### Authorization

Required scopes: [api:admin-read]

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
**include_deleted** | Optional[bool] | Whether to include deleted Markings. Defaults to true when omitted. | [optional] |
**marking_type** | Optional[MarkingType] | The marking type of the Markings to return. Defaults to all marking types when omitted.  | [optional] |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |

### Return type
**ListMarkingsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[bool] | Whether to include deleted Markings. Defaults to true when omitted.
include_deleted = None
# Optional[MarkingType] | The marking type of the Markings to return. Defaults to all marking types when omitted.
marking_type = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    for marking in client.admin.Marking.list(
        include_deleted=include_deleted,
        marking_type=marking_type,
        page_size=page_size,
        page_token=page_token,
    ):
        pprint(marking)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Marking.list: %s\n" % e)

```



### Authorization

Required scopes: [api:admin-read]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListMarkingsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **parse_classifications**
Parses classification marking strings (e.g. `MTS//MNF`) into their component marking IDs.
Strings that cannot be parsed are returned in `errors` with a human-readable message.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**classification_strings** | List[str] | The classification strings to parse, e.g. `MTS//MNF`. Requests must contain between 1 and 1000 entries. Duplicate entries count toward this limit but are parsed only once. An empty list returns a `MissingBatchRequest` error, and more than 1000 entries returns a `BatchRequestSizeExceededLimit` error.  |  |

### Return type
**ParseClassificationsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[str] | The classification strings to parse, e.g. `MTS//MNF`. Requests must contain between 1 and 1000 entries. Duplicate entries count toward this limit but are parsed only once. An empty list returns a `MissingBatchRequest` error, and more than 1000 entries returns a `BatchRequestSizeExceededLimit` error.
classification_strings = ["MTS//MNF", "INVALID_MARKING"]


try:
    api_response = client.admin.Marking.parse_classifications(
        classification_strings=classification_strings
    )
    print("The parse_classifications response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Marking.parse_classifications: %s\n" % e)

```



### Authorization

Required scopes: [api:admin-read]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ParseClassificationsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the Marking with the specified id.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_id** | MarkingId |  |  |
**name** | MarkingName |  |  |
**description** | Optional[str] |  | [optional] |

### Return type
**Marking**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarkingId
marking_id = None
# MarkingName
name = "PII"
# Optional[str]
description = "Contains personally identifiable information about our customers"


try:
    api_response = client.admin.Marking.replace(marking_id, name=name, description=description)
    print("The replace response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Marking.replace: %s\n" % e)

```



### Authorization

Required scopes: [api:admin-write]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Marking  | The replaced Marking | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

