# QueryType

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/queryTypes |
[**page**](#page) | **GET** /v2/ontologies/{ontology}/queryTypes |

# **get**
Gets a specific query type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**query_api_name** | QueryApiName | queryApiName |  |

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

# OntologyIdentifier | ontology
ontology = "palantir"

# QueryApiName | queryApiName
query_api_name = "getEmployeesInCity"


try:
    api_response = foundry_client.ontologies_v2.QueryType.get(
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
**200** | QueryTypeV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**
Lists the query types for the given Ontology.        

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.        

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |

### Return type
**ResourceIterator[QueryTypeV2]**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | ontology
ontology = "palantir"

# Optional[PageSize] | pageSize
page_size = None



try:
    for query_type in foundry_client.ontologies_v2.QueryType.list(ontology, page_size=page_size)
:
        pprint(query_type)
except PalantirRPCException as e:
    print("HTTP error when calling QueryType.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListQueryTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **page**
Lists the query types for the given Ontology.        

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.        

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListQueryTypesResponseV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | ontology
ontology = "palantir"

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None



try:
    api_response = foundry_client.ontologies_v2.QueryType.page(ontology, page_size=page_sizepage_token=page_token)
    print("The QueryType.page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling QueryType.page: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListQueryTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

