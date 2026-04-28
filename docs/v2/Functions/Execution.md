# Execution

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**cancel**](#cancel) | **POST** /v2/functions/executions/{executionId}/cancel | Private Beta |
[**get_result**](#get_result) | **POST** /v2/functions/executions/{executionId}/getResult | Private Beta |

# **cancel**
Cancel a running async query execution. This endpoint is idempotent.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**execution_id** | ExecutionId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**CancelExecutionResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ExecutionId
execution_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.functions.Execution.cancel(execution_id, preview=preview)
    print("The cancel response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Execution.cancel: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CancelExecutionResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_result**
Poll for the result of an async query execution.

Returns a discriminated union:
- running: execution is still in progress.
- succeeded: execution completed successfully with a return value.

If the execution failed, a service error is thrown.

Use the timeout parameter for long-polling: the server holds the
connection open for up to the specified number of seconds. If the
execution completes within that window, the result is returned
immediately. Otherwise, the running variant is returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**execution_id** | ExecutionId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**timeout** | Optional[int] | Maximum time in seconds to hold the connection open while waiting for execution to complete. Default: 0 (immediate status check). Values above 280 are clamped to 280.  | [optional] |

### Return type
**GetExecutionResultResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ExecutionId
execution_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[int] | Maximum time in seconds to hold the connection open while waiting for execution to complete. Default: 0 (immediate status check). Values above 280 are clamped to 280.
timeout = None


try:
    api_response = client.functions.Execution.get_result(
        execution_id, preview=preview, timeout=timeout
    )
    print("The get_result response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Execution.get_result: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetExecutionResultResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

