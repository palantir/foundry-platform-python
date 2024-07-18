# LoadObjectSetRequestV2Dict

Represents the API POST body when loading an `ObjectSet`.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**excludeRid** | NotRequired[StrictBool] | No | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  |
**objectSet** | ObjectSetDict | Yes |  |
**orderBy** | NotRequired[SearchOrderByV2Dict] | No |  |
**pageSize** | NotRequired[PageSize] | No |  |
**pageToken** | NotRequired[PageToken] | No |  |
**select** | List[SelectedPropertyApiName] | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
