# Action

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**apply**](#apply) | **POST** /v2/ontologies/{ontology}/actions/{action}/apply | Stable |
[**apply_batch**](#apply_batch) | **POST** /v2/ontologies/{ontology}/actions/{action}/applyBatch | Stable |

# **apply**
Applies an action using the given parameters. 

Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

Note that a 200 HTTP status code only indicates that the request was received and processed by the server. 
See the validation result in the response body to determine if the action was applied successfully.

Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
this endpoint.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**action** | ActionTypeApiName | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.  |  |
**parameters** | Dict[ParameterId, Optional[DataValue]] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to apply the action against. If not specified, the default branch is used.  | [optional] |
**options** | Optional[ApplyActionRequestOptions] |  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**SyncApplyActionResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ActionTypeApiName | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
action = "rename-employee"
# Dict[ParameterId, Optional[DataValue]]
parameters = {"id": 80060, "newName": "Anna Smith-Doe"}
# Optional[FoundryBranch] | The Foundry branch to apply the action against. If not specified, the default branch is used.
branch = None
# Optional[ApplyActionRequestOptions]
options = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.Action.apply(
        ontology,
        action,
        parameters=parameters,
        branch=branch,
        options=options,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
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
**ontology** | OntologyIdentifier |  |  |
**action** | ActionTypeApiName | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.  |  |
**requests** | List[BatchApplyActionRequestItem] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to apply the action against. If not specified, the default branch is used.  | [optional] |
**options** | Optional[BatchApplyActionRequestOptions] |  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**BatchApplyActionResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ActionTypeApiName | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
action = "rename-employee"
# List[BatchApplyActionRequestItem]
requests = [
    {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}},
    {"parameters": {"id": 80061, "newName": "Joe Bloggs"}},
]
# Optional[FoundryBranch] | The Foundry branch to apply the action against. If not specified, the default branch is used.
branch = None
# Optional[BatchApplyActionRequestOptions]
options = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.Action.apply_batch(
        ontology,
        action,
        requests=requests,
        branch=branch,
        options=options,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
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

