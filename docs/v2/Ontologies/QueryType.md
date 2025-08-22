# QueryType

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} | Stable |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/queryTypes | Stable |

# **get**
Gets a specific query type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**query_api_name** | QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.  |  |
**version** | Optional[FunctionVersion] | The version of the Query to get.  | [optional] |

### Return type
**QueryTypeV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.
query_api_name = "getEmployeesInCity"
# Optional[FunctionVersion] | The version of the Query to get.
version = None


try:
    api_response = client.ontologies.Ontology.QueryType.get(
        ontology, query_api_name, version=version
    )
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
**200** | QueryTypeV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the query types for the given Ontology.        

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListQueryTypesResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for query_type in client.ontologies.Ontology.QueryType.list(
        ontology, page_size=page_size, page_token=page_token
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
**200** | ListQueryTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

