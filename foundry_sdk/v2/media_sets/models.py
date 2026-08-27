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


class AnnotateImageOperation(core.ModelBase):
    """Annotates an image with bounding boxes, labels, and colors."""

    annotations: typing.List[Annotation]
    """The list of annotations to draw on the image."""

    type: typing.Literal["annotate"] = "annotate"


class Annotation(core.ModelBase):
    """An annotation to draw on an image."""

    geometry: AnnotateGeometry
    label: typing.Optional[str] = None
    """An optional text label to display with the annotation."""

    color: typing.Optional[Color] = None
    thickness: typing.Optional[float] = None
    """The thickness of the annotation lines."""

    font_size: typing.Optional[int] = pydantic.Field(alias=str("fontSize"), default=None)  # type: ignore[literal-required]
    """The font size for the label text."""


class ApiNameLocatorWrapper(core.ModelBase):
    """Wrapper for API name-based model locator."""

    api_name: str = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    """The API name of the language model."""

    type: typing.Literal["apiName"] = "apiName"


class AudioChannelOperation(core.ModelBase):
    """Selects a specific channel from multi-channel audio."""

    encode_format: AudioEncodeFormat = pydantic.Field(alias=str("encodeFormat"))  # type: ignore[literal-required]
    channel: int
    """The channel number to select."""

    type: typing.Literal["channel"] = "channel"


class AudioChunkOperation(core.ModelBase):
    """Chunks audio into smaller segments of the specified duration."""

    chunk_duration_milliseconds: int = pydantic.Field(alias=str("chunkDurationMilliseconds"))  # type: ignore[literal-required]
    """Duration of each chunk in milliseconds."""

    encode_format: AudioEncodeFormat = pydantic.Field(alias=str("encodeFormat"))  # type: ignore[literal-required]
    chunk_index: int = pydantic.Field(alias=str("chunkIndex"))  # type: ignore[literal-required]
    """The chunk index to retain."""

    type: typing.Literal["chunk"] = "chunk"


AudioDecodeFormat: typing_extensions.TypeAlias = typing.Literal[
    "FLAC", "MP2", "MP3", "MP4", "NIST_SPHERE", "OGG", "WAV", "WEBM"
]
"""The format of an audio media item."""


AudioEncodeFormat: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["Mp3Format", "WavEncodeFormat", "TsAudioContainerFormat"],
    pydantic.Field(discriminator="type"),
]
"""The output format for encoding audio."""


class AudioMediaItemMetadata(core.ModelBase):
    """Metadata for audio media items."""

    format: AudioDecodeFormat
    specification: AudioSpecification
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["audio"] = "audio"


AudioOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["AudioChannelOperation", "AudioChunkOperation", "ConvertAudioOperation"],
    pydantic.Field(discriminator="type"),
]
"""The operation to perform on audio."""


class AudioSpecification(core.ModelBase):
    """Technical specifications for audio media items."""

    bit_rate: int = pydantic.Field(alias=str("bitRate"))  # type: ignore[literal-required]
    """Approximate (average) bits per second of the audio, rounded up in case of a fractional average bits per second."""

    duration_seconds: float = pydantic.Field(alias=str("durationSeconds"))  # type: ignore[literal-required]
    """Approximate duration of the audio, in seconds with up to two decimal digits (rounded up)."""

    number_of_channels: typing.Optional[int] = pydantic.Field(alias=str("numberOfChannels"), default=None)  # type: ignore[literal-required]
    """Number of audio channels in the audio stream."""


AudioToTextOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["TranscribeOperation", "WaveformOperation"], pydantic.Field(discriminator="type")
]
"""The operation to perform for audio to text conversion."""


class AudioToTextTransformation(core.ModelBase):
    """Converts audio to text."""

    operation: AudioToTextOperation
    type: typing.Literal["audioToText"] = "audioToText"


class AudioTransformation(core.ModelBase):
    """Transforms audio media items."""

    operation: AudioOperation
    type: typing.Literal["audio"] = "audio"


AvailableEmbeddingModelIds: typing_extensions.TypeAlias = typing.Literal["GOOGLE_SIGLIP_2"]
"""Available embedding models that can be used with the service."""


class BandInfo(core.ModelBase):
    """Information about a band in an image."""

    data_type: typing.Optional[DataType] = pydantic.Field(alias=str("dataType"), default=None)  # type: ignore[literal-required]
    color_interpretation: typing.Optional[ColorInterpretation] = pydantic.Field(alias=str("colorInterpretation"), default=None)  # type: ignore[literal-required]
    palette_interpretation: typing.Optional[PaletteInterpretation] = pydantic.Field(alias=str("paletteInterpretation"), default=None)  # type: ignore[literal-required]
    unit_interpretation: typing.Optional[UnitInterpretation] = pydantic.Field(alias=str("unitInterpretation"), default=None)  # type: ignore[literal-required]


class BatchTransactionsTransactionPolicy(core.ModelBase):
    """
    All writes must be part of a transaction. Transactions are branch-scoped and created by calling
    create transaction. Writes are not visible until commit transaction is called.
    """

    type: typing.Literal["batchTransactions"] = "batchTransactions"


class BoundingBox(core.ModelBase):
    """A rectangular bounding box for annotations."""

    left: float
    """The left coordinate of the bounding box."""

    top: float
    """The top coordinate of the bounding box."""

    width: float
    """The width of the bounding box."""

    height: float
    """The height of the bounding box."""


class BoundingBoxGeometry(core.ModelBase):
    """A rectangular bounding box geometry for annotations."""

    bounding_box: BoundingBox = pydantic.Field(alias=str("boundingBox"))  # type: ignore[literal-required]
    type: typing.Literal["boundingBox"] = "boundingBox"


BranchName: typing_extensions.TypeAlias = str
"""
A name for a media set branch. Valid branch names must be (a) non-empty, (b) less than 256 characters, and 
(c) not a valid ResourceIdentifier.
"""


BranchRid: typing_extensions.TypeAlias = core.RID
"""A resource identifier that identifies a branch of a media set."""


CadDecodeFormat: typing_extensions.TypeAlias = typing.Literal["STEP"]
"""The format of a CAD media item."""


class CadMediaItemMetadata(core.ModelBase):
    """Metadata for CAD media items."""

    format: CadDecodeFormat
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    units: typing.Optional[CadUnits] = None
    type: typing.Literal["cad"] = "cad"


class CadUnits(core.ModelBase):
    """Units declared in a CAD file."""

    length_unit: typing.Optional[str] = pydantic.Field(alias=str("lengthUnit"), default=None)  # type: ignore[literal-required]
    """
    Raw declared length unit name, for example MILLIMETRE, METRE, INCH, or FOOT. Consumers should match
    case-insensitively and tolerate unknown values.
    """


class ChatLlmSpec(core.ModelBase):
    """Standard chat-based LLM specification with system and user prompts."""

    model_locator: LanguageModelLocator = pydantic.Field(alias=str("modelLocator"))  # type: ignore[literal-required]
    system_prompt: str = pydantic.Field(alias=str("systemPrompt"))  # type: ignore[literal-required]
    """System prompt for the LLM."""

    user_prompt: str = pydantic.Field(alias=str("userPrompt"))  # type: ignore[literal-required]
    """User prompt for the LLM."""

    max_tokens: typing.Optional[int] = pydantic.Field(alias=str("maxTokens"), default=None)  # type: ignore[literal-required]
    """Maximum number of tokens per request to generate."""


class ChatLlmSpecWrapper(core.ModelBase):
    """Wrapper for chat-based LLM specification."""

    chat: ChatLlmSpec
    type: typing.Literal["chat"] = "chat"


class Color(core.ModelBase):
    """An RGBA color value."""

    r: int
    """Red component (0-255)."""

    g: int
    """Green component (0-255)."""

    b: int
    """Blue component (0-255)."""

    a: typing.Optional[float] = None
    """Alpha component (0-1, where 0 is transparent and 1 is opaque)."""


ColorInterpretation: typing_extensions.TypeAlias = typing.Literal[
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


class ContrastBinarize(core.ModelBase):
    """Binarize contrast operation."""

    threshold: typing.Optional[int] = None
    """
    The threshold value (0-255). Pixels with intensity below this value become black,
    others become white. If not specified, the threshold is computed automatically.
    """

    type: typing.Literal["binarize"] = "binarize"


class ContrastEqualize(core.ModelBase):
    """Equalizes the histogram of an image to improve contrast."""

    type: typing.Literal["equalize"] = "equalize"


class ContrastImageOperation(core.ModelBase):
    """Applies contrast adjustments to an image."""

    contrast_type: ContrastType = pydantic.Field(alias=str("contrastType"))  # type: ignore[literal-required]
    type: typing.Literal["contrast"] = "contrast"


class ContrastRayleigh(core.ModelBase):
    """Applies Rayleigh distribution-based contrast adjustment."""

    sigma: float
    """The scaling parameter for the Rayleigh distribution (0-1)."""

    type: typing.Literal["rayleigh"] = "rayleigh"


ContrastType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["ContrastEqualize", "ContrastRayleigh", "ContrastBinarize"],
    pydantic.Field(discriminator="type"),
]
"""The type of contrast adjustment to apply."""


