# ActionType

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName} | Stable |
[**list**](#list) | **GET** /v1/ontologies/{ontologyRid}/actionTypes | Stable |

# **get**
Gets a specific action type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the action type.  |  |
**action_type_api_name** | ActionTypeApiName | The name of the action type in the API.  |  |

### Return type
**ActionType**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the action type.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ActionTypeApiName | The name of the action type in the API.
action_type_api_name = "promote-employee"


try:
    api_response = foundry_client.ontologies.Ontology.ActionType.get(
        ontology_rid, action_type_api_name
    )
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
**200** | ActionType  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **list**
Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListActionTypesResponse**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for action_type in client.ontologies.Ontology.ActionType.list(
        ontology_rid, page_size=page_size, page_token=page_token
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
**200** | ListActionTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

