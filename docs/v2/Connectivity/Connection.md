# Connection

Method | HTTP request |
------------- | ------------- |

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

Updates the secrets on the connection to the specified secret values.
Secrets that are currently configured on the connection but are omitted in the request will remain unchanged.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**secrets** | Dict[SecretName, SecretValue] | The secrets to be updated. The specified secret names must already be configured on the connection.  |  |
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
# Dict[SecretName, SecretValue] | The secrets to be updated. The specified secret names must already be configured on the connection.
secrets = None
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

