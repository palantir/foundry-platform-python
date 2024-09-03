# OntologyObjectSet

Method | HTTP request |
------------- | ------------- |
[**aggregate**](#aggregate) | **POST** /v2/ontologies/{ontology}/objectSets/aggregate |
[**create_temporary**](#create_temporary) | **POST** /v2/ontologies/{ontology}/objectSets/createTemporary |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/objectSets/{objectSetRid} |
[**load**](#load) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjects |

# **aggregate**
Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.        

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**aggregate_object_set_request_v2** | Union[AggregateObjectSetRequestV2, AggregateObjectSetRequestV2Dict] | Body of the request |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

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

# Union[AggregateObjectSetRequestV2, AggregateObjectSetRequestV2Dict] | Body of the request
aggregate_object_set_request_v2 = None

# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None

# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.OntologyObjectSet.aggregate(
        ontology,
        aggregate_object_set_request_v2,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The aggregate response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.aggregate: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AggregateObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **create_temporary**
Creates a temporary `ObjectSet` from the given definition.        

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**create_temporary_object_set_request_v2** | Union[CreateTemporaryObjectSetRequestV2, CreateTemporaryObjectSetRequestV2Dict] | Body of the request |  |

### Return type
**CreateTemporaryObjectSetResponseV2**

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

# Union[CreateTemporaryObjectSetRequestV2, CreateTemporaryObjectSetRequestV2Dict] | Body of the request
create_temporary_object_set_request_v2 = {"objectSet": {"type": "base", "objectType": "Employee"}}


try:
    api_response = foundry_client.ontologies.OntologyObjectSet.create_temporary(
        ontology,
        create_temporary_object_set_request_v2,
    )
    print("The create_temporary response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.create_temporary: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CreateTemporaryObjectSetResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **get**
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
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
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
except PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.get: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectSet  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

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
**load_object_set_request_v2** | Union[LoadObjectSetRequestV2, LoadObjectSetRequestV2Dict] | Body of the request |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**LoadObjectSetResponseV2**

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

# Union[LoadObjectSetRequestV2, LoadObjectSetRequestV2Dict] | Body of the request
load_object_set_request_v2 = {
    "objectSet": {"type": "base", "objectType": "Employee"},
    "pageSize": 10000,
    "nextPageToken": "v1.VGhlcmUgaXMgc28gbXVjaCBsZWZ0IHRvIGJ1aWxkIC0gcGFsYW50aXIuY29tL2NhcmVlcnMv",
}

# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None

# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.OntologyObjectSet.load(
        ontology,
        load_object_set_request_v2,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The load response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.load: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadObjectSetResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

