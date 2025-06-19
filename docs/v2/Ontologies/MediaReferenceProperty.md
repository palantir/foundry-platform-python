# MediaReferenceProperty

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get_media_content**](#get_media_content) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/media/{property}/content | Public Beta |
[**get_media_metadata**](#get_media_metadata) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/media/{property}/metadata | Private Beta |
[**upload**](#upload) | **POST** /v2/ontologies/{ontology}/objectTypes/{objectType}/media/{property}/upload | Public Beta |
[**upload_media**](#upload_media) | **POST** /v2/ontologies/{ontology}/actions/{actionType}/media/upload | Private Beta |

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
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object with the media reference property.
primary_key = 50030
# PropertyApiName | The API name of the media reference property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.
property = "profile_picture"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.MediaReferenceProperty.get_media_content(
        ontology,
        object_type,
        primary_key,
        property,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The get_media_content response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**MediaMetadata**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object with the media reference property.
primary_key = 50030
# PropertyApiName | The API name of the media reference backed property. To find the API name, check the **Ontology Manager** or use the **Get object type** endpoint.
property = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.MediaReferenceProperty.get_media_metadata(
        ontology,
        object_type,
        primary_key,
        property,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The get_media_metadata response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

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
    api_response = client.ontologies.MediaReferenceProperty.upload(
        ontology, object_type, property, body, media_item_path=media_item_path, preview=preview
    )
    print("The upload response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaReferenceProperty.upload: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MediaReference  | The media reference for the uploaded media. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload_media**
Uploads a media item for use by the specified action. If the media item isn't persisted by the associated action within 1 hour, the item will be deleted. 

The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:ontologies-read api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**action_type** | ActionTypeApiName | The name of the action type in the API.  |  |
**body** | bytes | Body of the request |  |
**media_item_path** | Optional[MediaItemPath] | The path to write the media item to. Required if the backing media set requires paths.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**MediaReference**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ActionTypeApiName | The name of the action type in the API.
action_type = "add-profile-picture"
# bytes | Body of the request
body = None
# Optional[MediaItemPath] | The path to write the media item to. Required if the backing media set requires paths.
media_item_path = "my-file.png"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.MediaReferenceProperty.upload_media(
        ontology, action_type, body, media_item_path=media_item_path, preview=preview
    )
    print("The upload_media response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaReferenceProperty.upload_media: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MediaReference  | The media reference for the uploaded media. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

