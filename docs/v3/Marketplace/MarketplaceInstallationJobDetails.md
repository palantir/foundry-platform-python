# MarketplaceInstallationJobDetails

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v3/platform/marketplaceInstallationJobs/{marketplaceInstallationJobRid}/details | Public Beta |

# **get**
Get available validation results and failure diagnostics for an installation job or draft. Use the
installation job's `status` to track its progress and outcome. These details can help explain why a draft or
job has not progressed or completed as expected.

Draft owners receive full validation errors. Other authorized viewers receive a validation summary instead.
Failed and aborted jobs return HTTP 200 with their available diagnostics. An explicit abort or a
validation-only submission rejection may have no failure diagnostics.
The job remains queryable under the same RID after its draft is submitted, subject to retention and access.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marketplace_installation_job_rid** | MarketplaceInstallationJobRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**MarketplaceInstallationJobDetails**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarketplaceInstallationJobRid
marketplace_installation_job_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.marketplace.MarketplaceInstallationJob.Details.get(
        marketplace_installation_job_rid, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Details.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:marketplace-installation-job-details:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MarketplaceInstallationJobDetails  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

