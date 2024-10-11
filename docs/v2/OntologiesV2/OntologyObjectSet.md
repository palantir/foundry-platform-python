# OntologyObjectSet

Method | HTTP request |
------------- | ------------- |
[**aggregate**](#aggregate) | **POST** /v2/ontologies/{ontology}/objectSets/aggregate |
[**load**](#load) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjects |

# **aggregate**
Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.        

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**aggregation** | List[AggregationV2Dict] |  |  |
**group_by** | List[AggregationGroupByV2Dict] |  |  |
**object_set** | ObjectSetDict |  |  |
**accuracy** | Optional[AggregationAccuracyRequest] |  | [optional] |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

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

# OntologyIdentifier | ontology
ontology = "palantir"
# List[AggregationV2Dict] |
aggregation = None
# List[AggregationGroupByV2Dict] |
group_by = None
# ObjectSetDict |
object_set = None
# Optional[AggregationAccuracyRequest] |
accuracy = None
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.OntologyObjectSet.aggregate(
        ontology,
        aggregation=aggregation,
        group_by=group_by,
        object_set=object_set,
        accuracy=accuracy,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The aggregate response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.aggregate: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AggregateObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Creates a temporary `ObjectSet` from the given definition.        

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_set** | ObjectSetDict |  |  |

### Return type
**CreateTemporaryObjectSetResponseV2**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"
# ObjectSetDict |
object_set = {"type": "base", "objectType": "Employee"}


try:
    api_response = foundry_client.ontologies.OntologyObjectSet.create_temporary(
        ontology,
        object_set=object_set,
    )
    print("The create_temporary response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.create_temporary: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CreateTemporaryObjectSetResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Gets the definition of the `ObjectSet` with the given RID.        

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_set_rid** | ObjectSetRid | objectSetRid |  |

### Return type
**ObjectSet**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"
# ObjectSetRid | objectSetRid
object_set_rid = "ri.object-set.main.object-set.c32ccba5-1a55-4cfe-ad71-160c4c77a053"


try:
    api_response = foundry_client.ontologies.OntologyObjectSet.get(
        ontology,
        object_set_rid,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectSet  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **load**
Load the ontology objects present in the `ObjectSet` from the provided object set definition.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Note that null value properties will not be returned.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_set** | ObjectSetDict |  |  |
**select** | List[SelectedPropertyApiName] |  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**exclude_rid** | Optional[pydantic.StrictBool] | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**order_by** | Optional[SearchOrderByV2Dict] |  | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**LoadObjectSetResponseV2**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"
# ObjectSetDict |
object_set = {"type": "base", "objectType": "Employee"}
# List[SelectedPropertyApiName] |
select = None
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[pydantic.StrictBool] | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[SearchOrderByV2Dict] |
order_by = None
# Optional[SdkPackageName] | packageName
package_name = None
# Optional[PageSize] |
page_size = 10000
# Optional[PageToken] |
page_token = None


try:
    api_response = foundry_client.ontologies.OntologyObjectSet.load(
        ontology,
        object_set=object_set,
        select=select,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=order_by,
        package_name=package_name,
        page_size=page_size,
        page_token=page_token,
    )
    print("The load response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.load: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadObjectSetResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

