# Build

Method | HTTP request |
------------- | ------------- |
[**cancel**](#cancel) | **POST** /v2/orchestration/builds/{buildRid}/cancel |
[**create**](#create) | **POST** /v2/orchestration/builds/create |
[**get**](#get) | **GET** /v2/orchestration/builds/{buildRid} |

# **cancel**
Request a cancellation for all unfinished jobs in a build. The build's status will not update immediately. This endpoint is asynchronous and a success response indicates that the cancellation request has been acknowledged and the build is expected to be canceled soon. If the build has already finished or finishes shortly after the request and before the cancellation, the build will not change.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**build_rid** | BuildRid | buildRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

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

# BuildRid | buildRid
build_rid = "ri.foundry.main.build.a4386b7e-d546-49be-8a36-eefc355f5c58"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Build.cancel(
        build_rid,
        preview=preview,
    )
    print("The cancel response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Build.cancel: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**fallback_branches** | FallbackBranches |  |  |
**target** | BuildTargetDict | The targets of the schedule. |  |
**abort_on_failure** | Optional[AbortOnFailure] |  | [optional] |
**branch_name** | Optional[BranchName] | The target branch the build should run on. | [optional] |
**force_build** | Optional[ForceBuild] |  | [optional] |
**notifications_enabled** | Optional[NotificationsEnabled] | The notification will be sent to the user that has most recently edited the schedule. No notification will be sent if the schedule has `scopeMode` set to `ProjectScope`. | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**retry_backoff_duration** | Optional[RetryBackoffDurationDict] |  | [optional] |
**retry_count** | Optional[RetryCount] | The number of retry attempts for failed jobs. | [optional] |

### Return type
**Build**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# FallbackBranches |
fallback_branches = ["master"]
# BuildTargetDict | The targets of the schedule.
target = None
# Optional[AbortOnFailure] |
abort_on_failure = False
# Optional[BranchName] | The target branch the build should run on.
branch_name = "master"
# Optional[ForceBuild] |
force_build = None
# Optional[NotificationsEnabled] | The notification will be sent to the user that has most recently edited the schedule. No notification will be sent if the schedule has `scopeMode` set to `ProjectScope`.
notifications_enabled = None
# Optional[PreviewMode] | preview
preview = None
# Optional[RetryBackoffDurationDict] |
retry_backoff_duration = {"unit": "SECONDS", "value": 30}
# Optional[RetryCount] | The number of retry attempts for failed jobs.
retry_count = 1


try:
    api_response = foundry_client.orchestration.Build.create(
        fallback_branches=fallback_branches,
        target=target,
        abort_on_failure=abort_on_failure,
        branch_name=branch_name,
        force_build=force_build,
        notifications_enabled=notifications_enabled,
        preview=preview,
        retry_backoff_duration=retry_backoff_duration,
        retry_count=retry_count,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Build.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Build  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Build with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**build_rid** | BuildRid | buildRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Build**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# BuildRid | buildRid
build_rid = "ri.foundry.main.build.a4386b7e-d546-49be-8a36-eefc355f5c58"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Build.get(
        build_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Build.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Build  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

