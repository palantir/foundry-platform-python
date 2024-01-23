# foundry.OntologiesApiServiceApi

The official Python library for the Foundry API

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_type**](<OntologiesApiServiceApi.md#get_action_type>) | **GET** /v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName} |
[**get_object_type**](<OntologiesApiServiceApi.md#get_object_type>) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType} |
[**get_ontology**](<OntologiesApiServiceApi.md#get_ontology>) | **GET** /v1/ontologies/{ontologyRid} |
[**get_outgoing_link_type**](<OntologiesApiServiceApi.md#get_outgoing_link_type>) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
[**get_query_type**](<OntologiesApiServiceApi.md#get_query_type>) | **GET** /v1/ontologies/{ontologyRid}/queryTypes/{queryApiName} |
[**list_action_types**](<OntologiesApiServiceApi.md#list_action_types>) | **GET** /v1/ontologies/{ontologyRid}/actionTypes |
[**list_object_types**](<OntologiesApiServiceApi.md#list_object_types>) | **GET** /v1/ontologies/{ontologyRid}/objectTypes |
[**list_ontologies**](<OntologiesApiServiceApi.md#list_ontologies>) | **GET** /v1/ontologies |
[**list_outgoing_link_types**](<OntologiesApiServiceApi.md#list_outgoing_link_types>) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes |
[**list_query_types**](<OntologiesApiServiceApi.md#list_query_types>) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |

# **get_action_type**

> ActionType get_action_type(ontology_rid, action_type_api_name)

Gets a specific action type with the given API name.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.action_type import ActionType
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = 'ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367' # str | The unique Resource Identifier (RID) of the Ontology that contains the action type. 
action_type_api_name = 'promote-employee' # str | The name of the action type in the API. 

try:
    api_response = foundry_client.ontologies.get_action_type(ontology_rid, action_type_api_name)
    print("The response of OntologiesApiServiceApi -> get_action_type:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> get_action_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology_rid** | **str**| The unique Resource Identifier (RID) of the Ontology that contains the action type.  |
**action_type_api_name** | **str**| The name of the action type in the API.  |

### Return type

[**ActionType**](ActionType.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_object_type**

> ObjectType get_object_type(ontology_rid, object_type)

Gets a specific object type with the given API name.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.object_type import ObjectType
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = 'ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367' # str | The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. 
object_type = 'employee' # str | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. 

try:
    api_response = foundry_client.ontologies.get_object_type(ontology_rid, object_type)
    print("The response of OntologiesApiServiceApi -> get_object_type:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> get_object_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology_rid** | **str**| The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**object_type** | **str**| The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |

### Return type

[**ObjectType**](ObjectType.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_ontology**

> Ontology get_ontology(ontology_rid)

Gets a specific ontology with the given Ontology RID.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.ontology import Ontology
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = 'ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367' # str | The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. 

try:
    api_response = foundry_client.ontologies.get_ontology(ontology_rid)
    print("The response of OntologiesApiServiceApi -> get_ontology:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> get_ontology: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology_rid** | **str**| The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |

### Return type

[**Ontology**](Ontology.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_outgoing_link_type**

> LinkTypeSide get_outgoing_link_type(ontology_rid, object_type, link_type)

Get an outgoing link for an object type.  Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.link_type_side import LinkTypeSide
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = 'ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367' # str | The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager** application. 
object_type = 'Employee' # str | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application. 
link_type = 'directReport' # str | The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**. 

try:
    api_response = foundry_client.ontologies.get_outgoing_link_type(ontology_rid, object_type, link_type)
    print("The response of OntologiesApiServiceApi -> get_outgoing_link_type:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> get_outgoing_link_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology_rid** | **str**| The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager** application.  |
**object_type** | **str**| The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |
**link_type** | **str**| The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.  |

### Return type

[**LinkTypeSide**](LinkTypeSide.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **get_query_type**

> QueryType get_query_type(ontology_rid, query_api_name, preview=preview)

Gets a specific query type with the given API name.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.query_type import QueryType
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = 'ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367' # str | The unique Resource Identifier (RID) of the Ontology that contains the query type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. 
query_api_name = 'getEmployeesInCity' # str | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**. 
preview = true # bool |  (optional)

try:
    api_response = foundry_client.ontologies.get_query_type(ontology_rid, query_api_name, preview=preview)
    print("The response of OntologiesApiServiceApi -> get_query_type:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> get_query_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology_rid** | **str**| The unique Resource Identifier (RID) of the Ontology that contains the query type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**query_api_name** | **str**| The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.  |
**preview** | **bool**|  | \[optional\]

### Return type

[**QueryType**](QueryType.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **list_action_types**

> ListActionTypesResponse list_action_types(ontology_rid, page_size=page_size, page_token=page_token)

Lists the action types for the given Ontology.  Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_action_types_response import ListActionTypesResponse
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = 'ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367' # str | The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = 56 # int | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    api_response = foundry_client.ontologies.list_action_types(ontology_rid, page_size=page_size, page_token=page_token)
    print("The response of OntologiesApiServiceApi -> list_action_types:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> list_action_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology_rid** | **str**| The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**page_size** | **int**| The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | \[optional\]
**page_token** | **str**|  | \[optional\]

### Return type

[**ListActionTypesResponse**](ListActionTypesResponse.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **list_object_types**

> ListObjectTypesResponse list_object_types(ontology_rid, page_size=page_size, page_token=page_token)

Lists the object types for the given Ontology.  Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_object_types_response import ListObjectTypesResponse
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = 'ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367' # str | The unique Resource Identifier (RID) of the Ontology that contains the object types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = 56 # int | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    api_response = foundry_client.ontologies.list_object_types(ontology_rid, page_size=page_size, page_token=page_token)
    print("The response of OntologiesApiServiceApi -> list_object_types:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> list_object_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology_rid** | **str**| The unique Resource Identifier (RID) of the Ontology that contains the object types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**page_size** | **int**| The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | \[optional\]
**page_token** | **str**|  | \[optional\]

### Return type

[**ListObjectTypesResponse**](ListObjectTypesResponse.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **list_ontologies**

> ListOntologiesResponse list_ontologies()

Lists the Ontologies visible to the current user.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_ontologies_response import ListOntologiesResponse
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")


try:
    api_response = foundry_client.ontologies.list_ontologies()
    print("The response of OntologiesApiServiceApi -> list_ontologies:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> list_ontologies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListOntologiesResponse**](ListOntologiesResponse.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **list_outgoing_link_types**

> ListOutgoingLinkTypesResponse list_outgoing_link_types(ontology_rid, object_type, page_size=page_size, page_token=page_token)

List the outgoing links for an object type.  Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_outgoing_link_types_response import ListOutgoingLinkTypesResponse
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = 'ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367' # str | The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager** application. 
object_type = 'Flight' # str | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application. 
page_size = 56 # int | The desired size of the page to be returned. (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    api_response = foundry_client.ontologies.list_outgoing_link_types(ontology_rid, object_type, page_size=page_size, page_token=page_token)
    print("The response of OntologiesApiServiceApi -> list_outgoing_link_types:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> list_outgoing_link_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology_rid** | **str**| The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager** application.  |
**object_type** | **str**| The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |
**page_size** | **int**| The desired size of the page to be returned. | \[optional\]
**page_token** | **str**|  | \[optional\]

### Return type

[**ListOutgoingLinkTypesResponse**](ListOutgoingLinkTypesResponse.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)

# **list_query_types**

> ListQueryTypesResponse list_query_types(ontology_rid, page_size=page_size, page_token=page_token, preview=preview)

Lists the query types for the given Ontology.  Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_query_types_response import ListQueryTypesResponse
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology_rid = 'ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367' # str | The unique Resource Identifier (RID) of the Ontology that contains the query types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = 56 # int | The desired size of the page to be returned. Defaults to 100. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  (optional)
page_token = 'page_token_example' # str |  (optional)
preview = true # bool |  (optional)

try:
    api_response = foundry_client.ontologies.list_query_types(ontology_rid, page_size=page_size, page_token=page_token, preview=preview)
    print("The response of OntologiesApiServiceApi -> list_query_types:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesApiServiceApi -> list_query_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology_rid** | **str**| The unique Resource Identifier (RID) of the Ontology that contains the query types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**page_size** | **int**| The desired size of the page to be returned. Defaults to 100. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | \[optional\]
**page_token** | **str**|  | \[optional\]
**preview** | **bool**|  | \[optional\]

### Return type

[**ListQueryTypesResponse**](ListQueryTypesResponse.md)

### Authorization

See [README](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  -  |

[\[Back to top\]](#) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to README\]](../README.md)
