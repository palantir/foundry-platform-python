# Schedule

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/orchestration/schedules/{scheduleRid} |

# **get**
Get the Schedule

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**schedule_rid** | ScheduleRid | scheduleRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Schedule**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
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

See [README](../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Schedule  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

