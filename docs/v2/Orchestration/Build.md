# Build

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**cancel**](#cancel) | **POST** /v2/orchestration/builds/{buildRid}/cancel | Stable |
[**create**](#create) | **POST** /v2/orchestration/builds/create | Stable |
[**get**](#get) | **GET** /v2/orchestration/builds/{buildRid} | Stable |
[**get_batch**](#get_batch) | **POST** /v2/orchestration/builds/getBatch | Stable |
[**jobs**](#jobs) | **GET** /v2/orchestration/builds/{buildRid}/jobs | Stable |
[**search**](#search) | **POST** /v2/orchestration/builds/search | Private Beta |

# **cancel**
Request a cancellation for all unfinished jobs in a build. The build's status will not update immediately. This endpoint is asynchronous and a success response indicates that the cancellation request has been acknowledged and the build is expected to be canceled soon. If the build has already finished or finishes shortly after the request and before the cancellation, the build will not change.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**build_rid** | BuildRid | The RID of a Build. |  |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# BuildRid | The RID of a Build.
build_rid = "ri.foundry.main.build.a4386b7e-d546-49be-8a36-eefc355f5c58"


try:
    api_response = client.orchestration.Build.cancel(build_rid)
    print("The cancel response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**target** | BuildTarget | The targets of the schedule. |  |
**abort_on_failure** | Optional[AbortOnFailure] |  | [optional] |
**branch_name** | Optional[BranchName] | The target branch the build should run on. | [optional] |
**force_build** | Optional[ForceBuild] |  | [optional] |
**notifications_enabled** | Optional[NotificationsEnabled] |  | [optional] |
**retry_backoff_duration** | Optional[RetryBackoffDuration] |  | [optional] |
**retry_count** | Optional[RetryCount] | The number of retry attempts for failed jobs. | [optional] |

### Return type
**Build**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# FallbackBranches
fallback_branches = []
# BuildTarget | The targets of the schedule.
target = {
    "type": "manual",
    "targetRids": [
        "ri.foundry.main.dataset.4263bdd9-d6bc-4244-9cca-893c1a2aef62",
        "ri.foundry.main.dataset.86939c1e-4256-41db-9fe7-e7ee9e0f752a",
    ],
}
# Optional[AbortOnFailure]
abort_on_failure = False
# Optional[BranchName] | The target branch the build should run on.
branch_name = "master"
# Optional[ForceBuild]
force_build = None
# Optional[NotificationsEnabled]
notifications_enabled = None
# Optional[RetryBackoffDuration]
retry_backoff_duration = {"unit": "SECONDS", "value": 30}
# Optional[RetryCount] | The number of retry attempts for failed jobs.
retry_count = 1


try:
    api_response = client.orchestration.Build.create(
        fallback_branches=fallback_branches,
        target=target,
        abort_on_failure=abort_on_failure,
        branch_name=branch_name,
        force_build=force_build,
        notifications_enabled=notifications_enabled,
        retry_backoff_duration=retry_backoff_duration,
        retry_count=retry_count,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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

Users are allowed to make a maximum of **4 requests per second** and **25 concurrent requests**.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**build_rid** | BuildRid | The RID of a Build. |  |

### Return type
**Build**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# BuildRid | The RID of a Build.
build_rid = "ri.foundry.main.build.a4386b7e-d546-49be-8a36-eefc355f5c58"


try:
    api_response = client.orchestration.Build.get(build_rid)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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

Users are allowed to make a maximum of **4 requests per second** and **25 concurrent requests**.


The maximum batch size for this endpoint is 100.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetBuildsBatchRequestElement] | Body of the request |  |

### Return type
**GetBuildsBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetBuildsBatchRequestElement] | Body of the request
body = [{"buildRid": "ri.foundry.main.build.a4386b7e-d546-49be-8a36-eefc355f5c58"}]


try:
    api_response = client.orchestration.Build.get_batch(body)
    print("The get_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Build.get_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetBuildsBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **jobs**
Get the Jobs in the Build.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**build_rid** | BuildRid | The RID of a Build. |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |

### Return type
**ListJobsOfBuildResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# BuildRid | The RID of a Build.
build_rid = "ri.foundry.main.build.a4386b7e-d546-49be-8a36-eefc355f5c58"
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    for build in client.orchestration.Build.jobs(
        build_rid, page_size=page_size, page_token=page_token
    ):
        pprint(build)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Build.jobs: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListJobsOfBuildResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**
Search for Builds.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**where** | SearchBuildsFilter |  |  |
**order_by** | Optional[SearchBuildsOrderBy] |  | [optional] |
**page_size** | Optional[PageSize] | The page size for the search request. If no value is provided, a default of `100` will be used.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**SearchBuildsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SearchBuildsFilter
where = None
# Optional[SearchBuildsOrderBy]
order_by = {"fields": [{"field": "STARTED_TIME", "direction": "ASC"}]}
# Optional[PageSize] | The page size for the search request. If no value is provided, a default of `100` will be used.
page_size = 100
# Optional[PageToken]
page_token = "v1.QnVpbGQgdGhlIEZ1dHVyZTogaHR0cHM6Ly93d3cucGFsYW50aXIuY29tL2NhcmVlcnMvP2xldmVyLXNvdXJjZSU1YiU1ZD1BUElEb2NzI29wZW4tcG9zaXRpb25z"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.orchestration.Build.search(
        where=where, order_by=order_by, page_size=page_size, page_token=page_token, preview=preview
    )
    print("The search response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Build.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchBuildsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

