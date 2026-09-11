# EndpointSetEndpoint

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v3/platform/endpointSets/{endpointSetRid}/endpoints/{endpointRid} | Private Beta |
[**list**](#list) | **GET** /v3/platform/endpointSets/{endpointSetRid}/endpoints | Private Beta |

# **get**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**endpoint_set_rid** | EndpointSetRid |  |  |
**endpoint_rid** | EndpointSetEndpointRid |  |  |

### Return type
**EndpointSetEndpoint**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# EndpointSetRid
endpoint_set_rid = None
# EndpointSetEndpointRid
endpoint_rid = None


try:
    api_response = client.endpoints.EndpointSet.Endpoint.get(endpoint_set_rid, endpoint_rid)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Endpoint.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EndpointSetEndpoint  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)
# **list**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**endpoint_set_rid** | EndpointSetRid |  |  |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListEndpointSetEndpointsResponse**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# EndpointSetRid
endpoint_set_rid = None
# Optional[PageSize]
page_size = None
# Optional[PageToken]
page_token = None


try:
    for endpoint_set_endpoint in client.endpoints.EndpointSet.Endpoint.list(
        endpoint_set_rid, page_size=page_size, page_token=page_token
    ):
        pprint(endpoint_set_endpoint)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Endpoint.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListEndpointSetEndpointsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)
