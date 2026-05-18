# OntologyScenario

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create_scenario**](#create_scenario) | **POST** /v2/ontologies/{ontology}/scenarios/create | Private Beta |

# **create_scenario**
Creates an ontology scenario.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**base** | Optional[OntologyBase] |  | [optional] |

### Return type
**CreateOntologyScenarioResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[OntologyBase]
base = {"type": "branch", "branch": "my-branch"}


try:
    api_response = client.ontologies.OntologyScenario.create_scenario(ontology, base=base)
    print("The create_scenario response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyScenario.create_scenario: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CreateOntologyScenarioResponse  | Successfully created a scenario. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

