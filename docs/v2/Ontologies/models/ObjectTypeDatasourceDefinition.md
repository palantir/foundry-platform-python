# ObjectTypeDatasourceDefinition

The definition of an object type datasource, identifying the kind of Foundry resource that backs the object
type.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ObjectTypeTimeSeriesDatasource | timeSeries
ObjectTypeUnsupportedDatasource | unsupported
ObjectTypeRestrictedViewDatasource | restrictedView
ObjectTypeStreamDatasource | stream
ObjectTypeMediaSetViewDatasource | mediaSetView
ObjectTypeDirectDatasource | direct
ObjectTypeGeotimeSeriesDatasource | geotimeSeries
ObjectTypeEditsOnlyDatasource | editsOnly
ObjectTypeDatasetDatasource | dataset
ObjectTypeTableDatasource | table


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
