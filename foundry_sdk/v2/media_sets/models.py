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
from foundry_sdk.v2.core import models as core_models


class AffineTransform(core.ModelBase):
    """An affine transformation for geo-referencing."""

    x_translate: typing.Optional[float] = pydantic.Field(alias=str("xTranslate"), default=None)  # type: ignore[literal-required]
    x_scale: typing.Optional[float] = pydantic.Field(alias=str("xScale"), default=None)  # type: ignore[literal-required]
    x_shear: typing.Optional[float] = pydantic.Field(alias=str("xShear"), default=None)  # type: ignore[literal-required]
    y_translate: typing.Optional[float] = pydantic.Field(alias=str("yTranslate"), default=None)  # type: ignore[literal-required]
    y_shear: typing.Optional[float] = pydantic.Field(alias=str("yShear"), default=None)  # type: ignore[literal-required]
    y_scale: typing.Optional[float] = pydantic.Field(alias=str("yScale"), default=None)  # type: ignore[literal-required]


AudioDecodeFormat = typing.Literal["FLAC", "MP2", "MP3", "MP4", "NIST_SPHERE", "OGG", "WAV", "WEBM"]
"""The format of an audio media item."""


class AudioMediaItemMetadata(core.ModelBase):
    """Metadata for audio media items."""

    format: AudioDecodeFormat
    specification: AudioSpecification
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["audio"] = "audio"


class AudioSpecification(core.ModelBase):
    """Technical specifications for audio media items."""

    bit_rate: int = pydantic.Field(alias=str("bitRate"))  # type: ignore[literal-required]
    """Approximate (average) bits per second of the audio, rounded up in case of a fractional average bits per second."""

    duration_seconds: float = pydantic.Field(alias=str("durationSeconds"))  # type: ignore[literal-required]
    """Approximate duration of the audio, in seconds with up to two decimal digits (rounded up)."""

    number_of_channels: typing.Optional[int] = pydantic.Field(alias=str("numberOfChannels"), default=None)  # type: ignore[literal-required]
    """Number of audio channels in the audio stream."""


class BandInfo(core.ModelBase):
    """Information about a band in an image."""

    data_type: typing.Optional[DataType] = pydantic.Field(alias=str("dataType"), default=None)  # type: ignore[literal-required]
    color_interpretation: typing.Optional[ColorInterpretation] = pydantic.Field(alias=str("colorInterpretation"), default=None)  # type: ignore[literal-required]
    palette_interpretation: typing.Optional[PaletteInterpretation] = pydantic.Field(alias=str("paletteInterpretation"), default=None)  # type: ignore[literal-required]
    unit_interpretation: typing.Optional[UnitInterpretation] = pydantic.Field(alias=str("unitInterpretation"), default=None)  # type: ignore[literal-required]


BranchName = str
"""
A name for a media set branch. Valid branch names must be (a) non-empty, (b) less than 256 characters, and 
(c) not a valid ResourceIdentifier.
"""


BranchRid = core.RID
"""A resource identifier that identifies a branch of a media set."""


ColorInterpretation = typing.Literal[
    "UNDEFINED",
    "GRAY",
    "PALETTE_INDEX",
    "RED",
    "GREEN",
    "BLUE",
    "ALPHA",
    "HUE",
    "SATURATION",
    "LIGHTNESS",
    "CYAN",
    "MAGENTA",
    "YELLOW",
    "BLACK",
    "Y_CB_CR_SPACE_Y",
    "Y_CB_CR_SPACE_CB",
    "Y_CB_CR_SPACE_CR",
]
"""The color interpretation of a band."""


