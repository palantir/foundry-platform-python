# ThirdPartyApplication

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid} |

# **get**
Get the ThirdPartyApplication with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | thirdPartyApplicationRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ThirdPartyApplication**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ThirdPartyApplicationRid | thirdPartyApplicationRid
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.third_party_applications.ThirdPartyApplication.get(
        third_party_application_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling ThirdPartyApplication.get: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ThirdPartyApplication  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

