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


import pytest

from foundry_sdk._core.context_and_environment_vars import HOSTNAME_VAR
from foundry_sdk._core.context_and_environment_vars import TOKEN_VAR
from foundry_sdk._core.http_client import HttpClient, AsyncHttpClient
from foundry_sdk.v2.language_models import (
    get_anthropic_base_url,
    get_foundry_token,
    get_google_base_url,
    get_http_client,
    get_async_http_client,
    get_openai_base_url,
)
from foundry_sdk.v2.language_models.utils import _get_api_gateway_base_url


class TestPreviewParameter:
    """Test that all functions require preview=True."""

    def test__get_api_gateway_base_url_requires_preview(self):
        with pytest.raises(ValueError, match="preview parameter"):
            _get_api_gateway_base_url()

    def test_get_foundry_token_requires_preview(self):
        with pytest.raises(ValueError, match="preview parameter"):
            get_foundry_token()

    def test_get_openai_base_url_requires_preview(self):
        with pytest.raises(ValueError, match="preview parameter"):
            get_openai_base_url()

    def test_get_anthropic_base_url_requires_preview(self):
        with pytest.raises(ValueError, match="preview parameter"):
            get_anthropic_base_url()

    def test_get_google_base_url_requires_preview(self):
        with pytest.raises(ValueError, match="preview parameter"):
            get_google_base_url()

    def test_get_http_client_requires_preview(self):
        with pytest.raises(ValueError, match="preview parameter"):
            get_http_client()


class TestGetApiGatewayBaseUrl:
    """Test _get_api_gateway_base_url function."""

    def test_returns_hostname_from_context(self):
        token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        try:
            result = _get_api_gateway_base_url(preview=True)
            assert result == "test.palantirfoundry.com"
        finally:
            HOSTNAME_VAR.reset(token)

    def test_raises_runtime_error_when_not_in_context(self):
        with pytest.raises(RuntimeError, match="not available"):
            _get_api_gateway_base_url(preview=True)


class TestGetFoundryToken:
    """Test get_foundry_token function."""

    def test_returns_token_from_context(self):
        token = TOKEN_VAR.set("test-token-12345")
        try:
            result = get_foundry_token(preview=True)
            assert result == "test-token-12345"
        finally:
            TOKEN_VAR.reset(token)

    def test_raises_runtime_error_when_not_in_context(self):
        with pytest.raises(RuntimeError, match="not available"):
            get_foundry_token(preview=True)


class TestGetOpenaiBaseUrl:
    """Test get_openai_base_url function."""

    def test_returns_correct_url(self):
        token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        try:
            result = get_openai_base_url(preview=True)
            assert result == "https://test.palantirfoundry.com/api/v2/llm/proxy/openai/v1"
        finally:
            HOSTNAME_VAR.reset(token)

    def test_raises_runtime_error_when_not_in_context(self):
        with pytest.raises(RuntimeError, match="not available"):
            get_openai_base_url(preview=True)


class TestGetAnthropicBaseUrl:
    """Test get_anthropic_base_url function."""

    def test_returns_correct_url(self):
        token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        try:
            result = get_anthropic_base_url(preview=True)
            assert result == "https://test.palantirfoundry.com/api/v2/llm/proxy/anthropic"
        finally:
            HOSTNAME_VAR.reset(token)

    def test_raises_runtime_error_when_not_in_context(self):
        with pytest.raises(RuntimeError, match="not available"):
            get_anthropic_base_url(preview=True)


class TestGetGoogleBaseUrl:
    """Test get_google_base_url function."""

    def test_returns_correct_url(self):
        token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        try:
            result = get_google_base_url(preview=True)
            assert result == "https://test.palantirfoundry.com/api/v2/llm/proxy/google"
        finally:
            HOSTNAME_VAR.reset(token)

    def test_raises_runtime_error_when_not_in_context(self):
        with pytest.raises(RuntimeError, match="not available"):
            get_google_base_url(preview=True)


class TestGetHttpClient:
    """Test get_http_client function."""

    def test_returns_http_client(self):
        hostname_token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        auth_token = TOKEN_VAR.set("test-token-12345")
        try:
            result = get_http_client(preview=True)
            assert isinstance(result, HttpClient)
        finally:
            HOSTNAME_VAR.reset(hostname_token)
            TOKEN_VAR.reset(auth_token)

    def test_injects_auth_header(self):
        hostname_token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        auth_token = TOKEN_VAR.set("test-token-12345")
        try:
            client = get_http_client(preview=True)
            assert client.headers["Authorization"] == "Bearer test-token-12345"
        finally:
            HOSTNAME_VAR.reset(hostname_token)
            TOKEN_VAR.reset(auth_token)

    def test_merges_auth_header_with_custom_headers(self):
        from foundry_sdk._core.config import Config

        hostname_token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        auth_token = TOKEN_VAR.set("test-token-12345")
        try:
            config = Config(default_headers={"X-Custom-Header": "custom-value"})
            client = get_http_client(preview=True, config=config)
            assert client.headers["Authorization"] == "Bearer test-token-12345"
            assert client.headers["X-Custom-Header"] == "custom-value"
        finally:
            HOSTNAME_VAR.reset(hostname_token)
            TOKEN_VAR.reset(auth_token)

    def test_user_headers_override_auth_header(self):
        from foundry_sdk._core.config import Config

        hostname_token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        auth_token = TOKEN_VAR.set("test-token-12345")
        try:
            config = Config(default_headers={"Authorization": "Bearer custom-token"})
            client = get_http_client(preview=True, config=config)
            # User-provided auth header should override the auto-injected one
            assert client.headers["Authorization"] == "Bearer custom-token"
        finally:
            HOSTNAME_VAR.reset(hostname_token)
            TOKEN_VAR.reset(auth_token)

    def test_raises_runtime_error_when_hostname_not_in_context(self):
        with pytest.raises(RuntimeError, match="not available"):
            get_http_client(preview=True)

    def test_raises_runtime_error_when_token_not_in_context(self):
        hostname_token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        try:
            with pytest.raises(RuntimeError, match="not available"):
                get_http_client(preview=True)
        finally:
            HOSTNAME_VAR.reset(hostname_token)


class TestGetAsyncHttpClient:
    """Test get_async_http_client function."""

    def test_returns_async_http_client(self):
        hostname_token = HOSTNAME_VAR.set("test.palantirfoundry.com")
        auth_token = TOKEN_VAR.set("test-token-12345")
        try:
            result = get_async_http_client(preview=True)
            assert isinstance(result, AsyncHttpClient)
        finally:
            HOSTNAME_VAR.reset(hostname_token)
            TOKEN_VAR.reset(auth_token)
