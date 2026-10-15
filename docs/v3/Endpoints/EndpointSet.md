# EndpointSet

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v3/platform/endpointSets/{endpointSetRid} | Private Beta |

# **get**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**endpoint_set_rid** | EndpointSetRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**EndpointSet**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# EndpointSetRid
endpoint_set_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.endpoints.EndpointSet.get(endpoint_set_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling EndpointSet.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:endpoint-set:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EndpointSet  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