class ConvertAudioOperation(core.ModelBase):
    """Converts audio to the specified format."""

    encode_format: AudioEncodeFormat = pydantic.Field(alias=str("encodeFormat"))  # type: ignore[literal-required]
    type: typing.Literal["convert"] = "convert"


class ConvertDocumentOperation(core.ModelBase):
    """Converts a document to PDF format."""

    type: typing.Literal["convertDocument"] = "convertDocument"


class ConvertSheetToJsonOperation(core.ModelBase):
    """Converts a specified sheet to JSON format."""

    sheet_name: str = pydantic.Field(alias=str("sheetName"))  # type: ignore[literal-required]
    """The sheet name."""

    type: typing.Literal["convertSheetToJson"] = "convertSheetToJson"


class CoordinateReferenceSystem(core.ModelBase):
    """The coordinate reference system for geo-referenced imagery."""

    wkt: typing.Optional[str] = None
    """The Well-Known Text representation of the CRS."""


class CreatePdfOperation(core.ModelBase):
    """Converts an image to a PDF document."""

    type: typing.Literal["createPdf"] = "createPdf"


class CropConfig(core.ModelBase):
    """Configuration for table cropping."""

    table_prompt: str = pydantic.Field(alias=str("tablePrompt"))  # type: ignore[literal-required]
    """Prompt for table extraction."""


class CropImageOperation(core.ModelBase):
    """Crops an image to a rectangular sub-window."""

    x_offset: int = pydantic.Field(alias=str("xOffset"))  # type: ignore[literal-required]
    """The x offset in pixels from the left hand side of the image."""

    y_offset: int = pydantic.Field(alias=str("yOffset"))  # type: ignore[literal-required]
    """The y offset in pixels from the top of the image."""

    width: int
    """The width of the cropping box in pixels."""

    height: int
    """The height of the cropping box in pixels."""

    type: typing.Literal["crop"] = "crop"


DataType: typing_extensions.TypeAlias = typing.Literal[
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


class DecryptImageOperation(core.ModelBase):
    """Decrypts bounding boxes in an image using a commutative encryption algorithm."""

    polygons: typing.List[ImageRegionPolygon]
    """The polygons defining the regions to decrypt."""

    cipher_license_rid: core.RID = pydantic.Field(alias=str("cipherLicenseRid"))  # type: ignore[literal-required]
    """The resource identifier for the cipher license."""

    type: typing.Literal["decrypt"] = "decrypt"


DicomDataElementKey: typing_extensions.TypeAlias = str
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


DicomMediaType: typing_extensions.TypeAlias = typing.Literal[
    "IMAGE", "MULTI_FRAME_IMAGE", "VIDEO", "STRUCTURED_REPORT"
]
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


class DicomToImageTransformation(core.ModelBase):
    """Renders DICOM (Digital Imaging and Communications in Medicine) files as images."""

    encoding: ImageryEncodeFormat
    operation: DicomToImageOperation
    type: typing.Literal["dicomToImage"] = "dicomToImage"


class Dimensions(core.ModelBase):
    """The dimensions of an image."""

    width: int
    """The width of the image in pixels."""

    height: int
    """The height of the image in pixels."""


DocumentDecodeFormat: typing_extensions.TypeAlias = typing.Literal[
    "PDF", "DOC", "DOCX", "TXT", "PPTX", "RTF"
]
"""The format of a document media item."""


class DocumentExtractLayoutAwareContentOperation(core.ModelBase):
    """Extracts content from a document with layout information preserved."""

    parameters: LayoutAwareExtractionParameters
    type: typing.Literal["extractLayoutAwareContent"] = "extractLayoutAwareContent"


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


DocumentToDocumentOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["SlicePdfRangeOperation", "ConvertDocumentOperation"],
    pydantic.Field(discriminator="type"),
]
"""The operation to perform for document to document conversion."""


class DocumentToDocumentTransformation(core.ModelBase):
    """Transforms documents to documents."""

    encoding: DocumentEncodeFormat
    operation: DocumentToDocumentOperation
    type: typing.Literal["documentToDocument"] = "documentToDocument"


DocumentToImageOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["RenderPageToFitBoundingBoxOperation", "RenderPageOperation"],
    pydantic.Field(discriminator="type"),
]
"""The operation to perform for document to image conversion."""


class DocumentToImageTransformation(core.ModelBase):
    """Renders document pages as images."""

    encoding: ImageryEncodeFormat
    operation: DocumentToImageOperation
    type: typing.Literal["documentToImage"] = "documentToImage"


DocumentToTextOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ExtractTableOfContentsOperation",
        "GetPdfPageDimensionsOperation",
        "ExtractAllTextOperation",
        "ExtractVlmTextOperation",
        "ExtractTextFromPagesToArrayOperation",
        "OcrOnPageOperation",
        "ExtractFormFieldsOperation",
        "ExtractDocumentLayoutAwareTextV2Operation",
        "ExtractDocumentTextV2Operation",
        "ExtractUnstructuredTextFromPageOperation",
        "DocumentExtractLayoutAwareContentOperation",
        "OcrOnPagesOperation",
    ],
    pydantic.Field(discriminator="type"),
]
"""The operation to perform for document to text conversion."""


class DocumentToTextTransformation(core.ModelBase):
    """Extracts text from documents."""

    operation: DocumentToTextOperation
    type: typing.Literal["documentToText"] = "documentToText"


class EmailAttachment(core.ModelBase):
    """Metadata about an email attachment."""

    attachment_index: int = pydantic.Field(alias=str("attachmentIndex"))  # type: ignore[literal-required]
    """The index of the attachment in the email."""

    file_name: typing.Optional[str] = pydantic.Field(alias=str("fileName"), default=None)  # type: ignore[literal-required]
    """The file name of the attachment, if available."""

    mime_type: str = pydantic.Field(alias=str("mimeType"))  # type: ignore[literal-required]
    """The verified MIME type of the attachment."""


EmailDecodeFormat: typing_extensions.TypeAlias = typing.Literal["EML"]
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


class EmailToAttachmentTransformation(core.ModelBase):
    """Extracts attachments from email."""

    operation: EmailToAttachmentOperation
    type: typing.Literal["emailToAttachment"] = "emailToAttachment"


EmailToTextEncodeFormat: typing_extensions.TypeAlias = typing.Literal["TEXT", "HTML"]
"""The output format for email body extraction."""


class EmailToTextTransformation(core.ModelBase):
    """Extracts text content from email."""

    operation: EmailToTextOperation
    type: typing.Literal["emailToText"] = "emailToText"


class EncryptImageOperation(core.ModelBase):
    """Encrypts bounding boxes in an image using a commutative encryption algorithm."""

    polygons: typing.List[ImageRegionPolygon]
    """The polygons defining the regions to encrypt."""

    cipher_license_rid: core.RID = pydantic.Field(alias=str("cipherLicenseRid"))  # type: ignore[literal-required]
    """The resource identifier for the cipher license."""

    type: typing.Literal["encrypt"] = "encrypt"


class ExtractAllTextOperation(core.ModelBase):
    """
    Extracts text across all pages of the document.
    For PDF documents, includes all text. For DocX documents, includes only regular paragraphs.
    """

    type: typing.Literal["extractAllText"] = "extractAllText"


class ExtractAudioOperation(core.ModelBase):
    """Extracts the first audio stream from the video unchanged."""

    type: typing.Literal["extractAudio"] = "extractAudio"


class ExtractDocumentLayoutAwareTextV2Config(core.ModelBase):
    """Configuration for v2 layout-aware document text extraction."""

    format: typing.Optional[TextOutputFormat] = None
    mode: typing.Optional[OcrMode] = None
    languages: typing.List[OcrLanguageOrScript]
    """List of OCR languages or scripts to use."""


class ExtractDocumentLayoutAwareTextV2Operation(core.ModelBase):
    """
    Extract layout aware text with bounding boxes across all pages using the v2 text extraction endpoint.
    This only supports PDFs.
    """

    page_range: typing.Optional[PageRange] = pydantic.Field(alias=str("pageRange"), default=None)  # type: ignore[literal-required]
    config: ExtractDocumentLayoutAwareTextV2Config
    type: typing.Literal["extractLayoutAwareTextV2"] = "extractLayoutAwareTextV2"


class ExtractDocumentTextV2Config(core.ModelBase):
    """Configuration for v2 document text extraction."""

    format: typing.Optional[TextOutputFormat] = None
    mode: typing.Optional[OcrMode] = None
    languages: typing.List[OcrLanguageOrScript]
    """List of OCR languages or scripts to use."""


