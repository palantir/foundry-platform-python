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


__all__ = [
    "AnthropicMessagesPermissionDenied",
    "MultipleSystemPromptsNotSupported",
    "MultipleToolResultContentsNotSupported",
]
