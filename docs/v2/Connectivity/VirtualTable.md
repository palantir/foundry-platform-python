# VirtualTable

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/connectivity/connections/{connectionRid}/virtualTables | Stable |

# **create**
Creates a new [Virtual Table](https://palantir.com/docs/foundry/data-integration/virtual-tables/) from an upstream table. The VirtualTable will be created
in the specified parent folder and can be queried through Foundry's data access APIs.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid |  |  |
**config** | VirtualTableConfig |  |  |
**name** | TableName |  |  |
**parent_rid** | FolderRid |  |  |
**markings** | Optional[List[MarkingId]] |  | [optional] |

### Return type
**VirtualTable**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# VirtualTableConfig
config = None
# TableName
name = "my_table"
# FolderRid
parent_rid = "ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791"
# Optional[List[MarkingId]]
markings = ["18212f9a-0e63-4b79-96a0-aae04df23336"]


try:
    api_response = client.connectivity.Connection.VirtualTable.create(
        connection_rid, config=config, name=name, parent_rid=parent_rid, markings=markings
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling VirtualTable.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | VirtualTable  | The created VirtualTable | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

