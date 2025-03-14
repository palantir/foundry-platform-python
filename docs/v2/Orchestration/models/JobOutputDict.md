# JobOutputDict

Other types of Job Outputs exist in Foundry. Currently, only Dataset and Media Set are supported by the API.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
DatasetJobOutputDict | datasetJobOutput
TransactionalMediaSetJobOutputDict | transactionalMediaSetJobOutput


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
