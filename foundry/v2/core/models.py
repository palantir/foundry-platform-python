#  Copyright 2024 Palantir Technologies, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from __future__ import annotations

import typing
from datetime import datetime

import pydantic
import typing_extensions

from foundry import _core as core


class AnyType(pydantic.BaseModel):
    """AnyType"""

    type: typing.Literal["any"] = "any"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AnyTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AnyTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class AnyTypeDict(typing_extensions.TypedDict):
    """AnyType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["any"]


class ArrayFieldType(pydantic.BaseModel):
    """ArrayFieldType"""

    items_schema: FieldSchema = pydantic.Field(alias=str("itemsSchema"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ArrayFieldTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ArrayFieldTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class ArrayFieldTypeDict(typing_extensions.TypedDict):
    """ArrayFieldType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    itemsSchema: FieldSchemaDict
    type: typing.Literal["array"]


class AttachmentType(pydantic.BaseModel):
    """AttachmentType"""

    type: typing.Literal["attachment"] = "attachment"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AttachmentTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AttachmentTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class AttachmentTypeDict(typing_extensions.TypedDict):
    """AttachmentType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["attachment"]


class BinaryType(pydantic.BaseModel):
    """BinaryType"""

    type: typing.Literal["binary"] = "binary"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BinaryTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(BinaryTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class BinaryTypeDict(typing_extensions.TypedDict):
    """BinaryType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["binary"]


class BooleanType(pydantic.BaseModel):
    """BooleanType"""

    type: typing.Literal["boolean"] = "boolean"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BooleanTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(BooleanTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class BooleanTypeDict(typing_extensions.TypedDict):
    """BooleanType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["boolean"]


BuildRid = core.RID
"""The RID of a Build."""


class ByteType(pydantic.BaseModel):
    """ByteType"""

    type: typing.Literal["byte"] = "byte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ByteTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ByteTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class ByteTypeDict(typing_extensions.TypedDict):
    """ByteType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["byte"]


class ChangeDataCaptureConfiguration(pydantic.BaseModel):
    """
    Configuration for utilizing the stream as a change data capture (CDC) dataset. To configure CDC on a stream, at
    least one key needs to be provided.

    For more information on CDC in
    Foundry, see the [Change Data Capture](/docs/foundry/data-integration/change-data-capture/) user documentation.
    """

    deletion_field_name: FieldName = pydantic.Field(alias=str("deletionFieldName"))  # type: ignore[literal-required]
    """The name of a boolean field in the schema that indicates whether or not a row has been deleted."""

    ordering_field_name: FieldName = pydantic.Field(alias=str("orderingFieldName"))  # type: ignore[literal-required]
    """
    The name of an ordering field that determines the newest state for a row in the dataset. 

    The ordering field can only be of the following types:
    - Byte
    - Date
    - Decimal
    - Integer
    - Long
    - Short
    - String
    - Timestamp
    """

    type: typing.Literal["fullRow"] = "fullRow"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ChangeDataCaptureConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ChangeDataCaptureConfigurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ChangeDataCaptureConfigurationDict(typing_extensions.TypedDict):
    """
    Configuration for utilizing the stream as a change data capture (CDC) dataset. To configure CDC on a stream, at
    least one key needs to be provided.

    For more information on CDC in
    Foundry, see the [Change Data Capture](/docs/foundry/data-integration/change-data-capture/) user documentation.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    deletionFieldName: FieldName
    """The name of a boolean field in the schema that indicates whether or not a row has been deleted."""

    orderingFieldName: FieldName
    """
    The name of an ordering field that determines the newest state for a row in the dataset. 

    The ordering field can only be of the following types:
    - Byte
    - Date
    - Decimal
    - Integer
    - Long
    - Short
    - String
    - Timestamp
    """

    type: typing.Literal["fullRow"]


class CipherTextType(pydantic.BaseModel):
    """CipherTextType"""

    default_cipher_channel: typing.Optional[core.RID] = pydantic.Field(alias=str("defaultCipherChannel"), default=None)  # type: ignore[literal-required]
    """An optional Cipher Channel RID which can be used for encryption updates to empty values."""

    type: typing.Literal["cipherText"] = "cipherText"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CipherTextTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(CipherTextTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class CipherTextTypeDict(typing_extensions.TypedDict):
    """CipherTextType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    defaultCipherChannel: typing_extensions.NotRequired[core.RID]
    """An optional Cipher Channel RID which can be used for encryption updates to empty values."""

    type: typing.Literal["cipherText"]


ContentLength = core.Long
"""ContentLength"""


ContentType = str
"""ContentType"""


CreatedBy = str
"""The Foundry user who created this resource"""


CreatedTime = datetime
"""The time at which the resource was created."""


CustomMetadata = typing.Dict[str, typing.Any]
"""CustomMetadata"""


class DateType(pydantic.BaseModel):
    """DateType"""

    type: typing.Literal["date"] = "date"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DateTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DateTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class DateTypeDict(typing_extensions.TypedDict):
    """DateType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["date"]


class DecimalType(pydantic.BaseModel):
    """DecimalType"""

    precision: typing.Optional[int] = None
    """The total number of digits of the Decimal type. The maximum value is 38."""

    scale: typing.Optional[int] = None
    """The number of digits to the right of the decimal point. The maximum value is 38."""

    type: typing.Literal["decimal"] = "decimal"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DecimalTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DecimalTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class DecimalTypeDict(typing_extensions.TypedDict):
    """DecimalType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    precision: typing_extensions.NotRequired[int]
    """The total number of digits of the Decimal type. The maximum value is 38."""

    scale: typing_extensions.NotRequired[int]
    """The number of digits to the right of the decimal point. The maximum value is 38."""

    type: typing.Literal["decimal"]


DisplayName = str
"""The display name of the entity."""


class Distance(pydantic.BaseModel):
    """A measurement of distance."""

    value: float
    unit: DistanceUnit
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DistanceDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DistanceDict, self.model_dump(by_alias=True, exclude_none=True))


