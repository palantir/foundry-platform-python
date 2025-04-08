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

from foundry_sdk import _core as core


class AnyType(pydantic.BaseModel):
    """AnyType"""

    type: typing.Literal["any"] = "any"
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


class ByteType(pydantic.BaseModel):
    """ByteType"""

    type: typing.Literal["byte"] = "byte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CipherTextType(pydantic.BaseModel):
    """CipherTextType"""

    default_cipher_channel: typing.Optional[str] = pydantic.Field(alias=str("defaultCipherChannel"), default=None)  # type: ignore[literal-required]
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


FilePath = str
"""The path to a File within Foundry. Examples: `my-file.txt`, `path/to/my-file.jpg`, `dataframe.snappy.parquet`."""


Filename = str
"""The name of a File within Foundry. Examples: `my-file.txt`, `my-file.jpg`, `dataframe.snappy.parquet`."""


class FloatType(pydantic.BaseModel):
    """FloatType"""

    type: typing.Literal["float"] = "float"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FolderRid = core.RID
"""FolderRid"""


class IntegerType(pydantic.BaseModel):
    """IntegerType"""

    type: typing.Literal["integer"] = "integer"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LongType(pydantic.BaseModel):
    """LongType"""

    type: typing.Literal["long"] = "long"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MarkingType(pydantic.BaseModel):
    """MarkingType"""

    type: typing.Literal["marking"] = "marking"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


OperationScope = str
"""OperationScope"""


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


ReleaseStatus = typing.Literal["ACTIVE", "ENDORSED", "EXPERIMENTAL", "DEPRECATED"]
"""The release status of the entity."""


class ShortType(pydantic.BaseModel):
    """ShortType"""

    type: typing.Literal["short"] = "short"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


SizeBytes = core.Long
"""The size of the file or attachment in bytes."""


class StringType(pydantic.BaseModel):
    """StringType"""

    type: typing.Literal["string"] = "string"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


StructFieldName = str
"""The name of a field in a `Struct`."""


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


__all__ = [
    "AnyType",
    "AttachmentType",
    "BinaryType",
    "BooleanType",
    "ByteType",
    "CipherTextType",
    "ContentLength",
    "ContentType",
    "DateType",
    "DecimalType",
    "DisplayName",
    "DistanceUnit",
    "DoubleType",
    "FilePath",
    "Filename",
    "FloatType",
    "FolderRid",
    "IntegerType",
    "LongType",
    "MarkingType",
    "MediaType",
    "NullType",
    "OperationScope",
    "PageSize",
    "PageToken",
    "PreviewMode",
    "ReleaseStatus",
    "ShortType",
    "SizeBytes",
    "StringType",
    "StructFieldName",
    "TimestampType",
    "TotalCount",
    "UnsupportedType",
]
