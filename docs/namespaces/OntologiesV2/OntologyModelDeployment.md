# OntologyModelDeployment

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/models/deployments/{deployment} |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/models/deployments |

# **get**
Fetches information about a model deployment within a given Ontology.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**deployment** | DeploymentApiName | The API name of the deployment you want to fetch information about.  |  |

### Return type
**DeploymentMetadata**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

ontology = "palantir"  # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
deployment = "nextTokenPredictor"  # DeploymentApiName | The API name of the deployment you want to fetch information about.


try:
    api_response = foundry_client.ontologiesv2.OntologyModelDeployment.get(
        ontology,
        deployment,
    )
    print("The OntologyModelDeployment.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyModelDeployment.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | DeploymentMetadata  | Metadata related to a model deployment.  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**
Fetches a list of the available model deployments within a given Ontology.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |

### Return type
**ListDeploymentsResponse**

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
    api_response = foundry_client.ontologiesv2.OntologyModelDeployment.list(
        ontology,
    )
    print("The OntologyModelDeployment.list response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyModelDeployment.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListDeploymentsResponse  | ListDeploymentsResponse | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

