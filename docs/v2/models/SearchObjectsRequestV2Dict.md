# SearchObjectsRequestV2Dict

SearchObjectsRequestV2

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**where** | NotRequired[SearchJsonQueryV2Dict] | No |  |
**orderBy** | NotRequired[SearchOrderByV2Dict] | No |  |
**pageSize** | NotRequired[PageSize] | No |  |
**pageToken** | NotRequired[PageToken] | No |  |
**select** | List[PropertyApiName] | Yes | The API names of the object type properties to include in the response.  |
**excludeRid** | NotRequired[StrictBool] | No | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
