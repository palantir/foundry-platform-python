# OntologyV2

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/ontologies/{ontology} |
[**get_full_metadata**](#get_full_metadata) | **GET** /v2/ontologies/{ontology}/fullMetadata |
[**list**](#list) | **GET** /v2/ontologies |

# **get**
Gets a specific ontology with the given Ontology RID.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |

### Return type
**OntologyV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"


try:
    api_response = foundry_client.ontologies_v2.OntologyV2.get(
        ontology,
    )
    print("The OntologyV2.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyV2.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_full_metadata**
Get the full Ontology metadata. This includes the objects, links, actions, queries, and interfaces.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |

### Return type
**OntologyFullMetadata**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"


try:
    api_response = foundry_client.ontologies_v2.OntologyV2.get_full_metadata(
        ontology,
    )
    print("The OntologyV2.get_full_metadata response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyV2.get_full_metadata: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyFullMetadata  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**
Lists the Ontologies visible to the current user.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |

### Return type
**ListOntologiesV2Response**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)


try:
    api_response = foundry_client.ontologies_v2.OntologyV2.list()
    print("The OntologyV2.list response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyV2.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOntologiesV2Response  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