class ExtractDocumentTextV2Operation(core.ModelBase):
    """
    Extract text across all pages using the v2 text extraction endpoint with per page text.
    This only supports PDFs.
    """

    page_range: typing.Optional[PageRange] = pydantic.Field(alias=str("pageRange"), default=None)  # type: ignore[literal-required]
    config: ExtractDocumentTextV2Config
    type: typing.Literal["extractTextV2"] = "extractTextV2"


class ExtractFirstFrameOperation(core.ModelBase):
    """
    Extracts the first full scene frame from the video.
    If both width and height are not specified, preserves the original size.
    If only one dimension is specified, the other is calculated to preserve aspect ratio.
    """

    height: typing.Optional[int] = None
    """The desired height in pixels."""

    width: typing.Optional[int] = None
    """The desired width in pixels."""

    type: typing.Literal["extractFirstFrame"] = "extractFirstFrame"


class ExtractFormFieldsOperation(core.ModelBase):
    """Extracts form field data from a PDF document."""

    type: typing.Literal["extractFormFields"] = "extractFormFields"


class ExtractFramesAtTimestampsOperation(core.ModelBase):
    """
    Extracts frames from the video at specified timestamps.
    If only one dimension is specified, the other is calculated to preserve aspect ratio.
    """

    height: typing.Optional[int] = None
    """The desired height in pixels."""

    width: typing.Optional[int] = None
    """The desired width in pixels."""

    timestamp: float
    """The timestamp in seconds."""

    type: typing.Literal["extractFramesAtTimestamps"] = "extractFramesAtTimestamps"


