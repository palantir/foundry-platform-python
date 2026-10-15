# TileSource

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**compute_elevation**](#compute_elevation) | **POST** /v3/platform/tileSources/{tileSourceId}/computeElevation | Private Beta |
[**get**](#get) | **GET** /v3/platform/tileSources/{tileSourceId} | Private Beta |
[**list**](#list) | **GET** /v3/platform/tileSources | Private Beta |

# **compute_elevation**
Compute ground elevation at one or more points using this tile source. Results are returned in
the same order as the requested points. Returns a not-found error if the source does not exist
or the token cannot access it.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**tile_source_id** | TileSourceId |  |  |
**points** | List[Position] | The points to compute elevation for. Results are returned in the same order as the request. A request may contain at most 1,000 points by default, though the configured limit may differ; exceeding it returns a `MaxElevationPointCountExceeded` error that reports the limit. |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**ComputeElevationResponse**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TileSourceId
tile_source_id = None
# List[Position] | The points to compute elevation for. Results are returned in the same order as the request. A request may contain at most 1,000 points by default, though the configured limit may differ; exceeding it returns a `MaxElevationPointCountExceeded` error that reports the limit.
points = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.tiles.TileSource.compute_elevation(
        tile_source_id, points=points, preview=preview
    )
    print("The compute_elevation response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling TileSource.compute_elevation: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:tile-source:read:compute-elevation]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ComputeElevationResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get**
Get metadata for a single tile source, including its tile sets. Returns a not-found error if
the source does not exist or the token cannot access it.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**tile_source_id** | TileSourceId |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**TileSource**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TileSourceId
tile_source_id = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.tiles.TileSource.get(tile_source_id, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling TileSource.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:tile-source:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TileSource  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **list**
List the tile sources accessible by the token.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**capability** | Optional[Capability] |  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**ListTileSourcesResponse**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[Capability]
capability = None
# Optional[PageSize]
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode]
preview = None


try:
    for tile_source in client.tiles.TileSource.list(
        capability=capability, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(tile_source)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling TileSource.list: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:tile-source:read:list]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListTileSourcesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