class DistanceDict(typing_extensions.TypedDict):
    """A measurement of distance."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: float
    unit: DistanceUnit


DistanceUnit = typing.Literal[
    "MILLIMETERS",
    "CENTIMETERS",
    "METERS",
    "KILOMETERS",
    "INCHES",
    "FEET",
    "YARDS",
    "MILES",
    "NAUTICAL_MILES",
]
"""DistanceUnit"""


class DoubleType(pydantic.BaseModel):
    """DoubleType"""

    type: typing.Literal["double"] = "double"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DoubleTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DoubleTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class DoubleTypeDict(typing_extensions.TypedDict):
    """DoubleType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["double"]


class Duration(pydantic.BaseModel):
    """A measurement of duration."""

    value: int
    """The duration value."""

    unit: TimeUnit
    """The unit of duration."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DurationDict, self.model_dump(by_alias=True, exclude_none=True))


class DurationDict(typing_extensions.TypedDict):
    """A measurement of duration."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: int
    """The duration value."""

    unit: TimeUnit
    """The unit of duration."""


EmbeddingModel = typing_extensions.Annotated[
    typing.Union["LmsEmbeddingModel", "FoundryLiveDeployment"], pydantic.Field(discriminator="type")
]
"""EmbeddingModel"""


EmbeddingModelDict = typing_extensions.Annotated[
    typing.Union["LmsEmbeddingModelDict", "FoundryLiveDeploymentDict"],
    pydantic.Field(discriminator="type"),
]
"""EmbeddingModel"""


EnrollmentRid = core.RID
"""EnrollmentRid"""


class Field(pydantic.BaseModel):
    """
    A field in a Foundry schema. For more information on supported data types, see the
    [supported field types](/docs/foundry/data-integration/datasets/#supported-field-types) user documentation.
    """

    name: FieldName
    schema_: FieldSchema = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FieldDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FieldDict, self.model_dump(by_alias=True, exclude_none=True))