class ExtractSceneFramesOperation(core.ModelBase):
    """Extracts all scene frames from a video as images in an archive."""

    encoding: ImageryEncodeFormat
    scene_score: typing.Optional[SceneScore] = pydantic.Field(alias=str("sceneScore"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["extractSceneFrames"] = "extractSceneFrames"


class ExtractTableOfContentsOperation(core.ModelBase):
    """Extracts the table of contents from a document."""

    type: typing.Literal["extractTableOfContents"] = "extractTableOfContents"


class ExtractTextFromPagesToArrayOperation(core.ModelBase):
    """Extracts text from multiple pages into a list of strings."""

    start_page: typing.Optional[int] = pydantic.Field(alias=str("startPage"), default=None)  # type: ignore[literal-required]
    """The zero-indexed start page. Defaults to the first page if not specified."""

    end_page: typing.Optional[int] = pydantic.Field(alias=str("endPage"), default=None)  # type: ignore[literal-required]
    """The zero-indexed end page (inclusive). Defaults to the last page if not specified."""

    type: typing.Literal["extractTextFromPagesToArray"] = "extractTextFromPagesToArray"


class ExtractTextPreprocessingWrapper(core.ModelBase):
    """Wrapper for text extraction preprocessing."""

    extract_text: ExtractDocumentTextV2Config = pydantic.Field(alias=str("extractText"))  # type: ignore[literal-required]
    type: typing.Literal["extractText"] = "extractText"


class ExtractUnstructuredTextFromPageOperation(core.ModelBase):
    """Extracts unstructured text from a specified page."""

    page_number: int = pydantic.Field(alias=str("pageNumber"))  # type: ignore[literal-required]
    """The page number."""

    type: typing.Literal["extractUnstructuredTextFromPage"] = "extractUnstructuredTextFromPage"


class ExtractVlmTextOperation(core.ModelBase):
    """
    Extract text from a document using vision language models (VLMs).
    VLMs can understand document layout and structure more intelligently than traditional OCR.
    """

    llm_spec: LlmSpec = pydantic.Field(alias=str("llmSpec"))  # type: ignore[literal-required]
    preprocessing_configuration: typing.Optional[VlmPreprocessingConfig] = pydantic.Field(alias=str("preprocessingConfiguration"), default=None)  # type: ignore[literal-required]
    image_spec: typing.Optional[ImageSpec] = pydantic.Field(alias=str("imageSpec"), default=None)  # type: ignore[literal-required]
    output_format: VlmOutputFormat = pydantic.Field(alias=str("outputFormat"))  # type: ignore[literal-required]
    page_range: typing.Optional[PageRange] = pydantic.Field(alias=str("pageRange"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["extractVlmText"] = "extractVlmText"


FlipAxis: typing_extensions.TypeAlias = typing.Literal["HORIZONTAL", "VERTICAL", "UNKNOWN"]
"""The flip axis from EXIF orientation."""


class GcpList(core.ModelBase):
    """A list of ground control points for geo-referencing."""

    gcps: typing.List[GroundControlPoint]


class GenerateEmbeddingOperation(core.ModelBase):
    """Generates a vector embedding for an image using the specified model."""

    model_id: AvailableEmbeddingModelIds = pydantic.Field(alias=str("modelId"))  # type: ignore[literal-required]
    type: typing.Literal["generateEmbedding"] = "generateEmbedding"


class GeoMetadata(core.ModelBase):
    """Embedded geo-referencing data for an image."""

    crs: typing.Optional[CoordinateReferenceSystem] = None
    geotransform: typing.Optional[AffineTransform] = None
    gcp_info: typing.Optional[GcpList] = pydantic.Field(alias=str("gcpInfo"), default=None)  # type: ignore[literal-required]
    gps_data: typing.Optional[GpsMetadata] = pydantic.Field(alias=str("gpsData"), default=None)  # type: ignore[literal-required]


class GetEmailAttachmentOperation(core.ModelBase):
    """Retrieves the bytes of an email attachment by index."""

    mime_type: str = pydantic.Field(alias=str("mimeType"))  # type: ignore[literal-required]
    """The MIME type of the attachment. Must match the metadata attachment MIME type."""

    attachment_index: int = pydantic.Field(alias=str("attachmentIndex"))  # type: ignore[literal-required]
    """The attachment index."""

    type: typing.Literal["getEmailAttachment"] = "getEmailAttachment"


class GetEmailBodyOperation(core.ModelBase):
    """Gets the email body in the specified format."""

    output_format: EmailToTextEncodeFormat = pydantic.Field(alias=str("outputFormat"))  # type: ignore[literal-required]
    type: typing.Literal["getEmailBody"] = "getEmailBody"


class GetMediaItemInfoResponse(core.ModelBase):
    """GetMediaItemInfoResponse"""

    view_rid: core_models.MediaSetViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]
    path: typing.Optional[core_models.MediaItemPath] = None
    logical_timestamp: LogicalTimestamp = pydantic.Field(alias=str("logicalTimestamp"))  # type: ignore[literal-required]
    attribution: typing.Optional[MediaAttribution] = None
    originally_uploaded_file_mime_type: typing.Optional[core_models.MediaType] = pydantic.Field(alias=str("originallyUploadedFileMimeType"), default=None)  # type: ignore[literal-required]
    mime_type: typing.Optional[core_models.MediaType] = pydantic.Field(alias=str("mimeType"), default=None)  # type: ignore[literal-required]
    size_bytes: typing.Optional[int] = pydantic.Field(alias=str("sizeBytes"), default=None)  # type: ignore[literal-required]
    """The size of the media item in bytes."""


class GetMediaItemRidByPathResponse(core.ModelBase):
    """GetMediaItemRidByPathResponse"""

    media_item_rid: typing.Optional[core_models.MediaItemRid] = pydantic.Field(alias=str("mediaItemRid"), default=None)  # type: ignore[literal-required]


class GetMediaSetResponse(core.ModelBase):
    """Information about a media set."""

    rid: core_models.MediaSetRid
    media_schema: MediaSchema = pydantic.Field(alias=str("mediaSchema"))  # type: ignore[literal-required]
    default_branch_name: BranchName = pydantic.Field(alias=str("defaultBranchName"))  # type: ignore[literal-required]
    transaction_policy: TransactionPolicy = pydantic.Field(alias=str("transactionPolicy"))  # type: ignore[literal-required]
    paths_required: bool = pydantic.Field(alias=str("pathsRequired"))  # type: ignore[literal-required]
    """Whether media items in this media set require paths."""


class GetPdfPageDimensionsOperation(core.ModelBase):
    """Returns the dimensions of each page in a PDF document as JSON (in points)."""

    type: typing.Literal["getPdfPageDimensions"] = "getPdfPageDimensions"


class GetTimestampsForSceneFramesOperation(core.ModelBase):
    """Returns a list of timestamps for scene frames in the video as JSON."""

    scene_score: typing.Optional[SceneScore] = pydantic.Field(alias=str("sceneScore"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["getTimestampsForSceneFrames"] = "getTimestampsForSceneFrames"


class GetTransformationJobStatusResponse(core.ModelBase):
    """Response containing the status of a transformation job."""

    status: TransformationJobStatus
    job_id: TransformationJobId = pydantic.Field(alias=str("jobId"))  # type: ignore[literal-required]


class GpsMetadata(core.ModelBase):
    """GPS location metadata extracted from EXIF data embedded in the image."""

    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    altitude: typing.Optional[float] = None


class GrayscaleImageOperation(core.ModelBase):
    """Converts an image to grayscale."""

    type: typing.Literal["grayscale"] = "grayscale"


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


ImageAttributeDomain: typing_extensions.TypeAlias = str
"""The domain of an image attribute."""


ImageAttributeKey: typing_extensions.TypeAlias = str
"""The key of an image attribute within a domain."""


class ImageExtractLayoutAwareContentOperation(core.ModelBase):
    """Extracts text from an image with layout information preserved."""

    parameters: LayoutAwareExtractionParameters
    type: typing.Literal["extractLayoutAwareContent"] = "extractLayoutAwareContent"


class ImageOcrOperation(core.ModelBase):
    """Performs OCR (Optical Character Recognition) on an image."""

    parameters: OcrParameters
    type: typing.Literal["ocr"] = "ocr"


ImageOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "RotateImageOperation",
        "ResizeToFitBoundingBoxOperation",
        "EncryptImageOperation",
        "ContrastImageOperation",
        "TileImageOperation",
        "ResizeImageOperation",
        "AnnotateImageOperation",
        "DecryptImageOperation",
        "CropImageOperation",
        "GrayscaleImageOperation",
    ],
    pydantic.Field(discriminator="type"),
]
"""An operation to perform on an image."""


class ImagePixelCoordinate(core.ModelBase):
    """Coordinate of a pixel in an image (x, y). Top left corner of the image is (0, 0)."""

    x: int
    """Coordinate on the x-axis (width)."""

    y: int
    """Coordinate on the y-axis (height)."""


ImageRegionPolygon: typing_extensions.TypeAlias = typing.List["ImagePixelCoordinate"]
"""
Polygon drawn by connecting adjacent coordinates in the list with straight lines.
A line is drawn between the last and first coordinates in the list to create a closed shape.
Used to define regions in an image for operations like encryption/decryption.
"""


class ImageSpec(core.ModelBase):
    """
    Specification for image processing parameters used in vision-based extraction.
    Controls how document pages are converted to images before being sent to vision models.
    """

    resizing_mode: ResizingMode = pydantic.Field(alias=str("resizingMode"))  # type: ignore[literal-required]
    height: typing.Optional[int] = None
    """Target height in pixels."""

    width: typing.Optional[int] = None
    """Target width in pixels."""

    mime_type: ImageryDecodeFormat = pydantic.Field(alias=str("mimeType"))  # type: ignore[literal-required]


class ImageToDocumentTransformation(core.ModelBase):
    """Converts images to documents."""

    operation: ImageToDocumentOperation
    type: typing.Literal["imageToDocument"] = "imageToDocument"


class ImageToEmbeddingTransformation(core.ModelBase):
    """Generates embeddings from images."""

    operation: ImageToEmbeddingOperation
    type: typing.Literal["imageToEmbedding"] = "imageToEmbedding"


ImageToTextOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["ImageExtractLayoutAwareContentOperation", "ImageOcrOperation"],
    pydantic.Field(discriminator="type"),
]
"""The operation to perform for image to text conversion."""


class ImageToTextTransformation(core.ModelBase):
    """Extracts text from images."""

    operation: ImageToTextOperation
    type: typing.Literal["imageToText"] = "imageToText"


class ImageTransformation(core.ModelBase):
    """
    Transforms images with multiple operations applied in sequence.
    Operations are applied in the order they appear in the list.
    """

    encoding: ImageryEncodeFormat
    operations: typing.List[ImageOperation]
    """The list of operations to apply to the image, in order."""

    type: typing.Literal["image"] = "image"


ImageryDecodeFormat: typing_extensions.TypeAlias = typing.Literal[
    "BMP", "TIFF", "NITF", "JP2K", "JPG", "PNG", "WEBP"
]
"""The format of an imagery media item."""


ImageryEncodeFormat: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["JpgFormat", "TiffFormat", "PngFormat", "WebpFormat"],
    pydantic.Field(discriminator="type"),
]
"""The output format for encoding imagery."""


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


class JpgFormat(core.ModelBase):
    """JPEG image format."""

    type: typing.Literal["jpg"] = "jpg"


class LayoutAwareExtractionParameters(core.ModelBase):
    """Parameters for layout-aware content extraction."""

    languages: typing.List[OcrLanguage]
    """The languages to use for extraction."""


class LayoutAwareExtractionPreprocessingConfig(core.ModelBase):
    """Configuration for layout-aware extraction preprocessing."""

    transformation_config: ExtractDocumentLayoutAwareTextV2Config = pydantic.Field(alias=str("transformationConfig"))  # type: ignore[literal-required]
    crop_config: typing.Optional[CropConfig] = pydantic.Field(alias=str("cropConfig"), default=None)  # type: ignore[literal-required]


class LayoutAwarePreprocessingWrapper(core.ModelBase):
    """Wrapper for layout-aware preprocessing."""

    layout_aware: LayoutAwareExtractionPreprocessingConfig = pydantic.Field(alias=str("layoutAware"))  # type: ignore[literal-required]
    type: typing.Literal["layoutAware"] = "layoutAware"


LogicalTimestamp: typing_extensions.TypeAlias = core.Long
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


MailboxOrGroup: typing_extensions.TypeAlias = typing_extensions.Annotated[
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


MediaItemMetadata: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "CadMediaItemMetadata",
        "DocumentMediaItemMetadata",
        "ImageryMediaItemMetadata",
        "SpreadsheetMediaItemMetadata",
        "UntypedMediaItemMetadata",
        "AudioMediaItemMetadata",
        "Model3dMediaItemMetadata",
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


MediaItemXmlFormat: typing_extensions.TypeAlias = typing.Literal["DOCX", "XLSX", "PPTX"]
"""Format of the media item attempted to be decoded based on the XML structure."""


MediaSchema: typing_extensions.TypeAlias = typing.Literal[
    "AUDIO",
    "CAD",
    "DICOM",
    "DOCUMENT",
    "IMAGERY",
    "MODEL_3D",
    "MULTIMODAL",
    "SPREADSHEET",
    "STREAMING_VIDEO",
    "TILED_RASTER",
    "VIDEO",
    "EMAIL",
]
"""The schema type of a media set, indicating what type of media items it can contain."""


class MkvVideoContainerFormat(core.ModelBase):
    """MKV (Matroska) video container format."""

    type: typing.Literal["mkv"] = "mkv"


Modality: typing_extensions.TypeAlias = typing.Literal[
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


Model3dDecodeFormat: typing_extensions.TypeAlias = typing.Literal["LAS", "PLY", "OBJ"]
"""The format of a 3D model media item."""


class Model3dMediaItemMetadata(core.ModelBase):
    """Metadata for 3D model media items."""

    format: Model3dDecodeFormat
    model_type: Model3dType = pydantic.Field(alias=str("modelType"))  # type: ignore[literal-required]
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["model3d"] = "model3d"


Model3dType: typing_extensions.TypeAlias = typing.Literal["POINT_CLOUD", "MESH"]
"""The type of 3D model representation."""


class MovVideoContainerFormat(core.ModelBase):
    """MOV (QuickTime) video container format."""

    type: typing.Literal["mov"] = "mov"


class Mp3Format(core.ModelBase):
    """MP3 audio format."""

    type: typing.Literal["mp3"] = "mp3"


class Mp4VideoContainerFormat(core.ModelBase):
    """MP4 video container format."""

    type: typing.Literal["mp4"] = "mp4"


class NoTransactionsTransactionPolicy(core.ModelBase):
    """
    Writes are not part of a transaction and are immediately visible.
    Calls to create transaction or commit transaction will error.
    """

    type: typing.Literal["noTransactions"] = "noTransactions"


class NumberOfChannels(core.ModelBase):
    """Specifies the number of audio channels. Defaults to 2 (stereo)."""

    number_of_channels: int = pydantic.Field(alias=str("numberOfChannels"))  # type: ignore[literal-required]
    """The number of audio channels."""

    type: typing.Literal["numberOfChannels"] = "numberOfChannels"


class OcrHocrOutputFormat(core.ModelBase):
    """hOCR (HTML-based OCR) output format."""

    type: typing.Literal["hocr"] = "hocr"


OcrLanguage: typing_extensions.TypeAlias = typing.Literal[
    "AFR",
    "AMH",
    "ARA",
    "ASM",
    "AZE",
    "AZE_CYRL",
    "BEL",
    "BEN",
    "BOD",
    "BOS",
    "BRE",
    "BUL",
    "CAT",
    "CEB",
    "CES",
    "CHI_SIM",
    "CHI_SIM_VERT",
    "CHI_TRA",
    "CHI_TRA_VERT",
    "CHR",
    "COS",
    "CYM",
    "DAN",
    "DEU",
    "DIV",
    "DZO",
    "ELL",
    "ENG",
    "ENM",
    "EPO",
    "EST",
    "EUS",
    "FAO",
    "FAS",
    "FIL",
    "FIN",
    "FRA",
    "FRM",
    "FRY",
    "GLA",
    "GLE",
    "GLG",
    "GRC",
    "GUJ",
    "HAT",
    "HEB",
    "HIN",
    "HRV",
    "HUN",
    "HYE",
    "IKU",
    "IND",
    "ISL",
    "ITA",
    "ITA_OLD",
    "JAV",
    "JPN",
    "JPN_VERT",
    "KAN",
    "KAT",
    "KAT_OLD",
    "KAZ",
    "KHM",
    "KIR",
    "KMR",
    "KOR",
    "KOR_VERT",
    "LAO",
    "LAT",
    "LAV",
    "LIT",
    "LTZ",
    "MAL",
    "MAR",
    "MKD",
    "MLT",
    "MON",
    "MRI",
    "MSA",
    "MYA",
    "NEP",
    "NLD",
    "NOR",
    "OCI",
    "ORI",
    "OSD",
    "PAN",
    "POL",
    "POR",
    "PUS",
    "QUE",
    "RON",
    "RUS",
    "SAN",
    "SIN",
    "SLK",
    "SLV",
    "SND",
    "SPA",
    "SPA_OLD",
    "SQI",
    "SRP",
    "SRP_LATN",
    "SUN",
    "SWA",
    "SWE",
    "SYR",
    "TAM",
    "TAT",
    "TEL",
    "TGK",
    "THA",
    "TIR",
    "TON",
    "TUR",
    "UIG",
    "UKR",
    "URD",
    "UZB",
    "UZB_CYRL",
    "VIE",
    "YID",
    "YOR",
]
"""Language codes for OCR."""


OcrLanguageOrScript: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["OcrLanguageWrapper", "OcrScriptWrapper"], pydantic.Field(discriminator="type")
]
"""Either a specific language or a script for OCR."""


class OcrLanguageWrapper(core.ModelBase):
    """Wrapper for an OCR language."""

    language: OcrLanguage
    type: typing.Literal["language"] = "language"


OcrMode: typing_extensions.TypeAlias = typing.Literal["AUTO", "ELECTRONIC", "SCAN"]
"""OCR mode for document extraction."""


class OcrOnPageOperation(core.ModelBase):
    """Performs OCR (Optical Character Recognition) on a specific page of a document."""

    page_number: int = pydantic.Field(alias=str("pageNumber"))  # type: ignore[literal-required]
    """The page number to perform OCR on."""

    parameters: OcrParameters
    type: typing.Literal["ocrOnPage"] = "ocrOnPage"


class OcrOnPagesOperation(core.ModelBase):
    """Creates access patterns for OCR across pages of a document."""

    parameters: OcrParameters
    page_number: int = pydantic.Field(alias=str("pageNumber"))  # type: ignore[literal-required]
    """The page number."""

    type: typing.Literal["ocrOnPages"] = "ocrOnPages"


OcrOutputFormat: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["OcrHocrOutputFormat", "OcrTextOutputFormat"], pydantic.Field(discriminator="type")
]
"""The output format for OCR results."""


class OcrParameters(core.ModelBase):
    """Parameters for OCR (Optical Character Recognition) operations."""

    output_format: OcrOutputFormat = pydantic.Field(alias=str("outputFormat"))  # type: ignore[literal-required]
    languages: typing.List[OcrLanguageOrScript]
    """The languages or scripts to use for OCR."""


OcrScript: typing_extensions.TypeAlias = typing.Literal[
    "ARABIC",
    "ARMENIAN",
    "BENGALI",
    "CANADIAN_ABORIGINAL",
    "CHEROKEE",
    "CYRILLIC",
    "DEVANAGARI",
    "ETHIOPIC",
    "FRAKTUR",
    "GEORGIAN",
    "GREEK",
    "GUJARATI",
    "GURMUKHI",
    "HAN_SIMPLIFIED",
    "HAN_SIMPLIFIED_VERT",
    "HAN_TRADITIONAL",
    "HAN_TRADITIONAL_VERT",
    "HANGUL",
    "HANGUL_VERT",
    "HEBREW",
    "JAPANESE",
    "JAPANESE_VERT",
    "KANNADA",
    "KHMER",
    "LAO",
    "LATIN",
    "MALAYALAM",
    "MYANMAR",
    "ORIYA",
    "SINHALA",
    "SYRIAC",
    "TAMIL",
    "TELUGU",
    "THAANA",
    "THAI",
    "TIBETAN",
    "VIETNAMESE",
]
"""Script codes for OCR."""


class OcrScriptWrapper(core.ModelBase):
    """Wrapper for an OCR script."""

    script: OcrScript
    type: typing.Literal["script"] = "script"


class OcrTextOutputFormat(core.ModelBase):
    """Plain text output format for OCR."""

    type: typing.Literal["text"] = "text"


class Orientation(core.ModelBase):
    """The orientation information as encoded in EXIF metadata."""

    rotation_angle: typing.Optional[RotationAngle] = pydantic.Field(alias=str("rotationAngle"), default=None)  # type: ignore[literal-required]
    flip_axis: typing.Optional[FlipAxis] = pydantic.Field(alias=str("flipAxis"), default=None)  # type: ignore[literal-required]


class PageRange(core.ModelBase):
    """Page range for document extraction."""

    start_page_inclusive: typing.Optional[int] = pydantic.Field(alias=str("startPageInclusive"), default=None)  # type: ignore[literal-required]
    """Start page index (0-based, inclusive). If not provided, defaults to start of document."""

    end_page_exclusive: typing.Optional[int] = pydantic.Field(alias=str("endPageExclusive"), default=None)  # type: ignore[literal-required]
    """End page index (0-based, exclusive). If not provided, defaults to end of document."""


PaletteInterpretation: typing_extensions.TypeAlias = typing.Literal[
    "GRAY", "RGB", "RGBA", "CMYK", "HLS"
]
"""The palette interpretation of a band."""


class PdfFormat(core.ModelBase):
    """PDF document format."""

    type: typing.Literal["pdf"] = "pdf"


PerformanceMode: typing_extensions.TypeAlias = typing.Literal["MORE_ECONOMICAL", "MORE_PERFORMANT"]
"""The performance mode for transcription."""


class PlainTextNoSegmentData(core.ModelBase):
    """Plain text transcription output format."""

    add_timestamps: bool = pydantic.Field(alias=str("addTimestamps"))  # type: ignore[literal-required]
    """Whether to include timestamps in the output."""

    type: typing.Literal["plainTextNoSegmentData"] = "plainTextNoSegmentData"


class PngFormat(core.ModelBase):
    """PNG image format."""

    type: typing.Literal["png"] = "png"


class Pttml(core.ModelBase):
    """PTTML (Palantir Timed Text Markup Language) transcription output format."""

    type: typing.Literal["pttml"] = "pttml"


class PutMediaItemResponse(core.ModelBase):
    """PutMediaItemResponse"""

    media_item_rid: core_models.MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]
    media_set_view_rid: core_models.MediaSetViewRid = pydantic.Field(alias=str("mediaSetViewRid"))  # type: ignore[literal-required]