class CommonDicomDataElements(core.ModelBase):
    """Common DICOM data elements."""

    number_frames: typing.Optional[int] = pydantic.Field(alias=str("numberFrames"), default=None)  # type: ignore[literal-required]
    """The number of frames in the DICOM file."""

    modality: typing.Optional[Modality] = None
    patient_id: typing.Optional[str] = pydantic.Field(alias=str("patientId"), default=None)  # type: ignore[literal-required]
    """The patient ID."""

    study_id: typing.Optional[str] = pydantic.Field(alias=str("studyId"), default=None)  # type: ignore[literal-required]
    """The study ID."""

    study_uid: typing.Optional[str] = pydantic.Field(alias=str("studyUid"), default=None)  # type: ignore[literal-required]
    """The study UID."""

    series_uid: typing.Optional[str] = pydantic.Field(alias=str("seriesUid"), default=None)  # type: ignore[literal-required]
    """The series UID."""

    study_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("studyTime"), default=None)  # type: ignore[literal-required]
    """The study time."""

    series_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("seriesTime"), default=None)  # type: ignore[literal-required]
    """The series time."""


class CoordinateReferenceSystem(core.ModelBase):
    """The coordinate reference system for geo-referenced imagery."""

    wkt: typing.Optional[str] = None
    """The Well-Known Text representation of the CRS."""


DataType = typing.Literal[
    "UNDEFINED",
    "BYTE",
    "UINT16",
    "INT16",
    "UINT32",
    "INT32",
    "FLOAT32",
    "FLOAT64",
    "COMPLEX_INT16",
    "COMPLEX_INT32",
    "COMPLEX_FLOAT32",
    "COMPLEX_FLOAT64",
    "UINT64",
    "INT64",
    "INT8",
]
"""The data type of a band."""


DicomDataElementKey = str
"""The key of a DICOM data element."""


class DicomMediaItemMetadata(core.ModelBase):
    """Metadata for DICOM (Digital Imaging and Communications in Medicine) media items."""

    meta_information: DicomMetaInformation = pydantic.Field(alias=str("metaInformation"))  # type: ignore[literal-required]
    media_type: DicomMediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]
    common_data_elements: CommonDicomDataElements = pydantic.Field(alias=str("commonDataElements"))  # type: ignore[literal-required]
    other_data_elements: typing.Dict[DicomDataElementKey, typing.Any] = pydantic.Field(alias=str("otherDataElements"))  # type: ignore[literal-required]
    """
    The data elements for a particular DICOM file outside of the media contained within it and the
    data elements within the commonDataElements field.
    """

    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["dicom"] = "dicom"


DicomMediaType = typing.Literal["IMAGE", "MULTI_FRAME_IMAGE", "VIDEO", "STRUCTURED_REPORT"]
"""The type of DICOM media."""


class DicomMetaInformationV1(core.ModelBase):
    """DICOM meta information version 1."""

    media_storage_sop: str = pydantic.Field(alias=str("mediaStorageSop"))  # type: ignore[literal-required]
    """
    The Media Storage SOP (Service-Object Pair) Class UID, which identifies 
    the type of DICOM object stored (e.g., CT Image, MR Image).
    """

    media_storage_sop_instance: str = pydantic.Field(alias=str("mediaStorageSopInstance"))  # type: ignore[literal-required]
    """The Media Storage SOP Instance UID."""

    transfer_syntax: str = pydantic.Field(alias=str("transferSyntax"))  # type: ignore[literal-required]
    """
    The Transfer Syntax UID, which specifies how the DICOM data is encoded 
    (e.g., compression method, byte ordering).
    """

    type: typing.Literal["v1"] = "v1"


class Dimensions(core.ModelBase):
    """The dimensions of an image."""

    width: int
    """The width of the image in pixels."""

    height: int
    """The height of the image in pixels."""


DocumentDecodeFormat = typing.Literal["PDF", "DOCX", "TXT", "PPTX"]
"""The format of a document media item."""


class DocumentMediaItemMetadata(core.ModelBase):
    """Metadata for document media items."""

    format: DocumentDecodeFormat
    pages: typing.Optional[int] = None
    """The number of pages in the document."""

    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    title: typing.Optional[str] = None
    """The title of the document, if available."""

    author: typing.Optional[str] = None
    """The author of the document, if available."""

    type: typing.Literal["document"] = "document"


