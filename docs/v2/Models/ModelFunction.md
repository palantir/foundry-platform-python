# ModelFunction

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/models/{modelRid}/function | Private Beta |
[**get**](#get) | **GET** /v2/models/{modelRid}/function | Private Beta |
[**replace**](#replace) | **PUT** /v2/models/{modelRid}/function | Private Beta |

# **create**
Creates a function for the model.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**api_name** | ModelFunctionApiName |  |  |
**display_name** | ModelFunctionDisplayName |  |  |
**is_row_wise** | ModelFunctionIsRowWise |  |  |
**ontology_binding** | Optional[OntologyRid] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ModelFunction**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# ModelFunctionApiName
api_name = "myModelFunction"
# ModelFunctionDisplayName
display_name = "Core.DisplayName"
# ModelFunctionIsRowWise
is_row_wise = False
# Optional[OntologyRid]
ontology_binding = "ri.ontology.main.ontology.a1b2c3d4-e5f6-7890-abcd-ef1234567890"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.Function.create(
        model_rid,
        api_name=api_name,
        display_name=display_name,
        is_row_wise=is_row_wise,
        ontology_binding=ontology_binding,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Function.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ModelFunction  | The created ModelFunction | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Gets the function for the model.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ModelFunction**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.Function.get(model_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Function.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ModelFunction  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replaces the function for the model.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**api_name** | ModelFunctionApiName |  |  |
**is_row_wise** | ModelFunctionIsRowWise |  |  |
**ontology_binding** | Optional[OntologyRid] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ModelFunction**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# ModelFunctionApiName
api_name = "myModelFunction"
# ModelFunctionIsRowWise
is_row_wise = False
# Optional[OntologyRid]
ontology_binding = "ri.ontology.main.ontology.a1b2c3d4-e5f6-7890-abcd-ef1234567890"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.Function.replace(
        model_rid,
        api_name=api_name,
        is_row_wise=is_row_wise,
        ontology_binding=ontology_binding,
        preview=preview,
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Function.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ModelFunction  | The replaced ModelFunction | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

