# LiveDeployment

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/models/liveDeployments | Private Beta |
[**get**](#get) | **GET** /v2/models/liveDeployments/{liveDeploymentRid} | Private Beta |
[**replace**](#replace) | **PUT** /v2/models/liveDeployments/{liveDeploymentRid} | Private Beta |
[**transform_json**](#transform_json) | **POST** /v2/models/liveDeployments/{liveDeploymentRid}/transformJson | Public Beta |

# **create**
Creates a new live deployment for a model version with the specified runtime configuration. The deployment will begin provisioning compute resources and deploying the target model version.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**deployment_type** | CreateLiveDeploymentTarget | The target model source for the live deployment. Determines which model and version selection strategy to use when creating the deployment.  |  |
**runtime_configuration** | LiveDeploymentRuntimeConfiguration | The compute resource configuration for the deployment. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**LiveDeployment**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# CreateLiveDeploymentTarget | The target model source for the live deployment. Determines which model and version selection strategy to use when creating the deployment.
deployment_type = None
# LiveDeploymentRuntimeConfiguration | The compute resource configuration for the deployment.
runtime_configuration = {
    "minReplicas": 1,
    "maxReplicas": 3,
    "cpu": 1.0,
    "memory": "256MiB",
    "threadCount": 32,
}
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.LiveDeployment.create(
        deployment_type=deployment_type,
        runtime_configuration=runtime_configuration,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling LiveDeployment.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LiveDeployment  | The created LiveDeployment | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Retrieves a live deployment by its Resource Identifier (RID), including its deployed model version and runtime configuration.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**live_deployment_rid** | LiveDeploymentRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**LiveDeployment**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# LiveDeploymentRid
live_deployment_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.LiveDeployment.get(live_deployment_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling LiveDeployment.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LiveDeployment  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Updates the runtime configuration of the live deployment. The deployment will apply the new configuration to the running replicas.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**live_deployment_rid** | LiveDeploymentRid |  |  |
**runtime_configuration** | LiveDeploymentRuntimeConfiguration | The compute resource configuration for the deployment. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**LiveDeployment**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# LiveDeploymentRid
live_deployment_rid = None
# LiveDeploymentRuntimeConfiguration | The compute resource configuration for the deployment.
runtime_configuration = {
    "minReplicas": 1,
    "maxReplicas": 3,
    "cpu": 1.0,
    "memory": "256MiB",
    "threadCount": 32,
}
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.LiveDeployment.replace(
        live_deployment_rid, runtime_configuration=runtime_configuration, preview=preview
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling LiveDeployment.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LiveDeployment  | The replaced LiveDeployment | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **transform_json**
Performs inference on the live deployment.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**live_deployment_rid** | LiveDeploymentRid |  |  |
**input** | Dict[str, Any] | The input data for the model inference. The structure should match the model's transform API specification, where each key is an input name and the value is the corresponding input data.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**TransformLiveDeploymentResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# LiveDeploymentRid
live_deployment_rid = None
# Dict[str, Any] | The input data for the model inference. The structure should match the model's transform API specification, where each key is an input name and the value is the corresponding input data.
input = {"input_df": [{"feature_1": 1.0, "feature_2": 2}]}
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.LiveDeployment.transform_json(
        live_deployment_rid, input=input, preview=preview
    )
    print("The transform_json response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling LiveDeployment.transform_json: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TransformLiveDeploymentResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