class RegisterMediaItemRequest(core.ModelBase):
    """Request to register a media item from a federated store."""

    physical_item_name: str = pydantic.Field(alias=str("physicalItemName"))  # type: ignore[literal-required]
    """The relative path within the federated media store where the media item exists."""

    media_item_path: typing.Optional[core_models.MediaItemPath] = pydantic.Field(alias=str("mediaItemPath"), default=None)  # type: ignore[literal-required]


class RegisterMediaItemResponse(core.ModelBase):
    """Response after successfully registering a media item."""

    media_item_rid: core_models.MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]
    media_type: core_models.MediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]


class RenderImageLayerOperation(core.ModelBase):
    """
    Renders a frame of a DICOM file as an image.
    If only one dimension is specified, the other is calculated to preserve aspect ratio.
    """

    layer_number: typing.Optional[int] = pydantic.Field(alias=str("layerNumber"), default=None)  # type: ignore[literal-required]
    """The layer number to render. If not specified, renders the middle layer."""

    height: typing.Optional[int] = None
    """The desired height in pixels."""

    width: typing.Optional[int] = None
    """The desired width in pixels."""

    type: typing.Literal["renderImageLayer"] = "renderImageLayer"


class RenderPageOperation(core.ModelBase):
    """
    Renders a PDF page as an image.
    If only one dimension is specified, the other is calculated to preserve aspect ratio.
    """

    page_number: typing.Optional[int] = pydantic.Field(alias=str("pageNumber"), default=None)  # type: ignore[literal-required]
    """The zero-indexed page number to render. Defaults to the first page if not specified."""

    height: typing.Optional[int] = None
    """The desired height in pixels."""

    width: typing.Optional[int] = None
    """The desired width in pixels."""

    type: typing.Literal["renderPage"] = "renderPage"


