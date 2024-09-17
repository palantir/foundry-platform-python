# Action

Method | HTTP request |
------------- | ------------- |
[**apply**](#apply) | **POST** /v2/ontologies/{ontology}/actions/{action}/apply |
[**apply_batch**](#apply_batch) | **POST** /v2/ontologies/{ontology}/actions/{action}/applyBatch |

# **apply**
Applies an action using the given parameters. 

Changes to the Ontology are eventually consistent and may take some time to be visible.

Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) are not currently supported by
this endpoint.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**action** | ActionTypeApiName | action |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**options** | Optional[ApplyActionRequestOptionsDict] |  | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**SyncApplyActionResponseV2**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"
# ActionTypeApiName | action
action = "rename-employee"
# Dict[ParameterId, Optional[DataValue]] |
parameters = {"id": 80060, "newName": "Anna Smith-Doe"}
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[ApplyActionRequestOptionsDict] |
options = None
# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.Action.apply(
        ontology,
        action,
        parameters=parameters,
        artifact_repository=artifact_repository,
        options=options,
        package_name=package_name,
    )
    print("The apply response:\n")
    pprint(api_response)
except PalantirRPCException as e:
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
Changes to the Ontology are eventually consistent and may take some time to be visible.

Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
call Functions may receive a higher limit.

Note that [notifications](/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**action** | ActionTypeApiName | action |  |
**requests** | List[BatchApplyActionRequestItemDict] |  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**options** | Optional[BatchApplyActionRequestOptionsDict] |  | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**BatchApplyActionResponseV2**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"
# ActionTypeApiName | action
action = "rename-employee"
# List[BatchApplyActionRequestItemDict] |
requests = [
    {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}},
    {"parameters": {"id": 80061, "newName": "Joe Bloggs"}},
]
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[BatchApplyActionRequestOptionsDict] |
options = None
# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.Action.apply_batch(
        ontology,
        action,
        requests=requests,
        artifact_repository=artifact_repository,
        options=options,
        package_name=package_name,
    )
    print("The apply_batch response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Action.apply_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | BatchApplyActionResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

