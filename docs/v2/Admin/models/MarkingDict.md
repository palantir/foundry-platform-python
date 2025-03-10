# MarkingDict

Marking

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | core_models.MarkingId | Yes |  |
**categoryId** | MarkingCategoryId | Yes |  |
**name** | MarkingName | Yes |  |
**description** | typing_extensions.NotRequired[str] | No |  |
**organization** | typing_extensions.NotRequired[core_models.OrganizationRid] | No | If this marking is associated with an Organization, its RID will be populated here.  |
**createdTime** | core_models.CreatedTime | Yes |  |
**createdBy** | typing_extensions.NotRequired[core_models.CreatedBy] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
