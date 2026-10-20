# MarketplaceInstallationInputs

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v3/platform/marketplaceInstallations/{marketplaceInstallationRid}/inputs | Public Beta |

# **get**
Get the current fulfilled input values and explicit unset inputs of an installation.

By default, only manually fulfilled inputs are returned. Set `selection` to `ALL` to return fulfilled inputs
from every stored source. Explicitly unset inputs are returned regardless of `selection`.

Optional inputs with neither a value nor an explicit unset are omitted.

Returned values may use a different supported representation from the value originally provided.

Credential values expose secret names only, never plaintext, and cannot be submitted to another installation job.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marketplace_installation_rid** | MarketplaceInstallationRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |
**selection** | Optional[InstallationInputSelection] |  | [optional] |

### Return type
**MarketplaceInstallationInputs**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarketplaceInstallationRid
marketplace_installation_rid = None
# Optional[PreviewMode]
preview = None
# Optional[InstallationInputSelection]
selection = None


try:
    api_response = client.marketplace.MarketplaceInstallation.Inputs.get(
        marketplace_installation_rid, preview=preview, selection=selection
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Inputs.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:marketplace-installation-inputs:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MarketplaceInstallationInputs  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

