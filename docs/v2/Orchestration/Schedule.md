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
**action** | typing.Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict] |  |  |
**description** | typing.Optional[str] |  | [optional] |
**display_name** | typing.Optional[str] |  | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |
**scope_mode** | typing.Optional[typing.Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]] |  | [optional] |
**trigger** | typing.Optional[typing.Union[Trigger, TriggerDict]] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# typing.Union[CreateScheduleRequestAction, CreateScheduleRequestActionDict] |
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
# typing.Optional[str] |
description = "Run all the transforms at midnight"
# typing.Optional[str] |
display_name = "My Daily Schedule"
# typing.Optional[core_models.PreviewMode] | preview
preview = None
# typing.Optional[typing.Union[CreateScheduleRequestScopeMode, CreateScheduleRequestScopeModeDict]] |
scope_mode = {"type": "user"}
# typing.Optional[typing.Union[Trigger, TriggerDict]] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
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
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.delete(
        schedule_rid,
        preview=preview,
    )
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
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.get(
        schedule_rid,
        preview=preview,
    )
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
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.pause(
        schedule_rid,
        preview=preview,
    )
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
**schedule_rid** | ScheduleRid | scheduleRid |  |
**action** | typing.Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict] |  |  |
**description** | typing.Optional[str] |  | [optional] |
**display_name** | typing.Optional[str] |  | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |
**scope_mode** | typing.Optional[typing.Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]] |  | [optional] |
**trigger** | typing.Optional[typing.Union[Trigger, TriggerDict]] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# typing.Union[ReplaceScheduleRequestAction, ReplaceScheduleRequestActionDict] |
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
# typing.Optional[str] |
description = "Run all the transforms at midnight"
# typing.Optional[str] |
display_name = "My Daily Schedule"
# typing.Optional[core_models.PreviewMode] | preview
preview = None
# typing.Optional[typing.Union[ReplaceScheduleRequestScopeMode, ReplaceScheduleRequestScopeModeDict]] |
scope_mode = {"type": "user"}
# typing.Optional[typing.Union[Trigger, TriggerDict]] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
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
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ScheduleRun**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.run(
        schedule_rid,
        preview=preview,
    )
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
**schedule_rid** | ScheduleRid | scheduleRid |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ListRunsOfScheduleResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    for schedule in foundry_client.orchestration.Schedule.runs(
        schedule_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
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
**schedule_rid** | ScheduleRid | scheduleRid |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ListRunsOfScheduleResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.runs_page(
        schedule_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
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
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleRid | scheduleRid
schedule_rid = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Schedule.unpause(
        schedule_rid,
        preview=preview,
    )
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

