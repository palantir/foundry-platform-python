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

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.language_models import errors as language_models_errors
from foundry_sdk.v2.language_models import models as language_models_models


class AnthropicModelClient:
    """
    The API client for the AnthropicModel Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AnthropicModelClientStreaming(self)
        self.with_raw_response = _AnthropicModelClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def messages(
        self,
        anthropic_model_model_id: language_models_models.LanguageModelApiName,
        *,
        max_tokens: int,
        messages: typing.List[language_models_models.AnthropicMessage],
        preview: typing.Optional[core_models.PreviewMode] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        system: typing.Optional[typing.List[language_models_models.AnthropicSystemMessage]] = None,
        temperature: typing.Optional[float] = None,
        thinking: typing.Optional[language_models_models.AnthropicThinkingConfig] = None,
        tool_choice: typing.Optional[language_models_models.AnthropicToolChoice] = None,
        tools: typing.Optional[typing.List[language_models_models.AnthropicTool]] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> language_models_models.AnthropicMessagesResponse:
        """

        :param anthropic_model_model_id:
        :type anthropic_model_model_id: LanguageModelApiName
        :param max_tokens: The maximum number of tokens to generate before stopping.
        :type max_tokens: int
        :param messages: Input messages to the model. This can include a single user-role message or multiple messages with alternating user and assistant roles.
        :type messages: List[AnthropicMessage]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param stop_sequences: Custom text sequences that will cause the model to stop generating.
        :type stop_sequences: Optional[List[str]]
        :param system: A system prompt is a way of providing context and instructions to Claude, such as specifying a  particular goal or role. As of now, sending multiple system prompts is not supported.
        :type system: Optional[List[AnthropicSystemMessage]]
        :param temperature: Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Note that even with  temperature of 0.0, the results will not be fully deterministic. Defaults to 1.0
        :type temperature: Optional[float]
        :param thinking: Configuration for enabling Claude's extended thinking.
        :type thinking: Optional[AnthropicThinkingConfig]
        :param tool_choice: How the model should use the provided tools.
        :type tool_choice: Optional[AnthropicToolChoice]
        :param tools: Definitions of tools that the model may use.
        :type tools: Optional[List[AnthropicTool]]
        :param top_k: Only sample from the top K options for each subsequent token.
        :type top_k: Optional[int]
        :param top_p: Use nucleus sampling. You should either alter temperature or top_p, but not both
        :type top_p: Optional[float]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: language_models_models.AnthropicMessagesResponse

        :raises AnthropicMessagesPermissionDenied: Could not messages the AnthropicModel.
        :raises MultipleSystemPromptsNotSupported: Multiple system prompts are not currently supported, but will be in the future.
        :raises MultipleToolResultContentsNotSupported: Multiple tool result contents are not currently supported, but will be in the future.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/languageModels/anthropic/{anthropicModelModelId}/messages",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "anthropicModelModelId": anthropic_model_model_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=language_models_models.AnthropicMessagesRequest(
                    messages=messages,
                    max_tokens=max_tokens,
                    stop_sequences=stop_sequences,
                    system=system,
                    temperature=temperature,
                    thinking=thinking,
                    tool_choice=tool_choice,
                    tools=tools,
                    top_k=top_k,
                    top_p=top_p,
                ),
                response_type=language_models_models.AnthropicMessagesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AnthropicMessagesPermissionDenied": language_models_errors.AnthropicMessagesPermissionDenied,
                    "MultipleSystemPromptsNotSupported": language_models_errors.MultipleSystemPromptsNotSupported,
                    "MultipleToolResultContentsNotSupported": language_models_errors.MultipleToolResultContentsNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AnthropicModelClientRaw:
    def __init__(self, client: AnthropicModelClient) -> None:
        def messages(_: language_models_models.AnthropicMessagesResponse): ...

        self.messages = core.with_raw_response(messages, client.messages)


class _AnthropicModelClientStreaming:
    def __init__(self, client: AnthropicModelClient) -> None:
        def messages(_: language_models_models.AnthropicMessagesResponse): ...

        self.messages = core.with_streaming_response(messages, client.messages)


