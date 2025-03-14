# OntologyInterface

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**aggregate**](#aggregate) | **POST** /v2/ontologies/{ontology}/interfaces/{interfaceType}/aggregate | Private Beta |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/interfaceTypes/{interfaceType} | Public Beta |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/interfaceTypes | Public Beta |
[**page**](#page) | **GET** /v2/ontologies/{ontology}/interfaceTypes | Public Beta |

# **aggregate**
:::callout{theme=warning title=Warning}
This endpoint will be removed once TS OSDK is updated to use `objectSets/aggregate` with interface object
sets.
:::
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
**ontology** | str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**interface_type** | str | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.  |  |
**aggregation** | List[Union[AggregationV2, AggregationV2Dict]] |  |  |
**group_by** | List[Union[AggregationGroupByV2, AggregationGroupByV2Dict]] |  |  |
**accuracy** | Optional[AggregationAccuracyRequest] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**where** | Optional[Union[SearchJsonQueryV2, SearchJsonQueryV2Dict]] |  | [optional] |

### Return type
**AggregateObjectsResponseV2**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# str | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
interface_type = "Employee"
# List[Union[AggregationV2, AggregationV2Dict]]
aggregation = [
    {"type": "min", "field": "properties.tenure", "name": "min_tenure"},
    {"type": "avg", "field": "properties.tenure", "name": "avg_tenure"},
]
# List[Union[AggregationGroupByV2, AggregationGroupByV2Dict]]
group_by = [
    {
        "field": "startDate",
        "type": "range",
        "ranges": [{"startValue": "2020-01-01", "endValue": "2020-06-01"}],
    },
    {"field": "city", "type": "exact"},
]
# Optional[AggregationAccuracyRequest]
accuracy = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[Union[SearchJsonQueryV2, SearchJsonQueryV2Dict]]
where = {"type": "eq", "field": "name", "value": "john"}


try:
    api_response = foundry_client.ontologies.OntologyInterface.aggregate(
        ontology,
        interface_type,
        aggregation=aggregation,
        group_by=group_by,
        accuracy=accuracy,
        preview=preview,
        where=where,
    )
    print("The aggregate response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.aggregate: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AggregateObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
:::callout{theme=warning title=Warning}
  This endpoint is in preview and may be modified or removed at any time.
  To use this endpoint, add `preview=true` to the request query parameters.
:::

Gets a specific interface type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**interface_type** | str | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**InterfaceType**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# str | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
interface_type = "Employee"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = foundry_client.ontologies.OntologyInterface.get(
        ontology,
        interface_type,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | InterfaceType  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

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
**ontology** | str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListInterfaceTypesResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    for ontology_interface in foundry_client.ontologies.OntologyInterface.list(
        ontology,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(ontology_interface)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListInterfaceTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

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
**ontology** | str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListInterfaceTypesResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
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
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListInterfaceTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

