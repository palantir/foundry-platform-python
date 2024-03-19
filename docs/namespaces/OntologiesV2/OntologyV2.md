# OntologyV2

Method | HTTP request |
------------- | ------------- |
[**iterator**](#iterator) | **GET** /v2/ontologies |
[**get**](#get) | **GET** /v2/ontologies/{ontology} |
[**get_ontology_full_metadata**](#get_ontology_full_metadata) | **GET** /v2/ontologies/{ontology}/fullMetadata |

# **iterator**
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
    api_response = foundry_client.ontologies_v2.OntologyV2.iterator()
    print("The OntologyV2.iterator response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyV2.iterator: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOntologiesV2Response  | ListOntologiesV2Response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Gets a specific ontology with the given Ontology RID.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |

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

ontology = "palantir"  # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.


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
**200** | OntologyV2  | Metadata about an Ontology. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_ontology_full_metadata**
Get the full Ontology metadata. This includes the objects, links, actions, and queries.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |

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

ontology = "palantir"  # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.


try:
    api_response = foundry_client.ontologies_v2.OntologyV2.get_ontology_full_metadata(
        ontology,
    )
    print("The OntologyV2.get_ontology_full_metadata response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyV2.get_ontology_full_metadata: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyFullMetadata  | OntologyFullMetadata | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

