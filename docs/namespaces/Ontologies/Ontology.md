# Ontology

Method | HTTP request |
------------- | ------------- |
[**iterator**](#iterator) | **GET** /v1/ontologies |
[**get**](#get) | **GET** /v1/ontologies/{ontologyRid} |

# **iterator**
Lists the Ontologies visible to the current user.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |

### Return type
**ListOntologiesResponse**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)


try:
    api_response = foundry_client.ontologies.Ontology.iterator()
    print("The Ontology.iterator response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Ontology.iterator: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOntologiesResponse  | ListOntologiesResponse | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
Gets a specific ontology with the given Ontology RID.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |

### Return type
**Ontology**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"  # OntologyRid | The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.


try:
    api_response = foundry_client.ontologies.Ontology.get(
        ontology_rid,
    )
    print("The Ontology.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Ontology.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Ontology  | Metadata about an Ontology. | application/json |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

