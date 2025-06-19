# DatabricksAuthenticationMode

The method of authentication for connecting to an external Databricks system.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
WorkflowIdentityFederation | workflowIdentityFederation
OauthMachineToMachineAuth | oauthM2M
PersonalAccessToken | personalAccessToken
BasicCredentials | basic


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
