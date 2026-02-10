# OntologyObject

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**aggregate**](#aggregate) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate | Stable |
[**get**](#get) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey} | Stable |
[**get_linked_object**](#get_linked_object) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} | Stable |
[**list**](#list) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType} | Stable |
[**list_linked_objects**](#list_linked_objects) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType} | Stable |
[**search**](#search) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/search | Stable |

# **aggregate**
Perform functions on object fields in the specified ontology and object type.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the objects. |  |
**object_type** | ObjectTypeApiName | The type of the object to aggregate on. |  |
**aggregation** | List[Aggregation] |  |  |
**group_by** | List[AggregationGroupBy] |  |  |
**query** | Optional[SearchJsonQuery] |  | [optional] |

### Return type
**AggregateObjectsResponse**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the objects.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The type of the object to aggregate on.
object_type = "employee"
# List[Aggregation]
aggregation = [
    {"type": "min", "field": "properties.tenure", "name": "min_tenure"},
    {"type": "avg", "field": "properties.tenure", "name": "avg_tenure"},
]
# List[AggregationGroupBy]
group_by = [
    {
        "field": "properties.startDate",
        "type": "range",
        "ranges": [{"gte": "2020-01-01", "lt": "2020-06-01"}],
    },
    {"field": "properties.city", "type": "exact"},
]
# Optional[SearchJsonQuery]
query = {"not": {"field": "properties.name", "eq": "john"}}


try:
    api_response = client.ontologies.OntologyObject.aggregate(
        ontology_rid, object_type, aggregation=aggregation, group_by=group_by, query=query
    )
    print("The aggregate response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the object. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the requested object. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.  |  |
**properties** | Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |

### Return type
**OntologyObject**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the object. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the requested object. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
primary_key = 50030
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
properties = None


try:
    api_response = client.ontologies.OntologyObject.get(
        ontology_rid, object_type, primary_key, properties=properties
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the object. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object from which the links originate. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object from which the link originates. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.  |  |
**link_type** | LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.  |  |
**linked_object_primary_key** | PropertyValueEscapedString | The primary key of the requested linked object. To look up the expected primary key for your object type, use the `Get object type` endpoint (passing the linked object type) or the **Ontology Manager**.  |  |
**properties** | Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |

### Return type
**OntologyObject**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the object. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The API name of the object from which the links originate. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object from which the link originates. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
primary_key = 50030
# LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
link_type = "directReport"
# PropertyValueEscapedString | The primary key of the requested linked object. To look up the expected primary key for your object type, use the `Get object type` endpoint (passing the linked object type) or the **Ontology Manager**.
linked_object_primary_key = 80060
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
properties = None


try:
    api_response = client.ontologies.OntologyObject.get_linked_object(
        ontology_rid,
        object_type,
        primary_key,
        link_type,
        linked_object_primary_key,
        properties=properties,
    )
    print("The get_linked_object response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
See the [Filtering Objects documentation](https://palantir.com/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the objects. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**order_by** | Optional[OrderBy] |  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**properties** | Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |

### Return type
**ListObjectsResponse**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the objects. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# Optional[OrderBy]
order_by = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
properties = None


try:
    for ontology_object in client.ontologies.OntologyObject.list(
        ontology_rid,
        object_type,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        properties=properties,
    ):
        pprint(ontology_object)
except foundry_sdk.PalantirRPCException as e:
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
See the [Filtering Objects documentation](https://palantir.com/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the objects. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object from which the links originate. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.  |  |
**link_type** | LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.  |  |
**order_by** | Optional[OrderBy] |  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**properties** | Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |

### Return type
**ListLinkedObjectsResponse**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the objects. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The API name of the object from which the links originate. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
primary_key = 50030
# LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
link_type = "directReport"
# Optional[OrderBy]
order_by = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
properties = None


try:
    for ontology_object in client.ontologies.OntologyObject.list_linked_objects(
        ontology_rid,
        object_type,
        primary_key,
        link_type,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        properties=properties,
    ):
        pprint(ontology_object)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.list_linked_objects: %s\n" % e)

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
| prefix   | The provided property starts with the provided term.                              | string                          |
| phrase   | The provided property contains the provided term as a substring.                  | string                          |
| anyTerm  | The provided property contains at least one of the terms separated by whitespace. | string                          |
| allTerms | The provided property contains all the terms separated by whitespace.             | string                          |

Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
Partial terms are not matched by terms filters except where explicitly noted.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the objects. |  |
**object_type** | ObjectTypeApiName | The type of the requested objects. |  |
**fields** | List[PropertyApiName] | The API names of the object type properties to include in the response.  |  |
**query** | SearchJsonQuery |  |  |
**order_by** | Optional[SearchOrderBy] |  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**SearchObjectsResponse**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyRid | The unique Resource Identifier (RID) of the Ontology that contains the objects.
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The type of the requested objects.
object_type = "employee"
# List[PropertyApiName] | The API names of the object type properties to include in the response.
fields = None
# SearchJsonQuery
query = {"not": {"field": "properties.age", "eq": 21}}
# Optional[SearchOrderBy]
order_by = None
# Optional[PageSize]
page_size = None
# Optional[PageToken]
page_token = None


try:
    api_response = client.ontologies.OntologyObject.search(
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
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