class EmailAttachment(core.ModelBase):
    """Metadata about an email attachment."""

    attachment_index: int = pydantic.Field(alias=str("attachmentIndex"))  # type: ignore[literal-required]
    """The index of the attachment in the email."""

    file_name: typing.Optional[str] = pydantic.Field(alias=str("fileName"), default=None)  # type: ignore[literal-required]
    """The file name of the attachment, if available."""

    mime_type: str = pydantic.Field(alias=str("mimeType"))  # type: ignore[literal-required]
    """The verified MIME type of the attachment."""


EmailDecodeFormat = typing.Literal["EML"]
"""The format of an email media item."""


class EmailMediaItemMetadata(core.ModelBase):
    """Metadata for email media items."""

    format: EmailDecodeFormat
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    sender: typing.List[Mailbox]
    """The sender(s) of the email."""

    date: core.AwareDatetime
    """The date the email was sent."""

    attachment_count: int = pydantic.Field(alias=str("attachmentCount"))  # type: ignore[literal-required]
    """The number of attachments in the email."""

    to: typing.List[MailboxOrGroup]
    """The recipient(s) of the email."""

    cc: typing.List[MailboxOrGroup]
    """The CC recipient(s) of the email."""

    subject: typing.Optional[str] = None
    """The subject of the email."""

    attachments: typing.List[EmailAttachment]
    """The attachments of the email."""

    type: typing.Literal["email"] = "email"


FlipAxis = typing.Literal["HORIZONTAL", "VERTICAL", "UNKNOWN"]
"""The flip axis from EXIF orientation."""


class GcpList(core.ModelBase):
    """A list of ground control points for geo-referencing."""

    gcps: typing.List[GroundControlPoint]


class GeoMetadata(core.ModelBase):
    """Embedded geo-referencing data for an image."""

    crs: typing.Optional[CoordinateReferenceSystem] = None
    geotransform: typing.Optional[AffineTransform] = None
    gcp_info: typing.Optional[GcpList] = pydantic.Field(alias=str("gcpInfo"), default=None)  # type: ignore[literal-required]
    gps_data: typing.Optional[GpsMetadata] = pydantic.Field(alias=str("gpsData"), default=None)  # type: ignore[literal-required]


class GetMediaItemInfoResponse(core.ModelBase):
    """GetMediaItemInfoResponse"""

    view_rid: core_models.MediaSetViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]
    path: typing.Optional[core_models.MediaItemPath] = None
    logical_timestamp: LogicalTimestamp = pydantic.Field(alias=str("logicalTimestamp"))  # type: ignore[literal-required]
    attribution: typing.Optional[MediaAttribution] = None


class GetMediaItemRidByPathResponse(core.ModelBase):
    """GetMediaItemRidByPathResponse"""

    media_item_rid: typing.Optional[core_models.MediaItemRid] = pydantic.Field(alias=str("mediaItemRid"), default=None)  # type: ignore[literal-required]


class GpsMetadata(core.ModelBase):
    """GPS location metadata extracted from EXIF data embedded in the image."""

    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    altitude: typing.Optional[float] = None


class GroundControlPoint(core.ModelBase):
    """A ground control point for geo-referencing."""

    pix_x: typing.Optional[float] = pydantic.Field(alias=str("pixX"), default=None)  # type: ignore[literal-required]
    """The pixel X coordinate."""

    pix_y: typing.Optional[float] = pydantic.Field(alias=str("pixY"), default=None)  # type: ignore[literal-required]
    """The pixel Y coordinate."""

    proj_x: typing.Optional[float] = pydantic.Field(alias=str("projX"), default=None)  # type: ignore[literal-required]
    """The projected X coordinate."""

    proj_y: typing.Optional[float] = pydantic.Field(alias=str("projY"), default=None)  # type: ignore[literal-required]
    """The projected Y coordinate."""

    proj_z: typing.Optional[float] = pydantic.Field(alias=str("projZ"), default=None)  # type: ignore[literal-required]
    """The projected Z coordinate."""


