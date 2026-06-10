# ActionType

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} | Stable |
[**get_by_rid**](#get_by_rid) | **GET** /v2/ontologies/{ontology}/actionTypes/byRid/{actionTypeRid} | Stable |
[**get_by_rid_batch**](#get_by_rid_batch) | **POST** /v2/ontologies/{ontology}/actionTypes/getByRidBatch | Public Beta |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/actionTypes | Stable |
[**search**](#search) | **POST** /v2/ontologies/{ontology}/actionTypes/search | Private Beta |

# **get**
Gets a specific action type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**action_type** | ActionTypeApiName | The name of the action type in the API.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |

### Return type
**ActionTypeV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ActionTypeApiName | The name of the action type in the API.
action_type = "promote-employee"
# Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None


try:
    api_response = client.ontologies.Ontology.ActionType.get(ontology, action_type, branch=branch)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionType.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ActionTypeV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_by_rid**
Gets a specific action type with the given RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**action_type_rid** | ActionTypeRid | The RID of the action type.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |

### Return type
**ActionTypeV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ActionTypeRid | The RID of the action type.
action_type_rid = "ri.ontology.main.action-type.7ed72754-7491-428a-bb18-4d7296eb2167"
# Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None


try:
    api_response = client.ontologies.Ontology.ActionType.get_by_rid(
        ontology, action_type_rid, branch=branch
    )
    print("The get_by_rid response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionType.get_by_rid: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ActionTypeV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_by_rid_batch**
Gets a list of action types by RID in bulk.

Action types are filtered from the response if they don't exist or the requesting token lacks the required
permissions.

The maximum batch size for this endpoint is 100.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**requests** | List[GetActionTypeByRidBatchRequestElement] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**GetActionTypeByRidBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# List[GetActionTypeByRidBatchRequestElement]
requests = None
# Optional[FoundryBranch] | The Foundry branch to load the action type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.Ontology.ActionType.get_by_rid_batch(
        ontology, requests=requests, branch=branch, preview=preview
    )
    print("The get_by_rid_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionType.get_by_rid_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetActionTypeByRidBatchResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListActionTypesResponseV2**

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
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for action_type in client.ontologies.Ontology.ActionType.list(
        ontology, branch=branch, page_size=page_size, page_token=page_token
    ):
        pprint(action_type)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionType.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListActionTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**
Search for action types in the given Ontology that match the provided filters. Results are returned by
relevance of the match unless an explicit `orderBy` is provided.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response. Search results are eventually
consistent with the latest Ontology version and may lag slightly behind the last Ontology modification.


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
**SearchActionTypesResponseV2**

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
    api_response = client.ontologies.Ontology.ActionType.search(
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
    print("HTTP error when calling ActionType.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchActionTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

