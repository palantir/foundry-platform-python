# LinkedObjectV2

Method | HTTP request |
------------- | ------------- |
[**get_linked_object**](#get_linked_object) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} |
[**list_linked_objects**](#list_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} |
[**page_linked_objects**](#page_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} |

# **get_linked_object**
Get a specific linked object that originates from another object.

If there is no link between the two objects, `LinkedObjectNotFound` is thrown.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**link_type** | LinkTypeApiName | linkType |  |
**linked_object_primary_key** | PropertyValueEscapedString | linkedObjectPrimaryKey |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**exclude_rid** | Optional[StrictBool] | excludeRid | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |
**select** | Optional[List[SelectedPropertyApiName]] | select | [optional] |

### Return type
**OntologyObjectV2**

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
# ObjectTypeApiName | objectType
object_type = "employee"
# PropertyValueEscapedString | primaryKey
primary_key = 50030
# LinkTypeApiName | linkType
link_type = "directReport"
# PropertyValueEscapedString | linkedObjectPrimaryKey
linked_object_primary_key = 80060
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[StrictBool] | excludeRid
exclude_rid = None
# Optional[SdkPackageName] | packageName
package_name = None
# Optional[List[SelectedPropertyApiName]] | select
select = None


try:
    api_response = foundry_client.ontologies.LinkedObject.get_linked_object(
        ontology,
        object_type,
        primary_key,
        link_type,
        linked_object_primary_key,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        package_name=package_name,
        select=select,
    )
    print("The get_linked_object response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling LinkedObject.get_linked_object: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OntologyObjectV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_linked_objects**
Lists the linked objects for a specific object and the given link type.

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
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**link_type** | LinkTypeApiName | linkType |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**exclude_rid** | Optional[StrictBool] | excludeRid | [optional] |
**order_by** | Optional[OrderBy] | orderBy | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**select** | Optional[List[SelectedPropertyApiName]] | select | [optional] |

### Return type
**ResourceIterator[OntologyObjectV2]**

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
# ObjectTypeApiName | objectType
object_type = "employee"
# PropertyValueEscapedString | primaryKey
primary_key = 50030
# LinkTypeApiName | linkType
link_type = "directReport"
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[StrictBool] | excludeRid
exclude_rid = None
# Optional[OrderBy] | orderBy
order_by = None
# Optional[SdkPackageName] | packageName
package_name = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[List[SelectedPropertyApiName]] | select
select = None


try:
    for linked_object in foundry_client.ontologies.LinkedObject.list_linked_objects(
        ontology,
        object_type,
        primary_key,
        link_type,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=order_by,
        package_name=package_name,
        page_size=page_size,
        select=select,
    ):
        pprint(linked_object)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling LinkedObject.list_linked_objects: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListLinkedObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page_linked_objects**
Lists the linked objects for a specific object and the given link type.

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
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**link_type** | LinkTypeApiName | linkType |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**exclude_rid** | Optional[StrictBool] | excludeRid | [optional] |
**order_by** | Optional[OrderBy] | orderBy | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**select** | Optional[List[SelectedPropertyApiName]] | select | [optional] |

### Return type
**ListLinkedObjectsResponseV2**

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
# ObjectTypeApiName | objectType
object_type = "employee"
# PropertyValueEscapedString | primaryKey
primary_key = 50030
# LinkTypeApiName | linkType
link_type = "directReport"
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[StrictBool] | excludeRid
exclude_rid = None
# Optional[OrderBy] | orderBy
order_by = None
# Optional[SdkPackageName] | packageName
package_name = None
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[List[SelectedPropertyApiName]] | select
select = None


try:
    api_response = foundry_client.ontologies.LinkedObject.page_linked_objects(
        ontology,
        object_type,
        primary_key,
        link_type,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=order_by,
        package_name=package_name,
        page_size=page_size,
        page_token=page_token,
        select=select,
    )
    print("The page_linked_objects response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling LinkedObject.page_linked_objects: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListLinkedObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

