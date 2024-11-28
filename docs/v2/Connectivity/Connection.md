# Connection

Method | HTTP request |
------------- | ------------- |
[**update_secrets**](#update_secrets) | **POST** /v2/connectivity/connections/{connectionRid}/updateSecrets |

Get the Connection with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Connection**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ConnectionRid | connectionRid
connection_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.get(
        connection_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Connection.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Connection  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **update_secrets**
Updates the secrets on the connection to the specified secret values.
Secrets that are currently configured on the connection but are omitted in the request will remain unchanged.

Secrets are transmitted over the network encrypted using TLS. Once the secrets reach Foundry's servers, 
they will be temporarily decrypted and remain in plaintext in memory to be processed as needed. 
They will stay in plaintext in memory until the garbage collection process cleans up the memory. 
The secrets are always stored encrypted on our servers.

By using this endpoint, you acknowledge and accept any potential risks associated with the temporary 
in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should 
use the Foundry UI instead.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**secrets** | Dict[SecretName, PlaintextValue] | The secrets to be updated. The specified secret names must already be configured on the connection.  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ConnectionRid | connectionRid
connection_rid = None
# Dict[SecretName, PlaintextValue] | The secrets to be updated. The specified secret names must already be configured on the connection.
secrets = {"Password": "MySecretPassword"}
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.update_secrets(
        connection_rid,
        secrets=secrets,
        preview=preview,
    )
    print("The update_secrets response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Connection.update_secrets: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

