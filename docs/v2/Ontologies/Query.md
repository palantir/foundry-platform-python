# Query

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**execute**](#execute) | **POST** /v2/ontologies/{ontology}/queries/{queryApiName}/execute | Stable |

# **execute**
Executes a Query using the given parameters.

Optional parameters do not need to be supplied.

Third-party applications using this endpoint via OAuth2 must request the 
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**query_api_name** | QueryApiName | The API name of the Query to execute.  |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**version** | Optional[FunctionVersion] | The version of the Query to execute.  | [optional] |

### Return type
**ExecuteQueryResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# QueryApiName | The API name of the Query to execute.
query_api_name = "getEmployeesInCity"
# Dict[ParameterId, Optional[DataValue]]
parameters = {"city": "New York"}
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[FunctionVersion] | The version of the Query to execute.
version = None


try:
    api_response = client.ontologies.Query.execute(
        ontology,
        query_api_name,
        parameters=parameters,
        artifact_repository=artifact_repository,
        package_name=package_name,
        version=version,
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

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

