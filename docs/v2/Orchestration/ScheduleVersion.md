# ScheduleVersion

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/orchestration/scheduleVersions/{scheduleVersionRid} | Public Beta |
[**schedule**](#schedule) | **GET** /v2/orchestration/scheduleVersions/{scheduleVersionRid}/schedule | Public Beta |

# **get**
Get the ScheduleVersion with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_version_rid** | ScheduleVersionRid | scheduleVersionRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ScheduleVersion**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleVersionRid | scheduleVersionRid
schedule_version_rid = "ri.scheduler.main.schedule-version.4d1eb55f-6c13-411c-a911-5d84e08d8017"
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.ScheduleVersion.get(
        schedule_version_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling ScheduleVersion.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ScheduleVersion  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **schedule**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_version_rid** | ScheduleVersionRid | scheduleVersionRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**typing.Optional[Schedule]**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ScheduleVersionRid | scheduleVersionRid
schedule_version_rid = "ri.scheduler.main.schedule-version.4d1eb55f-6c13-411c-a911-5d84e08d8017"
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.ScheduleVersion.schedule(
        schedule_version_rid,
        preview=preview,
    )
    print("The schedule response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling ScheduleVersion.schedule: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | typing.Optional[Schedule]  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

