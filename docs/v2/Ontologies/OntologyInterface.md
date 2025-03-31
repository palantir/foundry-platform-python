# OntologyInterface

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**aggregate**](#aggregate) | **POST** /v2/ontologies/{ontology}/interfaces/{interfaceType}/aggregate | Private Beta |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/interfaceTypes/{interfaceType} | Public Beta |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/interfaceTypes | Public Beta |
[**page**](#page) | **GET** /v2/ontologies/{ontology}/interfaceTypes | Public Beta |
[**search**](#search) | **POST** /v2/ontologies/{ontology}/interfaces/{interfaceType}/search | Private Beta |

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
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.  |  |
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

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
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
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**InterfaceType**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
interface_type = "Employee"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = foundry_client.ontologies.OntologyInterface.get(
        ontology, interface_type, preview=preview
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
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
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

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    for ontology_interface in client.ontologies.OntologyInterface.list(
        ontology, page_size=page_size, page_token=page_token, preview=preview
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
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
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

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = foundry_client.ontologies.OntologyInterface.page(
        ontology, page_size=page_size, page_token=page_token, preview=preview
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

# **search**
:::callout{theme=warning title=Warning}
  This endpoint will be removed once TS OSDK is updated to use `objectSets/loadObjects` with interface object
  sets.
:::
:::callout{theme=warning title=Warning}
  This endpoint is in preview and may be modified or removed at any time.
  To use this endpoint, add `preview=true` to the request query parameters.
:::

Search for objects in the specified ontology and interface type. Any properties specified in the "where" or 
"orderBy" parameters must be shared property type API names defined on the interface. The following search 
queries are supported:

| Query type                              | Description                                                                                                       | Supported Types                 |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------|
| lt                                      | The provided property is less than the provided value.                                                            | number, string, date, timestamp |
| gt                                      | The provided property is greater than the provided value.                                                         | number, string, date, timestamp |
| lte                                     | The provided property is less than or equal to the provided value.                                                | number, string, date, timestamp |
| gte                                     | The provided property is greater than or equal to the provided value.                                             | number, string, date, timestamp |
| eq                                      | The provided property is exactly equal to the provided value.                                                     | number, string, date, timestamp |
| isNull                                  | The provided property is (or is not) null.                                                                        | all                             |
| contains                                | The provided property contains the provided value.                                                                | array                           |
| not                                     | The sub-query does not match.                                                                                     | N/A (applied on a query)        |
| and                                     | All the sub-queries match.                                                                                        | N/A (applied on queries)        |
| or                                      | At least one of the sub-queries match.                                                                            | N/A (applied on queries)        |
| startsWith                              | The provided property starts with the provided term.                                                              | string                          |
| containsAllTermsInOrderPrefixLastTerm   | The provided property contains all the terms provided in order. The last term can be a partial prefix match.      | string                          |
| containsAllTermsInOrder                 | The provided property contains the provided terms as a substring.                                                 | string                          |
| containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
| containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |

Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
Partial terms are not matched by terms filters except where explicitly noted.

Attempting to use an unsupported query will result in a validation error. Third-party applications using this 
endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.  |  |
**augmented_properties** | Dict[ObjectTypeApiName, List[PropertyApiName]] | A map from object type API name to a list of property type API names. For each returned object, if the  object’s object type is a key in the map, then we augment the response for that object type with the list  of properties specified in the value.  |  |
**augmented_shared_property_types** | Dict[InterfaceTypeApiName, List[SharedPropertyTypeApiName]] | A map from interface type API name to a list of shared property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.  |  |
**other_interface_types** | List[InterfaceTypeApiName] | A list of interface type API names. Object types must implement all the mentioned interfaces in order to be  included in the response.  |  |
**selected_object_types** | List[ObjectTypeApiName] | A list of object type API names that should be included in the response. If non-empty, object types that are not mentioned will not be included in the response even if they implement the specified interface. Omit the  parameter to include all object types.  |  |
**selected_shared_property_types** | List[SharedPropertyTypeApiName] | A list of shared property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.  |  |
**order_by** | Optional[Union[SearchOrderByV2, SearchOrderByV2Dict]] |  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**where** | Optional[Union[SearchJsonQueryV2, SearchJsonQueryV2Dict]] |  | [optional] |

### Return type
**SearchObjectsResponseV2**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
interface_type = "Employee"
# Dict[ObjectTypeApiName, List[PropertyApiName]] | A map from object type API name to a list of property type API names. For each returned object, if the  object’s object type is a key in the map, then we augment the response for that object type with the list  of properties specified in the value.
augmented_properties = None
# Dict[InterfaceTypeApiName, List[SharedPropertyTypeApiName]] | A map from interface type API name to a list of shared property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.
augmented_shared_property_types = None
# List[InterfaceTypeApiName] | A list of interface type API names. Object types must implement all the mentioned interfaces in order to be  included in the response.
other_interface_types = None
# List[ObjectTypeApiName] | A list of object type API names that should be included in the response. If non-empty, object types that are not mentioned will not be included in the response even if they implement the specified interface. Omit the  parameter to include all object types.
selected_object_types = None
# List[SharedPropertyTypeApiName] | A list of shared property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.
selected_shared_property_types = None
# Optional[Union[SearchOrderByV2, SearchOrderByV2Dict]]
order_by = None
# Optional[PageSize]
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[Union[SearchJsonQueryV2, SearchJsonQueryV2Dict]]
where = None


try:
    api_response = foundry_client.ontologies.OntologyInterface.search(
        ontology,
        interface_type,
        augmented_properties=augmented_properties,
        augmented_shared_property_types=augmented_shared_property_types,
        other_interface_types=other_interface_types,
        selected_object_types=selected_object_types,
        selected_shared_property_types=selected_shared_property_types,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        where=where,
    )
    print("The search response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

