# ObjectTypeV2

Method | HTTP request |
------------- | ------------- |
[**iterator**](#iterator) | **GET** /v2/ontologies/{ontology}/objectTypes |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} |
[**list_outgoing_link_types_v2**](#list_outgoing_link_types_v2) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
[**get_outgoing_link_type_v2**](#get_outgoing_link_type_v2) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |

# **iterator**
Lists the object types for the given Ontology.

Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
more results available, at least one result will be present in the
response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListObjectTypesV2Response**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = "palantir" # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = None # Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details. 
page_token = None # Optional[PageToken] | pageToken


try:
    api_response = foundry_client.ontologiesv2.ObjectTypeV2.iterator(
ontology,page_size=page_sizepage_token=page_token    )
    print("The ObjectTypeV2.iterator response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ObjectTypeV2.iterator: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListObjectTypesV2Response  | ListObjectTypesV2Response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
Gets a specific object type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |

### Return type
**ObjectTypeV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

ontology = "palantir"  # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
object_type = "employee"  # ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.


try:
    api_response = foundry_client.ontologiesv2.ObjectTypeV2.get(
        ontology,
        object_type,
    )
    print("The ObjectTypeV2.get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ObjectTypeV2.get: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectTypeV2  | Represents an object type in the Ontology. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_outgoing_link_types_v2**
List the outgoing links for an object type.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |  |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListOutgoingLinkTypesResponseV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = "palantir" # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
object_type = "Flight" # ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application. 
page_size = None # Optional[PageSize] | The desired size of the page to be returned.
page_token = None # Optional[PageToken] | pageToken


try:
    api_response = foundry_client.ontologiesv2.ObjectTypeV2.list_outgoing_link_types_v2(
ontology,object_type,page_size=page_sizepage_token=page_token    )
    print("The ObjectTypeV2.list_outgoing_link_types_v2 response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ObjectTypeV2.list_outgoing_link_types_v2: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOutgoingLinkTypesResponseV2  | ListOutgoingLinkTypesResponseV2 | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_outgoing_link_type_v2**
Get an outgoing link for an object type.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:read-data`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |  |
**link_type** | LinkTypeApiName | The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.  |  |

### Return type
**LinkTypeSideV2**

### Example

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

ontology = "palantir"  # OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
object_type = "Employee"  # ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
link_type = "directReport"  # LinkTypeApiName | The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.


try:
    api_response = foundry_client.ontologiesv2.ObjectTypeV2.get_outgoing_link_type_v2(
        ontology,
        object_type,
        link_type,
    )
    print("The ObjectTypeV2.get_outgoing_link_type_v2 response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ObjectTypeV2.get_outgoing_link_type_v2: %s\n" % e)

```



### Authorization

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LinkTypeSideV2  | LinkTypeSide | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