class Group(core.ModelBase):
    """A named group of mailboxes."""

    group_name: str = pydantic.Field(alias=str("groupName"))  # type: ignore[literal-required]
    """The name of the group."""

    mailboxes: typing.List[Mailbox]
    """The mailboxes in the group."""


class GroupWrapper(core.ModelBase):
    """A wrapper for a group in the MailboxOrGroup union."""

    group: Group
    type: typing.Literal["group"] = "group"


ImageAttributeDomain = str
"""The domain of an image attribute."""


ImageAttributeKey = str
"""The key of an image attribute within a domain."""


ImageryDecodeFormat = typing.Literal["BMP", "TIFF", "NITF", "JP2K", "JPG", "PNG", "WEBP"]
"""The format of an imagery media item."""


class ImageryMediaItemMetadata(core.ModelBase):
    """Metadata for imagery (image) media items."""

    format: ImageryDecodeFormat
    dimensions: typing.Optional[Dimensions] = None
    bands: typing.List[BandInfo]
    """Information about the bands of the image, if available."""

    attributes: typing.Dict[ImageAttributeDomain, typing.Dict[ImageAttributeKey, str]]
    """
    The metadata attributes described in the image header in the form of a map <domain, <key, value>>.
    For the default domain, or when the domain is not specified, the domain key will be the empty string ("").
    """

    icc_profile: typing.Optional[str] = pydantic.Field(alias=str("iccProfile"), default=None)  # type: ignore[literal-required]
    """The base64-encoded ICC profile for the image, if available."""

    geo: typing.Optional[GeoMetadata] = None
    pages: typing.Optional[int] = None
    """
    The number of pages associated with this image. Usually 1, but may be more for some formats
    (multi-page TIFFs, for example).
    """

    orientation: typing.Optional[Orientation] = None
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["imagery"] = "imagery"


LogicalTimestamp = core.Long
"""
A number representing a logical ordering to be used for transactions, etc.
This can be interpreted as a timestamp in microseconds, but may differ slightly from system clock time due 
to clock drift and slight adjustments for the sake of ordering.

Only positive timestamps (representing times after epoch) are supported.
"""


class Mailbox(core.ModelBase):
    """An email mailbox with an optional display name and email address."""

    display_name: typing.Optional[str] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    """The display name of the mailbox."""

    email_address: str = pydantic.Field(alias=str("emailAddress"))  # type: ignore[literal-required]
    """The email address of the mailbox."""


MailboxOrGroup = typing_extensions.Annotated[
    typing.Union["MailboxWrapper", "GroupWrapper"], pydantic.Field(discriminator="type")
]
"""Either a mailbox or a group of mailboxes."""


class MailboxWrapper(core.ModelBase):
    """A wrapper for a mailbox in the MailboxOrGroup union."""

    mailbox: Mailbox
    type: typing.Literal["mailbox"] = "mailbox"


class MediaAttribution(core.ModelBase):
    """MediaAttribution"""

    creator_id: core_models.UserId = pydantic.Field(alias=str("creatorId"))  # type: ignore[literal-required]
    creation_timestamp: core.AwareDatetime = pydantic.Field(alias=str("creationTimestamp"))  # type: ignore[literal-required]
    """The timestamp when the media item was created, in ISO 8601 timestamp format."""


MediaItemMetadata = typing_extensions.Annotated[
    typing.Union[
        "DocumentMediaItemMetadata",
        "ImageryMediaItemMetadata",
        "SpreadsheetMediaItemMetadata",
        "UntypedMediaItemMetadata",
        "AudioMediaItemMetadata",
        "VideoMediaItemMetadata",
        "DicomMediaItemMetadata",
        "EmailMediaItemMetadata",
    ],
    pydantic.Field(discriminator="type"),
]
"""
Detailed metadata about a media item, including type-specific information such as dimensions for images,
duration for audio/video, page count for documents, etc.
"""


