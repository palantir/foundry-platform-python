# ComputeElevationRequest

A request to compute elevation at a list of points.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**points** | List[Position] | Yes | The points to compute elevation for. Results are returned in the same order as the request. A request may contain at most 1,000 points by default, though the configured limit may differ; exceeding it returns a `MaxElevationPointCountExceeded` error that reports the limit. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
