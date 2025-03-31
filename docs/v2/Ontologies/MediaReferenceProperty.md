# MediaReferenceProperty

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get_media_content**](#get_media_content) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/media/{property}/content | Public Beta |
[**get_media_metadata**](#get_media_metadata) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/media/{property}/metadata | Private Beta |
[**upload**](#upload) | **POST** /v2/ontologies/{ontology}/objectTypes/{objectType}/media/{property}/upload | Public Beta |

# **get_media_content**
Gets the content of a media item referenced by this property.

Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the media reference property.  |  |
**property** | PropertyApiName | The API name of the media reference property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**bytes**

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
# PropertyValueEscapedString | The primary key of the object with the media reference property.
primary_key = 50030
# PropertyApiName | The API name of the media reference property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.
property = "profile_picture"
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = foundry_client.ontologies.MediaReferenceProperty.get_media_content(
        ontology,
        object_type,
        primary_key,
        property,
        artifact_repository=artifact_repository,
        package_name=package_name,
        preview=preview,
    )
    print("The get_media_content response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MediaReferenceProperty.get_media_content: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | The content stream. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_media_metadata**
Gets metadata about the media item referenced by this property.

Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the media reference property.  |  |
**property** | PropertyApiName | The API name of the media reference backed property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**MediaMetadata**

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
# PropertyValueEscapedString | The primary key of the object with the media reference property.
primary_key = 50030
# PropertyApiName | The API name of the media reference backed property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.
property = None
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = foundry_client.ontologies.MediaReferenceProperty.get_media_metadata(
        ontology,
        object_type,
        primary_key,
        property,
        artifact_repository=artifact_repository,
        package_name=package_name,
        preview=preview,
    )
    print("The get_media_metadata response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MediaReferenceProperty.get_media_metadata: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MediaMetadata  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload**
Uploads a media item to the media set which backs the specified property.  The property must be backed by a single media set and branch, otherwise an error will be thrown.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:ontologies-read api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**property** | PropertyApiName | The API name of the media reference property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**body** | bytes | Body of the request |  |
**media_item_path** | Optional[MediaItemPath] | A path for the media item within its backing media set. Required if the backing media set requires paths.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**MediaReference**

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
# PropertyApiName | The API name of the media reference property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.
property = "profile_picture"
# bytes | Body of the request
body = None
# Optional[MediaItemPath] | A path for the media item within its backing media set. Required if the backing media set requires paths.
media_item_path = "my-file.png"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = foundry_client.ontologies.MediaReferenceProperty.upload(
        ontology, object_type, property, body, media_item_path=media_item_path, preview=preview
    )
    print("The upload response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MediaReferenceProperty.upload: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MediaReference  | The media reference for the uploaded media. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

