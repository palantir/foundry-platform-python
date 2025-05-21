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

import pydantic
import typing_extensions

from foundry_sdk import _core as core


class AnyType(pydantic.BaseModel):
    """AnyType"""

    type: typing.Literal["any"] = "any"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ArrayFieldType(pydantic.BaseModel):
    """ArrayFieldType"""

    items_schema: FieldSchema = pydantic.Field(alias=str("itemsSchema"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AttachmentType(pydantic.BaseModel):
    """AttachmentType"""

    type: typing.Literal["attachment"] = "attachment"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class BinaryType(pydantic.BaseModel):
    """BinaryType"""

    type: typing.Literal["binary"] = "binary"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class BooleanType(pydantic.BaseModel):
    """BooleanType"""

    type: typing.Literal["boolean"] = "boolean"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


BuildRid = core.RID
"""The RID of a Build."""


class ByteType(pydantic.BaseModel):
    """ByteType"""

    type: typing.Literal["byte"] = "byte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CipherTextType(pydantic.BaseModel):
    """CipherTextType"""

    default_cipher_channel: typing.Optional[core.RID] = pydantic.Field(alias=str("defaultCipherChannel"), default=None)  # type: ignore[literal-required]
    """An optional Cipher Channel RID which can be used for encryption updates to empty values."""

    type: typing.Literal["cipherText"] = "cipherText"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ContentLength = core.Long
"""ContentLength"""


ContentType = str
"""ContentType"""


CreatedTime = core.AwareDatetime
"""The time at which the resource was created."""


CustomMetadata = typing.Dict[str, typing.Any]
"""CustomMetadata"""


class DateType(pydantic.BaseModel):
    """DateType"""

    type: typing.Literal["date"] = "date"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DecimalType(pydantic.BaseModel):
    """DecimalType"""

    precision: typing.Optional[int] = None
    """The total number of digits of the Decimal type. The maximum value is 38."""

    scale: typing.Optional[int] = None
    """The number of digits to the right of the decimal point. The maximum value is 38."""

    type: typing.Literal["decimal"] = "decimal"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


DisplayName = str
"""The display name of the entity."""


class Distance(pydantic.BaseModel):
    """A measurement of distance."""

    value: float
    unit: DistanceUnit
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Duration(pydantic.BaseModel):
    """A measurement of duration."""

    value: int
    """The duration value."""

    unit: TimeUnit
    """The unit of duration."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


EmbeddingModel = typing_extensions.Annotated[
    typing.Union["LmsEmbeddingModel", "FoundryLiveDeployment"], pydantic.Field(discriminator="type")
]
"""EmbeddingModel"""


EnrollmentRid = core.RID
"""EnrollmentRid"""


class Field(pydantic.BaseModel):
    """
    A field in a Foundry schema. For more information on supported data types, see the
    [supported field types](https://palantir.com/docs/foundry/data-integration/datasets/#supported-field-types) user documentation.
    """

    name: FieldName
    schema_: FieldSchema = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FieldDataType = typing_extensions.Annotated[
    typing.Union[
        "StructFieldType",
        DateType,
        "StringType",
        ByteType,
        DoubleType,
        "IntegerType",
        "FloatType",
        "LongType",
        BooleanType,
        ArrayFieldType,
        BinaryType,
        "ShortType",
        DecimalType,
        "MapFieldType",
        "TimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
"""FieldDataType"""


FieldName = str
"""FieldName"""


class FieldSchema(pydantic.BaseModel):
    """The specification of the type of a Foundry schema field."""

    nullable: bool
    custom_metadata: typing.Optional[CustomMetadata] = pydantic.Field(alias=str("customMetadata"), default=None)  # type: ignore[literal-required]
    data_type: FieldDataType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FilePath = str
"""The path to a File within Foundry. Examples: `my-file.txt`, `path/to/my-file.jpg`, `dataframe.snappy.parquet`."""


Filename = str
"""The name of a File within Foundry. Examples: `my-file.txt`, `my-file.jpg`, `dataframe.snappy.parquet`."""


class FilterBinaryType(pydantic.BaseModel):
    """FilterBinaryType"""

    type: typing.Literal["binary"] = "binary"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterBooleanType(pydantic.BaseModel):
    """FilterBooleanType"""

    type: typing.Literal["boolean"] = "boolean"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterDateTimeType(pydantic.BaseModel):
    """FilterDateTimeType"""

    type: typing.Literal["dateTime"] = "dateTime"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterDateType(pydantic.BaseModel):
    """FilterDateType"""

    type: typing.Literal["date"] = "date"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterDoubleType(pydantic.BaseModel):
    """FilterDoubleType"""

    type: typing.Literal["double"] = "double"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterEnumType(pydantic.BaseModel):
    """FilterEnumType"""

    values: typing.List[str]
    """The values allowed by the enum type."""

    type: typing.Literal["enum"] = "enum"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterFloatType(pydantic.BaseModel):
    """FilterFloatType"""

    type: typing.Literal["float"] = "float"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterIntegerType(pydantic.BaseModel):
    """FilterIntegerType"""

    type: typing.Literal["integer"] = "integer"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterLongType(pydantic.BaseModel):
    """FilterLongType"""

    type: typing.Literal["long"] = "long"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterRidType(pydantic.BaseModel):
    """FilterRidType"""

    type: typing.Literal["rid"] = "rid"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FilterStringType(pydantic.BaseModel):
    """FilterStringType"""

    type: typing.Literal["string"] = "string"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FilterType = typing_extensions.Annotated[
    typing.Union[
        FilterDateTimeType,
        FilterDateType,
        FilterBooleanType,
        FilterStringType,
        FilterDoubleType,
        FilterBinaryType,
        FilterIntegerType,
        FilterFloatType,
        FilterRidType,
        "FilterUuidType",
        FilterEnumType,
        FilterLongType,
    ],
    pydantic.Field(discriminator="type"),
]
"""FilterType"""


class FilterUuidType(pydantic.BaseModel):
    """FilterUuidType"""

    type: typing.Literal["uuid"] = "uuid"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FloatType(pydantic.BaseModel):
    """FloatType"""

    type: typing.Literal["float"] = "float"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FullRowChangeDataCaptureConfiguration(pydantic.BaseModel):
    """
    Configuration for change data capture which resolves the latest state of the dataset based on new full rows
    being pushed to the stream. For example, if a value for a row is updated, it is only sufficient to publish
    the entire new state of that row to the stream.
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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GeoPointType(pydantic.BaseModel):
    """GeoPointType"""

    type: typing.Literal["geopoint"] = "geopoint"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GeoShapeType(pydantic.BaseModel):
    """GeoShapeType"""

    type: typing.Literal["geoshape"] = "geoshape"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GeohashType(pydantic.BaseModel):
    """GeohashType"""

    type: typing.Literal["geohash"] = "geohash"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GeotimeSeriesReferenceType(pydantic.BaseModel):
    """GeotimeSeriesReferenceType"""

    type: typing.Literal["geotimeSeriesReference"] = "geotimeSeriesReference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


GroupName = str
"""The display name of a multipass group."""


GroupRid = core.RID
"""The unique resource identifier (RID) of a multipass group."""


class IntegerType(pydantic.BaseModel):
    """IntegerType"""

    type: typing.Literal["integer"] = "integer"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


JobRid = core.RID
"""The RID of a Job."""


class LmsEmbeddingModel(pydantic.BaseModel):
    """A model provided by Language Model Service."""

    value: LmsEmbeddingModelValue
    type: typing.Literal["lms"] = "lms"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MapFieldType(pydantic.BaseModel):
    """MapFieldType"""

    key_schema: FieldSchema = pydantic.Field(alias=str("keySchema"))  # type: ignore[literal-required]
    value_schema: FieldSchema = pydantic.Field(alias=str("valueSchema"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MarkingId = core.UUID
"""The ID of a security marking."""


class MarkingType(pydantic.BaseModel):
    """MarkingType"""

    type: typing.Literal["marking"] = "marking"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MediaReferenceType(pydantic.BaseModel):
    """MediaReferenceType"""

    type: typing.Literal["mediaReference"] = "mediaReference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MediaSetRid = core.RID
"""The Resource Identifier (RID) of a Media Set in Foundry."""


class MediaSetViewItem(pydantic.BaseModel):
    """MediaSetViewItem"""

    media_set_rid: MediaSetRid = pydantic.Field(alias=str("mediaSetRid"))  # type: ignore[literal-required]
    media_set_view_rid: MediaSetViewRid = pydantic.Field(alias=str("mediaSetViewRid"))  # type: ignore[literal-required]
    media_item_rid: MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]
    token: typing.Optional[MediaItemReadToken] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MediaSetViewItemWrapper(pydantic.BaseModel):
    """MediaSetViewItemWrapper"""

    media_set_view_item: MediaSetViewItem = pydantic.Field(alias=str("mediaSetViewItem"))  # type: ignore[literal-required]
    type: typing.Literal["mediaSetViewItem"] = "mediaSetViewItem"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


Operation = str
"""
An operation that can be performed on a resource. Operations are used to define the permissions that a Role has.
Operations are typically in the format `service:action`, where `service` is related to the type of resource and `action` is the action being performed.
"""


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


ReleaseStatus = typing.Literal["ACTIVE", "ENDORSED", "EXPERIMENTAL", "DEPRECATED"]
"""The release status of the entity."""


class Role(pydantic.BaseModel):
    """A set of permissions that can be assigned to a principal for a specific resource type."""

    id: RoleId
    role_set_id: RoleSetId = pydantic.Field(alias=str("roleSetId"))  # type: ignore[literal-required]
    name: str
    description: str
    is_default: bool = pydantic.Field(alias=str("isDefault"))  # type: ignore[literal-required]
    """Default roles are provided by Palantir and cannot be edited or modified by administrators."""

    type: RoleContext
    """The type of resource that is valid for this role."""

    operations: typing.List[Operation]
    """The operations that a principal can perform with this role on the assigned resource."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class RoleAssignmentUpdate(pydantic.BaseModel):
    """RoleAssignmentUpdate"""

    role_id: RoleId = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]
    principal_id: PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


RoleContext = typing.Literal["ORGANIZATION"]
"""RoleContext"""


RoleId = str
"""
The unique ID for a Role. Roles are sets of permissions that grant different levels of access to resources.
The default roles in Foundry are: Owner, Editor, Viewer, and Discoverer. See more about 
[roles](https://palantir.com/docs/foundry/security/projects-and-roles#roles) in the user documentation.
"""


RoleSetId = str
"""RoleSetId"""


ScheduleRid = core.RID
"""The RID of a Schedule."""


class ShortType(pydantic.BaseModel):
    """ShortType"""

    type: typing.Literal["short"] = "short"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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
    [streaming keys](https://palantir.com/docs/foundry/building-pipelines/streaming-keys/) user documentation.
    """

    change_data_capture: typing.Optional[ChangeDataCaptureConfiguration] = pydantic.Field(alias=str("changeDataCapture"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class StringType(pydantic.BaseModel):
    """StringType"""

    type: typing.Literal["string"] = "string"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


StructFieldName = str
"""The name of a field in a `Struct`."""


class StructFieldType(pydantic.BaseModel):
    """StructFieldType"""

    sub_fields: typing.List[Field] = pydantic.Field(alias=str("subFields"))  # type: ignore[literal-required]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TimeSeriesItemType = typing_extensions.Annotated[
    typing.Union[StringType, DoubleType], pydantic.Field(discriminator="type")
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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class TimestampType(pydantic.BaseModel):
    """TimestampType"""

    type: typing.Literal["timestamp"] = "timestamp"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TotalCount = core.Long
"""The total number of items across all pages."""


class UnsupportedType(pydantic.BaseModel):
    """UnsupportedType"""

    unsupported_type: str = pydantic.Field(alias=str("unsupportedType"))  # type: ignore[literal-required]
    type: typing.Literal["unsupported"] = "unsupported"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


UpdatedTime = core.AwareDatetime
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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ZoneId = str
"""A string representation of a java.time.ZoneId"""


ChangeDataCaptureConfiguration = FullRowChangeDataCaptureConfiguration
"""
Configuration for utilizing the stream as a change data capture (CDC) dataset. To configure CDC on a stream, at
least one key needs to be provided.

For more information on CDC in
Foundry, see the [Change Data Capture](https://palantir.com/docs/foundry/data-integration/change-data-capture/) user documentation.
"""


CreatedBy = PrincipalId
"""The Foundry user who created this resource"""


Reference = MediaSetViewItemWrapper
"""A union of the types supported by media reference properties."""


UpdatedBy = UserId
"""The Foundry user who last updated this resource"""


core.resolve_forward_references(CustomMetadata, globalns=globals(), localns=locals())
core.resolve_forward_references(EmbeddingModel, globalns=globals(), localns=locals())
core.resolve_forward_references(FieldDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(FilterType, globalns=globals(), localns=locals())
core.resolve_forward_references(TimeSeriesItemType, globalns=globals(), localns=locals())

__all__ = [
    "AnyType",
    "ArrayFieldType",
    "AttachmentType",
    "BinaryType",
    "BooleanType",
    "BuildRid",
    "ByteType",
    "ChangeDataCaptureConfiguration",
    "CipherTextType",
    "ContentLength",
    "ContentType",
    "CreatedBy",
    "CreatedTime",
    "CustomMetadata",
    "DateType",
    "DecimalType",
    "DisplayName",
    "Distance",
    "DistanceUnit",
    "DoubleType",
    "Duration",
    "EmbeddingModel",
    "EnrollmentRid",
    "Field",
    "FieldDataType",
    "FieldName",
    "FieldSchema",
    "FilePath",
    "Filename",
    "FilterBinaryType",
    "FilterBooleanType",
    "FilterDateTimeType",
    "FilterDateType",
    "FilterDoubleType",
    "FilterEnumType",
    "FilterFloatType",
    "FilterIntegerType",
    "FilterLongType",
    "FilterRidType",
    "FilterStringType",
    "FilterType",
    "FilterUuidType",
    "FloatType",
    "FolderRid",
    "FoundryLiveDeployment",
    "FullRowChangeDataCaptureConfiguration",
    "GeoPointType",
    "GeoShapeType",
    "GeohashType",
    "GeotimeSeriesReferenceType",
    "GroupName",
    "GroupRid",
    "IntegerType",
    "JobRid",
    "LmsEmbeddingModel",
    "LmsEmbeddingModelValue",
    "LongType",
    "MapFieldType",
    "MarkingId",
    "MarkingType",
    "MediaItemPath",
    "MediaItemReadToken",
    "MediaItemRid",
    "MediaReference",
    "MediaReferenceType",
    "MediaSetRid",
    "MediaSetViewItem",
    "MediaSetViewItemWrapper",
    "MediaSetViewRid",
    "MediaType",
    "NullType",
    "Operation",
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
    "ReleaseStatus",
    "Role",
    "RoleAssignmentUpdate",
    "RoleContext",
    "RoleId",
    "RoleSetId",
    "ScheduleRid",
    "ShortType",
    "SizeBytes",
    "StreamSchema",
    "StringType",
    "StructFieldName",
    "StructFieldType",
    "TimeSeriesItemType",
    "TimeUnit",
    "TimeseriesType",
    "TimestampType",
    "TotalCount",
    "UnsupportedType",
    "UpdatedBy",
    "UpdatedTime",
    "UserId",
    "VectorSimilarityFunction",
    "VectorSimilarityFunctionValue",
    "VectorType",
    "ZoneId",
]
