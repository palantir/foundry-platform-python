# LinkedObject

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get_linked_object**](#get_linked_object) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} | Stable |
[**list_linked_objects**](#list_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} | Stable |
[**page_linked_objects**](#page_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} | Stable |

# **get_linked_object**
Get a specific linked object that originates from another object.

If there is no link between the two objects, `LinkedObjectNotFound` is thrown.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.  |  |
**link_type** | LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.  |  |
**linked_object_primary_key** | PropertyValueEscapedString | The primary key of the requested linked object. To look up the expected primary key for your object type, use the `Get object type` endpoint (passing the linked object type) or the **Ontology Manager**.  |  |
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
# PropertyValueEscapedString | The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
primary_key = 50030
# LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
link_type = "directReport"
# PropertyValueEscapedString | The primary key of the requested linked object. To look up the expected primary key for your object type, use the `Get object type` endpoint (passing the linked object type) or the **Ontology Manager**.
linked_object_primary_key = 80060
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
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
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.  |  |
**link_type** | LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**order_by** | Optional[OrderBy] |  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**select** | Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |

### Return type
**ListLinkedObjectsResponseV2**

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
# PropertyValueEscapedString | The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
primary_key = 50030
# LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
link_type = "directReport"
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[OrderBy]
order_by = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
select = None


try:
    for linked_object in client.ontologies.LinkedObject.list_linked_objects(
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
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.  |  |
**link_type** | LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**order_by** | Optional[OrderBy] |  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**select** | Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |

### Return type
**ListLinkedObjectsResponseV2**

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
# PropertyValueEscapedString | The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
primary_key = 50030
# LinkTypeApiName | The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
link_type = "directReport"
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[OrderBy]
order_by = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
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

