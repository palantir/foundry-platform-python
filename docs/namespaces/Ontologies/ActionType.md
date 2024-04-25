# ActionType

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName} |
[**list**](#list) | **GET** /v1/ontologies/{ontologyRid}/actionTypes |
[**page**](#page) | **GET** /v1/ontologies/{ontologyRid}/actionTypes |

# **get**
Gets a specific action type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**action_type_api_name** | ActionTypeApiName | actionTypeApiName |  |

### Return type
**ActionType**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"

# ActionTypeApiName | actionTypeApiName
action_type_api_name = "promote-employee"


try:
    api_response = foundry_client.ontologies.ActionType.get(
        ontology_rid,
        action_type_api_name,
    )
    print("The ActionType.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ActionType.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ActionType  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list**
Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |

### Return type
**ResourceIterator[ActionType]**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"

# Optional[PageSize] | pageSize
page_size = None



try:
    for action_type in foundry_client.ontologies.ActionType.list(ontology_rid, page_size=page_size)
:
        pprint(action_type)
except PalantirRPCException as e:
    print("HTTP error when calling ActionType.list: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListActionTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **page**
Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListActionTypesResponse**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None



try:
    api_response = foundry_client.ontologies.ActionType.page(ontology_rid, page_size=page_sizepage_token=page_token)
    print("The ActionType.page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ActionType.page: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListActionTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

