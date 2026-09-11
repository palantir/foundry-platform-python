# ProcessExecutionSignal

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**complete**](#complete) | **POST** /v3/platform/processExecutions/{processExecutionId}/signals/{signalId}/complete | Private Beta |

# **complete**
Complete a signal on a process execution.

A signal may be completed multiple times, each contributing toward the execution's wait conditions.
If the execution is suspended waiting on this signal, it resumes once its wait conditions are
satisfied. Resuming an execution runs user-authored logic. Only the token that originally invoked the
process execution can complete its signals.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**process_execution_id** | ProcessExecutionId |  |  |
**signal_id** | SignalId |  |  |
**payload** | Optional[Any] | Arbitrary JSON passed to the process execution that consumes the signal. Empty when the completion carries no payload. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ProcessExecutionId
process_execution_id = None
# SignalId
signal_id = None
# Optional[Any] | Arbitrary JSON passed to the process execution that consumes the signal. Empty when the completion carries no payload.
payload = None


try:
    api_response = client.orchestrator.ProcessExecution.Signal.complete(
        process_execution_id, signal_id, payload=payload
    )
    print("The complete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Signal.complete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)
