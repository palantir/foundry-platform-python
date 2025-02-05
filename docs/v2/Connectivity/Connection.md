# Connection

Method | HTTP request |
------------- | ------------- |
[**update_secrets**](#update_secrets) | **POST** /v2/connectivity/connections/{connectionRid}/updateSecrets |

Creates a new Connection.
Any secrets specified in the request body are transmitted over the network encrypted using TLS. Once the
secrets reach Foundry's servers, they will be temporarily decrypted and remain in plaintext in memory to
be processed as needed. They will stay in plaintext in memory until the garbage collection process cleans
up the memory. The secrets are always stored encrypted on our servers.
By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
use the Foundry UI instead.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**configuration** | Union[CreateConnectionRequestConnectionConfiguration, CreateConnectionRequestConnectionConfigurationDict] |  |  |
**display_name** | ConnectionDisplayName | The display name of the Connection. The display name must not be blank. |  |
**parent_folder_rid** | FolderRid |  |  |
**runtime_platform** | Union[CreateConnectionRequestRuntimePlatform, CreateConnectionRequestRuntimePlatformDict] |  |  |
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

# Union[CreateConnectionRequestConnectionConfiguration, CreateConnectionRequestConnectionConfigurationDict] |
configuration = None
# ConnectionDisplayName | The display name of the Connection. The display name must not be blank.
display_name = "Connection to my external system"
# FolderRid |
parent_folder_rid = "ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791"
# Union[CreateConnectionRequestRuntimePlatform, CreateConnectionRequestRuntimePlatformDict] |
runtime_platform = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.create(
        configuration=configuration,
        display_name=display_name,
        parent_folder_rid=parent_folder_rid,
        runtime_platform=runtime_platform,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Connection.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Connection  | The created Connection | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

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

