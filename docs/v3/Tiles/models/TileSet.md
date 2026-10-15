# TileSet

A servable set of tiles for a source, grouping tiles that share a format and layout.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | TileFormat | Yes | The encoding of the tiles in this set, which also determines the type of tiles the set serves. |
**max_zoom** | int | Yes | The highest zoom level served by this tile set, inclusive. |
**min_zoom** | int | Yes | The lowest zoom level served by this tile set, inclusive. |
**tiling_scheme** | TilingScheme | Yes |  |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