class RenderPageToFitBoundingBoxOperation(core.ModelBase):
    """Renders a PDF page to maximally fit within a bounding box while preserving aspect ratio."""

    page_number: typing.Optional[int] = pydantic.Field(alias=str("pageNumber"), default=None)  # type: ignore[literal-required]
    """The zero-indexed page number to render. Defaults to the first page if not specified."""

    width: int
    """The width of the bounding box in pixels."""

    height: int
    """The height of the bounding box in pixels."""

    type: typing.Literal["renderPageToFitBoundingBox"] = "renderPageToFitBoundingBox"


class ResizeImageOperation(core.ModelBase):
    """
    Resizes an image to the specified dimensions.
    If only one dimension is specified, the other is calculated to preserve aspect ratio.
    """

    height: typing.Optional[int] = None
    """The desired height in pixels."""

    width: typing.Optional[int] = None
    """The desired width in pixels."""

    auto_orient: typing.Optional[bool] = pydantic.Field(alias=str("autoOrient"), default=None)  # type: ignore[literal-required]
    """Whether to automatically orient the image based on EXIF metadata."""

    type: typing.Literal["resize"] = "resize"


class ResizeToFitBoundingBoxOperation(core.ModelBase):
    """Resizes an image to maximally fit within a bounding box while preserving aspect ratio."""

    width: int
    """The width of the bounding box in pixels."""

    height: int
    """The height of the bounding box in pixels."""

    type: typing.Literal["resizeToFitBoundingBox"] = "resizeToFitBoundingBox"


ResizingMode: typing_extensions.TypeAlias = typing.Literal["RESIZING", "FIT_INTO_BOUNDING_BOX"]
"""Image resizing strategy."""


class RotateImageOperation(core.ModelBase):
    """Rotates an image clockwise by the specified angle."""

    angle: RotationAngle
    type: typing.Literal["rotate"] = "rotate"


RotationAngle: typing_extensions.TypeAlias = typing.Literal[
    "DEGREE_90", "DEGREE_180", "DEGREE_270", "UNKNOWN"
]
"""The rotation angle from EXIF orientation."""


SceneScore: typing_extensions.TypeAlias = typing.Literal[
    "MORE_SENSITIVE", "STANDARD", "LESS_SENSITIVE"
]
"""The sensitivity threshold for scene detection."""


class SlicePdfRangeOperation(core.ModelBase):
    """Slices a PDF to a specified page range."""

    start_page_inclusive: int = pydantic.Field(alias=str("startPageInclusive"))  # type: ignore[literal-required]
    """The zero-indexed start page (inclusive)."""

    end_page_exclusive: int = pydantic.Field(alias=str("endPageExclusive"))  # type: ignore[literal-required]
    """The zero-indexed end page (exclusive)."""

    strictly_enforce_end_page: typing.Optional[bool] = pydantic.Field(alias=str("strictlyEnforceEndPage"), default=None)  # type: ignore[literal-required]
    """
    If true (default), the operation fails if endPage exceeds the document's page count.
    If false, ends at min(endPage, lastPage).
    """

    type: typing.Literal["slicePdfRange"] = "slicePdfRange"


SpreadsheetDecodeFormat: typing_extensions.TypeAlias = typing.Literal["CSV", "XLSX"]
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


class SpreadsheetToTextTransformation(core.ModelBase):
    """Converts spreadsheet data to text/JSON."""

    operation: SpreadsheetToTextOperation
    type: typing.Literal["spreadsheetToText"] = "spreadsheetToText"


class TarFormat(core.ModelBase):
    """TAR archive format."""

    type: typing.Literal["tar"] = "tar"


TextOutputFormat: typing_extensions.TypeAlias = typing.Literal["TEXT", "MARKDOWN", "HTML"]
"""Format in which to return extracted text."""


class TiffFormat(core.ModelBase):
    """TIFF image format."""

    type: typing.Literal["tiff"] = "tiff"


class TileImageOperation(core.ModelBase):
    """
    Generates Slippy map tiles (EPSG 3857) from a geo-embedded image.
    Only supported for geo-embedded TIFF and NITF images with at most 100M square pixels.
    """

    zoom: int
    """The zoom level of the tile."""

    x: int
    """The x coordinate of the tile."""

    y: int
    """The y coordinate of the tile."""

    type: typing.Literal["tile"] = "tile"


class TrackedTransformationFailedResponse(core.ModelBase):
    """TrackedTransformationFailedResponse"""

    type: typing.Literal["failed"] = "failed"


class TrackedTransformationPendingResponse(core.ModelBase):
    """TrackedTransformationPendingResponse"""

    type: typing.Literal["pending"] = "pending"


TrackedTransformationResponse: typing_extensions.TypeAlias = typing_extensions.Annotated[
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


TransactionId: typing_extensions.TypeAlias = core.UUID
"""An identifier which represents a transaction on a media set."""


TransactionPolicy: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["BatchTransactionsTransactionPolicy", "NoTransactionsTransactionPolicy"],
    pydantic.Field(discriminator="type"),
]
"""The transaction policy for a media set, determining how writes are handled."""


class TranscodeOperation(core.ModelBase):
    """Encodes video to the specified format."""

    type: typing.Literal["transcode"] = "transcode"


class TranscribeJson(core.ModelBase):
    """JSON transcription output format."""

    type: typing.Literal["json"] = "json"


class TranscribeOperation(core.ModelBase):
    """Transcribes speech in audio to text."""

    language: typing.Optional[TranscriptionLanguage] = None
    diarize: typing.Optional[bool] = None
    """
    Whether to perform speaker diarization. Defaults to false.
    Not supported in economical performance mode.
    """

    output_format: typing.Optional[TranscribeTextEncodeFormat] = pydantic.Field(alias=str("outputFormat"), default=None)  # type: ignore[literal-required]
    performance_mode: typing.Optional[PerformanceMode] = pydantic.Field(alias=str("performanceMode"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["transcribe"] = "transcribe"


TranscribeTextEncodeFormat: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["PlainTextNoSegmentData", "TranscribeJson", "Pttml"],
    pydantic.Field(discriminator="type"),
]
"""The output format for transcription results."""


TranscriptionLanguage: typing_extensions.TypeAlias = typing.Literal[
    "AF",
    "AM",
    "AR",
    "AS",
    "AZ",
    "BA",
    "BE",
    "BG",
    "BN",
    "BO",
    "BR",
    "BS",
    "CA",
    "CS",
    "CY",
    "DA",
    "DE",
    "EL",
    "EN",
    "ES",
    "ET",
    "EU",
    "FA",
    "FI",
    "FO",
    "FR",
    "GL",
    "GU",
    "HA",
    "HAW",
    "HE",
    "HI",
    "HR",
    "HT",
    "HU",
    "HY",
    "ID",
    "IS",
    "IT",
    "JA",
    "JW",
    "KA",
    "KK",
    "KM",
    "KN",
    "KO",
    "LA",
    "LB",
    "LN",
    "LO",
    "LT",
    "LV",
    "MG",
    "MI",
    "MK",
    "ML",
    "MN",
    "MR",
    "MS",
    "MT",
    "MY",
    "NE",
    "NL",
    "NN",
    "NO",
    "OC",
    "PA",
    "PL",
    "PS",
    "PT",
    "RO",
    "RU",
    "SA",
    "SD",
    "SI",
    "SK",
    "SL",
    "SN",
    "SO",
    "SQ",
    "SR",
    "SU",
    "SV",
    "SW",
    "TA",
    "TE",
    "TG",
    "TH",
    "TK",
    "TL",
    "TR",
    "TT",
    "UK",
    "UR",
    "UZ",
    "VI",
    "YI",
    "YO",
    "YUE",
    "ZH",
    "AFRIKAANS",
    "ALBANIAN",
    "AMHARIC",
    "ARABIC",
    "ARMENIAN",
    "ASSAMESE",
    "AZERBAIJANI",
    "BASHKIR",
    "BASQUE",
    "BELARUSIAN",
    "BENGALI",
    "BOSNIAN",
    "BRETON",
    "BULGARIAN",
    "BURMESE",
    "CANTONESE",
    "CASTILIAN",
    "CATALAN",
    "CHINESE",
    "CROATIAN",
    "CZECH",
    "DANISH",
    "DUTCH",
    "ENGLISH",
    "ESTONIAN",
    "FAROESE",
    "FINNISH",
    "FLEMISH",
    "FRENCH",
    "GALICIAN",
    "GEORGIAN",
    "GERMAN",
    "GREEK",
    "GUJARATI",
    "HAITIAN",
    "HAITIAN_CREOLE",
    "HAUSA",
    "HAWAIIAN",
    "HEBREW",
    "HINDI",
    "HUNGARIAN",
    "ICELANDIC",
    "INDONESIAN",
    "ITALIAN",
    "JAPANESE",
    "JAVANESE",
    "KANNADA",
    "KAZAKH",
    "KHMER",
    "KOREAN",
    "LAO",
    "LATIN",
    "LATVIAN",
    "LETZEBURGESCH",
    "LINGALA",
    "LITHUANIAN",
    "LUXEMBOURGISH",
    "MACEDONIAN",
    "MALAGASY",
    "MALAY",
    "MALAYALAM",
    "MALTESE",
    "MANDARIN",
    "MAORI",
    "MARATHI",
    "MOLDAVIAN",
    "MOLDOVAN",
    "MONGOLIAN",
    "MYANMAR",
    "NEPALI",
    "NORWEGIAN",
    "NYNORSK",
    "OCCITAN",
    "PANJABI",
    "PASHTO",
    "PERSIAN",
    "POLISH",
    "PORTUGUESE",
    "PUNJABI",
    "PUSHTO",
    "ROMANIAN",
    "RUSSIAN",
    "SANSKRIT",
    "SERBIAN",
    "SHONA",
    "SINDHI",
    "SINHALA",
    "SINHALESE",
    "SLOVAK",
    "SLOVENIAN",
    "SOMALI",
    "SPANISH",
    "SUNDANESE",
    "SWAHILI",
    "SWEDISH",
    "TAGALOG",
    "TAJIK",
    "TAMIL",
    "TATAR",
    "TELUGU",
    "THAI",
    "TIBETAN",
    "TURKISH",
    "TURKMEN",
    "UKRAINIAN",
    "URDU",
    "UZBEK",
    "VALENCIAN",
    "VIETNAMESE",
    "WELSH",
    "YIDDISH",
    "YORUBA",
]
"""
Language codes for audio transcription.
If not specified, the language will be auto-detected from the first 30 seconds of audio.
"""


class TransformMediaItemRequest(core.ModelBase):
    """Request to transform a media item."""

    transformation: Transformation


class TransformMediaItemResponse(core.ModelBase):
    """Response from initiating a media item transformation."""

    status: TransformationJobStatus
    job_id: TransformationJobId = pydantic.Field(alias=str("jobId"))  # type: ignore[literal-required]


Transformation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "EmailToTextTransformation",
        "ImageTransformation",
        "SpreadsheetToTextTransformation",
        "VideoToAudioTransformation",
        "AudioToTextTransformation",
        "EmailToAttachmentTransformation",
        "VideoToArchiveTransformation",
        "VideoToTextTransformation",
        "ImageToTextTransformation",
        "VideoToImageTransformation",
        "VideoTransformation",
        "ImageToDocumentTransformation",
        "DicomToImageTransformation",
        "DocumentToDocumentTransformation",
        "DocumentToImageTransformation",
        "ImageToEmbeddingTransformation",
        "AudioTransformation",
        "DocumentToTextTransformation",
    ],
    pydantic.Field(discriminator="type"),
]
"""
A transformation to apply to a media item. Each variant specifies the type of transformation
and any parameters required for the operation.
"""


