# ActionType

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} | Stable |
[**get_by_rid**](#get_by_rid) | **GET** /v2/ontologies/{ontology}/actionTypes/byRid/{actionTypeRid} | Stable |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/actionTypes | Stable |

# **get**
Gets a specific action type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**action_type** | ActionTypeApiName | The name of the action type in the API.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used.  | [optional] |

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
# Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
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
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used.  | [optional] |

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
# Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
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

# **list**
Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to list the action types from. If not specified, the default branch will be used.  | [optional] |
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
# Optional[FoundryBranch] | The Foundry branch to list the action types from. If not specified, the default branch will be used.
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

