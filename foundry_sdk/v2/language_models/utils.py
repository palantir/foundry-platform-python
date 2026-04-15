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


from dataclasses import replace
from typing import Optional

from foundry_sdk._core.config import Config
from foundry_sdk._core.context_and_environment_vars import HOSTNAME_VAR
from foundry_sdk._core.context_and_environment_vars import TOKEN_VAR
from foundry_sdk._core.http_client import AsyncHttpClient
from foundry_sdk._core.http_client import HttpClient


def _get_api_gateway_base_url(*, preview: bool = False) -> str:
    """Get the Foundry hostname from the current execution context.

    Args:
        preview: Must be set to True to use this beta feature.

    Returns:
        The Foundry API gateway base URL.

    Raises:
        ValueError: If preview is not set to True.
        RuntimeError: If the Foundry API gateway base URL is not available in the current context.
    """
    if not preview:
        raise ValueError(
            "get_api_gateway_base_url() is in beta. "
            "Please set the preview parameter to True to use it."
        )
    hostname = HOSTNAME_VAR.get()
    if hostname is None:
        raise RuntimeError("Foundry API gateway base URL is not available in the current context.")
    return hostname


def get_foundry_token(*, preview: bool = False) -> str:
    """Get the Foundry token from the current execution context.

    Args:
        preview: Must be set to True to use this beta feature.

    Returns:
        The Foundry token.

    Raises:
        ValueError: If preview is not set to True.
        RuntimeError: If the Foundry token is not available in the current context.
    """
    if not preview:
        raise ValueError(
            "get_foundry_token() is in beta. " "Please set the preview parameter to True to use it."
        )
    token = TOKEN_VAR.get()
    if token is None:
        raise RuntimeError("Foundry token is not available in the current context.")
    return token


def get_openai_base_url(*, preview: bool = False) -> str:
    """Get the OpenAI proxy base URL for the current Foundry environment.

    Args:
        preview: Must be set to True to use this beta feature.

    Returns:
        The OpenAI proxy base URL.

    Raises:
        ValueError: If preview is not set to True.
        RuntimeError: If the Foundry API gateway base URL is not available in the current context.
    """
    if not preview:
        raise ValueError(
            "get_openai_base_url() is in beta. "
            "Please set the preview parameter to True to use it."
        )
    hostname = _get_api_gateway_base_url(preview=True)
    return f"https://{hostname}/api/v2/llm/proxy/openai/v1"


def get_anthropic_base_url(*, preview: bool = False) -> str:
    """Get the Anthropic proxy base URL for the current Foundry environment.

    Args:
        preview: Must be set to True to use this beta feature.

    Returns:
        The Anthropic proxy base URL.

    Raises:
        ValueError: If preview is not set to True.
        RuntimeError: If the Foundry API gateway base URL is not available in the current context.
    """
    if not preview:
        raise ValueError(
            "get_anthropic_base_url() is in beta. "
            "Please set the preview parameter to True to use it."
        )
    hostname = _get_api_gateway_base_url(preview=True)
    return f"https://{hostname}/api/v2/llm/proxy/anthropic"


def get_http_client(*, preview: bool = False, config: Optional[Config] = None) -> HttpClient:
    """Get an HTTP client configured for the current Foundry environment.

    Args:
        preview: Must be set to True to use this beta feature.
        config: Optional configuration for the HTTP client.

    Returns:
        An HttpClient instance configured with the Foundry hostname and authentication.

    Raises:
        ValueError: If preview is not set to True.
        RuntimeError: If the Foundry token is not available in the current context.
    """
    if not preview:
        raise ValueError(
            "get_http_client() is in beta. " "Please set the preview parameter to True to use it."
        )

    return HttpClient(config=_create_http_client_config(config))


def get_async_http_client(
    *, preview: bool = False, config: Optional[Config] = None
) -> AsyncHttpClient:
    """Get an async HTTP client configured for the current Foundry environment.

    Args:
        preview: Must be set to True to use this beta feature.
        config: Optional configuration for the async HTTP client.

    Returns:
        An AsyncHttpClient instance configured with the Foundry hostname and authentication.

    Raises:
        ValueError: If preview is not set to True.
        RuntimeError: If the Foundry token is not available in the current context.
    """
    if not preview:
        raise ValueError(
            "get_async_http_client() is in beta. "
            "Please set the preview parameter to True to use it."
        )

    return AsyncHttpClient(config=_create_http_client_config(config))


def _create_http_client_config(config: Optional[Config]) -> Config:
    """Create a Config object for the HTTP client, ensuring that the Foundry token is included in the headers.

    Args:
        config: An optional Config object provided by the user.

    Returns:
        A Config object with the Foundry token included in the default headers.

    Raises:
        RuntimeError: If the Foundry token is not available in the current context.
    """
    token = get_foundry_token(preview=True)
    auth_header = {"Authorization": f"Bearer {token}"}

    if config is None:
        return Config(default_headers=auth_header)
    else:
        merged_headers = {**auth_header, **(config.default_headers or {})}
        return replace(config, default_headers=merged_headers)
