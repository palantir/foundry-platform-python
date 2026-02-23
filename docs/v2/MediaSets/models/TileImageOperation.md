# TileImageOperation

Generates Slippy map tiles (EPSG 3857) from a geo-embedded image.
Only supported for geo-embedded TIFF and NITF images with at most 100M square pixels.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**zoom** | int | Yes | The zoom level of the tile. |
**x** | int | Yes | The x coordinate of the tile. |
**y** | int | Yes | The y coordinate of the tile. |
**type** | Literal["tile"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
