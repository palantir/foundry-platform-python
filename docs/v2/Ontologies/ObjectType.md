# ObjectType

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} | Stable |
[**get_full_metadata**](#get_full_metadata) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/fullMetadata | Private Beta |
[**get_outgoing_link_type**](#get_outgoing_link_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} | Stable |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/objectTypes | Stable |
[**list_outgoing_link_types**](#list_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes | Stable |

# **get**
Gets a specific object type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the object type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |

### Return type
**ObjectTypeV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# Optional[FoundryBranch] | The Foundry branch to load the object type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None


try:
    api_response = client.ontologies.Ontology.ObjectType.get(ontology, object_type, branch=branch)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectTypeV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_full_metadata**
Gets the full metadata for a specific object type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**ObjectTypeFullMetadata**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# Optional[FoundryBranch] | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.Ontology.ObjectType.get_full_metadata(
        ontology,
        object_type,
        branch=branch,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The get_full_metadata response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.get_full_metadata: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectTypeFullMetadata  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_outgoing_link_type**
Get an outgoing link for an object type.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |  |
**link_type** | LinkTypeApiName | The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |

### Return type
**LinkTypeSideV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
object_type = "Employee"
# LinkTypeApiName | The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.
link_type = "directReport"
# Optional[FoundryBranch] | The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None


try:
    api_response = client.ontologies.Ontology.ObjectType.get_outgoing_link_type(
        ontology, object_type, link_type, branch=branch
    )
    print("The get_outgoing_link_type response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.get_outgoing_link_type: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LinkTypeSideV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the object types for the given Ontology.

Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
more results available, at least one result will be present in the
response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to list the object types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListObjectTypesV2Response**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[FoundryBranch] | The Foundry branch to list the object types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for object_type in client.ontologies.Ontology.ObjectType.list(
        ontology, branch=branch, page_size=page_size, page_token=page_token
    ):
        pprint(object_type)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListObjectTypesV2Response  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_outgoing_link_types**
List the outgoing links for an object type.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the outgoing link types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListOutgoingLinkTypesResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
object_type = "Flight"
# Optional[FoundryBranch] | The Foundry branch to load the outgoing link types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PageSize] | The desired size of the page to be returned.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for object_type in client.ontologies.Ontology.ObjectType.list_outgoing_link_types(
        ontology, object_type, branch=branch, page_size=page_size, page_token=page_token
    ):
        pprint(object_type)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ObjectType.list_outgoing_link_types: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOutgoingLinkTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

