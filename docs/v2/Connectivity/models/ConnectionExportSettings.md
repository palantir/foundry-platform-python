# ConnectionExportSettings

The [export settings of a Connection](https://palantir.com/docs/foundry/data-connection/export-overview/#enable-exports-for-source).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**exports_enabled** | bool | Yes | Allow exporting datasets from Foundry to this Connection.  |
**export_enabled_without_markings_validation** | bool | Yes | In certain interactive workflows the Connection can be used in, it is not currently possible to validate the  security markings of the data being exported.  By enabling exports without markings validation, you acknowledge that you are responsible for ensuring  that the data being exported is compliant with your organization's policies.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
