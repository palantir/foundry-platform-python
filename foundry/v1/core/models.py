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


class CipherTextType(pydantic.BaseModel):
    """CipherTextType"""

    default_cipher_channel: typing.Optional[str] = pydantic.Field(alias=str("defaultCipherChannel"), default=None)  # type: ignore[literal-required]
    """An optional Cipher Channel RID which can be used for encryption updates to empty values."""

    type: typing.Literal["cipherText"] = "cipherText"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CipherTextTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(CipherTextTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class CipherTextTypeDict(typing_extensions.TypedDict):
    """CipherTextType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    defaultCipherChannel: typing_extensions.NotRequired[str]
    """An optional Cipher Channel RID which can be used for encryption updates to empty values."""

    type: typing.Literal["cipherText"]


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


FilePath = str
"""The path to a File within Foundry. Examples: `my-file.txt`, `path/to/my-file.jpg`, `dataframe.snappy.parquet`."""


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


class NullTypeDict(typing_extensions.TypedDict):
    """NullType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["null"]


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

    def to_dict(self) -> "ShortTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ShortTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class ShortTypeDict(typing_extensions.TypedDict):
    """ShortType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["short"]


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


__all__ = [
    "AnyType",
    "AnyTypeDict",
    "AttachmentTypeDict",
    "BinaryType",
    "BinaryTypeDict",
    "BooleanType",
    "BooleanTypeDict",
    "ByteType",
    "ByteTypeDict",
    "CipherTextType",
    "CipherTextTypeDict",
    "DateType",
    "DateTypeDict",
    "DecimalType",
    "DecimalTypeDict",
    "DisplayName",
    "DistanceUnit",
    "DoubleType",
    "DoubleTypeDict",
    "FilePath",
    "FloatType",
    "FloatTypeDict",
    "FolderRid",
    "IntegerType",
    "IntegerTypeDict",
    "LongType",
    "LongTypeDict",
    "MarkingType",
    "MarkingTypeDict",
    "NullTypeDict",
    "OperationScope",
    "PageSize",
    "PageToken",
    "PreviewMode",
    "ReleaseStatus",
    "ShortType",
    "ShortTypeDict",
    "StringType",
    "StringTypeDict",
    "StructFieldName",
    "TimestampType",
    "TimestampTypeDict",
    "TotalCount",
    "UnsupportedType",
    "UnsupportedTypeDict",
]