MediaItemXmlFormat = typing.Literal["DOCX", "XLSX", "PPTX"]
"""Format of the media item attempted to be decoded based on the XML structure."""


Modality = typing.Literal[
    "AR",
    "ASMT",
    "AU",
    "BDUS",
    "BI",
    "BMD",
    "CR",
    "CT",
    "CTPROTOCOL",
    "DG",
    "DOC",
    "DX",
    "ECG",
    "EPS",
    "ES",
    "FID",
    "GM",
    "HC",
    "HD",
    "IO",
    "IOL",
    "IVOCT",
    "IVUS",
    "KER",
    "KO",
    "LEN",
    "LS",
    "MG",
    "MR",
    "M3D",
    "NM",
    "OAM",
    "OCT",
    "OP",
    "OPM",
    "OPT",
    "OPTBSV",
    "OPTENF",
    "OPV",
    "OSS",
    "OT",
    "PLAN",
    "PR",
    "PT",
    "PX",
    "REG",
    "RESP",
    "RF",
    "RG",
    "RTDOSE",
    "RTIMAGE",
    "RTINTENT",
    "RTPLAN",
    "RTRAD",
    "RTRECORD",
    "RTSEGANN",
    "RTSTRUCT",
    "RWV",
    "SEG",
    "SM",
    "SMR",
    "SR",
    "SRF",
    "STAIN",
    "TEXTUREMAP",
    "TG",
    "US",
    "VA",
    "XA",
    "XC",
    "AS",
    "CD",
    "CF",
    "CP",
    "CS",
    "DD",
    "DF",
    "DM",
    "DS",
    "EC",
    "FA",
    "FS",
    "LP",
    "MA",
    "MS",
    "OPR",
    "ST",
    "VF",
]
"""
DICOM modality code. A list of modalities and their meanings can be found in the DICOM specification. 
https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.3.html#sect_C.7.3.1.1.1
"""


class Orientation(core.ModelBase):
    """The orientation information as encoded in EXIF metadata."""

    rotation_angle: typing.Optional[RotationAngle] = pydantic.Field(alias=str("rotationAngle"), default=None)  # type: ignore[literal-required]
    flip_axis: typing.Optional[FlipAxis] = pydantic.Field(alias=str("flipAxis"), default=None)  # type: ignore[literal-required]


PaletteInterpretation = typing.Literal["GRAY", "RGB", "RGBA", "CMYK", "HLS"]
"""The palette interpretation of a band."""


class PutMediaItemResponse(core.ModelBase):
    """PutMediaItemResponse"""

    media_item_rid: core_models.MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]


RotationAngle = typing.Literal["DEGREE_90", "DEGREE_180", "DEGREE_270", "UNKNOWN"]
"""The rotation angle from EXIF orientation."""


SpreadsheetDecodeFormat = typing.Literal["XLSX"]
"""The format of a spreadsheet media item."""


class SpreadsheetMediaItemMetadata(core.ModelBase):
    """Metadata for spreadsheet media items."""

    format: SpreadsheetDecodeFormat
    sheet_names: typing.List[str] = pydantic.Field(alias=str("sheetNames"))  # type: ignore[literal-required]
    """The names of the sheets in the spreadsheet."""

    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    title: typing.Optional[str] = None
    """The title of the spreadsheet, if available."""

    author: typing.Optional[str] = None
    """The author of the spreadsheet, if available."""

    type: typing.Literal["spreadsheet"] = "spreadsheet"


class TrackedTransformationFailedResponse(core.ModelBase):
    """TrackedTransformationFailedResponse"""

    type: typing.Literal["failed"] = "failed"


class TrackedTransformationPendingResponse(core.ModelBase):
    """TrackedTransformationPendingResponse"""

    type: typing.Literal["pending"] = "pending"


