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


class AnthropicAnyToolChoice(core.ModelBase):
    """AnthropicAnyToolChoice"""

    disable_parallel_tool_use: typing.Optional[AnthropicDisableParallelToolUse] = pydantic.Field(alias=str("disableParallelToolUse"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["any"] = "any"


class AnthropicAutoToolChoice(core.ModelBase):
    """AnthropicAutoToolChoice"""

    disable_parallel_tool_use: typing.Optional[AnthropicDisableParallelToolUse] = pydantic.Field(alias=str("disableParallelToolUse"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["auto"] = "auto"


class AnthropicBase64PdfDocumentSource(core.ModelBase):
    """AnthropicBase64PdfDocumentSource"""

    data: str
    type: typing.Literal["pdf"] = "pdf"


class AnthropicCharacterLocationCitation(core.ModelBase):
    """AnthropicCharacterLocationCitation"""

    cited_text: str = pydantic.Field(alias=str("citedText"))  # type: ignore[literal-required]
    document_index: int = pydantic.Field(alias=str("documentIndex"))  # type: ignore[literal-required]
    document_title: typing.Optional[str] = pydantic.Field(alias=str("documentTitle"), default=None)  # type: ignore[literal-required]
    start_char_index: int = pydantic.Field(alias=str("startCharIndex"))  # type: ignore[literal-required]
    end_char_index: int = pydantic.Field(alias=str("endCharIndex"))  # type: ignore[literal-required]
    type: typing.Literal["charLocation"] = "charLocation"


AnthropicCompletionContent = typing_extensions.Annotated[
    typing.Union[
        "AnthropicCompletionToolUse",
        "AnthropicCompletionText",
        "AnthropicCompletionThinking",
        "AnthropicCompletionRedactedThinking",
    ],
    pydantic.Field(discriminator="type"),
]
"""AnthropicCompletionContent"""


class AnthropicCompletionRedactedThinking(core.ModelBase):
    """AnthropicCompletionRedactedThinking"""

    data: str
    type: typing.Literal["redactedThinking"] = "redactedThinking"


class AnthropicCompletionText(core.ModelBase):
    """AnthropicCompletionText"""

    text: str
    citations: typing.Optional[typing.List[AnthropicCompletionCitation]] = None
    type: typing.Literal["text"] = "text"


class AnthropicCompletionThinking(core.ModelBase):
    """AnthropicCompletionThinking"""

    signature: str
    thinking: str
    type: typing.Literal["thinking"] = "thinking"


class AnthropicCompletionToolUse(core.ModelBase):
    """AnthropicCompletionToolUse"""

    id: str
    input: typing.Any
    name: str
    type: typing.Literal["toolUse"] = "toolUse"


class AnthropicCustomTool(core.ModelBase):
    """AnthropicCustomTool"""

    name: str
    description: typing.Optional[str] = None
    input_schema: JsonSchema = pydantic.Field(alias=str("inputSchema"))  # type: ignore[literal-required]
    type: typing.Literal["custom"] = "custom"


AnthropicDisableParallelToolUse = bool
"""
Whether to disable parallel tool use. Defaults to false. If set to true, the model will output 
exactly one tool use.
"""


class AnthropicDisabledThinking(core.ModelBase):
    """AnthropicDisabledThinking"""

    type: typing.Literal["disabled"] = "disabled"


class AnthropicDocument(core.ModelBase):
    """AnthropicDocument"""

    source: AnthropicDocumentSource
    cache_control: typing.Optional[AnthropicCacheControl] = pydantic.Field(alias=str("cacheControl"), default=None)  # type: ignore[literal-required]
    citations: typing.Optional[AnthropicDocumentCitations] = None
    context: typing.Optional[str] = None
    title: typing.Optional[str] = None
    type: typing.Literal["document"] = "document"


class AnthropicDocumentCitations(core.ModelBase):
    """AnthropicDocumentCitations"""

    enabled: bool


AnthropicDocumentSource = typing_extensions.Annotated[
    typing.Union[AnthropicBase64PdfDocumentSource, "AnthropicTextDocumentSource"],
    pydantic.Field(discriminator="type"),
]
"""AnthropicDocumentSource"""


class AnthropicEnabledThinking(core.ModelBase):
    """AnthropicEnabledThinking"""

    budget_tokens: int = pydantic.Field(alias=str("budgetTokens"))  # type: ignore[literal-required]
    """Must be greater than 1024."""

    type: typing.Literal["enabled"] = "enabled"


class AnthropicEphemeralCacheControl(core.ModelBase):
    """This currently does not support the ttl field, but will in the future."""

    type: typing.Literal["ephemeral"] = "ephemeral"


class AnthropicImage(core.ModelBase):
    """AnthropicImage"""

    source: AnthropicImageSource
    cache_control: typing.Optional[AnthropicCacheControl] = pydantic.Field(alias=str("cacheControl"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["image"] = "image"


class AnthropicImageBase64Source(core.ModelBase):
    """AnthropicImageBase64Source"""

    data: str
    media_type: AnthropicMediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]
    """This can include image/jpeg, image/png, image/gif or image/webp."""

    type: typing.Literal["base64"] = "base64"


AnthropicMediaType = typing.Literal["IMAGE_JPEG", "IMAGE_PNG", "IMAGE_GIF", "IMAGE_WEBP"]
"""AnthropicMediaType"""


class AnthropicMessage(core.ModelBase):
    """AnthropicMessage"""

    content: typing.List[AnthropicMessageContent]
    role: AnthropicMessageRole


AnthropicMessageContent = typing_extensions.Annotated[
    typing.Union[
        AnthropicImage,
        "AnthropicToolUse",
        AnthropicDocument,
        "AnthropicText",
        "AnthropicToolResult",
        "AnthropicThinking",
        "AnthropicRedactedThinking",
    ],
    pydantic.Field(discriminator="type"),
]
"""AnthropicMessageContent"""


AnthropicMessageRole = typing.Literal["USER", "ASSISTANT"]
"""AnthropicMessageRole"""


class AnthropicMessagesRequest(core.ModelBase):
    """AnthropicMessagesRequest"""

    messages: typing.List[AnthropicMessage]
    """
    Input messages to the model. This can include a single user-role message or multiple messages with
    alternating user and assistant roles.
    """

    max_tokens: int = pydantic.Field(alias=str("maxTokens"))  # type: ignore[literal-required]
    """The maximum number of tokens to generate before stopping."""

    stop_sequences: typing.Optional[typing.List[str]] = pydantic.Field(alias=str("stopSequences"), default=None)  # type: ignore[literal-required]
    """Custom text sequences that will cause the model to stop generating."""

    system: typing.Optional[typing.List[AnthropicSystemMessage]] = None
    """
    A system prompt is a way of providing context and instructions to Claude, such as specifying a 
    particular goal or role. As of now, sending multiple system prompts is not supported.
    """

    temperature: typing.Optional[float] = None
    """
    Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Note that even with 
    temperature of 0.0, the results will not be fully deterministic. Defaults to 1.0
    """

    thinking: typing.Optional[AnthropicThinkingConfig] = None
    """Configuration for enabling Claude's extended thinking."""

    tool_choice: typing.Optional[AnthropicToolChoice] = pydantic.Field(alias=str("toolChoice"), default=None)  # type: ignore[literal-required]
    """How the model should use the provided tools."""

    tools: typing.Optional[typing.List[AnthropicTool]] = None
    """Definitions of tools that the model may use."""

    top_k: typing.Optional[int] = pydantic.Field(alias=str("topK"), default=None)  # type: ignore[literal-required]
    """Only sample from the top K options for each subsequent token."""

    top_p: typing.Optional[float] = pydantic.Field(alias=str("topP"), default=None)  # type: ignore[literal-required]
    """Use nucleus sampling. You should either alter temperature or top_p, but not both"""


class AnthropicMessagesResponse(core.ModelBase):
    """AnthropicMessagesResponse"""

    content: typing.List[AnthropicCompletionContent]
    id: str
    model: str
    role: AnthropicMessageRole
    stop_reason: typing.Optional[str] = pydantic.Field(alias=str("stopReason"), default=None)  # type: ignore[literal-required]
    stop_sequence: typing.Optional[str] = pydantic.Field(alias=str("stopSequence"), default=None)  # type: ignore[literal-required]
    usage: AnthropicTokenUsage


class AnthropicNoneToolChoice(core.ModelBase):
    """AnthropicNoneToolChoice"""

    type: typing.Literal["none"] = "none"


class AnthropicRedactedThinking(core.ModelBase):
    """AnthropicRedactedThinking"""

    data: str
    type: typing.Literal["redactedThinking"] = "redactedThinking"


class AnthropicText(core.ModelBase):
    """AnthropicText"""

    text: str
    citations: typing.Optional[typing.List[AnthropicCompletionCitation]] = None
    cache_control: typing.Optional[AnthropicCacheControl] = pydantic.Field(alias=str("cacheControl"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["text"] = "text"


class AnthropicTextDocumentSource(core.ModelBase):
    """AnthropicTextDocumentSource"""

    data: str
    type: typing.Literal["text"] = "text"


class AnthropicThinking(core.ModelBase):
    """AnthropicThinking"""

    signature: str
    thinking: str
    type: typing.Literal["thinking"] = "thinking"


AnthropicThinkingConfig = typing_extensions.Annotated[
    typing.Union[AnthropicDisabledThinking, AnthropicEnabledThinking],
    pydantic.Field(discriminator="type"),
]
"""AnthropicThinkingConfig"""


class AnthropicTokenUsage(core.ModelBase):
    """AnthropicTokenUsage"""

    cache_creation_input_tokens: typing.Optional[int] = pydantic.Field(alias=str("cacheCreationInputTokens"), default=None)  # type: ignore[literal-required]
    cache_read_input_tokens: typing.Optional[int] = pydantic.Field(alias=str("cacheReadInputTokens"), default=None)  # type: ignore[literal-required]
    input_tokens: int = pydantic.Field(alias=str("inputTokens"))  # type: ignore[literal-required]
    output_tokens: int = pydantic.Field(alias=str("outputTokens"))  # type: ignore[literal-required]


AnthropicToolChoice = typing_extensions.Annotated[
    typing.Union[
        AnthropicAutoToolChoice,
        AnthropicNoneToolChoice,
        AnthropicAnyToolChoice,
        "AnthropicToolToolChoice",
    ],
    pydantic.Field(discriminator="type"),
]
"""AnthropicToolChoice"""


class AnthropicToolResult(core.ModelBase):
    """AnthropicToolResult"""

    tool_use_id: str = pydantic.Field(alias=str("toolUseId"))  # type: ignore[literal-required]
    content: typing.Optional[typing.List[AnthropicToolResultContent]] = None
    is_error: typing.Optional[bool] = pydantic.Field(alias=str("isError"), default=None)  # type: ignore[literal-required]
    cache_control: typing.Optional[AnthropicCacheControl] = pydantic.Field(alias=str("cacheControl"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["toolResult"] = "toolResult"


class AnthropicToolToolChoice(core.ModelBase):
    """AnthropicToolToolChoice"""

    name: str
    disable_parallel_tool_use: typing.Optional[AnthropicDisableParallelToolUse] = pydantic.Field(alias=str("disableParallelToolUse"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["tool"] = "tool"


class AnthropicToolUse(core.ModelBase):
    """AnthropicToolUse"""

    id: str
    input: typing.Any
    name: str
    cache_control: typing.Optional[AnthropicCacheControl] = pydantic.Field(alias=str("cacheControl"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["toolUse"] = "toolUse"


JsonSchema = typing.Dict[str, typing.Any]
"""JsonSchema"""


LanguageModelApiName = str
"""The name of the LanguageModel in the API."""


AnthropicCacheControl = AnthropicEphemeralCacheControl
"""AnthropicCacheControl"""


AnthropicCompletionCitation = AnthropicCharacterLocationCitation
"""AnthropicCompletionCitation"""


AnthropicImageSource = AnthropicImageBase64Source
"""AnthropicImageSource"""


AnthropicSystemMessage = AnthropicText
"""AnthropicSystemMessage"""


AnthropicTool = AnthropicCustomTool
"""AnthropicTool"""


AnthropicToolResultContent = AnthropicText
"""AnthropicToolResultContent"""


core.resolve_forward_references(AnthropicCompletionContent, globalns=globals(), localns=locals())
core.resolve_forward_references(AnthropicDocumentSource, globalns=globals(), localns=locals())
core.resolve_forward_references(AnthropicMessageContent, globalns=globals(), localns=locals())
core.resolve_forward_references(AnthropicThinkingConfig, globalns=globals(), localns=locals())
core.resolve_forward_references(AnthropicToolChoice, globalns=globals(), localns=locals())
core.resolve_forward_references(JsonSchema, globalns=globals(), localns=locals())

__all__ = [
    "AnthropicAnyToolChoice",
    "AnthropicAutoToolChoice",
    "AnthropicBase64PdfDocumentSource",
    "AnthropicCacheControl",
    "AnthropicCharacterLocationCitation",
    "AnthropicCompletionCitation",
    "AnthropicCompletionContent",
    "AnthropicCompletionRedactedThinking",
    "AnthropicCompletionText",
    "AnthropicCompletionThinking",
    "AnthropicCompletionToolUse",
    "AnthropicCustomTool",
    "AnthropicDisableParallelToolUse",
    "AnthropicDisabledThinking",
    "AnthropicDocument",
    "AnthropicDocumentCitations",
    "AnthropicDocumentSource",
    "AnthropicEnabledThinking",
    "AnthropicEphemeralCacheControl",
    "AnthropicImage",
    "AnthropicImageBase64Source",
    "AnthropicImageSource",
    "AnthropicMediaType",
    "AnthropicMessage",
    "AnthropicMessageContent",
    "AnthropicMessageRole",
    "AnthropicMessagesRequest",
    "AnthropicMessagesResponse",
    "AnthropicNoneToolChoice",
    "AnthropicRedactedThinking",
    "AnthropicSystemMessage",
    "AnthropicText",
    "AnthropicTextDocumentSource",
    "AnthropicThinking",
    "AnthropicThinkingConfig",
    "AnthropicTokenUsage",
    "AnthropicTool",
    "AnthropicToolChoice",
    "AnthropicToolResult",
    "AnthropicToolResultContent",
    "AnthropicToolToolChoice",
    "AnthropicToolUse",
    "JsonSchema",
    "LanguageModelApiName",
]
