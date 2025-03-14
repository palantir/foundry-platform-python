# OrganizationDict

Organization

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**name** | str | Yes |  |
**description** | NotRequired[str] | No |  |
**markingId** | UUID | Yes | The ID of this Organization's underlying marking. Organization guest access can be managed by updating the membership of this Marking.  |
**host** | NotRequired[HostName] | No | The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
