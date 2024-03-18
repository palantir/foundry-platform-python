# QueryType

Method | HTTP request |
------------- | ------------- |
[**iterator**](#iterator) | **GET** /v2/ontologies/{ontology}/queryTypes |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} |

# **iterator**
Lists the query types for the given Ontology.        

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.        

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListQueryTypesResponseV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = "palantir" # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = None # Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details. 
page_token = None # Optional[PageToken] | pageToken


try:
    api_response = foundry_client.ontologiesv2.QueryType.iterator(
ontology,page_size=page_sizepage_token=page_token    )
    print("The QueryType.iterator response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling QueryType.iterator: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListQueryTypesResponseV2  | ListQueryTypesResponseV2 | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Gets a specific query type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**query_api_name** | QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.  |  |

### Return type
**QueryTypeV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

ontology = "palantir"  # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
query_api_name = "getEmployeesInCity"  # QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.


try:
    api_response = foundry_client.ontologiesv2.QueryType.get(
        ontology,
        query_api_name,
    )
    print("The QueryType.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling QueryType.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | QueryTypeV2  | Represents a query type in the Ontology. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

