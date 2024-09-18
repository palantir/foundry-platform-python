# Schedule

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/orchestration/schedules/{scheduleRid} |
[**pause**](#pause) | **POST** /v2/orchestration/schedules/{scheduleRid}/pause |
[**run**](#run) | **POST** /v2/orchestration/schedules/{scheduleRid}/run |
[**unpause**](#unpause) | **POST** /v2/orchestration/schedules/{scheduleRid}/unpause |

# **get**
Get the Schedule with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.get(
        schedule_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Schedule.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Schedule  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **pause**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.pause(
        schedule_rid,
        preview=preview,
    )
    print("The pause response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Schedule.pause: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **run**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ScheduleRun**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.run(
        schedule_rid,
        preview=preview,
    )
    print("The run response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Schedule.run: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ScheduleRun  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **unpause**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.unpause(
        schedule_rid,
        preview=preview,
    )
    print("The unpause response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Schedule.unpause: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

