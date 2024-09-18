# Query

Method | HTTP request |
------------- | ------------- |
[**execute**](#execute) | **POST** /v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute |

# **execute**
Executes a Query using the given parameters. Optional parameters do not need to be supplied.
Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**query_api_name** | QueryApiName | queryApiName |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |

### Return type
**ExecuteQueryResponse**

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
# Dict[ParameterId, Optional[DataValue]] |
parameters = {"city": "New York"}


try:
    api_response = foundry_client.ontologies.Query.execute(
        ontology_rid,
        query_api_name,
        parameters=parameters,
    )
    print("The execute response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Query.execute: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ExecuteQueryResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