class AsyncAnthropicModelClient:
    """
    The API client for the AnthropicModel Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncAnthropicModelClientStreaming(self)
        self.with_raw_response = _AsyncAnthropicModelClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def messages(
        self,
        anthropic_model_model_id: language_models_models.LanguageModelApiName,
        *,
        max_tokens: int,
        messages: typing.List[language_models_models.AnthropicMessage],
        preview: typing.Optional[core_models.PreviewMode] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        system: typing.Optional[typing.List[language_models_models.AnthropicSystemMessage]] = None,
        temperature: typing.Optional[float] = None,
        thinking: typing.Optional[language_models_models.AnthropicThinkingConfig] = None,
        tool_choice: typing.Optional[language_models_models.AnthropicToolChoice] = None,
        tools: typing.Optional[typing.List[language_models_models.AnthropicTool]] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[language_models_models.AnthropicMessagesResponse]:
        """

        :param anthropic_model_model_id:
        :type anthropic_model_model_id: LanguageModelApiName
        :param max_tokens: The maximum number of tokens to generate before stopping.
        :type max_tokens: int
        :param messages: Input messages to the model. This can include a single user-role message or multiple messages with alternating user and assistant roles.
        :type messages: List[AnthropicMessage]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param stop_sequences: Custom text sequences that will cause the model to stop generating.
        :type stop_sequences: Optional[List[str]]
        :param system: A system prompt is a way of providing context and instructions to Claude, such as specifying a  particular goal or role. As of now, sending multiple system prompts is not supported.
        :type system: Optional[List[AnthropicSystemMessage]]
        :param temperature: Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Note that even with  temperature of 0.0, the results will not be fully deterministic. Defaults to 1.0
        :type temperature: Optional[float]
        :param thinking: Configuration for enabling Claude's extended thinking.
        :type thinking: Optional[AnthropicThinkingConfig]
        :param tool_choice: How the model should use the provided tools.
        :type tool_choice: Optional[AnthropicToolChoice]
        :param tools: Definitions of tools that the model may use.
        :type tools: Optional[List[AnthropicTool]]
        :param top_k: Only sample from the top K options for each subsequent token.
        :type top_k: Optional[int]
        :param top_p: Use nucleus sampling. You should either alter temperature or top_p, but not both
        :type top_p: Optional[float]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[language_models_models.AnthropicMessagesResponse]

        :raises AnthropicMessagesPermissionDenied: Could not messages the AnthropicModel.
        :raises MultipleSystemPromptsNotSupported: Multiple system prompts are not currently supported, but will be in the future.
        :raises MultipleToolResultContentsNotSupported: Multiple tool result contents are not currently supported, but will be in the future.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/languageModels/anthropic/{anthropicModelModelId}/messages",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "anthropicModelModelId": anthropic_model_model_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=language_models_models.AnthropicMessagesRequest(
                    messages=messages,
                    max_tokens=max_tokens,
                    stop_sequences=stop_sequences,
                    system=system,
                    temperature=temperature,
                    thinking=thinking,
                    tool_choice=tool_choice,
                    tools=tools,
                    top_k=top_k,
                    top_p=top_p,
                ),
                response_type=language_models_models.AnthropicMessagesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AnthropicMessagesPermissionDenied": language_models_errors.AnthropicMessagesPermissionDenied,
                    "MultipleSystemPromptsNotSupported": language_models_errors.MultipleSystemPromptsNotSupported,
                    "MultipleToolResultContentsNotSupported": language_models_errors.MultipleToolResultContentsNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncAnthropicModelClientRaw:
    def __init__(self, client: AsyncAnthropicModelClient) -> None:
        def messages(_: language_models_models.AnthropicMessagesResponse): ...

        self.messages = core.async_with_raw_response(messages, client.messages)


class _AsyncAnthropicModelClientStreaming:
    def __init__(self, client: AsyncAnthropicModelClient) -> None:
        def messages(_: language_models_models.AnthropicMessagesResponse): ...

        self.messages = core.async_with_streaming_response(messages, client.messages)
