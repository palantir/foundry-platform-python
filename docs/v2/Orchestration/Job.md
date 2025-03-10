# Job

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/orchestration/jobs/{jobRid} | Private Beta |

# **get**
Get the Job with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**job_rid** | core_models.JobRid | jobRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**Job**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# core_models.JobRid | jobRid
job_rid = "ri.foundry.main.job.aaf94076-d773-4732-a1df-3b638eb50448"
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.orchestration.Job.get(
        job_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Job.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Job  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