TrackedTransformationResponse = typing_extensions.Annotated[
    typing.Union[
        "TrackedTransformationPendingResponse",
        "TrackedTransformationFailedResponse",
        "TrackedTransformationSuccessfulResponse",
    ],
    pydantic.Field(discriminator="type"),
]
"""TrackedTransformationResponse"""


class TrackedTransformationSuccessfulResponse(core.ModelBase):
    """TrackedTransformationSuccessfulResponse"""

    type: typing.Literal["successful"] = "successful"


TransactionId = core.UUID
"""An identifier which represents a transaction on a media set."""


class UnitInterpretation(core.ModelBase):
    """The unit interpretation for a band."""

    unit: typing.Optional[str] = None
    scale: typing.Optional[float] = None
    offset: typing.Optional[float] = None


class UntypedMediaItemMetadata(core.ModelBase):
    """Metadata for untyped media items (media items without a recognized type)."""

    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["untyped"] = "untyped"


VideoDecodeFormat = typing.Literal["MP4", "MKV", "MOV", "TS"]
"""The format of a video media item."""


class VideoMediaItemMetadata(core.ModelBase):
    """Metadata for video media items."""

    format: VideoDecodeFormat
    specification: VideoSpecification
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["video"] = "video"


class VideoSpecification(core.ModelBase):
    """Technical specifications for video media items."""

    bit_rate: int = pydantic.Field(alias=str("bitRate"))  # type: ignore[literal-required]
    """Approximate (average) bits per second of the video, rounded up in case of a fractional average bits per second."""

    duration_seconds: float = pydantic.Field(alias=str("durationSeconds"))  # type: ignore[literal-required]
    """Approximate duration of the video, in seconds with up to two decimal digits (rounded up)."""


DicomMetaInformation = DicomMetaInformationV1
"""DICOM meta information."""


core.resolve_forward_references(MailboxOrGroup, globalns=globals(), localns=locals())
core.resolve_forward_references(MediaItemMetadata, globalns=globals(), localns=locals())
core.resolve_forward_references(TrackedTransformationResponse, globalns=globals(), localns=locals())

__all__ = [
    "AffineTransform",
    "AudioDecodeFormat",
    "AudioMediaItemMetadata",
    "AudioSpecification",
    "BandInfo",
    "BranchName",
    "BranchRid",
    "ColorInterpretation",
    "CommonDicomDataElements",
    "CoordinateReferenceSystem",
    "DataType",
    "DicomDataElementKey",
    "DicomMediaItemMetadata",
    "DicomMediaType",
    "DicomMetaInformation",
    "DicomMetaInformationV1",
    "Dimensions",
    "DocumentDecodeFormat",
    "DocumentMediaItemMetadata",
    "EmailAttachment",
    "EmailDecodeFormat",
    "EmailMediaItemMetadata",
    "FlipAxis",
    "GcpList",
    "GeoMetadata",
    "GetMediaItemInfoResponse",
    "GetMediaItemRidByPathResponse",
    "GpsMetadata",
    "GroundControlPoint",
    "Group",
    "GroupWrapper",
    "ImageAttributeDomain",
    "ImageAttributeKey",
    "ImageryDecodeFormat",
    "ImageryMediaItemMetadata",
    "LogicalTimestamp",
    "Mailbox",
    "MailboxOrGroup",
    "MailboxWrapper",
    "MediaAttribution",
    "MediaItemMetadata",
    "MediaItemXmlFormat",
    "Modality",
    "Orientation",
    "PaletteInterpretation",
    "PutMediaItemResponse",
    "RotationAngle",
    "SpreadsheetDecodeFormat",
    "SpreadsheetMediaItemMetadata",
    "TrackedTransformationFailedResponse",
    "TrackedTransformationPendingResponse",
    "TrackedTransformationResponse",
    "TrackedTransformationSuccessfulResponse",
    "TransactionId",
    "UnitInterpretation",
    "UntypedMediaItemMetadata",
    "VideoDecodeFormat",
    "VideoMediaItemMetadata",
    "VideoSpecification",
]
