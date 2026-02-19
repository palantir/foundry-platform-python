# ModelStudioTrainer

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/models/modelStudioTrainers/{modelStudioTrainerTrainerId} | Private Beta |
[**list**](#list) | **GET** /v2/models/modelStudioTrainers | Private Beta |

# **get**
Gets details about a specific trainer by its ID and optional version.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_studio_trainer_trainer_id** | TrainerId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**version** | Optional[TrainerVersion] | Specific version of the trainer to retrieve. If not specified, returns the latest version. | [optional] |

### Return type
**ModelStudioTrainer**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TrainerId
model_studio_trainer_trainer_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[TrainerVersion] | Specific version of the trainer to retrieve. If not specified, returns the latest version.
version = None


try:
    api_response = client.models.ModelStudioTrainer.get(
        model_studio_trainer_trainer_id, preview=preview, version=version
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ModelStudioTrainer.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ModelStudioTrainer  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all available trainers for Model Studios.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListModelStudioTrainersResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.ModelStudioTrainer.list(preview=preview)
    print("The list response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ModelStudioTrainer.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListModelStudioTrainersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

