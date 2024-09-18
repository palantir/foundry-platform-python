# ObjectTypeV2

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} |
[**get_outgoing_link_type**](#get_outgoing_link_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/objectTypes |
[**list_outgoing_link_types**](#list_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
[**page**](#page) | **GET** /v2/ontologies/{ontology}/objectTypes |
[**page_outgoing_link_types**](#page_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |

# **get**
Gets a specific object type with the given API name.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |

### Return type
**ObjectTypeV2**

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


try:
    api_response = foundry_client.ontologies.Ontology.ObjectType.get(
        ontology,
        object_type,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ObjectType.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectTypeV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_outgoing_link_type**
Get an outgoing link for an object type.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**link_type** | LinkTypeApiName | linkType |  |

### Return type
**LinkTypeSideV2**

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
object_type = "Employee"
# LinkTypeApiName | linkType
link_type = "directReport"


try:
    api_response = foundry_client.ontologies.Ontology.ObjectType.get_outgoing_link_type(
        ontology,
        object_type,
        link_type,
    )
    print("The get_outgoing_link_type response:\n")
    pprint(api_response)
except PalantirRPCException as e:
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

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |

### Return type
**ResourceIterator[ObjectTypeV2]**

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
# Optional[PageSize] | pageSize
page_size = None


try:
    for object_type in foundry_client.ontologies.Ontology.ObjectType.list(
        ontology,
        page_size=page_size,
    ):
        pprint(object_type)
except PalantirRPCException as e:
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

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |

### Return type
**ResourceIterator[LinkTypeSideV2]**

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
object_type = "Flight"
# Optional[PageSize] | pageSize
page_size = None


try:
    for object_type in foundry_client.ontologies.Ontology.ObjectType.list_outgoing_link_types(
        ontology,
        object_type,
        page_size=page_size,
    ):
        pprint(object_type)
except PalantirRPCException as e:
    print("HTTP error when calling ObjectType.list_outgoing_link_types: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOutgoingLinkTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists the object types for the given Ontology.

Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
more results available, at least one result will be present in the
response.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListObjectTypesV2Response**

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
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None


try:
    api_response = foundry_client.ontologies.Ontology.ObjectType.page(
        ontology,
        page_size=page_size,
        page_token=page_token,
    )
    print("The page response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ObjectType.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListObjectTypesV2Response  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page_outgoing_link_types**
List the outgoing links for an object type.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |

### Return type
**ListOutgoingLinkTypesResponseV2**

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
object_type = "Flight"
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None


try:
    api_response = foundry_client.ontologies.Ontology.ObjectType.page_outgoing_link_types(
        ontology,
        object_type,
        page_size=page_size,
        page_token=page_token,
    )
    print("The page_outgoing_link_types response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ObjectType.page_outgoing_link_types: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOutgoingLinkTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

