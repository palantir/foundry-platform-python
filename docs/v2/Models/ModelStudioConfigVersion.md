# ModelStudioConfigVersion

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/models/modelStudios/{modelStudioRid}/configVersions | Private Beta |
[**get**](#get) | **GET** /v2/models/modelStudios/{modelStudioRid}/configVersions/{modelStudioConfigVersionVersion} | Private Beta |
[**latest**](#latest) | **GET** /v2/models/modelStudios/{modelStudioRid}/configVersions/latest | Private Beta |
[**list**](#list) | **GET** /v2/models/modelStudios/{modelStudioRid}/configVersions | Private Beta |

# **create**
Creates a new Model Studio configuration version.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_studio_rid** | ModelStudioRid |  |  |
**name** | ModelStudioConfigVersionName | Human readable name of the configuration version and experiment. |  |
**resources** | ResourceConfiguration | The compute resources allocated for training runs. |  |
**trainer_id** | TrainerId | The identifier of the trainer to use for this configuration. |  |
**worker_config** | ModelStudioWorkerConfig | The worker configuration including inputs, outputs, and custom settings. |  |
**changelog** | Optional[str] | Changelog describing changes in this version. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ModelStudioConfigVersion**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelStudioRid
model_studio_rid = None
# ModelStudioConfigVersionName | Human readable name of the configuration version and experiment.
name = None
# ResourceConfiguration | The compute resources allocated for training runs.
resources = {"gpu": "A100"}
# TrainerId | The identifier of the trainer to use for this configuration.
trainer_id = "autogluon"
# ModelStudioWorkerConfig | The worker configuration including inputs, outputs, and custom settings.
worker_config = None
# Optional[str] | Changelog describing changes in this version.
changelog = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.ModelStudio.ConfigVersion.create(
        model_studio_rid,
        name=name,
        resources=resources,
        trainer_id=trainer_id,
        worker_config=worker_config,
        changelog=changelog,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ConfigVersion.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ModelStudioConfigVersion  | The created ModelStudioConfigVersion | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Gets a specific Model Studio configuration version.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_studio_rid** | ModelStudioRid |  |  |
**model_studio_config_version_version** | ModelStudioConfigVersionNumber | The version number of this configuration. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ModelStudioConfigVersion**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelStudioRid
model_studio_rid = None
# ModelStudioConfigVersionNumber | The version number of this configuration.
model_studio_config_version_version = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.ModelStudio.ConfigVersion.get(
        model_studio_rid, model_studio_config_version_version, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ConfigVersion.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ModelStudioConfigVersion  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **latest**
Gets the latest configuration version for a Model Studio.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_studio_rid** | ModelStudioRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Optional[ModelStudioConfigVersion]**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelStudioRid
model_studio_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.ModelStudio.ConfigVersion.latest(model_studio_rid, preview=preview)
    print("The latest response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ConfigVersion.latest: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Optional[ModelStudioConfigVersion]  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all configuration versions for a Model Studio.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_studio_rid** | ModelStudioRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListModelStudioConfigVersionsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelStudioRid
model_studio_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for model_studio_config_version in client.models.ModelStudio.ConfigVersion.list(
        model_studio_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(model_studio_config_version)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ConfigVersion.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListModelStudioConfigVersionsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

