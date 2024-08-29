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
**apply_action_request_v2** | Union[ApplyActionRequestV2, ApplyActionRequestV2Dict] | Body of the request |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**SyncApplyActionResponseV2**

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

# ActionTypeApiName | action
action = "rename-employee"

# Union[ApplyActionRequestV2, ApplyActionRequestV2Dict] | Body of the request
apply_action_request_v2 = {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}}

# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None

# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.Action.apply(
        ontology,
        action,
        apply_action_request_v2,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The apply response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Action.apply: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SyncApplyActionResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

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
**batch_apply_action_request_v2** | Union[BatchApplyActionRequestV2, BatchApplyActionRequestV2Dict] | Body of the request |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**BatchApplyActionResponseV2**

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

# ActionTypeApiName | action
action = "rename-employee"

# Union[BatchApplyActionRequestV2, BatchApplyActionRequestV2Dict] | Body of the request
batch_apply_action_request_v2 = {
    "requests": [
        {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}},
        {"parameters": {"id": 80061, "newName": "Joe Bloggs"}},
    ]
}

# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None

# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.Action.apply_batch(
        ontology,
        action,
        batch_apply_action_request_v2,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The apply_batch response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Action.apply_batch: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | BatchApplyActionResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

