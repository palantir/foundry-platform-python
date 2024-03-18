# ActionTypeV2

Method | HTTP request |
------------- | ------------- |
[**iterator**](#iterator) | **GET** /v2/ontologies/{ontology}/actionTypes |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} |

# **iterator**
Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListActionTypesResponseV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = "palantir" # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = None # Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details. 
page_token = None # Optional[PageToken] | pageToken


try:
    api_response = foundry_client.ontologiesv2.ActionTypeV2.iterator(
ontology,page_size=page_sizepage_token=page_token    )
    print("The ActionTypeV2.iterator response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ActionTypeV2.iterator: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListActionTypesResponseV2  | ListActionTypesResponseV2 | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Gets a specific action type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**action_type** | ActionTypeApiName | The name of the action type in the API.  |  |

### Return type
**ActionTypeV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

ontology = "palantir"  # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
action_type = "promote-employee"  # ActionTypeApiName | The name of the action type in the API.


try:
    api_response = foundry_client.ontologiesv2.ActionTypeV2.get(
        ontology,
        action_type,
    )
    print("The ActionTypeV2.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ActionTypeV2.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ActionTypeV2  | Represents an action type in the Ontology. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

