# Action

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**apply**](#apply) | **POST** /v2/ontologies/{ontology}/actions/{action}/apply | Stable |
[**apply_batch**](#apply_batch) | **POST** /v2/ontologies/{ontology}/actions/{action}/applyBatch | Stable |

# **apply**
Applies an action using the given parameters. 

Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
this endpoint.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**action** | ActionTypeApiName | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.  |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**branch** | Optional[FoundryBranch] | The Foundry branch to apply the action against. If not specified, the default branch is used.  | [optional] |
**options** | Optional[ApplyActionRequestOptions] |  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |

### Return type
**SyncApplyActionResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ActionTypeApiName | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
action = "rename-employee"
# Dict[ParameterId, Optional[DataValue]]
parameters = {"id": 80060, "newName": "Anna Smith-Doe"}
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[FoundryBranch] | The Foundry branch to apply the action against. If not specified, the default branch is used.
branch = None
# Optional[ApplyActionRequestOptions]
options = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None


try:
    api_response = client.ontologies.Action.apply(
        ontology,
        action,
        parameters=parameters,
        artifact_repository=artifact_repository,
        branch=branch,
        options=options,
        package_name=package_name,
    )
    print("The apply response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Action.apply: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SyncApplyActionResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **apply_batch**
Applies multiple actions (of the same Action Type) using the given parameters.

Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
call Functions may receive a higher limit.

Note that [notifications](https://palantir.com/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**action** | ActionTypeApiName | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.  |  |
**requests** | List[BatchApplyActionRequestItem] |  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**branch** | Optional[FoundryBranch] | The Foundry branch to apply the action against. If not specified, the default branch is used.  | [optional] |
**options** | Optional[BatchApplyActionRequestOptions] |  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |

### Return type
**BatchApplyActionResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ActionTypeApiName | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
action = "rename-employee"
# List[BatchApplyActionRequestItem]
requests = [
    {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}},
    {"parameters": {"id": 80061, "newName": "Joe Bloggs"}},
]
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[FoundryBranch] | The Foundry branch to apply the action against. If not specified, the default branch is used.
branch = None
# Optional[BatchApplyActionRequestOptions]
options = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None


try:
    api_response = client.ontologies.Action.apply_batch(
        ontology,
        action,
        requests=requests,
        artifact_repository=artifact_repository,
        branch=branch,
        options=options,
        package_name=package_name,
    )
    print("The apply_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Action.apply_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | BatchApplyActionResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

