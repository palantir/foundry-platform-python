# CheckReport

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/dataHealth/checks/{checkRid}/checkReports/{checkReportRid} | Public Beta |
[**get_latest**](#get_latest) | **GET** /v2/dataHealth/checks/{checkRid}/checkReports/getLatest | Public Beta |

# **get**
Get the CheckReport with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**check_rid** | CheckRid |  |  |
**check_report_rid** | CheckReportRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**CheckReport**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# CheckRid
check_rid = "ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3"
# CheckReportRid
check_report_rid = "ri.data-health.main.check-report.a1b2c3d4-e5f6-7890-abcd-ef1234567890"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.data_health.Check.CheckReport.get(
        check_rid, check_report_rid, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling CheckReport.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CheckReport  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_latest**
Get the most recent check reports for this Check. Reports are returned
in reverse chronological order (most recent first).


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**check_rid** | CheckRid |  |  |
**limit** | Optional[CheckReportLimit] | The maximum number of check reports to return. Defaults to 10. Maximum allowed value is 100.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GetLatestCheckReportsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# CheckRid
check_rid = "ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3"
# Optional[CheckReportLimit] | The maximum number of check reports to return. Defaults to 10. Maximum allowed value is 100.
limit = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.data_health.Check.CheckReport.get_latest(
        check_rid, limit=limit, preview=preview
    )
    print("The get_latest response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling CheckReport.get_latest: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetLatestCheckReportsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

