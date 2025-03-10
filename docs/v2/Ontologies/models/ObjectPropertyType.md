# ObjectPropertyType

A union of all the types supported by Ontology Object properties.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
core_models.DateType | date
StructType | struct
core_models.StringType | string
core_models.ByteType | byte
core_models.DoubleType | double
core_models.GeoPointType | geopoint
core_models.GeotimeSeriesReferenceType | geotimeSeriesReference
core_models.IntegerType | integer
core_models.FloatType | float
core_models.GeoShapeType | geoshape
core_models.LongType | long
core_models.BooleanType | boolean
core_models.CipherTextType | cipherText
core_models.MarkingType | marking
core_models.AttachmentType | attachment
core_models.MediaReferenceType | mediaReference
core_models.TimeseriesType | timeseries
OntologyObjectArrayType | array
core_models.ShortType | short
core_models.VectorType | vector
core_models.DecimalType | decimal
core_models.TimestampType | timestamp


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
