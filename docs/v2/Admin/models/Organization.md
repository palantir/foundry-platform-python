# Organization

Organization

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | core_models.OrganizationRid | Yes |  |
**name** | OrganizationName | Yes |  |
**description** | typing.Optional[str] | No |  |
**marking_id** | core_models.MarkingId | Yes | The ID of this Organization's underlying marking. Organization guest access can be managed by updating the membership of this Marking.  |
**host** | typing.Optional[HostName] | No | The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
