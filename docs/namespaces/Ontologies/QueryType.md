# QueryType

Method | HTTP request |
------------- | ------------- |
[**iterator**](#iterator) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |
[**get**](#get) | **GET** /v1/ontologies/{ontologyRid}/queryTypes/{queryApiName} |

# **iterator**
Lists the query types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the query types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListQueryTypesResponse**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367" # OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the query types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = None # Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details. 
page_token = None # Optional[PageToken] | pageToken
preview = True # Optional[PreviewMode] | preview


try:
    api_response = foundry_client.ontologies.QueryType.iterator(
ontology_rid,page_size=page_sizepage_token=page_tokenpreview=preview    )
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
**200** | ListQueryTypesResponse  | ListQueryTypesResponse | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Gets a specific query type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the query type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**query_api_name** | QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**QueryType**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"  # OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the query type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
query_api_name = "getEmployeesInCity"  # QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.
preview = True  # Optional[PreviewMode] | preview


try:
    api_response = foundry_client.ontologies.QueryType.get(
        ontology_rid, query_api_name, preview=preview
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
**200** | QueryType  | Represents a query type in the Ontology. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

