# ComputeElevationResponse

The elevation results for a batch of requested points.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**elevations** | List[ElevationPointResult] | Yes | One result per requested point, in the same order as the request. |
**vertical_reference** | VerticalReference | Yes | The vertical reference all elevations in this response are measured against, taken from the tile source. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
