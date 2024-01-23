# foundry.OntologiesV2ApiServiceApi

The official Python library for the Foundry API

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_type**](<OntologiesV2ApiServiceApi.md#get_action_type>) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} |
[**get_deployment**](<OntologiesV2ApiServiceApi.md#get_deployment>) | **GET** /v2/ontologies/{ontology}/models/deployments/{deployment} |
[**get_object_type**](<OntologiesV2ApiServiceApi.md#get_object_type>) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} |
[**get_ontology_full_metadata**](<OntologiesV2ApiServiceApi.md#get_ontology_full_metadata>) | **GET** /v2/ontologies/{ontology}/fullMetadata |
[**get_ontology**](<OntologiesV2ApiServiceApi.md#get_ontology>) | **GET** /v2/ontologies/{ontology} |
[**get_outgoing_link_type**](<OntologiesV2ApiServiceApi.md#get_outgoing_link_type>) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
[**get_query_type**](<OntologiesV2ApiServiceApi.md#get_query_type>) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} |
[**list_action_types**](<OntologiesV2ApiServiceApi.md#list_action_types>) | **GET** /v2/ontologies/{ontology}/actionTypes |
[**list_deployments**](<OntologiesV2ApiServiceApi.md#list_deployments>) | **GET** /v2/ontologies/{ontology}/models/deployments |
[**list_object_types**](<OntologiesV2ApiServiceApi.md#list_object_types>) | **GET** /v2/ontologies/{ontology}/objectTypes |
[**list_ontologies**](<OntologiesV2ApiServiceApi.md#list_ontologies>) | **GET** /v2/ontologies |
[**list_outgoing_link_types**](<OntologiesV2ApiServiceApi.md#list_outgoing_link_types>) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
[**list_query_types**](<OntologiesV2ApiServiceApi.md#list_query_types>) | **GET** /v2/ontologies/{ontology}/queryTypes |

# **get_action_type**

> ActionTypeV2 get_action_type(ontology, action_type)

Gets a specific action type with the given API name.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.action_type_v2 import ActionTypeV2
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
action_type = 'promote-employee' # str | The name of the action type in the API. 

try:
    api_response = foundry_client.ontologies_v2.get_action_type(ontology, action_type)
    print("The response of OntologiesV2ApiServiceApi -> get_action_type:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> get_action_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**action_type** | **str**| The name of the action type in the API.  |

### Return type

[**ActionTypeV2**](ActionTypeV2.md)

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

# **get_deployment**

> DeploymentMetadata get_deployment(ontology, deployment)

Fetches information about a model deployment within a given Ontology.

### Example

```python
import time
import os
import foundry
from foundry.models.deployment_metadata import DeploymentMetadata
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
deployment = 'nextTokenPredictor' # str | The API name of the deployment you want to fetch information about. 

try:
    api_response = foundry_client.ontologies_v2.get_deployment(ontology, deployment)
    print("The response of OntologiesV2ApiServiceApi -> get_deployment:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> get_deployment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**deployment** | **str**| The API name of the deployment you want to fetch information about.  |

### Return type

[**DeploymentMetadata**](DeploymentMetadata.md)

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

> ObjectTypeV2 get_object_type(ontology, object_type)

Gets a specific object type with the given API name.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.object_type_v2 import ObjectTypeV2
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
object_type = 'employee' # str | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. 

try:
    api_response = foundry_client.ontologies_v2.get_object_type(ontology, object_type)
    print("The response of OntologiesV2ApiServiceApi -> get_object_type:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> get_object_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**object_type** | **str**| The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |

### Return type

[**ObjectTypeV2**](ObjectTypeV2.md)

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

# **get_ontology_full_metadata**

> OntologyFullMetadata get_ontology_full_metadata(ontology)

Get the full Ontology metadata. This includes the objects, links, actions, and queries.

### Example

```python
import time
import os
import foundry
from foundry.models.ontology_full_metadata import OntologyFullMetadata
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 

try:
    api_response = foundry_client.ontologies_v2.get_ontology_full_metadata(ontology)
    print("The response of OntologiesV2ApiServiceApi -> get_ontology_full_metadata:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> get_ontology_full_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |

### Return type

[**OntologyFullMetadata**](OntologyFullMetadata.md)

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

> OntologyV2 get_ontology(ontology)

Gets a specific ontology with the given Ontology RID.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.ontology_v2 import OntologyV2
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 

try:
    api_response = foundry_client.ontologies_v2.get_ontology(ontology)
    print("The response of OntologiesV2ApiServiceApi -> get_ontology:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> get_ontology: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |

### Return type

[**OntologyV2**](OntologyV2.md)

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

> LinkTypeSideV2 get_outgoing_link_type(ontology, object_type, link_type)

Get an outgoing link for an object type.  Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.link_type_side_v2 import LinkTypeSideV2
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
object_type = 'Employee' # str | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application. 
link_type = 'directReport' # str | The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**. 

try:
    api_response = foundry_client.ontologies_v2.get_outgoing_link_type(ontology, object_type, link_type)
    print("The response of OntologiesV2ApiServiceApi -> get_outgoing_link_type:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> get_outgoing_link_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**object_type** | **str**| The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |
**link_type** | **str**| The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.  |

### Return type

[**LinkTypeSideV2**](LinkTypeSideV2.md)

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

> QueryTypeV2 get_query_type(ontology, query_api_name)

Gets a specific query type with the given API name.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.query_type_v2 import QueryTypeV2
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
query_api_name = 'getEmployeesInCity' # str | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**. 

try:
    api_response = foundry_client.ontologies_v2.get_query_type(ontology, query_api_name)
    print("The response of OntologiesV2ApiServiceApi -> get_query_type:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> get_query_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**query_api_name** | **str**| The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.  |

### Return type

[**QueryTypeV2**](QueryTypeV2.md)

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

> ListActionTypesResponseV2 list_action_types(ontology, page_size=page_size, page_token=page_token)

Lists the action types for the given Ontology.  Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_action_types_response_v2 import ListActionTypesResponseV2
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = 56 # int | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    api_response = foundry_client.ontologies_v2.list_action_types(ontology, page_size=page_size, page_token=page_token)
    print("The response of OntologiesV2ApiServiceApi -> list_action_types:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> list_action_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**page_size** | **int**| The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | \[optional\]
**page_token** | **str**|  | \[optional\]

### Return type

[**ListActionTypesResponseV2**](ListActionTypesResponseV2.md)

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

# **list_deployments**

> ListDeploymentsResponse list_deployments(ontology)

Fetches a list of the available model deployments within a given Ontology.

### Example

```python
import time
import os
import foundry
from foundry.models.list_deployments_response import ListDeploymentsResponse
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 

try:
    api_response = foundry_client.ontologies_v2.list_deployments(ontology)
    print("The response of OntologiesV2ApiServiceApi -> list_deployments:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> list_deployments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |

### Return type

[**ListDeploymentsResponse**](ListDeploymentsResponse.md)

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

> ListObjectTypesV2Response list_object_types(ontology, page_size=page_size, page_token=page_token)

Lists the object types for the given Ontology.  Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_object_types_v2_response import ListObjectTypesV2Response
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = 56 # int | The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    api_response = foundry_client.ontologies_v2.list_object_types(ontology, page_size=page_size, page_token=page_token)
    print("The response of OntologiesV2ApiServiceApi -> list_object_types:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> list_object_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**page_size** | **int**| The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | \[optional\]
**page_token** | **str**|  | \[optional\]

### Return type

[**ListObjectTypesV2Response**](ListObjectTypesV2Response.md)

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

> ListOntologiesV2Response list_ontologies()

Lists the Ontologies visible to the current user.  Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_ontologies_v2_response import ListOntologiesV2Response
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")


try:
    api_response = foundry_client.ontologies_v2.list_ontologies()
    print("The response of OntologiesV2ApiServiceApi -> list_ontologies:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> list_ontologies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListOntologiesV2Response**](ListOntologiesV2Response.md)

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

> ListOutgoingLinkTypesResponseV2 list_outgoing_link_types(ontology, object_type, page_size=page_size, page_token=page_token)

List the outgoing links for an object type.  Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_outgoing_link_types_response_v2 import ListOutgoingLinkTypesResponseV2
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
object_type = 'Flight' # str | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application. 
page_size = 56 # int | The desired size of the page to be returned. (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    api_response = foundry_client.ontologies_v2.list_outgoing_link_types(ontology, object_type, page_size=page_size, page_token=page_token)
    print("The response of OntologiesV2ApiServiceApi -> list_outgoing_link_types:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> list_outgoing_link_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**object_type** | **str**| The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |
**page_size** | **int**| The desired size of the page to be returned. | \[optional\]
**page_token** | **str**|  | \[optional\]

### Return type

[**ListOutgoingLinkTypesResponseV2**](ListOutgoingLinkTypesResponseV2.md)

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

> ListQueryTypesResponseV2 list_query_types(ontology, page_size=page_size, page_token=page_token)

Lists the query types for the given Ontology.          Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.          Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

### Example

```python
import time
import os
import foundry
from foundry.models.list_query_types_response_v2 import ListQueryTypesResponseV2
from foundry.rest import ApiException
from pprint import pprint

foundry_client = foundry.FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

ontology = 'palantir' # str | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**. 
page_size = 56 # int | The desired size of the page to be returned. Defaults to 100. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    api_response = foundry_client.ontologies_v2.list_query_types(ontology, page_size=page_size, page_token=page_token)
    print("The response of OntologiesV2ApiServiceApi -> list_query_types:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OntologiesV2ApiServiceApi -> list_query_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ontology** | **str**| The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |
**page_size** | **int**| The desired size of the page to be returned. Defaults to 100. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | \[optional\]
**page_token** | **str**|  | \[optional\]

### Return type

[**ListQueryTypesResponseV2**](ListQueryTypesResponseV2.md)

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
