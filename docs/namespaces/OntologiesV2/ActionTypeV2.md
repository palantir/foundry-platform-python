# ActionTypeV2

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/actionTypes |
[**page**](#page) | **GET** /v2/ontologies/{ontology}/actionTypes |

# **get**
Gets a specific action type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**action_type** | ActionTypeApiName | actionType |  |

### Return type
**ActionTypeV2**

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

# ActionTypeApiName | actionType
action_type = "promote-employee"


try:
    api_response = foundry_client.ontologies_v2.ActionTypeV2.get(
        ontology,
        action_type,
    )
    print("The ActionTypeV2.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ActionTypeV2.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ActionTypeV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**
Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |

### Return type
**ResourceIterator[ActionTypeV2]**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | ontology
ontology = "palantir"

# Optional[PageSize] | pageSize
page_size = None



try:
    for action_type_v2 in foundry_client.ontologies_v2.ActionTypeV2.list(ontology, page_size=page_size)
:
        pprint(action_type_v2)
except PalantirRPCException as e:
    print("HTTP error when calling ActionTypeV2.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListActionTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **page**
Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListActionTypesResponseV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | ontology
ontology = "palantir"

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None



try:
    api_response = foundry_client.ontologies_v2.ActionTypeV2.page(ontology, page_size=page_sizepage_token=page_token)
    print("The ActionTypeV2.page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ActionTypeV2.page: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListActionTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

