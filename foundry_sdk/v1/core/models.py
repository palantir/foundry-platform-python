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


class AnyType(core.ModelBase):
    """AnyType"""

    type: typing.Literal["any"] = "any"


class AttachmentType(core.ModelBase):
    """AttachmentType"""

    type: typing.Literal["attachment"] = "attachment"


class BinaryType(core.ModelBase):
    """BinaryType"""

    type: typing.Literal["binary"] = "binary"


class BooleanType(core.ModelBase):
    """BooleanType"""

    type: typing.Literal["boolean"] = "boolean"


class ByteType(core.ModelBase):
    """ByteType"""

    type: typing.Literal["byte"] = "byte"


class CipherTextType(core.ModelBase):
    """CipherTextType"""

    default_cipher_channel: typing.Optional[str] = pydantic.Field(alias=str("defaultCipherChannel"), default=None)  # type: ignore[literal-required]
    """An optional Cipher Channel RID which can be used for encryption updates to empty values."""

    type: typing.Literal["cipherText"] = "cipherText"


ContentLength = core.Long
"""ContentLength"""


ContentType = str
"""ContentType"""


class DateType(core.ModelBase):
    """DateType"""

    type: typing.Literal["date"] = "date"


class DecimalType(core.ModelBase):
    """DecimalType"""

    precision: typing.Optional[int] = None
    """The total number of digits of the Decimal type. The maximum value is 38."""

    scale: typing.Optional[int] = None
    """The number of digits to the right of the decimal point. The maximum value is 38."""

    type: typing.Literal["decimal"] = "decimal"


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


class DoubleType(core.ModelBase):
    """DoubleType"""

    type: typing.Literal["double"] = "double"


FilePath = str
"""The path to a File within Foundry. Examples: `my-file.txt`, `path/to/my-file.jpg`, `dataframe.snappy.parquet`."""


Filename = str
"""The name of a File within Foundry. Examples: `my-file.txt`, `my-file.jpg`, `dataframe.snappy.parquet`."""


class FloatType(core.ModelBase):
    """FloatType"""

    type: typing.Literal["float"] = "float"


FolderRid = core.RID
"""FolderRid"""


FoundryBranch = str
"""The Foundry branch identifier, specifically its rid. Different identifier types may be used in the future as values."""


class IntegerType(core.ModelBase):
    """IntegerType"""

    type: typing.Literal["integer"] = "integer"


class LongType(core.ModelBase):
    """LongType"""

    type: typing.Literal["long"] = "long"


class MarkingType(core.ModelBase):
    """MarkingType"""

    type: typing.Literal["marking"] = "marking"


MediaType = str
"""
The [media type](https://www.iana.org/assignments/media-types/media-types.xhtml) of the file or attachment.
Examples: `application/json`, `application/pdf`, `application/octet-stream`, `image/jpeg`
"""


class NullType(core.ModelBase):
    """NullType"""

    type: typing.Literal["null"] = "null"


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


class ShortType(core.ModelBase):
    """ShortType"""

    type: typing.Literal["short"] = "short"


SizeBytes = core.Long
"""The size of the file or attachment in bytes."""


class StringType(core.ModelBase):
    """StringType"""

    type: typing.Literal["string"] = "string"


StructFieldName = str
"""The name of a field in a `Struct`."""


class TimestampType(core.ModelBase):
    """TimestampType"""

    type: typing.Literal["timestamp"] = "timestamp"


TotalCount = core.Long
"""The total number of items across all pages."""


TraceParent = str
"""The W3C Trace Context `traceparent` header value used to propagate distributed tracing information for Foundry telemetry. See https://www.w3.org/TR/trace-context/#traceparent-header for more details. Note the 16 byte trace ID encoded in the header must be derived from a time based uuid to be used within Foundry."""


TraceState = str
"""The W3C Trace Context `tracestate` header value, which is used to propagate vendor specific distributed tracing information for Foundry telemetry. See https://www.w3.org/TR/trace-context/#tracestate-header for more details."""


class UnsupportedType(core.ModelBase):
    """UnsupportedType"""

    unsupported_type: str = pydantic.Field(alias=str("unsupportedType"))  # type: ignore[literal-required]
    type: typing.Literal["unsupported"] = "unsupported"


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
    "FoundryBranch",
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
    "TraceParent",
    "TraceState",
    "UnsupportedType",
]
