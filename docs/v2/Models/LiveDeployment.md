# LiveDeployment

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**transform_json**](#transform_json) | **POST** /v2/models/liveDeployments/{liveDeploymentRid}/transformJson | Public Beta |

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

