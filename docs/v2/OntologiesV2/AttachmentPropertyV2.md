# AttachmentPropertyV2

Method | HTTP request |
------------- | ------------- |
[**get_attachment**](#get_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property} |
[**get_attachment_by_rid**](#get_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid} |
[**read_attachment**](#read_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/content |
[**read_attachment_by_rid**](#read_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}/content |

# **get_attachment**
Get the metadata of attachments parented to the given object.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**property** | PropertyApiName | property |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**AttachmentMetadataResponse**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
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
# PropertyApiName | property
property = "performance"
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.AttachmentProperty.get_attachment(
        ontology,
        object_type,
        primary_key,
        property,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The get_attachment response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling AttachmentProperty.get_attachment: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AttachmentMetadataResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_attachment_by_rid**
Get the metadata of a particular attachment in an attachment list.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**property** | PropertyApiName | property |  |
**attachment_rid** | AttachmentRid | attachmentRid |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**AttachmentV2**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
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
# PropertyApiName | property
property = "performance"
# AttachmentRid | attachmentRid
attachment_rid = "ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f"
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.AttachmentProperty.get_attachment_by_rid(
        ontology,
        object_type,
        primary_key,
        property,
        attachment_rid,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The get_attachment_by_rid response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling AttachmentProperty.get_attachment_by_rid: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AttachmentV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **read_attachment**
Get the content of an attachment.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**property** | PropertyApiName | property |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**bytes**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
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
# PropertyApiName | property
property = "performance"
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.AttachmentProperty.read_attachment(
        ontology,
        object_type,
        primary_key,
        property,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The read_attachment response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling AttachmentProperty.read_attachment: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Success response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **read_attachment_by_rid**
Get the content of an attachment by its RID.

The RID must exist in the attachment array of the property.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**property** | PropertyApiName | property |  |
**attachment_rid** | AttachmentRid | attachmentRid |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**bytes**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
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
# PropertyApiName | property
property = "performance"
# AttachmentRid | attachmentRid
attachment_rid = "ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f"
# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None
# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.AttachmentProperty.read_attachment_by_rid(
        ontology,
        object_type,
        primary_key,
        property,
        attachment_rid,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The read_attachment_by_rid response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling AttachmentProperty.read_attachment_by_rid: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Success response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

