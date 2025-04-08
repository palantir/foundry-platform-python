# QueryType

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v1/ontologies/{ontologyRid}/queryTypes/{queryApiName} | Stable |
[**list**](#list) | **GET** /v1/ontologies/{ontologyRid}/queryTypes | Stable |

# **get**
Gets a specific query type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the query type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**query_api_name** | QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.  |  |

### Return type
**QueryType**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the query type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.
query_api_name = "getEmployeesInCity"


try:
    api_response = foundry_client.ontologies.Ontology.QueryType.get(ontology_rid, query_api_name)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling QueryType.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | QueryType  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **list**
Lists the query types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the query types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListQueryTypesResponse**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the query types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for query_type in client.ontologies.Ontology.QueryType.list(
        ontology_rid, page_size=page_size, page_token=page_token
    ):
        pprint(query_type)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling QueryType.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListQueryTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

