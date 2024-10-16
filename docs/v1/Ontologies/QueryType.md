# QueryType

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v1/ontologies/{ontologyRid}/queryTypes/{queryApiName} |
[**list**](#list) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |
[**page**](#page) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |

# **get**
Gets a specific query type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**query_api_name** | QueryApiName | queryApiName |  |

### Return type
**QueryType**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# QueryApiName | queryApiName
query_api_name = "getEmployeesInCity"


try:
    api_response = foundry_client.ontologies.Ontology.QueryType.get(
        ontology_rid,
        query_api_name,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
**ontology_rid** | OntologyRid | ontologyRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |

### Return type
**ResourceIterator[QueryType]**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# Optional[PageSize] | pageSize
page_size = None


try:
    for query_type in foundry_client.ontologies.Ontology.QueryType.list(
        ontology_rid,
        page_size=page_size,
    ):
        pprint(query_type)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling QueryType.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListQueryTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **page**
Lists the query types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListQueryTypesResponse**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None


try:
    api_response = foundry_client.ontologies.Ontology.QueryType.page(
        ontology_rid,
        page_size=page_size,
        page_token=page_token,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling QueryType.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListQueryTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

