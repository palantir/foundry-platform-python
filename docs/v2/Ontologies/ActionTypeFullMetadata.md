# ActionTypeFullMetadata

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType}/fullMetadata | Private Beta |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/actionTypesFullMetadata | Private Beta |

# **get**
Gets the full metadata associated with an action type.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**action_type** | ActionTypeApiName | The name of the action type in the API.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ActionTypeFullMetadata**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ActionTypeApiName | The name of the action type in the API.
action_type = "promote-employee"
# Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.ActionTypeFullMetadata.get(
        ontology, action_type, branch=branch, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionTypeFullMetadata.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ActionTypeFullMetadata  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the action types (with full metadata) for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**object_type_api_names** | Optional[List[ObjectTypeApiName]] | An set of object type api names that can be used to filter which actions are returned. Currently this only works for one object type, specifying more will cause the request to fail.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListActionTypesFullMetadataResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[FoundryBranch] | The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[List[ObjectTypeApiName]] | An set of object type api names that can be used to filter which actions are returned. Currently this only works for one object type, specifying more will cause the request to fail.
object_type_api_names = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    for action_type_full_metadata in client.ontologies.ActionTypeFullMetadata.list(
        ontology,
        branch=branch,
        object_type_api_names=object_type_api_names,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(action_type_full_metadata)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ActionTypeFullMetadata.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListActionTypesFullMetadataResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

