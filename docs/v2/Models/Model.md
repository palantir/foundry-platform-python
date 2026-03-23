# Model

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/models | Public Beta |
[**get**](#get) | **GET** /v2/models/{modelRid} | Public Beta |
[**promote_version**](#promote_version) | **POST** /v2/models/{modelRid}/promoteVersion | Public Beta |

# **create**
Creates a new Model with no versions.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**name** | ModelName |  |  |
**parent_folder_rid** | FolderRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Model**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelName
name = "House Pricing Model"
# FolderRid
parent_folder_rid = "ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.create(
        name=name, parent_folder_rid=parent_folder_rid, preview=preview
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Model.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Model  | The created Model | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Retrieves a Model by its Resource Identifier (RID).

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Model**

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
    api_response = client.models.Model.get(model_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Model.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Model  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **promote_version**
Promotes an existing Model Version to the target Model. The promoted Model Version will be copied to the target Model as the latest version on the master branch, but will have a new Model Version RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**source_model_version_rid** | ModelVersionRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ModelVersion**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# ModelVersionRid
source_model_version_rid = "ri.models.main.model-version.adf94926-c3ac-41ea-beb2-4946699d08ee"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.promote_version(
        model_rid, source_model_version_rid=source_model_version_rid, preview=preview
    )
    print("The promote_version response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Model.promote_version: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ModelVersion  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

