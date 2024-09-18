# OntologyV2

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/ontologies/{ontology} |

# **get**
Gets a specific ontology with the given Ontology RID.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |

### Return type
**OntologyV2**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"


try:
    api_response = foundry_client.ontologies.Ontology.get(
        ontology,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Ontology.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Get the full Ontology metadata. This includes the objects, links, actions, queries, and interfaces.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |

### Return type
**OntologyFullMetadata**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"


try:
    api_response = foundry_client.ontologies.Ontology.get_full_metadata(
        ontology,
    )
    print("The get_full_metadata response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Ontology.get_full_metadata: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyFullMetadata  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

