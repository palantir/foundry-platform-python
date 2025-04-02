# Schedule

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/orchestration/schedules | Public Beta |
[**delete**](#delete) | **DELETE** /v2/orchestration/schedules/{scheduleRid} | Public Beta |
[**get**](#get) | **GET** /v2/orchestration/schedules/{scheduleRid} | Public Beta |
[**pause**](#pause) | **POST** /v2/orchestration/schedules/{scheduleRid}/pause | Public Beta |
[**replace**](#replace) | **PUT** /v2/orchestration/schedules/{scheduleRid} | Public Beta |
[**run**](#run) | **POST** /v2/orchestration/schedules/{scheduleRid}/run | Public Beta |
[**runs**](#runs) | **GET** /v2/orchestration/schedules/{scheduleRid}/runs | Public Beta |
[**runs_page**](#runs_page) | **GET** /v2/orchestration/schedules/{scheduleRid}/runs | Public Beta |
[**unpause**](#unpause) | **POST** /v2/orchestration/schedules/{scheduleRid}/unpause | Public Beta |

# **create**
Creates a new Schedule.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**action** | Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict] |  |  |
**description** | Optional[str] |  | [optional] |
**display_name** | Optional[str] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**scope_mode** | Optional[Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]] |  | [optional] |
**trigger** | Optional[Union[Trigger, TriggerDict]] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict]
action = {
    "abortOnFailure": False,
    "forceBuild": False,
    "retryBackoffDuration": {"unit": "SECONDS", "value": 30},
    "retryCount": 1,
    "fallbackBranches": [],
    "branchName": "master",
    "notificationsEnabled": False,
    "target": {
        "type": "manual",
        "targetRids": [
            "ri.foundry.main.dataset.b737e24d-6b19-43aa-93d5-da9fc4073f6e",
            "ri.foundry.main.dataset.d2452a94-a755-4778-8bfc-a315ab52fc43",
        ],
    },
}
# Optional[str]
description = "Run all the transforms at midnight"
# Optional[str]
display_name = "My Daily Schedule"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]]
scope_mode = {"type": "user"}
# Optional[Union[Trigger, TriggerDict]] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
trigger = {"type": "time", "cronExpression": "0 0 * * *", "timeZone": "UTC"}


try:
    api_response = foundry_client.orchestration.Schedule.create(
        action=action,
        description=description,
        display_name=display_name,
        preview=preview,
        scope_mode=scope_mode,
        trigger=trigger,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Schedule.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Schedule  | The created Schedule | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **delete**
Delete the Schedule with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.delete(schedule_rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Schedule.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Schedule with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.get(schedule_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
**schedule_rid** | ScheduleRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.pause(schedule_rid, preview=preview)
    print("The pause response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Schedule.pause: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the Schedule with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid |  |  |
**action** | Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict] |  |  |
**description** | Optional[str] |  | [optional] |
**display_name** | Optional[str] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**scope_mode** | Optional[Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]] |  | [optional] |
**trigger** | Optional[Union[Trigger, TriggerDict]] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict]
action = {
    "abortOnFailure": False,
    "forceBuild": False,
    "retryBackoffDuration": {"unit": "SECONDS", "value": 30},
    "retryCount": 1,
    "fallbackBranches": [],
    "branchName": "master",
    "notificationsEnabled": False,
    "target": {
        "type": "manual",
        "targetRids": [
            "ri.foundry.main.dataset.b737e24d-6b19-43aa-93d5-da9fc4073f6e",
            "ri.foundry.main.dataset.d2452a94-a755-4778-8bfc-a315ab52fc43",
        ],
    },
}
# Optional[str]
description = "Run all the transforms at midnight"
# Optional[str]
display_name = "My Daily Schedule"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]]
scope_mode = {"type": "user"}
# Optional[Union[Trigger, TriggerDict]] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
trigger = {"type": "time", "cronExpression": "0 0 * * *", "timeZone": "UTC"}


try:
    api_response = foundry_client.orchestration.Schedule.replace(
        schedule_rid,
        action=action,
        description=description,
        display_name=display_name,
        preview=preview,
        scope_mode=scope_mode,
        trigger=trigger,
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Schedule.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Schedule  | The replaced Schedule | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **run**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ScheduleRun**

### Example

```python
from foundry import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.run(schedule_rid, preview=preview)
    print("The run response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Schedule.run: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ScheduleRun  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **runs**
Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListRunsOfScheduleResponse**

### Example

```python
from foundry import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for schedule in client.orchestration.Schedule.runs(
        schedule_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(schedule)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Schedule.runs: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListRunsOfScheduleResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **runs_page**
Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListRunsOfScheduleResponse**

### Example

```python
from foundry import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.runs_page(
        schedule_rid, page_size=page_size, page_token=page_token, preview=preview
    )
    print("The runs_page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Schedule.runs_page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListRunsOfScheduleResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **unpause**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.unpause(schedule_rid, preview=preview)
    print("The unpause response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Schedule.unpause: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

