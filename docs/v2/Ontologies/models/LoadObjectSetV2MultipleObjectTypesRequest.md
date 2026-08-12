# LoadObjectSetV2MultipleObjectTypesRequest

Represents the API POST body when loading an `ObjectSet`. Used on the `/loadObjectsMultipleObjectTypes` endpoint only.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**object_set** | ObjectSet | Yes |  |
**order_by** | Optional[SearchOrderByV2] | No |  |
**select** | List[SelectedPropertyApiName] | Yes |  |
**select_v2** | Optional[List[PropertyIdentifier]] | No | The identifiers of the properties to include in the response. Only selectV2 or select should be populated, but not both.  |
**default_load_level** | Optional[PropertyLoadLevel] | No |  |
**load_ontology_defined_derived_properties** | Optional[bool] | No | A flag to load ontology-defined derived properties (OTDPs) in the response. Defaults to true. Only applies when no explicit property selection (`select`/`selectV2`) is provided; when specific properties are selected, this flag has no effect and the selected properties are always returned.  This flag does not affect interface properties that are implemented by an OTDP on an object type; those are always returned regardless of this flag.  This feature is experimental and not yet generally available.  |
**page_token** | Optional[PageToken] | No |  |
**page_size** | Optional[PageSize] | No |  |
**exclude_rid** | Optional[bool] | No | A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  |
**load_property_securities** | Optional[bool] | No | A flag to load the securities for all properties. Setting this flag to true will return a list of securities in the `propertySecurities` field of the response. Returned objects will return all properties as Secured Property Values, which provide the property data as well an index into the `propertySecurities` list. This feature is experimental and not yet generally available.  |
**snapshot** | Optional[bool] | No | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.  |
**include_compute_usage** | Optional[IncludeComputeUsage] | No |  |
**reference_signing_options** | Optional[ReferenceSigningOptions] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
