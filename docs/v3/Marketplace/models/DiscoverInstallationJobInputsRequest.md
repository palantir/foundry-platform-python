# DiscoverInstallationJobInputsRequest

DiscoverInstallationJobInputsRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**installations** | List[InstallationTarget] | Yes | Between 1 and 10 distinct installations, with at most one installation per product. Targets must share a namespace and marketplace and have at most one resulting ontology after applying overrides. |
**recommendations** | List[RecommendationStrategy] | Yes | An empty list disables recommendations from installations outside the requested targets. Targets in this request may still supply inputs to one another. |
**source_filter** | Optional[SourceFilter] | No | When supplied, excludes an input if any of its available sources appears in `excludedSources`. If omitted, returns only inputs whose sole available source is `MANUAL`. Inputs with no available source are always omitted. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
