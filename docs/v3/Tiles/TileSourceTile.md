# TileSourceTile

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v3/media/tileSources/{tileSourceId}/tiles/{z}/{x}/{y} | Private Beta |

# **get**
Get a tile from a tile source.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**tile_source_id** | TileSourceId |  |  |
**z** | int |  |  |
**x** | int |  |  |
**y** | int |  |  |
**format** | Optional[TileFormat] |  | [optional] |
**preview** | Optional[PreviewMode] |  | [optional] |
**tiling_scheme** | Optional[TilingScheme] |  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TileSourceId
tile_source_id = None
# int
z = None
# int
x = None
# int
y = None
# Optional[TileFormat]
format = None
# Optional[PreviewMode]
preview = None
# Optional[TilingScheme]
tiling_scheme = None


try:
    api_response = client.tiles.TileSource.Tile.get(
        tile_source_id, z, x, y, format=format, preview=preview, tiling_scheme=tiling_scheme
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Tile.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:tile-source-tile:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