FieldDataType = typing_extensions.Annotated[
    typing.Union[
        "StructFieldType",
        "DateType",
        "StringType",
        "ByteType",
        "DoubleType",
        "IntegerType",
        "FloatType",
        "LongType",
        "BooleanType",
        "ArrayFieldType",
        "BinaryType",
        "ShortType",
        "DecimalType",
        "MapFieldType",
        "TimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
"""FieldDataType"""


FieldDataTypeDict = typing_extensions.Annotated[
    typing.Union[
        "StructFieldTypeDict",
        "DateTypeDict",
        "StringTypeDict",
        "ByteTypeDict",
        "DoubleTypeDict",
        "IntegerTypeDict",
        "FloatTypeDict",
        "LongTypeDict",
        "BooleanTypeDict",
        "ArrayFieldTypeDict",
        "BinaryTypeDict",
        "ShortTypeDict",
        "DecimalTypeDict",
        "MapFieldTypeDict",
        "TimestampTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""FieldDataType"""


class FieldDict(typing_extensions.TypedDict):
    """
    A field in a Foundry schema. For more information on supported data types, see the
    [supported field types](/docs/foundry/data-integration/datasets/#supported-field-types) user documentation.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: FieldName
    schema: FieldSchemaDict


FieldName = str
"""FieldName"""


class FieldSchema(pydantic.BaseModel):
    """The specification of the type of a Foundry schema field."""

    nullable: bool
    custom_metadata: typing.Optional[CustomMetadata] = pydantic.Field(alias=str("customMetadata"), default=None)  # type: ignore[literal-required]
    data_type: FieldDataType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FieldSchemaDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FieldSchemaDict, self.model_dump(by_alias=True, exclude_none=True))


class FieldSchemaDict(typing_extensions.TypedDict):
    """The specification of the type of a Foundry schema field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nullable: bool
    customMetadata: typing_extensions.NotRequired[CustomMetadata]
    dataType: FieldDataTypeDict


FilePath = str
"""The path to a File within Foundry. Examples: `my-file.txt`, `path/to/my-file.jpg`, `dataframe.snappy.parquet`."""


Filename = str
"""The name of a File within Foundry. Examples: `my-file.txt`, `my-file.jpg`, `dataframe.snappy.parquet`."""


class FilterBinaryTypeDict(typing_extensions.TypedDict):
    """FilterBinaryType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["binary"]


class FilterBooleanTypeDict(typing_extensions.TypedDict):
    """FilterBooleanType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["boolean"]


class FilterDateTimeTypeDict(typing_extensions.TypedDict):
    """FilterDateTimeType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["dateTime"]


class FilterDateTypeDict(typing_extensions.TypedDict):
    """FilterDateType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["date"]


class FilterDoubleTypeDict(typing_extensions.TypedDict):
    """FilterDoubleType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["double"]


class FilterEnumTypeDict(typing_extensions.TypedDict):
    """FilterEnumType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    values: typing.List[str]
    """The values allowed by the enum type."""

    type: typing.Literal["enum"]


class FilterFloatTypeDict(typing_extensions.TypedDict):
    """FilterFloatType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["float"]


class FilterIntegerTypeDict(typing_extensions.TypedDict):
    """FilterIntegerType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["integer"]


class FilterLongTypeDict(typing_extensions.TypedDict):
    """FilterLongType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["long"]


class FilterRidTypeDict(typing_extensions.TypedDict):
    """FilterRidType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["rid"]


class FilterStringTypeDict(typing_extensions.TypedDict):
    """FilterStringType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["string"]


FilterTypeDict = typing_extensions.Annotated[
    typing.Union[
        "FilterDateTimeTypeDict",
        "FilterDateTypeDict",
        "FilterBooleanTypeDict",
        "FilterStringTypeDict",
        "FilterDoubleTypeDict",
        "FilterBinaryTypeDict",
        "FilterIntegerTypeDict",
        "FilterFloatTypeDict",
        "FilterRidTypeDict",
        "FilterUuidTypeDict",
        "FilterEnumTypeDict",
        "FilterLongTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""FilterType"""


class FilterUuidTypeDict(typing_extensions.TypedDict):
    """FilterUuidType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["uuid"]


class FloatType(pydantic.BaseModel):
    """FloatType"""

    type: typing.Literal["float"] = "float"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FloatTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FloatTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class FloatTypeDict(typing_extensions.TypedDict):
    """FloatType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["float"]


FolderRid = core.RID
"""FolderRid"""


class FoundryLiveDeployment(pydantic.BaseModel):
    """FoundryLiveDeployment"""

    rid: typing.Optional[core.RID] = None
    """The live deployment identifier. This rid is of the format 'ri.foundry-ml-live.main.live-deployment.<uuid>'."""

    input_param_name: typing.Optional[str] = pydantic.Field(alias=str("inputParamName"), default=None)  # type: ignore[literal-required]
    """The name of the input parameter to the model which should contain the query string."""

    output_param_name: typing.Optional[str] = pydantic.Field(alias=str("outputParamName"), default=None)  # type: ignore[literal-required]
    """The name of the output parameter to the model which should contain the computed embedding."""

    type: typing.Literal["foundryLiveDeployment"] = "foundryLiveDeployment"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FoundryLiveDeploymentDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FoundryLiveDeploymentDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FoundryLiveDeploymentDict(typing_extensions.TypedDict):
    """FoundryLiveDeployment"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: typing_extensions.NotRequired[core.RID]
    """The live deployment identifier. This rid is of the format 'ri.foundry-ml-live.main.live-deployment.<uuid>'."""

    inputParamName: typing_extensions.NotRequired[str]
    """The name of the input parameter to the model which should contain the query string."""

    outputParamName: typing_extensions.NotRequired[str]
    """The name of the output parameter to the model which should contain the computed embedding."""

    type: typing.Literal["foundryLiveDeployment"]


class GeoPointType(pydantic.BaseModel):
    """GeoPointType"""

    type: typing.Literal["geopoint"] = "geopoint"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GeoPointTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GeoPointTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class GeoPointTypeDict(typing_extensions.TypedDict):
    """GeoPointType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["geopoint"]


class GeoShapeType(pydantic.BaseModel):
    """GeoShapeType"""

    type: typing.Literal["geoshape"] = "geoshape"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GeoShapeTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GeoShapeTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class GeoShapeTypeDict(typing_extensions.TypedDict):
    """GeoShapeType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["geoshape"]


class GeotimeSeriesReferenceType(pydantic.BaseModel):
    """GeotimeSeriesReferenceType"""

    type: typing.Literal["geotimeSeriesReference"] = "geotimeSeriesReference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GeotimeSeriesReferenceTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GeotimeSeriesReferenceTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GeotimeSeriesReferenceTypeDict(typing_extensions.TypedDict):
    """GeotimeSeriesReferenceType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["geotimeSeriesReference"]


GroupName = str
"""The display name of a multipass group."""


GroupRid = core.RID
"""The unique resource identifier (RID) of a multipass group."""


class IntegerType(pydantic.BaseModel):
    """IntegerType"""

    type: typing.Literal["integer"] = "integer"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "IntegerTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(IntegerTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class IntegerTypeDict(typing_extensions.TypedDict):
    """IntegerType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["integer"]


JobRid = core.RID
"""The RID of a Job."""


class LmsEmbeddingModel(pydantic.BaseModel):
    """A model provided by Language Model Service."""

    value: LmsEmbeddingModelValue
    type: typing.Literal["lms"] = "lms"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LmsEmbeddingModelDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LmsEmbeddingModelDict, self.model_dump(by_alias=True, exclude_none=True))


class LmsEmbeddingModelDict(typing_extensions.TypedDict):
    """A model provided by Language Model Service."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: LmsEmbeddingModelValue
    type: typing.Literal["lms"]


LmsEmbeddingModelValue = typing.Literal[
    "OPENAI_TEXT_EMBEDDING_ADA_002",
    "TEXT_EMBEDDING_3_SMALL",
    "SNOWFLAKE_ARCTIC_EMBED_M",
    "INSTRUCTOR_LARGE",
    "BGE_BASE_EN_V1_5",
]
"""LmsEmbeddingModelValue"""


class LongType(pydantic.BaseModel):
    """LongType"""

    type: typing.Literal["long"] = "long"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LongTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LongTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class LongTypeDict(typing_extensions.TypedDict):
    """LongType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["long"]


class MapFieldType(pydantic.BaseModel):
    """MapFieldType"""

    key_schema: FieldSchema = pydantic.Field(alias=str("keySchema"))  # type: ignore[literal-required]
    value_schema: FieldSchema = pydantic.Field(alias=str("valueSchema"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MapFieldTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MapFieldTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class MapFieldTypeDict(typing_extensions.TypedDict):
    """MapFieldType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keySchema: FieldSchemaDict
    valueSchema: FieldSchemaDict
    type: typing.Literal["map"]


MarkingId = core.UUID
"""The ID of a security marking."""


class MarkingType(pydantic.BaseModel):
    """MarkingType"""

    type: typing.Literal["marking"] = "marking"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MarkingTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MarkingTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class MarkingTypeDict(typing_extensions.TypedDict):
    """MarkingType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["marking"]


MediaItemPath = str
"""
A user-specified identifier for a media item within a media set.
Paths must be less than 256 characters long.
If multiple items are written to the same media set at the same path, then when retrieving by path the media
item which was written last is returned.
"""


MediaItemReadToken = str
"""A token that grants access to read specific media items."""


MediaItemRid = core.RID
"""The Resource Identifier (RID) of an individual Media Item within a Media Set in Foundry."""


class MediaReference(pydantic.BaseModel):
    """The representation of a media reference."""

    mime_type: MediaType = pydantic.Field(alias=str("mimeType"))  # type: ignore[literal-required]
    reference: Reference
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MediaReferenceDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MediaReferenceDict, self.model_dump(by_alias=True, exclude_none=True))


class MediaReferenceDict(typing_extensions.TypedDict):
    """The representation of a media reference."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mimeType: MediaType
    reference: ReferenceDict


class MediaReferenceType(pydantic.BaseModel):
    """MediaReferenceType"""

    type: typing.Literal["mediaReference"] = "mediaReference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MediaReferenceTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            MediaReferenceTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class MediaReferenceTypeDict(typing_extensions.TypedDict):
    """MediaReferenceType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["mediaReference"]


MediaSetRid = core.RID
"""The Resource Identifier (RID) of a Media Set in Foundry."""


class MediaSetViewItem(pydantic.BaseModel):
    """MediaSetViewItem"""

    media_set_rid: MediaSetRid = pydantic.Field(alias=str("mediaSetRid"))  # type: ignore[literal-required]
    media_set_view_rid: MediaSetViewRid = pydantic.Field(alias=str("mediaSetViewRid"))  # type: ignore[literal-required]
    media_item_rid: MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]
    token: typing.Optional[MediaItemReadToken] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MediaSetViewItemDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MediaSetViewItemDict, self.model_dump(by_alias=True, exclude_none=True))


class MediaSetViewItemDict(typing_extensions.TypedDict):
    """MediaSetViewItem"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetRid: MediaSetRid
    mediaSetViewRid: MediaSetViewRid
    mediaItemRid: MediaItemRid
    token: typing_extensions.NotRequired[MediaItemReadToken]


MediaSetViewRid = core.RID
"""The Resource Identifier (RID) of a single View of a Media Set. A Media Set View is an independent collection of Media Items."""


MediaType = str
"""
The [media type](https://www.iana.org/assignments/media-types/media-types.xhtml) of the file or attachment.
Examples: `application/json`, `application/pdf`, `application/octet-stream`, `image/jpeg`
"""


class NullType(pydantic.BaseModel):
    """NullType"""

    type: typing.Literal["null"] = "null"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "NullTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(NullTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class NullTypeDict(typing_extensions.TypedDict):
    """NullType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["null"]


OperationScope = str
"""OperationScope"""


OrderByDirection = typing.Literal["ASC", "DESC"]
"""Specifies the ordering direction (can be either `ASC` or `DESC`)"""


OrganizationRid = core.RID
"""OrganizationRid"""


PageSize = int
"""The page size to use for the endpoint."""


PageToken = str
"""
The page token indicates where to start paging. This should be omitted from the first page's request.
To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response
and use it to populate the `pageToken` field of the next request.
"""


PreviewMode = bool
"""Enables the use of preview functionality."""


PrincipalId = str
"""The ID of a Foundry Group or User."""


PrincipalType = typing.Literal["USER", "GROUP"]
"""PrincipalType"""


Realm = str
"""
Identifies which Realm a User or Group is a member of.
The `palantir-internal-realm` is used for Users or Groups that are created in Foundry by administrators and not associated with any SSO provider.
"""


class Reference(pydantic.BaseModel):
    """A union of the types supported by media reference properties."""

    media_set_view_item: MediaSetViewItem = pydantic.Field(alias=str("mediaSetViewItem"))  # type: ignore[literal-required]
    type: typing.Literal["mediaSetViewItem"] = "mediaSetViewItem"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ReferenceDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ReferenceDict, self.model_dump(by_alias=True, exclude_none=True))


class ReferenceDict(typing_extensions.TypedDict):
    """A union of the types supported by media reference properties."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaSetViewItem: MediaSetViewItemDict
    type: typing.Literal["mediaSetViewItem"]


ReleaseStatus = typing.Literal["ACTIVE", "ENDORSED", "EXPERIMENTAL", "DEPRECATED"]
"""The release status of the entity."""


RoleId = str
"""
The unique ID for a Role. Roles are sets of permissions that grant different levels of access to resources.
The default roles in Foundry are: Owner, Editor, Viewer, and Discoverer. See more about 
[roles](/docs/foundry/security/projects-and-roles#roles) in the user documentation.
"""


class ShortType(pydantic.BaseModel):
    """ShortType"""

    type: typing.Literal["short"] = "short"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ShortTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ShortTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class ShortTypeDict(typing_extensions.TypedDict):
    """ShortType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["short"]


SizeBytes = core.Long
"""The size of the file or attachment in bytes."""


class StreamSchema(pydantic.BaseModel):
    """The schema for a Foundry stream. Records pushed to this stream must match this schema."""

    fields: typing.List[Field]
    key_field_names: typing.Optional[typing.List[FieldName]] = pydantic.Field(alias=str("keyFieldNames"), default=None)  # type: ignore[literal-required]
    """
    The names of the fields to be used as keys for partitioning records. These key fields are used to group
    all records with the same key into the same partition, to guarantee processing order of grouped records. These
    keys are not meant to uniquely identify records, and do not by themselves deduplicate records. To deduplicate
    records, provide a change data capture configuration for the schema.

    Key fields can only be of the following types:
    - Boolean
    - Byte
    - Date
    - Decimal
    - Integer
    - Long
    - Short
    - String
    - Timestamp

    For additional information on keys for Foundry streams, see the
    [streaming keys](/docs/foundry/building-pipelines/streaming-keys/) user documentation.
    """

    change_data_capture: typing.Optional[ChangeDataCaptureConfiguration] = pydantic.Field(alias=str("changeDataCapture"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "StreamSchemaDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(StreamSchemaDict, self.model_dump(by_alias=True, exclude_none=True))


class StreamSchemaDict(typing_extensions.TypedDict):
    """The schema for a Foundry stream. Records pushed to this stream must match this schema."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: typing.List[FieldDict]
    keyFieldNames: typing_extensions.NotRequired[typing.List[FieldName]]
    """
    The names of the fields to be used as keys for partitioning records. These key fields are used to group
    all records with the same key into the same partition, to guarantee processing order of grouped records. These
    keys are not meant to uniquely identify records, and do not by themselves deduplicate records. To deduplicate
    records, provide a change data capture configuration for the schema.

    Key fields can only be of the following types:
    - Boolean
    - Byte
    - Date
    - Decimal
    - Integer
    - Long
    - Short
    - String
    - Timestamp

    For additional information on keys for Foundry streams, see the
    [streaming keys](/docs/foundry/building-pipelines/streaming-keys/) user documentation.
    """

    changeDataCapture: typing_extensions.NotRequired[ChangeDataCaptureConfigurationDict]


class StringType(pydantic.BaseModel):
    """StringType"""

    type: typing.Literal["string"] = "string"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "StringTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(StringTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class StringTypeDict(typing_extensions.TypedDict):
    """StringType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["string"]


StructFieldName = str
"""The name of a field in a `Struct`."""


class StructFieldType(pydantic.BaseModel):
    """StructFieldType"""

    sub_fields: typing.List[Field] = pydantic.Field(alias=str("subFields"))  # type: ignore[literal-required]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "StructFieldTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(StructFieldTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class StructFieldTypeDict(typing_extensions.TypedDict):
    """StructFieldType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subFields: typing.List[FieldDict]
    type: typing.Literal["struct"]


TimeSeriesItemType = typing_extensions.Annotated[
    typing.Union["StringType", "DoubleType"], pydantic.Field(discriminator="type")
]
"""A union of the types supported by time series properties."""


TimeSeriesItemTypeDict = typing_extensions.Annotated[
    typing.Union["StringTypeDict", "DoubleTypeDict"], pydantic.Field(discriminator="type")
]
"""A union of the types supported by time series properties."""


TimeUnit = typing.Literal[
    "MILLISECONDS", "SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS", "MONTHS", "YEARS"
]
"""TimeUnit"""


class TimeseriesType(pydantic.BaseModel):
    """TimeseriesType"""

    item_type: typing.Optional[TimeSeriesItemType] = pydantic.Field(alias=str("itemType"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["timeseries"] = "timeseries"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "TimeseriesTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(TimeseriesTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class TimeseriesTypeDict(typing_extensions.TypedDict):
    """TimeseriesType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    itemType: typing_extensions.NotRequired[TimeSeriesItemTypeDict]
    type: typing.Literal["timeseries"]


class TimestampType(pydantic.BaseModel):
    """TimestampType"""

    type: typing.Literal["timestamp"] = "timestamp"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "TimestampTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(TimestampTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class TimestampTypeDict(typing_extensions.TypedDict):
    """TimestampType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["timestamp"]


TotalCount = core.Long
"""The total number of items across all pages."""


class UnsupportedType(pydantic.BaseModel):
    """UnsupportedType"""

    unsupported_type: str = pydantic.Field(alias=str("unsupportedType"))  # type: ignore[literal-required]
    type: typing.Literal["unsupported"] = "unsupported"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "UnsupportedTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(UnsupportedTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class UnsupportedTypeDict(typing_extensions.TypedDict):
    """UnsupportedType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    unsupportedType: str
    type: typing.Literal["unsupported"]


UpdatedBy = core.UUID
"""The Foundry user who last updated this resource"""


UpdatedTime = datetime
"""The time at which the resource was most recently updated."""


UserId = core.UUID
"""A Foundry User ID."""


class VectorSimilarityFunction(pydantic.BaseModel):
    """
    The vector similarity function to support approximate nearest neighbors search. Will result in an index
    specific for the function.
    """

    value: typing.Optional[VectorSimilarityFunctionValue] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "VectorSimilarityFunctionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            VectorSimilarityFunctionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class VectorSimilarityFunctionDict(typing_extensions.TypedDict):
    """
    The vector similarity function to support approximate nearest neighbors search. Will result in an index
    specific for the function.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: typing_extensions.NotRequired[VectorSimilarityFunctionValue]


VectorSimilarityFunctionValue = typing.Literal[
    "COSINE_SIMILARITY", "DOT_PRODUCT", "EUCLIDEAN_DISTANCE"
]
"""VectorSimilarityFunctionValue"""


class VectorType(pydantic.BaseModel):
    """Represents a fixed size vector of floats. These can be used for vector similarity searches."""

    dimension: int
    """The dimension of the vector."""

    supports_search_with: typing.List[VectorSimilarityFunction] = pydantic.Field(alias=str("supportsSearchWith"))  # type: ignore[literal-required]
    embedding_model: typing.Optional[EmbeddingModel] = pydantic.Field(alias=str("embeddingModel"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["vector"] = "vector"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "VectorTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(VectorTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class VectorTypeDict(typing_extensions.TypedDict):
    """Represents a fixed size vector of floats. These can be used for vector similarity searches."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    dimension: int
    """The dimension of the vector."""

    supportsSearchWith: typing.List[VectorSimilarityFunctionDict]
    embeddingModel: typing_extensions.NotRequired[EmbeddingModelDict]
    type: typing.Literal["vector"]


ZoneId = str
"""A string representation of a java.time.ZoneId"""


__all__ = [
    "AnyType",
    "AnyTypeDict",
    "ArrayFieldType",
    "ArrayFieldTypeDict",
    "AttachmentType",
    "AttachmentTypeDict",
    "BinaryType",
    "BinaryTypeDict",
    "BooleanType",
    "BooleanTypeDict",
    "BuildRid",
    "ByteType",
    "ByteTypeDict",
    "ChangeDataCaptureConfiguration",
    "ChangeDataCaptureConfigurationDict",
    "CipherTextType",
    "CipherTextTypeDict",
    "ContentLength",
    "ContentType",
    "CreatedBy",
    "CreatedTime",
    "CustomMetadata",
    "DateType",
    "DateTypeDict",
    "DecimalType",
    "DecimalTypeDict",
    "DisplayName",
    "Distance",
    "DistanceDict",
    "DistanceUnit",
    "DoubleType",
    "DoubleTypeDict",
    "Duration",
    "DurationDict",
    "EmbeddingModel",
    "EmbeddingModelDict",
    "EnrollmentRid",
    "Field",
    "FieldDataType",
    "FieldDataTypeDict",
    "FieldDict",
    "FieldName",
    "FieldSchema",
    "FieldSchemaDict",
    "FilePath",
    "Filename",
    "FilterBinaryTypeDict",
    "FilterBooleanTypeDict",
    "FilterDateTimeTypeDict",
    "FilterDateTypeDict",
    "FilterDoubleTypeDict",
    "FilterEnumTypeDict",
    "FilterFloatTypeDict",
    "FilterIntegerTypeDict",
    "FilterLongTypeDict",
    "FilterRidTypeDict",
    "FilterStringTypeDict",
    "FilterTypeDict",
    "FilterUuidTypeDict",
    "FloatType",
    "FloatTypeDict",
    "FolderRid",
    "FoundryLiveDeployment",
    "FoundryLiveDeploymentDict",
    "GeoPointType",
    "GeoPointTypeDict",
    "GeoShapeType",
    "GeoShapeTypeDict",
    "GeotimeSeriesReferenceType",
    "GeotimeSeriesReferenceTypeDict",
    "GroupName",
    "GroupRid",
    "IntegerType",
    "IntegerTypeDict",
    "JobRid",
    "LmsEmbeddingModel",
    "LmsEmbeddingModelDict",
    "LmsEmbeddingModelValue",
    "LongType",
    "LongTypeDict",
    "MapFieldType",
    "MapFieldTypeDict",
    "MarkingId",
    "MarkingType",
    "MarkingTypeDict",
    "MediaItemPath",
    "MediaItemReadToken",
    "MediaItemRid",
    "MediaReference",
    "MediaReferenceDict",
    "MediaReferenceType",
    "MediaReferenceTypeDict",
    "MediaSetRid",
    "MediaSetViewItem",
    "MediaSetViewItemDict",
    "MediaSetViewRid",
    "MediaType",
    "NullType",
    "NullTypeDict",
    "OperationScope",
    "OrderByDirection",
    "OrganizationRid",
    "PageSize",
    "PageToken",
    "PreviewMode",
    "PrincipalId",
    "PrincipalType",
    "Realm",
    "Reference",
    "ReferenceDict",
    "ReleaseStatus",
    "RoleId",
    "ShortType",
    "ShortTypeDict",
    "SizeBytes",
    "StreamSchema",
    "StreamSchemaDict",
    "StringType",
    "StringTypeDict",
    "StructFieldName",
    "StructFieldType",
    "StructFieldTypeDict",
    "TimeSeriesItemType",
    "TimeSeriesItemTypeDict",
    "TimeUnit",
    "TimeseriesType",
    "TimeseriesTypeDict",
    "TimestampType",
    "TimestampTypeDict",
    "TotalCount",
    "UnsupportedType",
    "UnsupportedTypeDict",
    "UpdatedBy",
    "UpdatedTime",
    "UserId",
    "VectorSimilarityFunction",
    "VectorSimilarityFunctionDict",
    "VectorSimilarityFunctionValue",
    "VectorType",
    "VectorTypeDict",
    "ZoneId",
]
