# Ontology

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/ontologies/{ontology} | Stable |
[**get_full_metadata**](#get_full_metadata) | **GET** /v2/ontologies/{ontology}/fullMetadata | Public Beta |
[**list**](#list) | **GET** /v2/ontologies | Stable |
[**load_metadata**](#load_metadata) | **POST** /v2/ontologies/{ontology}/metadata | Private Beta |

# **get**
Gets a specific ontology for a given Ontology API name or RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |

### Return type
**OntologyV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"


try:
    api_response = client.ontologies.Ontology.get(ontology)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Ontology.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_full_metadata**
Get the full Ontology metadata. This includes the objects, links, actions, queries, and interfaces.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load metadata from. If not specified, the default branch will be used.  | [optional] |

### Return type
**OntologyFullMetadata**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[FoundryBranch] | The Foundry branch to load metadata from. If not specified, the default branch will be used.
branch = None


try:
    api_response = client.ontologies.Ontology.get_full_metadata(ontology, branch=branch)
    print("The get_full_metadata response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Ontology.get_full_metadata: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyFullMetadata  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the Ontologies visible to the current user.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |

### Return type
**ListOntologiesV2Response**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")


try:
    api_response = client.ontologies.Ontology.list()
    print("The list response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Ontology.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOntologiesV2Response  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **load_metadata**
Load Ontology metadata for the requested object, link, action, query, and interface types.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**action_types** | List[ActionTypeApiName] |  |  |
**interface_types** | List[InterfaceTypeApiName] |  |  |
**link_types** | List[LinkTypeApiName] |  |  |
**object_types** | List[ObjectTypeApiName] |  |  |
**query_types** | List[VersionedQueryTypeApiName] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load metadata from. If not specified, the default branch will be used.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**OntologyFullMetadata**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# List[ActionTypeApiName]
action_types = None
# List[InterfaceTypeApiName]
interface_types = None
# List[LinkTypeApiName]
link_types = None
# List[ObjectTypeApiName]
object_types = None
# List[VersionedQueryTypeApiName]
query_types = None
# Optional[FoundryBranch] | The Foundry branch to load metadata from. If not specified, the default branch will be used.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.Ontology.load_metadata(
        ontology,
        action_types=action_types,
        interface_types=interface_types,
        link_types=link_types,
        object_types=object_types,
        query_types=query_types,
        branch=branch,
        preview=preview,
    )
    print("The load_metadata response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Ontology.load_metadata: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyFullMetadata  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

