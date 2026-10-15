# TileSource

A source of map data that the platform can serve, such as satellite imagery, vector map layers,
or elevation models. A source's capabilities indicate which operations it supports.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**attribution** | Optional[str] | No | Attribution text for the source's data, for example a data provider name or copyright notice. Empty when the source declares no attribution. |
**bounds** | Optional[BBox] | No | The geographic extent the source covers. Absent when the source has no bounded extent, such as a globally-defined or non-geolocated source. |
**capabilities** | List[Capability] | Yes |  |
**description** | Optional[str] | No | A human-readable description of the source. Empty when the source does not define one. |
**display_name** | str | Yes |  |
**id** | TileSourceId | Yes |  |
**tile_sets** | List[TileSet] | Yes | The servable tile sets for this source. Empty for sources that serve no tiles. |
**vertical_reference** | Optional[VerticalReference] | No | For elevation-capable sources, the vertical reference that elevations are measured against (`WGS84_ELLIPSOID`, `MEAN_SEA_LEVEL`, `UNKNOWN`). Absent for sources that do not provide elevation. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
