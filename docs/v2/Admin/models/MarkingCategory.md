# MarkingCategory

MarkingCategory

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | MarkingCategoryId | Yes |  |
**name** | MarkingCategoryName | Yes |  |
**description** | MarkingCategoryDescription | Yes |  |
**category_type** | MarkingCategoryType | Yes |  |
**marking_type** | MarkingType | Yes |  |
**priority** | Optional[Long] | No | The priority, only used on CBAC categories. Higher numbers mean higher priority. |
**markings** | List[MarkingId] | Yes |  |
**deleted** | MarkingCategoryDeleted | Yes | Whether the Marking Category has been deleted. |
**created_time** | CreatedTime | Yes |  |
**created_by** | Optional[CreatedBy] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
