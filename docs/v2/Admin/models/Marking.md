# Marking

Marking

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | MarkingId | Yes |  |
**category_id** | MarkingCategoryId | Yes |  |
**name** | MarkingName | Yes |  |
**description** | Optional[str] | No |  |
**organization** | Optional[OrganizationRid] | No | If this marking is associated with an Organization, its RID will be populated here.  |
**priority** | Optional[Long] | No | The priority, only used on CBAC markings. Higher numbers mean higher priority. |
**prominence** | Optional[MarkingProminence] | No | A hint on whether to emphasize or deemphasize the marking. Only used on CBAC markings. |
**deleted** | MarkingDeleted | Yes | Whether the Marking has been deleted. |
**created_time** | CreatedTime | Yes |  |
**created_by** | Optional[CreatedBy] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
