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


class OpenAiModelClient:
    """
    The API client for the OpenAiModel Resource.

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

        self.with_streaming_response = _OpenAiModelClientStreaming(self)
        self.with_raw_response = _OpenAiModelClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def embeddings(
        self,
        open_ai_model_model_id: language_models_models.LanguageModelApiName,
        *,
        input: language_models_models.OpenAiEmbeddingInput,
        attribution: typing.Optional[core_models.Attribution] = None,
        dimensions: typing.Optional[int] = None,
        encoding_format: typing.Optional[language_models_models.OpenAiEncodingFormat] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> language_models_models.OpenAiEmbeddingsResponse:
        """

        :param open_ai_model_model_id:
        :type open_ai_model_model_id: LanguageModelApiName
        :param input: Input text to embed, encoded as an array of strings. Each input must not exceed the max input  tokens for the model (8192 tokens for all embedding models).
        :type input: OpenAiEmbeddingInput
        :param attribution:
        :type attribution: Optional[Attribution]
        :param dimensions: The number of dimensions the resulting output embeddings should have.  Only supported in text-embedding-3 and later models.
        :type dimensions: Optional[int]
        :param encoding_format: The format to return the embeddings in. Can be either float or base64.
        :type encoding_format: Optional[OpenAiEncodingFormat]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: language_models_models.OpenAiEmbeddingsResponse

        :raises OpenAiEmbeddingsPermissionDenied: Could not embeddings the OpenAiModel.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/languageModels/openAi/{openAiModelModelId}/embeddings",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "openAiModelModelId": open_ai_model_model_id,
                },
                header_params={
                    "attribution": attribution,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=language_models_models.OpenAiEmbeddingsRequest(
                    input=input,
                    dimensions=dimensions,
                    encoding_format=encoding_format,
                ),
                response_type=language_models_models.OpenAiEmbeddingsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "OpenAiEmbeddingsPermissionDenied": language_models_errors.OpenAiEmbeddingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OpenAiModelClientRaw:
    def __init__(self, client: OpenAiModelClient) -> None:
        def embeddings(_: language_models_models.OpenAiEmbeddingsResponse): ...

        self.embeddings = core.with_raw_response(embeddings, client.embeddings)


class _OpenAiModelClientStreaming:
    def __init__(self, client: OpenAiModelClient) -> None:
        def embeddings(_: language_models_models.OpenAiEmbeddingsResponse): ...

        self.embeddings = core.with_streaming_response(embeddings, client.embeddings)


class AsyncOpenAiModelClient:
    """
    The API client for the OpenAiModel Resource.

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

        self.with_streaming_response = _AsyncOpenAiModelClientStreaming(self)
        self.with_raw_response = _AsyncOpenAiModelClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def embeddings(
        self,
        open_ai_model_model_id: language_models_models.LanguageModelApiName,
        *,
        input: language_models_models.OpenAiEmbeddingInput,
        attribution: typing.Optional[core_models.Attribution] = None,
        dimensions: typing.Optional[int] = None,
        encoding_format: typing.Optional[language_models_models.OpenAiEncodingFormat] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[language_models_models.OpenAiEmbeddingsResponse]:
        """

        :param open_ai_model_model_id:
        :type open_ai_model_model_id: LanguageModelApiName
        :param input: Input text to embed, encoded as an array of strings. Each input must not exceed the max input  tokens for the model (8192 tokens for all embedding models).
        :type input: OpenAiEmbeddingInput
        :param attribution:
        :type attribution: Optional[Attribution]
        :param dimensions: The number of dimensions the resulting output embeddings should have.  Only supported in text-embedding-3 and later models.
        :type dimensions: Optional[int]
        :param encoding_format: The format to return the embeddings in. Can be either float or base64.
        :type encoding_format: Optional[OpenAiEncodingFormat]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[language_models_models.OpenAiEmbeddingsResponse]

        :raises OpenAiEmbeddingsPermissionDenied: Could not embeddings the OpenAiModel.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/languageModels/openAi/{openAiModelModelId}/embeddings",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "openAiModelModelId": open_ai_model_model_id,
                },
                header_params={
                    "attribution": attribution,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=language_models_models.OpenAiEmbeddingsRequest(
                    input=input,
                    dimensions=dimensions,
                    encoding_format=encoding_format,
                ),
                response_type=language_models_models.OpenAiEmbeddingsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "OpenAiEmbeddingsPermissionDenied": language_models_errors.OpenAiEmbeddingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOpenAiModelClientRaw:
    def __init__(self, client: AsyncOpenAiModelClient) -> None:
        def embeddings(_: language_models_models.OpenAiEmbeddingsResponse): ...

        self.embeddings = core.async_with_raw_response(embeddings, client.embeddings)


class _AsyncOpenAiModelClientStreaming:
    def __init__(self, client: AsyncOpenAiModelClient) -> None:
        def embeddings(_: language_models_models.OpenAiEmbeddingsResponse): ...

        self.embeddings = core.async_with_streaming_response(embeddings, client.embeddings)
