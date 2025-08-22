# Connection

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/connectivity/connections | Private Beta |
[**get**](#get) | **GET** /v2/connectivity/connections/{connectionRid} | Public Beta |
[**get_configuration**](#get_configuration) | **GET** /v2/connectivity/connections/{connectionRid}/getConfiguration | Public Beta |
[**update_export_settings**](#update_export_settings) | **POST** /v2/connectivity/connections/{connectionRid}/updateExportSettings | Private Beta |
[**update_secrets**](#update_secrets) | **POST** /v2/connectivity/connections/{connectionRid}/updateSecrets | Stable |
[**upload_custom_jdbc_drivers**](#upload_custom_jdbc_drivers) | **POST** /v2/connectivity/connections/{connectionRid}/uploadCustomJdbcDrivers | Public Beta |

# **create**
Creates a new Connection with a [direct connection](https://palantir.com/docs/foundry/data-connection/core-concepts/#direct-connection) runtime.

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
**configuration** | CreateConnectionRequestConnectionConfiguration |  |  |
**display_name** | ConnectionDisplayName | The display name of the Connection. The display name must not be blank. |  |
**parent_folder_rid** | FolderRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Connection**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# CreateConnectionRequestConnectionConfiguration
configuration = {
    "type": "jdbc",
    "url": "jdbc:postgresql://localhost:5432/test",
    "driverClass": "org.postgresql.Driver",
}
# ConnectionDisplayName | The display name of the Connection. The display name must not be blank.
display_name = "Connection to my external system"
# FolderRid
parent_folder_rid = "ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.connectivity.Connection.create(
        configuration=configuration,
        display_name=display_name,
        parent_folder_rid=parent_folder_rid,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Connection.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Connection  | The created Connection | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Connection with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Connection**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.connectivity.Connection.get(connection_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Connection.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Connection  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_configuration**
Retrieves the ConnectionConfiguration of the [Connection](https://palantir.com/docs/foundry/data-connection/set-up-source/) itself.
This operation is intended for use when other Connection data is not required, providing a lighter-weight alternative to `getConnection` operation.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ConnectionConfiguration**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.connectivity.Connection.get_configuration(connection_rid, preview=preview)
    print("The get_configuration response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Connection.get_configuration: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ConnectionConfiguration  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **update_export_settings**
Updates the [export settings on the Connection.](https://palantir.com/docs/foundry/data-connection/export-overview/#enable-exports-for-source)
Only users with Information Security Officer role can modify the export settings.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid |  |  |
**export_settings** | ConnectionExportSettings |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# ConnectionExportSettings
export_settings = {"exportsEnabled": True, "exportEnabledWithoutMarkingsValidation": False}
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.connectivity.Connection.update_export_settings(
        connection_rid, export_settings=export_settings, preview=preview
    )
    print("The update_export_settings response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Connection.update_export_settings: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

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
**connection_rid** | ConnectionRid |  |  |
**secrets** | Dict[SecretName, PlaintextValue] | The secrets to be updated. The specified secret names must already be configured on the connection.  |  |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# Dict[SecretName, PlaintextValue] | The secrets to be updated. The specified secret names must already be configured on the connection.
secrets = {"Password": "MySecretPassword"}


try:
    api_response = client.connectivity.Connection.update_secrets(connection_rid, secrets=secrets)
    print("The update_secrets response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Connection.update_secrets: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload_custom_jdbc_drivers**
Upload custom jdbc drivers to an existing JDBC connection.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid |  |  |
**body** | bytes | Body of the request |  |
**file_name** | str | The file name of the uploaded JDBC driver. Must end with .jar  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Connection**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# bytes | Body of the request
body = None
# str | The file name of the uploaded JDBC driver. Must end with .jar
file_name = "cdata.jdbc.oracle.jar"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.connectivity.Connection.upload_custom_jdbc_drivers(
        connection_rid, body, file_name=file_name, preview=preview
    )
    print("The upload_custom_jdbc_drivers response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Connection.upload_custom_jdbc_drivers: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Connection  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

