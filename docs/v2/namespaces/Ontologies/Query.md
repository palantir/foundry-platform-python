# Query

Method | HTTP request |
------------- | ------------- |
[**execute**](#execute) | **POST** /v2/ontologies/{ontology}/queries/{queryApiName}/execute |

# **execute**
Executes a Query using the given parameters.

Optional parameters do not need to be supplied.

Third-party applications using this endpoint via OAuth2 must request the 
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**query_api_name** | QueryApiName | queryApiName |  |
**execute_query_request** | Union[ExecuteQueryRequest, ExecuteQueryRequestDict] | Body of the request |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**ExecuteQueryResponse**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"

# QueryApiName | queryApiName
query_api_name = "getEmployeesInCity"

# Union[ExecuteQueryRequest, ExecuteQueryRequestDict] | Body of the request
execute_query_request = {"parameters": {"city": "New York"}}

# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None

# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.Query.execute(
        ontology,
        query_api_name,
        execute_query_request,
        artifact_repository=artifact_repository,
        package_name=package_name,
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

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