TransformationJobId: typing_extensions.TypeAlias = str
"""An identifier for a media item transformation job."""


TransformationJobStatus: typing_extensions.TypeAlias = typing.Literal[
    "PENDING", "FAILED", "SUCCESSFUL"
]
"""The status of a transformation job."""


class TsAudioContainerFormat(core.ModelBase):
    """MPEG Transport Stream audio container format."""

    type: typing.Literal["ts"] = "ts"


class TsVideoContainerFormat(core.ModelBase):
    """MPEG Transport Stream video container format."""

    type: typing.Literal["ts"] = "ts"


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


class VideoChunkOperation(core.ModelBase):
    """
    Chunks video into smaller segments of the specified duration.
    The final chunk may be smaller than the specified duration.
    """

    chunk_duration_milliseconds: int = pydantic.Field(alias=str("chunkDurationMilliseconds"))  # type: ignore[literal-required]
    """Duration of each chunk in milliseconds."""

    chunk_index: int = pydantic.Field(alias=str("chunkIndex"))  # type: ignore[literal-required]
    """The chunk index to retain."""

    type: typing.Literal["chunk"] = "chunk"


VideoDecodeFormat: typing_extensions.TypeAlias = typing.Literal["MP4", "MKV", "MOV", "TS", "WEBM"]
"""The format of a video media item."""


VideoEncodeFormat: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "Mp4VideoContainerFormat",
        "MovVideoContainerFormat",
        "MkvVideoContainerFormat",
        "TsVideoContainerFormat",
    ],
    pydantic.Field(discriminator="type"),
]
"""The output format for encoding video."""


class VideoMediaItemMetadata(core.ModelBase):
    """Metadata for video media items."""

    format: VideoDecodeFormat
    specification: VideoSpecification
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["video"] = "video"


VideoOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["TranscodeOperation", "VideoChunkOperation"], pydantic.Field(discriminator="type")
]
"""The operation to perform on the video."""


class VideoSpecification(core.ModelBase):
    """Technical specifications for video media items."""

    bit_rate: int = pydantic.Field(alias=str("bitRate"))  # type: ignore[literal-required]
    """Approximate (average) bits per second of the video, rounded up in case of a fractional average bits per second."""

    duration_seconds: float = pydantic.Field(alias=str("durationSeconds"))  # type: ignore[literal-required]
    """Approximate duration of the video, in seconds with up to two decimal digits (rounded up)."""


class VideoToArchiveTransformation(core.ModelBase):
    """Extracts video frames to an archive format."""

    encoding: ArchiveEncodeFormat
    operation: VideoToArchiveOperation
    type: typing.Literal["videoToArchive"] = "videoToArchive"


class VideoToAudioTransformation(core.ModelBase):
    """Extracts audio from video."""

    encoding: AudioEncodeFormat
    operation: VideoToAudioOperation
    type: typing.Literal["videoToAudio"] = "videoToAudio"


VideoToImageOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["ExtractFirstFrameOperation", "ExtractFramesAtTimestampsOperation"],
    pydantic.Field(discriminator="type"),
]
"""The operation to perform for video to image conversion."""


class VideoToImageTransformation(core.ModelBase):
    """Extracts video frames as images."""

    encoding: ImageryEncodeFormat
    operation: VideoToImageOperation
    type: typing.Literal["videoToImage"] = "videoToImage"


class VideoToTextTransformation(core.ModelBase):
    """Extracts metadata from video as text/JSON."""

    operation: VideoToTextOperation
    type: typing.Literal["videoToText"] = "videoToText"


class VideoTransformation(core.ModelBase):
    """Transforms video media items."""

    encoding: VideoEncodeFormat
    operation: VideoOperation
    type: typing.Literal["video"] = "video"


VlmOutputFormat: typing_extensions.TypeAlias = typing.Literal["MARKDOWN"]
"""Format in which to return text extracted by vision language models."""


VlmPreprocessingConfig: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["LayoutAwarePreprocessingWrapper", "ExtractTextPreprocessingWrapper"],
    pydantic.Field(discriminator="type"),
]
"""Preprocessing configuration for VLM extraction."""


