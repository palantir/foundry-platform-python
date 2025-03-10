# Build

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**cancel**](#cancel) | **POST** /v2/orchestration/builds/{buildRid}/cancel | Public Beta |
[**create**](#create) | **POST** /v2/orchestration/builds/create | Public Beta |
[**get**](#get) | **GET** /v2/orchestration/builds/{buildRid} | Public Beta |
[**get_batch**](#get_batch) | **POST** /v2/orchestration/builds/getBatch | Public Beta |
[**search**](#search) | **POST** /v2/orchestration/builds/search | Private Beta |

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
**target** | Union[BuildTarget, BuildTargetDict] | The targets of the schedule. |  |
**abort_on_failure** | Optional[AbortOnFailure] |  | [optional] |
**branch_name** | Optional[BranchName] | The target branch the build should run on. | [optional] |
**force_build** | Optional[ForceBuild] |  | [optional] |
**notifications_enabled** | Optional[NotificationsEnabled] | The notification will be sent to the user that has most recently edited the schedule. No notification will be sent if the schedule has `scopeMode` set to `ProjectScope`. | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**retry_backoff_duration** | Optional[Union[RetryBackoffDuration, RetryBackoffDurationDict]] |  | [optional] |
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
# Union[BuildTarget, BuildTargetDict] | The targets of the schedule.
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
# Optional[Union[RetryBackoffDuration, RetryBackoffDurationDict]] |
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

# **get_batch**
Execute multiple get requests on Build.

The maximum batch size for this endpoint is 100.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | typing_extensions.Annotated[List[Union[GetBuildsBatchRequestElement, GetBuildsBatchRequestElementDict]], annotated_types.Len(min_length=1, max_length=100)] | Body of the request |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**GetBuildsBatchResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# typing_extensions.Annotated[List[Union[GetBuildsBatchRequestElement, GetBuildsBatchRequestElementDict]], annotated_types.Len(min_length=1, max_length=100)] | Body of the request
body = [{"buildRid": "ri.foundry.main.build.a4386b7e-d546-49be-8a36-eefc355f5c58"}]
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Build.get_batch(
        body,
        preview=preview,
    )
    print("The get_batch response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Build.get_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetBuildsBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**
Search for Builds.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**where** | Union[SearchBuildsFilter, SearchBuildsFilterDict] |  |  |
**order_by** | Optional[Union[SearchBuildsOrderBy, SearchBuildsOrderByDict]] |  | [optional] |
**page_size** | Optional[PageSize] | The page size for the search request. If no value is provided, a default of `100` will be used.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**SearchBuildsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[SearchBuildsFilter, SearchBuildsFilterDict] |
where = None
# Optional[Union[SearchBuildsOrderBy, SearchBuildsOrderByDict]] |
order_by = {"fields": [{"field": "STARTED_TIME", "direction": "ASC"}]}
# Optional[PageSize] | The page size for the search request. If no value is provided, a default of `100` will be used.
page_size = 100
# Optional[PageToken] |
page_token = "v1.QnVpbGQgdGhlIEZ1dHVyZTogaHR0cHM6Ly93d3cucGFsYW50aXIuY29tL2NhcmVlcnMvP2xldmVyLXNvdXJjZSU1YiU1ZD1BUElEb2NzI29wZW4tcG9zaXRpb25z"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Build.search(
        where=where,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The search response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Build.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchBuildsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

