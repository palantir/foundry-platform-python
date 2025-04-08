# Query

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**execute**](#execute) | **POST** /v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute | Stable |

# **execute**
Executes a Query using the given parameters. Optional parameters do not need to be supplied.
Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the Query. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**query_api_name** | QueryApiName | The API name of the Query to execute.  |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |

### Return type
**ExecuteQueryResponse**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the Query. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# QueryApiName | The API name of the Query to execute.
query_api_name = "getEmployeesInCity"
# Dict[ParameterId, Optional[DataValue]]
parameters = {"city": "New York"}


try:
    api_response = foundry_client.ontologies.Query.execute(
        ontology_rid, query_api_name, parameters=parameters
    )
    print("The execute response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Query.execute: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ExecuteQueryResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

