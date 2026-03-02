# Query

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**execute**](#execute) | **POST** /v2/ontologies/{ontology}/queries/{queryApiName}/execute | Stable |

# **execute**
Executes a Query using the given parameters. By default, the latest version of the Query is executed.

Optional parameters do not need to be supplied.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**query_api_name** | QueryApiName | The API name of the Query to execute.  |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |
**attribution** | Optional[Attribution] | The Attribution to be used when executing this request.  | [optional] |
**branch** | Optional[FoundryBranch] | The Foundry branch to execute the query from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. When provided without `version`, the latest version on this branch is used, including pre-release versions. When provided with `version`, the specified version must exist on the branch.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |
**trace_parent** | Optional[TraceParent] | The W3C trace parent header included in the request.  | [optional] |
**trace_state** | Optional[TraceState] | The W3C trace state header included in the request.  | [optional] |
**transaction_id** | Optional[OntologyTransactionId] | The ID of an Ontology transaction to read from.  Transactions are an experimental feature and all workflows may not be supported.  | [optional] |
**version** | Optional[FunctionVersion] | The version of the Query to execute. When used with `branch`, the specified version must exist on the branch.  | [optional] |

### Return type
**ExecuteQueryResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# QueryApiName | The API name of the Query to execute.
query_api_name = "getEmployeesInCity"
# Dict[ParameterId, Optional[DataValue]]
parameters = {"city": "New York"}
# Optional[Attribution] | The Attribution to be used when executing this request.
attribution = None
# Optional[FoundryBranch] | The Foundry branch to execute the query from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. When provided without `version`, the latest version on this branch is used, including pre-release versions. When provided with `version`, the specified version must exist on the branch.
branch = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None
# Optional[TraceParent] | The W3C trace parent header included in the request.
trace_parent = None
# Optional[TraceState] | The W3C trace state header included in the request.
trace_state = None
# Optional[OntologyTransactionId] | The ID of an Ontology transaction to read from.  Transactions are an experimental feature and all workflows may not be supported.
transaction_id = None
# Optional[FunctionVersion] | The version of the Query to execute. When used with `branch`, the specified version must exist on the branch.
version = None


try:
    api_response = client.ontologies.Query.execute(
        ontology,
        query_api_name,
        parameters=parameters,
        attribution=attribution,
        branch=branch,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
        trace_parent=trace_parent,
        trace_state=trace_state,
        transaction_id=transaction_id,
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

