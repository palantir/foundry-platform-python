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
**schedule_version_rid** | ScheduleVersionRid | The RID of a schedule version |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ScheduleVersion**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleVersionRid | The RID of a schedule version
schedule_version_rid = "ri.scheduler.main.schedule-version.4d1eb55f-6c13-411c-a911-5d84e08d8017"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.orchestration.ScheduleVersion.get(
        schedule_version_rid, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**schedule_version_rid** | ScheduleVersionRid | The RID of a schedule version |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Optional[Schedule]**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ScheduleVersionRid | The RID of a schedule version
schedule_version_rid = "ri.scheduler.main.schedule-version.4d1eb55f-6c13-411c-a911-5d84e08d8017"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.orchestration.ScheduleVersion.schedule(
        schedule_version_rid, preview=preview
    )
    print("The schedule response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling ScheduleVersion.schedule: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Optional[Schedule]  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