class WavEncodeFormat(core.ModelBase):
    """WAV audio format with optional sample rate and channel layout."""

    sample_rate: typing.Optional[int] = pydantic.Field(alias=str("sampleRate"), default=None)  # type: ignore[literal-required]
    """The sample rate in Hz. Defaults to 44100 Hz if not specified."""

    audio_channel_layout: typing.Optional[AudioChannelLayout] = pydantic.Field(alias=str("audioChannelLayout"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["wav"] = "wav"


class WaveformOperation(core.ModelBase):
    """
    Generates waveform visualization data from audio.
    Returns JSON with normalized doubles (0-1) representing amplitude.
    """

    peaks_per_second: int = pydantic.Field(alias=str("peaksPerSecond"))  # type: ignore[literal-required]
    """The number of peaks per second (1-1000)."""

    type: typing.Literal["waveform"] = "waveform"


class WebpFormat(core.ModelBase):
    """WebP image format."""

    type: typing.Literal["webp"] = "webp"


AnnotateGeometry: typing_extensions.TypeAlias = BoundingBoxGeometry
"""The geometry for an annotation."""


ArchiveEncodeFormat: typing_extensions.TypeAlias = TarFormat
"""The output format for encoding archives."""


AudioChannelLayout: typing_extensions.TypeAlias = NumberOfChannels
"""The audio channel layout configuration."""


DicomMetaInformation: typing_extensions.TypeAlias = DicomMetaInformationV1
"""DICOM meta information."""


DicomToImageOperation: typing_extensions.TypeAlias = RenderImageLayerOperation
"""The operation to perform for DICOM to image conversion."""


DocumentEncodeFormat: typing_extensions.TypeAlias = PdfFormat
"""The output format for encoding documents."""


EmailToAttachmentOperation: typing_extensions.TypeAlias = GetEmailAttachmentOperation
"""The operation to perform for email to attachment extraction."""


EmailToTextOperation: typing_extensions.TypeAlias = GetEmailBodyOperation
"""The operation to perform for email to text extraction."""


ImageToDocumentOperation: typing_extensions.TypeAlias = CreatePdfOperation
"""The operation to perform for image to document conversion."""


ImageToEmbeddingOperation: typing_extensions.TypeAlias = GenerateEmbeddingOperation
"""The operation to perform for image to embedding conversion."""


LanguageModelLocator: typing_extensions.TypeAlias = ApiNameLocatorWrapper
"""Locator for identifying a language model."""


LlmSpec: typing_extensions.TypeAlias = ChatLlmSpecWrapper
"""Specification for language model requests."""


SpreadsheetToTextOperation: typing_extensions.TypeAlias = ConvertSheetToJsonOperation
"""The operation to perform for spreadsheet to text conversion."""


VideoToArchiveOperation: typing_extensions.TypeAlias = ExtractSceneFramesOperation
"""The operation to perform for video to archive conversion."""


VideoToAudioOperation: typing_extensions.TypeAlias = ExtractAudioOperation
"""The operation to perform for video to audio conversion."""


VideoToTextOperation: typing_extensions.TypeAlias = GetTimestampsForSceneFramesOperation
"""The operation to perform for video to text conversion."""


core.resolve_forward_references_in_module(__name__)

__all__ = [
    "AffineTransform",
    "AnnotateGeometry",
    "AnnotateImageOperation",
    "Annotation",
    "ApiNameLocatorWrapper",
    "ArchiveEncodeFormat",
    "AudioChannelLayout",
    "AudioChannelOperation",
    "AudioChunkOperation",
    "AudioDecodeFormat",
    "AudioEncodeFormat",
    "AudioMediaItemMetadata",
    "AudioOperation",
    "AudioSpecification",
    "AudioToTextOperation",
    "AudioToTextTransformation",
    "AudioTransformation",
    "AvailableEmbeddingModelIds",
    "BandInfo",
    "BatchTransactionsTransactionPolicy",
    "BoundingBox",
    "BoundingBoxGeometry",
    "BranchName",
    "BranchRid",
    "CadDecodeFormat",
    "CadMediaItemMetadata",
    "CadUnits",
    "ChatLlmSpec",
    "ChatLlmSpecWrapper",
    "Color",
    "ColorInterpretation",
    "CommonDicomDataElements",
    "ContrastBinarize",
    "ContrastEqualize",
    "ContrastImageOperation",
    "ContrastRayleigh",
    "ContrastType",
    "ConvertAudioOperation",
    "ConvertDocumentOperation",
    "ConvertSheetToJsonOperation",
    "CoordinateReferenceSystem",
    "CreatePdfOperation",
    "CropConfig",
    "CropImageOperation",
    "DataType",
    "DecryptImageOperation",
    "DicomDataElementKey",
    "DicomMediaItemMetadata",
    "DicomMediaType",
    "DicomMetaInformation",
    "DicomMetaInformationV1",
    "DicomToImageOperation",
    "DicomToImageTransformation",
    "Dimensions",
    "DocumentDecodeFormat",
    "DocumentEncodeFormat",
    "DocumentExtractLayoutAwareContentOperation",
    "DocumentMediaItemMetadata",
    "DocumentToDocumentOperation",
    "DocumentToDocumentTransformation",
    "DocumentToImageOperation",
    "DocumentToImageTransformation",
    "DocumentToTextOperation",
    "DocumentToTextTransformation",
    "EmailAttachment",
    "EmailDecodeFormat",
    "EmailMediaItemMetadata",
    "EmailToAttachmentOperation",
    "EmailToAttachmentTransformation",
    "EmailToTextEncodeFormat",
    "EmailToTextOperation",
    "EmailToTextTransformation",
    "EncryptImageOperation",
    "ExtractAllTextOperation",
    "ExtractAudioOperation",
    "ExtractDocumentLayoutAwareTextV2Config",
    "ExtractDocumentLayoutAwareTextV2Operation",
    "ExtractDocumentTextV2Config",
    "ExtractDocumentTextV2Operation",
    "ExtractFirstFrameOperation",
    "ExtractFormFieldsOperation",
    "ExtractFramesAtTimestampsOperation",
    "ExtractSceneFramesOperation",
    "ExtractTableOfContentsOperation",
    "ExtractTextFromPagesToArrayOperation",
    "ExtractTextPreprocessingWrapper",
    "ExtractUnstructuredTextFromPageOperation",
    "ExtractVlmTextOperation",
    "FlipAxis",
    "GcpList",
    "GenerateEmbeddingOperation",
    "GeoMetadata",
    "GetEmailAttachmentOperation",
    "GetEmailBodyOperation",
    "GetMediaItemInfoResponse",
    "GetMediaItemRidByPathResponse",
    "GetMediaSetResponse",
    "GetPdfPageDimensionsOperation",
    "GetTimestampsForSceneFramesOperation",
    "GetTransformationJobStatusResponse",
    "GpsMetadata",
    "GrayscaleImageOperation",
    "GroundControlPoint",
    "Group",
    "GroupWrapper",
    "ImageAttributeDomain",
    "ImageAttributeKey",
    "ImageExtractLayoutAwareContentOperation",
    "ImageOcrOperation",
    "ImageOperation",
    "ImagePixelCoordinate",
    "ImageRegionPolygon",
    "ImageSpec",
    "ImageToDocumentOperation",
    "ImageToDocumentTransformation",
    "ImageToEmbeddingOperation",
    "ImageToEmbeddingTransformation",
    "ImageToTextOperation",
    "ImageToTextTransformation",
    "ImageTransformation",
    "ImageryDecodeFormat",
    "ImageryEncodeFormat",
    "ImageryMediaItemMetadata",
    "JpgFormat",
    "LanguageModelLocator",
    "LayoutAwareExtractionParameters",
    "LayoutAwareExtractionPreprocessingConfig",
    "LayoutAwarePreprocessingWrapper",
    "LlmSpec",
    "LogicalTimestamp",
    "Mailbox",
    "MailboxOrGroup",
    "MailboxWrapper",
    "MediaAttribution",
    "MediaItemMetadata",
    "MediaItemXmlFormat",
    "MediaSchema",
    "MkvVideoContainerFormat",
    "Modality",
    "Model3dDecodeFormat",
    "Model3dMediaItemMetadata",
    "Model3dType",
    "MovVideoContainerFormat",
    "Mp3Format",
    "Mp4VideoContainerFormat",
    "NoTransactionsTransactionPolicy",
    "NumberOfChannels",
    "OcrHocrOutputFormat",
    "OcrLanguage",
    "OcrLanguageOrScript",
    "OcrLanguageWrapper",
    "OcrMode",
    "OcrOnPageOperation",
    "OcrOnPagesOperation",
    "OcrOutputFormat",
    "OcrParameters",
    "OcrScript",
    "OcrScriptWrapper",
    "OcrTextOutputFormat",
    "Orientation",
    "PageRange",
    "PaletteInterpretation",
    "PdfFormat",
    "PerformanceMode",
    "PlainTextNoSegmentData",
    "PngFormat",
    "Pttml",
    "PutMediaItemResponse",
    "RegisterMediaItemRequest",
    "RegisterMediaItemResponse",
    "RenderImageLayerOperation",
    "RenderPageOperation",
    "RenderPageToFitBoundingBoxOperation",
    "ResizeImageOperation",
    "ResizeToFitBoundingBoxOperation",
    "ResizingMode",
    "RotateImageOperation",
    "RotationAngle",
    "SceneScore",
    "SlicePdfRangeOperation",
    "SpreadsheetDecodeFormat",
    "SpreadsheetMediaItemMetadata",
    "SpreadsheetToTextOperation",
    "SpreadsheetToTextTransformation",
    "TarFormat",
    "TextOutputFormat",
    "TiffFormat",
    "TileImageOperation",
    "TrackedTransformationFailedResponse",
    "TrackedTransformationPendingResponse",
    "TrackedTransformationResponse",
    "TrackedTransformationSuccessfulResponse",
    "TransactionId",
    "TransactionPolicy",
    "TranscodeOperation",
    "TranscribeJson",
    "TranscribeOperation",
    "TranscribeTextEncodeFormat",
    "TranscriptionLanguage",
    "TransformMediaItemRequest",
    "TransformMediaItemResponse",
    "Transformation",
    "TransformationJobId",
    "TransformationJobStatus",
    "TsAudioContainerFormat",
    "TsVideoContainerFormat",
    "UnitInterpretation",
    "UntypedMediaItemMetadata",
    "VideoChunkOperation",
    "VideoDecodeFormat",
    "VideoEncodeFormat",
    "VideoMediaItemMetadata",
    "VideoOperation",
    "VideoSpecification",
    "VideoToArchiveOperation",
    "VideoToArchiveTransformation",
    "VideoToAudioOperation",
    "VideoToAudioTransformation",
    "VideoToImageOperation",
    "VideoToImageTransformation",
    "VideoToTextOperation",
    "VideoToTextTransformation",
    "VideoTransformation",
    "VlmOutputFormat",
    "VlmPreprocessingConfig",
    "WavEncodeFormat",
    "WaveformOperation",
    "WebpFormat",
]
