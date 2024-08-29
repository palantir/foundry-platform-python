# Build

Method | HTTP request |
------------- | ------------- |
[**get**](#get) | **GET** /v2/orchestration/builds/{buildRid} |

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
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
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
except PalantirRPCException as e:
    print("HTTP error when calling Build.get: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Build  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)
