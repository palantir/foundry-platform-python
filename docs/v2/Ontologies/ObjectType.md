# ObjectType

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} | Stable |
[**get_by_rid_batch**](#get_by_rid_batch) | **POST** /v2/ontologies/{ontology}/objectTypes/getByRidBatch | Public Beta |
[**get_edits_history**](#get_edits_history) | **POST** /v2/ontologies/{ontology}/objectTypes/{objectType}/editsHistory | Public Beta |
[**get_full_metadata**](#get_full_metadata) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/fullMetadata | Public Beta |
[**get_outgoing_link_type**](#get_outgoing_link_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} | Stable |
[**get_outgoing_link_types_by_object_type_rid_batch**](#get_outgoing_link_types_by_object_type_rid_batch) | **POST** /v2/ontologies/{ontology}/outgoingLinkTypes/getByRidBatch | Public Beta |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/objectTypes | Stable |
[**list_outgoing_link_types**](#list_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes | Stable |

# **get**
Gets a specific object type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the object type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |

### Return type
**ObjectTypeV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# Optional[FoundryBranch] | The Foundry branch to load the object type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None


try:
    api_response = client.ontologies.Ontology.ObjectType.get(ontology, object_type, branch=branch)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectTypeV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_by_rid_batch**
Gets a list of object types by RID in bulk.

Object types are filtered from the response if they don't exist or the requesting token lacks the required
permissions.

The maximum batch size for this endpoint is 100.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**requests** | List[GetObjectTypeByRidBatchRequestElement] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the object type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**GetObjectTypeByRidBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# List[GetObjectTypeByRidBatchRequestElement]
requests = None
# Optional[FoundryBranch] | The Foundry branch to load the object type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.Ontology.ObjectType.get_by_rid_batch(
        ontology, requests=requests, branch=branch, preview=preview
    )
    print("The get_by_rid_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.get_by_rid_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetObjectTypeByRidBatchResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_edits_history**
Returns the history of edits (additions, modifications, deletions) for objects of a
specific object type. This endpoint provides visibility into all actions that have
modified objects of this type.

The edits are returned in reverse chronological order (most recent first) by default. 

Note that filters are ignored for OSv1 object types.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The ontology RID or API name |  |
**object_type** | ObjectTypeApiName | The API name of the object type |  |
**branch** | Optional[FoundryBranch] | The Foundry branch from which we will get edits history. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**filters** | Optional[EditsHistoryFilter] |  | [optional] |
**include_all_previous_properties** | Optional[bool] |  | [optional] |
**object_primary_key** | Optional[ObjectPrimaryKeyV2] |  | [optional] |
**page_size** | Optional[int] | The maximum number of edits to return per page. Defaults to 100. | [optional] |
**page_token** | Optional[str] | Token for retrieving the next page of results | [optional] |
**sort_order** | Optional[EditsHistorySortOrder] |  | [optional] |

### Return type
**ObjectTypeEditsHistoryResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The ontology RID or API name
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type
object_type = "Employee"
# Optional[FoundryBranch] | The Foundry branch from which we will get edits history. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[EditsHistoryFilter]
filters = None
# Optional[bool]
include_all_previous_properties = None
# Optional[ObjectPrimaryKeyV2]
object_primary_key = None
# Optional[int] | The maximum number of edits to return per page. Defaults to 100.
page_size = None
# Optional[str] | Token for retrieving the next page of results
page_token = None
# Optional[EditsHistorySortOrder]
sort_order = None


try:
    api_response = client.ontologies.Ontology.ObjectType.get_edits_history(
        ontology,
        object_type,
        branch=branch,
        filters=filters,
        include_all_previous_properties=include_all_previous_properties,
        object_primary_key=object_primary_key,
        page_size=page_size,
        page_token=page_token,
        sort_order=sort_order,
    )
    print("The get_edits_history response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.get_edits_history: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectTypeEditsHistoryResponse  | Success response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_full_metadata**
Gets the full metadata for a specific object type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**ObjectTypeFullMetadata**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.Ontology.ObjectType.get_full_metadata(
        ontology,
        object_type,
        branch=branch,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The get_full_metadata response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.get_full_metadata: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectTypeFullMetadata  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_outgoing_link_type**
Get an outgoing link for an object type.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |  |
**link_type** | LinkTypeApiName | The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |

### Return type
**LinkTypeSideV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
object_type = "Employee"
# LinkTypeApiName | The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.
link_type = "directReport"
# Optional[FoundryBranch] | The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None


try:
    api_response = client.ontologies.Ontology.ObjectType.get_outgoing_link_type(
        ontology, object_type, link_type, branch=branch
    )
    print("The get_outgoing_link_type response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.get_outgoing_link_type: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LinkTypeSideV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_outgoing_link_types_by_object_type_rid_batch**
Gets outgoing link types for a batch of object types, identified by their RIDs.

For each requested object type, returns the list of outgoing link types visible to the
requesting token. Optionally, results can be filtered to only include specific link type RIDs.

Object types that don't exist or that the requesting token lacks permissions for are
silently omitted from the response.

The maximum batch size for this endpoint is 100.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**filter_link_type_rids** | List[LinkTypeRid] | If provided, only return outgoing link types with RIDs in this list. If omitted, all outgoing link types for each requested object type are returned.  |  |
**requests** | List[GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the outgoing link type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**GetOutgoingLinkTypesByObjectTypeRidBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# List[LinkTypeRid] | If provided, only return outgoing link types with RIDs in this list. If omitted, all outgoing link types for each requested object type are returned.
filter_link_type_rids = None
# List[GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement]
requests = None
# Optional[FoundryBranch] | The Foundry branch to load the outgoing link type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = (
        client.ontologies.Ontology.ObjectType.get_outgoing_link_types_by_object_type_rid_batch(
            ontology,
            filter_link_type_rids=filter_link_type_rids,
            requests=requests,
            branch=branch,
            preview=preview,
        )
    )
    print("The get_outgoing_link_types_by_object_type_rid_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print(
        "HTTP error when calling ObjectType.get_outgoing_link_types_by_object_type_rid_batch: %s\n"
        % e
    )

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetOutgoingLinkTypesByObjectTypeRidBatchResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the object types for the given Ontology.

Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
more results available, at least one result will be present in the
response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to list the object types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListObjectTypesV2Response**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[FoundryBranch] | The Foundry branch to list the object types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for object_type in client.ontologies.Ontology.ObjectType.list(
        ontology, branch=branch, page_size=page_size, page_token=page_token
    ):
        pprint(object_type)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListObjectTypesV2Response  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_outgoing_link_types**
List the outgoing links for an object type.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the outgoing link types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListOutgoingLinkTypesResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
object_type = "Flight"
# Optional[FoundryBranch] | The Foundry branch to load the outgoing link types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PageSize] | The desired size of the page to be returned.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for object_type in client.ontologies.Ontology.ObjectType.list_outgoing_link_types(
        ontology, object_type, branch=branch, page_size=page_size, page_token=page_token
    ):
        pprint(object_type)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.list_outgoing_link_types: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOutgoingLinkTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

