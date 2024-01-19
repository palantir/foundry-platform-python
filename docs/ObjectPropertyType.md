# ObjectPropertyType

A union of all the types supported by Ontology Object properties.

This is a discriminator class and does not contain any additional fields. Instead, it
is a union of of the classes listed below.

This discriminator class uses the `type` field to differentiate between classes.

Class | Value
------------ | -------------
[OntologyObjectArrayType](OntologyObjectArrayType.md) | array
[AttachmentType](AttachmentType.md) | attachment
[BooleanType](BooleanType.md) | boolean
[ByteType](ByteType.md) | byte
[DateType](DateType.md) | date
[DecimalType](DecimalType.md) | decimal
[DoubleType](DoubleType.md) | double
[FloatType](FloatType.md) | float
[GeoPointType](GeoPointType.md) | geopoint
[GeoShapeType](GeoShapeType.md) | geoshape
[IntegerType](IntegerType.md) | integer
[LongType](LongType.md) | long
[ShortType](ShortType.md) | short
[StringType](StringType.md) | string
[TimeseriesType](TimeseriesType.md) | timeseries
[TimestampType](TimestampType.md) | timestamp

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
