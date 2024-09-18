# OntologyObject

Method | HTTP request |
------------- | ------------- |
[**aggregate**](#aggregate) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate |
[**get**](#get) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey} |
[**get_linked_object**](#get_linked_object) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} |
[**list**](#list) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType} |
[**list_linked_objects**](#list_linked_objects) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType} |
[**page**](#page) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType} |
[**page_linked_objects**](#page_linked_objects) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType} |
[**search**](#search) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/search |

# **aggregate**
Perform functions on object fields in the specified ontology and object type.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**object_type** | ObjectTypeApiName | objectType |  |
**aggregation** | List[AggregationDict] |  |  |
**group_by** | List[AggregationGroupByDict] |  |  |
**query** | Optional[SearchJsonQueryDict] |  | [optional] |

### Return type
**AggregateObjectsResponse**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | objectType
object_type = "employee"
# List[AggregationDict] |
aggregation = [
    {"type": "min", "field": "properties.tenure", "name": "min_tenure"},
    {"type": "avg", "field": "properties.tenure", "name": "avg_tenure"},
]
# List[AggregationGroupByDict] |
group_by = [
    {
        "field": "properties.startDate",
        "type": "range",
        "ranges": [{"gte": "2020-01-01", "lt": "2020-06-01"}],
    },
    {"field": "properties.city", "type": "exact"},
]
# Optional[SearchJsonQueryDict] |
query = {"not": {"field": "properties.name", "eq": "john"}}


try:
    api_response = foundry_client.ontologies.OntologyObject.aggregate(
        ontology_rid,
        object_type,
        aggregation=aggregation,
        group_by=group_by,
        query=query,
    )
    print("The aggregate response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.aggregate: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AggregateObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **get**
Gets a specific object with the given primary key.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**properties** | Optional[List[SelectedPropertyApiName]] | properties | [optional] |

### Return type
**OntologyObject**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | objectType
object_type = "employee"
# PropertyValueEscapedString | primaryKey
primary_key = 50030
# Optional[List[SelectedPropertyApiName]] | properties
properties = None


try:
    api_response = foundry_client.ontologies.OntologyObject.get(
        ontology_rid,
        object_type,
        primary_key,
        properties=properties,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyObject  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **get_linked_object**
Get a specific linked object that originates from another object. If there is no link between the two objects,
LinkedObjectNotFound is thrown.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**link_type** | LinkTypeApiName | linkType |  |
**linked_object_primary_key** | PropertyValueEscapedString | linkedObjectPrimaryKey |  |
**properties** | Optional[List[SelectedPropertyApiName]] | properties | [optional] |

### Return type
**OntologyObject**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | objectType
object_type = "employee"
# PropertyValueEscapedString | primaryKey
primary_key = 50030
# LinkTypeApiName | linkType
link_type = "directReport"
# PropertyValueEscapedString | linkedObjectPrimaryKey
linked_object_primary_key = 80060
# Optional[List[SelectedPropertyApiName]] | properties
properties = None


try:
    api_response = foundry_client.ontologies.OntologyObject.get_linked_object(
        ontology_rid,
        object_type,
        primary_key,
        link_type,
        linked_object_primary_key,
        properties=properties,
    )
    print("The get_linked_object response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.get_linked_object: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyObject  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **list**
Lists the objects for the given Ontology and object type.

This endpoint supports filtering objects.
See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**object_type** | ObjectTypeApiName | objectType |  |
**order_by** | Optional[OrderBy] | orderBy | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**properties** | Optional[List[SelectedPropertyApiName]] | properties | [optional] |

### Return type
**ResourceIterator[OntologyObject]**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | objectType
object_type = "employee"
# Optional[OrderBy] | orderBy
order_by = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[List[SelectedPropertyApiName]] | properties
properties = None


try:
    for ontology_object in foundry_client.ontologies.OntologyObject.list(
        ontology_rid,
        object_type,
        order_by=order_by,
        page_size=page_size,
        properties=properties,
    ):
        pprint(ontology_object)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **list_linked_objects**
Lists the linked objects for a specific object and the given link type.

This endpoint supports filtering objects.
See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**link_type** | LinkTypeApiName | linkType |  |
**order_by** | Optional[OrderBy] | orderBy | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**properties** | Optional[List[SelectedPropertyApiName]] | properties | [optional] |

### Return type
**ResourceIterator[OntologyObject]**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | objectType
object_type = "employee"
# PropertyValueEscapedString | primaryKey
primary_key = 50030
# LinkTypeApiName | linkType
link_type = "directReport"
# Optional[OrderBy] | orderBy
order_by = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[List[SelectedPropertyApiName]] | properties
properties = None


try:
    for ontology_object in foundry_client.ontologies.OntologyObject.list_linked_objects(
        ontology_rid,
        object_type,
        primary_key,
        link_type,
        order_by=order_by,
        page_size=page_size,
        properties=properties,
    ):
        pprint(ontology_object)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.list_linked_objects: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListLinkedObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **page**
Lists the objects for the given Ontology and object type.

This endpoint supports filtering objects.
See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**object_type** | ObjectTypeApiName | objectType |  |
**order_by** | Optional[OrderBy] | orderBy | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**properties** | Optional[List[SelectedPropertyApiName]] | properties | [optional] |

### Return type
**ListObjectsResponse**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | objectType
object_type = "employee"
# Optional[OrderBy] | orderBy
order_by = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[List[SelectedPropertyApiName]] | properties
properties = None


try:
    api_response = foundry_client.ontologies.OntologyObject.page(
        ontology_rid,
        object_type,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        properties=properties,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **page_linked_objects**
Lists the linked objects for a specific object and the given link type.

This endpoint supports filtering objects.
See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**link_type** | LinkTypeApiName | linkType |  |
**order_by** | Optional[OrderBy] | orderBy | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**properties** | Optional[List[SelectedPropertyApiName]] | properties | [optional] |

### Return type
**ListLinkedObjectsResponse**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | objectType
object_type = "employee"
# PropertyValueEscapedString | primaryKey
primary_key = 50030
# LinkTypeApiName | linkType
link_type = "directReport"
# Optional[OrderBy] | orderBy
order_by = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[List[SelectedPropertyApiName]] | properties
properties = None


try:
    api_response = foundry_client.ontologies.OntologyObject.page_linked_objects(
        ontology_rid,
        object_type,
        primary_key,
        link_type,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        properties=properties,
    )
    print("The page_linked_objects response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.page_linked_objects: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListLinkedObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **search**
Search for objects in the specified ontology and object type. The request body is used
to filter objects based on the specified query. The supported queries are:

| Query type            | Description                                                                       | Supported Types                 |
|----------|-----------------------------------------------------------------------------------|---------------------------------|
| lt       | The provided property is less than the provided value.                            | number, string, date, timestamp |
| gt       | The provided property is greater than the provided value.                         | number, string, date, timestamp |
| lte      | The provided property is less than or equal to the provided value.                | number, string, date, timestamp |
| gte      | The provided property is greater than or equal to the provided value.             | number, string, date, timestamp |
| eq       | The provided property is exactly equal to the provided value.                     | number, string, date, timestamp |
| isNull   | The provided property is (or is not) null.                                        | all                             |
| contains | The provided property contains the provided value.                                | array                           |
| not      | The sub-query does not match.                                                     | N/A (applied on a query)        |
| and      | All the sub-queries match.                                                        | N/A (applied on queries)        |
| or       | At least one of the sub-queries match.                                            | N/A (applied on queries)        |
| prefix   | The provided property starts with the provided value.                             | string                          |
| phrase   | The provided property contains the provided value as a substring.                 | string                          |
| anyTerm  | The provided property contains at least one of the terms separated by whitespace. | string                          |
| allTerms | The provided property contains all the terms separated by whitespace.             | string                          |                                                                            |

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**object_type** | ObjectTypeApiName | objectType |  |
**fields** | List[PropertyApiName] | The API names of the object type properties to include in the response.  |  |
**query** | SearchJsonQueryDict |  |  |
**order_by** | Optional[SearchOrderByDict] |  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**SearchObjectsResponse**

### Example

```python
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | objectType
object_type = "employee"
# List[PropertyApiName] | The API names of the object type properties to include in the response.
fields = None
# SearchJsonQueryDict |
query = {"not": {"field": "properties.age", "eq": 21}}
# Optional[SearchOrderByDict] |
order_by = None
# Optional[PageSize] |
page_size = None
# Optional[PageToken] |
page_token = None


try:
    api_response = foundry_client.ontologies.OntologyObject.search(
        ontology_rid,
        object_type,
        fields=fields,
        query=query,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
    )
    print("The search response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

