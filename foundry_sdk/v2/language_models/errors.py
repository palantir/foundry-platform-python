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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.language_models import models as language_models_models


class AnthropicMessagesPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not messages the AnthropicModel."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    anthropicModelModelId: language_models_models.LanguageModelApiName


@dataclass
class AnthropicMessagesPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AnthropicMessagesPermissionDenied"]
    parameters: AnthropicMessagesPermissionDeniedParameters
    error_instance_id: str


class InvalidRequestParameters(typing_extensions.TypedDict):
    """
    The request was unable to be deserialized as a valid request to this endpoint. This may be either due to
    missing a required field or including a field which is not supported.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    message: str
    params: typing.Dict[str, str]


@dataclass
class InvalidRequest(errors.BadRequestError):
    name: typing.Literal["InvalidRequest"]
    parameters: InvalidRequestParameters
    error_instance_id: str


class LanguageModelInferenceErrorParameters(typing_extensions.TypedDict):
    """An error was thrown by the underlying model provider during inference."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    code: int
    message: typing_extensions.NotRequired[str]


@dataclass
class LanguageModelInferenceError(errors.BadRequestError):
    name: typing.Literal["LanguageModelInferenceError"]
    parameters: LanguageModelInferenceErrorParameters
    error_instance_id: str


class LanguageModelNotAvailableParameters(typing_extensions.TypedDict):
    """The language model requested is not available in this environment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class LanguageModelNotAvailable(errors.BadRequestError):
    name: typing.Literal["LanguageModelNotAvailable"]
    parameters: LanguageModelNotAvailableParameters
    error_instance_id: str


class LanguageModelNotFoundParameters(typing_extensions.TypedDict):
    """No known language model exists with the specified ID."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    modelId: str


@dataclass
class LanguageModelNotFound(errors.NotFoundError):
    name: typing.Literal["LanguageModelNotFound"]
    parameters: LanguageModelNotFoundParameters
    error_instance_id: str


class LanguageModelPermissionDeniedParameters(typing_extensions.TypedDict):
    """The token provided does not have permission to use this language model."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    languageModelRid: core.RID


@dataclass
class LanguageModelPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["LanguageModelPermissionDenied"]
    parameters: LanguageModelPermissionDeniedParameters
    error_instance_id: str


class MultipleSystemPromptsNotSupportedParameters(typing_extensions.TypedDict):
    """Multiple system prompts are not currently supported, but will be in the future."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    systemPromptSize: int


@dataclass
class MultipleSystemPromptsNotSupported(errors.BadRequestError):
    name: typing.Literal["MultipleSystemPromptsNotSupported"]
    parameters: MultipleSystemPromptsNotSupportedParameters
    error_instance_id: str


class MultipleToolResultContentsNotSupportedParameters(typing_extensions.TypedDict):
    """Multiple tool result contents are not currently supported, but will be in the future."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    toolResultContentsSize: int


@dataclass
class MultipleToolResultContentsNotSupported(errors.BadRequestError):
    name: typing.Literal["MultipleToolResultContentsNotSupported"]
    parameters: MultipleToolResultContentsNotSupportedParameters
    error_instance_id: str


class OpenAiEmbeddingsPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not embeddings the OpenAiModel."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    openAiModelModelId: language_models_models.LanguageModelApiName


@dataclass
class OpenAiEmbeddingsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["OpenAiEmbeddingsPermissionDenied"]
    parameters: OpenAiEmbeddingsPermissionDeniedParameters
    error_instance_id: str


__all__ = [
    "AnthropicMessagesPermissionDenied",
    "InvalidRequest",
    "LanguageModelInferenceError",
    "LanguageModelNotAvailable",
    "LanguageModelNotFound",
    "LanguageModelPermissionDenied",
    "MultipleSystemPromptsNotSupported",
    "MultipleToolResultContentsNotSupported",
    "OpenAiEmbeddingsPermissionDenied",
]
