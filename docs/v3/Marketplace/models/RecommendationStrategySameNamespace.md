# RecommendationStrategySameNamespace

Consider visible installations outside the trash in the targets' namespace. Multiple matches for one linked product are ambiguous, even if only one has a compatible version.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**suffix_filter** | Optional[str] | No | Include only installations whose titles end with ` - ` followed by this suffix. The separator is added automatically. If omitted, do not filter by title. |
**type** | Literal["sameNamespace"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
