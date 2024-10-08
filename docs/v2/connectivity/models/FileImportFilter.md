# FileImportFilter

[Filters](/docs/foundry/data-connection/file-based-syncs/#filters) allow you to filter source files
before they are imported into Foundry.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
FileImportCustomFilter | customFilter
FileLastModifiedAfterFilter | lastModifiedAfterFilter
FilePathMatchesFilter | pathMatchesFilter
FileSizeFilter | fileSizeFilter


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
