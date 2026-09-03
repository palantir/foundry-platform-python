# ActionTypeFullMetadata

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType}/fullMetadata | Private Beta |
[**get_full_metadata_batch**](#get_full_metadata_batch) | **POST** /v2/ontologies/{ontology}/actionTypes/getFullMetadataBatch | Private Beta |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/actionTypesFullMetadata | Private Beta |
[**search**](#search) | **POST** /v2/ontologies/{ontology}/actionTypes/searchFullMetadata | Private Beta |

# **get**
Gets the full metadata associated with an action type.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**action_type** | ActionTypeApiName | The name of the action type in the API.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ActionTypeFullMetadata**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ActionTypeApiName | The name of the action type in the API.
action_type = "promote-employee"
# Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.ActionTypeFullMetadata.get(
        ontology, action_type, branch=branch, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionTypeFullMetadata.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ActionTypeFullMetadata  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_full_metadata_batch**
Gets a list of action types with full metadata (parameters and logic rules) by their API names in
bulk.

Action types are filtered from the response if they don't exist, the requesting token lacks the
required permissions, or any of their logic rules are not supported by this API, so the response may
contain fewer entries than requested.

The maximum batch size for this endpoint is 100.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**requests** | List[GetActionTypeFullMetadataBatchRequestElement] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**GetActionTypeFullMetadataBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# List[GetActionTypeFullMetadataBatchRequestElement]
requests = None
# Optional[FoundryBranch] | The Foundry branch to load the action type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.ActionTypeFullMetadata.get_full_metadata_batch(
        ontology, requests=requests, branch=branch, preview=preview
    )
    print("The get_full_metadata_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionTypeFullMetadata.get_full_metadata_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetActionTypeFullMetadataBatchResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the action types (with full metadata) for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**object_type_api_names** | Optional[List[ObjectTypeApiName]] | A set of object type API names that can be used to filter which actions are returned.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListActionTypesFullMetadataResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[FoundryBranch] | The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[List[ObjectTypeApiName]] | A set of object type API names that can be used to filter which actions are returned.
object_type_api_names = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    for action_type_full_metadata in client.ontologies.ActionTypeFullMetadata.list(
        ontology,
        branch=branch,
        object_type_api_names=object_type_api_names,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(action_type_full_metadata)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionTypeFullMetadata.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListActionTypesFullMetadataResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**
Search for action types in the given Ontology that match the provided filters. Full action type metadata
results are returned by relevance of the match unless an explicit `orderBy` is provided.

Action types with logic rules that cannot be represented in the API are omitted from the results. 
As a consequence, totalCount counts all matching action types in the Ontology and may exceed the number
of results returned across all pages, and an individual page may be empty even when nextPageToken is present.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to search the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**fuzziness** | Optional[ActionTypeFuzziness] |  | [optional] |
**order_by** | Optional[SearchActionTypesOrderByV2] |  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**where** | Optional[ActionTypeSearchJsonQueryV2] |  | [optional] |

### Return type
**SearchActionTypesFullMetadataResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[FoundryBranch] | The Foundry branch to search the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[ActionTypeFuzziness]
fuzziness = None
# Optional[SearchActionTypesOrderByV2]
order_by = None
# Optional[PageSize]
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[ActionTypeSearchJsonQueryV2]
where = {"type": "actionTypeDisplayName", "value": {"type": "contains", "value": "promote"}}


try:
    api_response = client.ontologies.ActionTypeFullMetadata.search(
        ontology,
        branch=branch,
        fuzziness=fuzziness,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        where=where,
    )
    print("The search response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionTypeFullMetadata.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchActionTypesFullMetadataResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

