# OntologyInterface

Method | HTTP request |
------------- | ------------- |
[**aggregate**](#aggregate) | **POST** /v2/ontologies/{ontology}/interfaces/{interfaceType}/aggregate |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/interfaceTypes/{interfaceType} |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/interfaceTypes |
[**page**](#page) | **GET** /v2/ontologies/{ontology}/interfaceTypes |

# **aggregate**
:::callout{theme=warning title=Warning}
  This endpoint is in preview and may be modified or removed at any time.
  To use this endpoint, add `preview=true` to the request query parameters.
:::

Perform functions on object fields in the specified ontology and of the specified interface type. Any 
properties specified in the query must be shared property type API names defined on the interface.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**interface_type** | InterfaceTypeApiName | interfaceType |  |
**aggregate_objects_request_v2** | Union[AggregateObjectsRequestV2, AggregateObjectsRequestV2Dict] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**AggregateObjectsResponseV2**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"

# InterfaceTypeApiName | interfaceType
interface_type = "Employee"

# Union[AggregateObjectsRequestV2, AggregateObjectsRequestV2Dict] | Body of the request
aggregate_objects_request_v2 = {
    "aggregation": [
        {"type": "min", "field": "properties.tenure", "name": "min_tenure"},
        {"type": "avg", "field": "properties.tenure", "name": "avg_tenure"},
    ],
    "query": {"not": {"field": "name", "eq": "john"}},
    "groupBy": [
        {
            "field": "startDate",
            "type": "range",
            "ranges": [{"startValue": "2020-01-01", "endValue": "2020-06-01"}],
        },
        {"field": "city", "type": "exact"},
    ],
}

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.ontologies.OntologyInterface.aggregate(
        ontology,
        interface_type,
        aggregate_objects_request_v2,
        preview=preview,
    )
    print("The aggregate response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.aggregate: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AggregateObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **get**
:::callout{theme=warning title=Warning}
  This endpoint is in preview and may be modified or removed at any time.
  To use this endpoint, add `preview=true` to the request query parameters.
:::

Gets a specific object type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**interface_type** | InterfaceTypeApiName | interfaceType |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**InterfaceType**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"

# InterfaceTypeApiName | interfaceType
interface_type = "Employee"

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.ontologies.OntologyInterface.get(
        ontology,
        interface_type,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.get: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | InterfaceType  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **list**
:::callout{theme=warning title=Warning}
  This endpoint is in preview and may be modified or removed at any time.
  To use this endpoint, add `preview=true` to the request query parameters.
:::

Lists the interface types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.        

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[InterfaceType]**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"

# Optional[PageSize] | pageSize
page_size = None

# Optional[PreviewMode] | preview
preview = None


try:
    for ontology_interface in foundry_client.ontologies.OntologyInterface.list(
        ontology,
        page_size=page_size,
        preview=preview,
    ):
        pprint(ontology_interface)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.list: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListInterfaceTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **page**
:::callout{theme=warning title=Warning}
  This endpoint is in preview and may be modified or removed at any time.
  To use this endpoint, add `preview=true` to the request query parameters.
:::

Lists the interface types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.        

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListInterfaceTypesResponse**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"

# Optional[PageSize] | pageSize
page_size = None

# Optional[PageToken] | pageToken
page_token = None

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.ontologies.OntologyInterface.page(
        ontology,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.page: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListInterfaceTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

