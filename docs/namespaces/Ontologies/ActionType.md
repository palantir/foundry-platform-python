# ActionType

Method | HTTP request |
------------- | ------------- |
[**iterator**](#iterator) | **GET** /v1/ontologies/{ontologyRid}/actionTypes |
[**get**](#get) | **GET** /v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName} |

# **iterator**
Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListActionTypesResponse**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367" # OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = None # Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details. 
page_token = None # Optional[PageToken] | pageToken


try:
    api_response = foundry_client.ontologies.ActionType.iterator(
ontology_rid,page_size=page_sizepage_token=page_token    )
    print("The ActionType.iterator response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ActionType.iterator: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListActionTypesResponse  | ListActionTypesResponse | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
Gets a specific action type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the action type.  |  |
**action_type_api_name** | ActionTypeApiName | The name of the action type in the API.  |  |

### Return type
**ActionType**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"  # OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the action type.
action_type_api_name = (
    "promote-employee"  # ActionTypeApiName | The name of the action type in the API.
)


try:
    api_response = foundry_client.ontologies.ActionType.get(
        ontology_rid,
        action_type_api_name,
    )
    print("The ActionType.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ActionType.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ActionType  | Represents an action type in the Ontology. | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

