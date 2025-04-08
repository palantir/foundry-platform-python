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


import httpx
import pytest
from expects import equal
from expects import expect
from expects import raise_error
from mockito import mock
from mockito import unstub
from mockito import when

from foundry_sdk._core.http_client import HttpClient
from foundry_sdk._core.oauth_utils import OAuthUtils
from foundry_sdk._core.oauth_utils import PublicClientOAuthFlowProvider


@pytest.fixture(name="client", scope="module")
def instantiate_server_oauth_flow_provider():
    return PublicClientOAuthFlowProvider(
        client_id="client_id",
        redirect_url="redirect_url",
        multipass_context_path="/multipass",
        scopes=["scope1", "scope2"],
    )


@pytest.fixture(scope="module")
def http_client():
    return HttpClient("https://a.b.c.com")


def test_get_token(http_client, client):
    response = mock(httpx.Response)
    when(response).raise_for_status().thenReturn(None)
    when(response).json().thenReturn(
        {"access_token": "example_token", "expires_in": 42, "token_type": "Bearer"}
    )

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {
        "grant_type": "authorization_code",
        "code": "code",
        "redirect_uri": "redirect_url",
        "client_id": "client_id",
        "code_verifier": "code_verifier",
        "scope": "scope1 scope2 offline_access",
    }

    when(http_client).post("/multipass/api/oauth2/token", data=params, headers=headers).thenReturn(
        response
    )
    token = client.get_token(http_client, code="code", code_verifier="code_verifier")
    expect(token.access_token).to(equal("example_token"))
    expect(token.token_type).to(equal("Bearer"))
    unstub()


def test_get_token_throws_when_unsuccessful(http_client, client):
    response = mock(httpx.Response)
    when(response).raise_for_status().thenRaise(
        httpx.HTTPStatusError(
            "Foo",
            request=httpx.Request("GET", "/foo/bar"),
            response=httpx.Response(200),
        ),
    )

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {
        "grant_type": "authorization_code",
        "code": "code",
        "redirect_uri": "redirect_url",
        "client_id": "client_id",
        "code_verifier": "code_verifier",
        "scope": "scope1 scope2 offline_access",
    }

    when(http_client).post("/multipass/api/oauth2/token", data=params, headers=headers).thenReturn(
        response
    )

    with pytest.raises(httpx.HTTPStatusError):
        client.get_token(http_client, code="code", code_verifier="code_verifier")

    unstub()


def test_refresh_token(http_client, client):
    response = mock(httpx.Response)
    when(response).raise_for_status().thenReturn(None)
    when(response).json().thenReturn(
        {"access_token": "example_token", "expires_in": 42, "token_type": "Bearer"}
    )

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {
        "grant_type": "refresh_token",
        "client_id": "client_id",
        "refresh_token": "refresh_token",
    }

    when(http_client).post("/multipass/api/oauth2/token", data=params, headers=headers).thenReturn(
        response
    )
    token = client.refresh_token(http_client, refresh_token="refresh_token")
    expect(token.access_token).to(equal("example_token"))
    expect(token.token_type).to(equal("Bearer"))
    unstub()


def test_revoke_token(http_client, client):
    response = mock(httpx.Response)
    when(response).raise_for_status().thenReturn(None)
    when(http_client).post(
        "/multipass/api/oauth2/revoke_token",
        data={"client_id": "client_id", "token": "token_to_be_revoked"},
    ).thenReturn(response)
    client.revoke_token(http_client, "token_to_be_revoked")
    unstub()


def test_get_scopes(http_client, client):
    expect(client.get_scopes()).to(equal(["scope1", "scope2", "offline_access"]))
