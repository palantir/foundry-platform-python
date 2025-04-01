# OntologyObject

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**aggregate**](#aggregate) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/aggregate | Stable |
[**count**](#count) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/count | Private Beta |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey} | Stable |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/objects/{objectType} | Stable |
[**search**](#search) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/search | Stable |

# **aggregate**
Perform functions on object fields in the specified ontology and object type.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The type of the object to aggregate on. |  |
**aggregation** | List[AggregationV2] |  |  |
**group_by** | List[AggregationGroupByV2] |  |  |
**accuracy** | Optional[AggregationAccuracyRequest] |  | [optional] |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**where** | Optional[SearchJsonQueryV2] |  | [optional] |

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
# ObjectTypeApiName | The type of the object to aggregate on.
object_type = "employee"
# List[AggregationV2]
aggregation = [
    {"type": "min", "field": "properties.tenure", "name": "min_tenure"},
    {"type": "avg", "field": "properties.tenure", "name": "avg_tenure"},
]
# List[AggregationGroupByV2]
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
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[SearchJsonQueryV2]
where = {"type": "eq", "field": "name", "value": "john"}


try:
    api_response = foundry_client.ontologies.OntologyObject.aggregate(
        ontology,
        object_type,
        aggregation=aggregation,
        group_by=group_by,
        accuracy=accuracy,
        artifact_repository=artifact_repository,
        package_name=package_name,
        where=where,
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
**200** | AggregateObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **count**
Returns a count of the objects of the given object type.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |

### Return type
**CountObjectsResponseV2**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None


try:
    api_response = foundry_client.ontologies.OntologyObject.count(
        ontology, object_type, artifact_repository=artifact_repository, package_name=package_name
    )
    print("The count response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObject.count: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CountObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Gets a specific object with the given primary key.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the requested object. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**select** | Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |

### Return type
**OntologyObjectV2**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the requested object. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
primary_key = 50030
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
select = None


try:
    api_response = foundry_client.ontologies.OntologyObject.get(
        ontology,
        object_type,
        primary_key,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        package_name=package_name,
        select=select,
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
**200** | OntologyObjectV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the objects for the given Ontology and object type.

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
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**order_by** | Optional[OrderBy] |  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**select** | Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |

### Return type
**ListObjectsResponseV2**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[OrderBy]
order_by = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
select = None


try:
    for ontology_object in client.ontologies.OntologyObject.list(
        ontology,
        object_type,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=order_by,
        package_name=package_name,
        page_size=page_size,
        page_token=page_token,
        select=select,
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
**200** | ListObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**
Search for objects in the specified ontology and object type. The request body is used
to filter objects based on the specified query. The supported queries are:

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
| containsAllTermsInOrder                 | The provided property contains the provided term as a substring.                                                  | string                          |
| containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
| containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |

Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
Partial terms are not matched by terms filters except where explicitly noted.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**select** | List[PropertyApiName] | The API names of the object type properties to include in the response.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**order_by** | Optional[SearchOrderByV2] |  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**where** | Optional[SearchJsonQueryV2] |  | [optional] |

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
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# List[PropertyApiName] | The API names of the object type properties to include in the response.
select = None
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[bool] | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[SearchOrderByV2]
order_by = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[PageSize]
page_size = None
# Optional[PageToken]
page_token = None
# Optional[SearchJsonQueryV2]
where = {"type": "eq", "field": "age", "value": 21}


try:
    api_response = foundry_client.ontologies.OntologyObject.search(
        ontology,
        object_type,
        select=select,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=order_by,
        package_name=package_name,
        page_size=page_size,
        page_token=page_token,
        where=where,
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
**200** | SearchObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

