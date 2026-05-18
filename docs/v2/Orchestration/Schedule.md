# Schedule

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/orchestration/schedules | Public Beta |
[**delete**](#delete) | **DELETE** /v2/orchestration/schedules/{scheduleRid} | Stable |
[**get**](#get) | **GET** /v2/orchestration/schedules/{scheduleRid} | Public Beta |
[**get_affected_resources**](#get_affected_resources) | **POST** /v2/orchestration/schedules/{scheduleRid}/getAffectedResources | Public Beta |
[**get_batch**](#get_batch) | **POST** /v2/orchestration/schedules/getBatch | Public Beta |
[**pause**](#pause) | **POST** /v2/orchestration/schedules/{scheduleRid}/pause | Stable |
[**replace**](#replace) | **PUT** /v2/orchestration/schedules/{scheduleRid} | Public Beta |
[**run**](#run) | **POST** /v2/orchestration/schedules/{scheduleRid}/run | Stable |
[**runs**](#runs) | **GET** /v2/orchestration/schedules/{scheduleRid}/runs | Stable |
[**unpause**](#unpause) | **POST** /v2/orchestration/schedules/{scheduleRid}/unpause | Stable |

# **create**
Creates a new Schedule.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**action** | CreateScheduleRequestAction |  |  |
**description** | Optional[str] |  | [optional] |
**display_name** | Optional[str] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**scope_mode** | Optional[CreateScheduleRequestScopeMode] |  | [optional] |
**trigger** | Optional[Trigger] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# CreateScheduleRequestAction
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
# Optional[CreateScheduleRequestScopeMode]
scope_mode = {"type": "user"}
# Optional[Trigger] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
trigger = {"type": "time", "cronExpression": "0 0 * * *", "timeZone": "UTC"}


try:
    api_response = client.orchestration.Schedule.create(
        action=action,
        description=description,
        display_name=display_name,
        preview=preview,
        scope_mode=scope_mode,
        trigger=trigger,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None


try:
    api_response = client.orchestration.Schedule.delete(schedule_rid)
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.orchestration.Schedule.get(schedule_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Schedule.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Schedule  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_affected_resources**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**AffectedResourcesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.orchestration.Schedule.get_affected_resources(
        schedule_rid, preview=preview
    )
    print("The get_affected_resources response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Schedule.get_affected_resources: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AffectedResourcesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_batch**
Fetch multiple schedules in a single request. Schedules not found or inaccessible to the user will be 
omitted from the response.


The maximum batch size for this endpoint is 1000.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetSchedulesBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GetSchedulesBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetSchedulesBatchRequestElement] | Body of the request
body = [{"scheduleRid": "ri.scheduler.main.schedule.5ad5c340-59f3-4a60-9fc6-161bb984f871"}]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.orchestration.Schedule.get_batch(body, preview=preview)
    print("The get_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Schedule.get_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetSchedulesBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **pause**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid |  |  |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None


try:
    api_response = client.orchestration.Schedule.pause(schedule_rid)
    print("The pause response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**action** | ReplaceScheduleRequestAction |  |  |
**description** | Optional[str] |  | [optional] |
**display_name** | Optional[str] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**scope_mode** | Optional[ReplaceScheduleRequestScopeMode] |  | [optional] |
**trigger** | Optional[Trigger] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.  | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# ReplaceScheduleRequestAction
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
# Optional[ReplaceScheduleRequestScopeMode]
scope_mode = {"type": "user"}
# Optional[Trigger] | The schedule trigger. If the requesting user does not have permission to see the trigger, this will be empty.
trigger = {"type": "time", "cronExpression": "0 0 * * *", "timeZone": "UTC"}


try:
    api_response = client.orchestration.Schedule.replace(
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
except foundry_sdk.PalantirRPCException as e:
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

### Return type
**ScheduleRun**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None


try:
    api_response = client.orchestration.Schedule.run(schedule_rid)
    print("The run response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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

### Return type
**ListRunsOfScheduleResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    for schedule in client.orchestration.Schedule.runs(
        schedule_rid, page_size=page_size, page_token=page_token
    ):
        pprint(schedule)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Schedule.runs: %s\n" % e)

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

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleRid
schedule_rid = None


try:
    api_response = client.orchestration.Schedule.unpause(schedule_rid)
    print("The unpause response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Schedule.unpause: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

