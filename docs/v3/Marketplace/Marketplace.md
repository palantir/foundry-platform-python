# Marketplace

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v3/platform/marketplaces/{marketplaceRid} | Private Beta |

# **get**
Get a local or remote Marketplace store by its RID, including its current display metadata.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marketplace_rid** | MarketplaceRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**Marketplace**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarketplaceRid
marketplace_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.marketplace.Marketplace.get(marketplace_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Marketplace.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:marketplace:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Marketplace  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

