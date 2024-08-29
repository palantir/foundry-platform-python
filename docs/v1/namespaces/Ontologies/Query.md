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
**execute_query_request** | Union[ExecuteQueryRequest, ExecuteQueryRequestDict] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ExecuteQueryResponse**

### Example

```python
from foundry.v1 import FoundryV1Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV1Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"

# QueryApiName | queryApiName
query_api_name = "getEmployeesInCity"

# Union[ExecuteQueryRequest, ExecuteQueryRequestDict] | Body of the request
execute_query_request = {"parameters": {"city": "New York"}}

# Optional[PreviewMode] | preview
preview = true


try:
    api_response = foundry_client.ontologies.Query.execute(
        ontology_rid,
        query_api_name,
        execute_query_request,
        preview=preview,
    )
    print("The execute response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Query.execute: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ExecuteQueryResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v1-link) [[Back to README]](../../../../README.md)

