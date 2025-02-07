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
from mockito import mock
from mockito import unstub
from mockito import when

from foundry._core.http_client import HttpClient
from foundry._core.oauth_utils import ConfidentialClientOAuthFlowProvider
from foundry._core.oauth_utils import OAuthUtils


@pytest.fixture(name="client", scope="module")
def instantiate_server_oauth_flow_provider():
    return ConfidentialClientOAuthFlowProvider(
        client_id="client_id",
        client_secret="client_secret",
        multipass_context_path="/multipass",
        scopes=["scope1", "scope2"],
    )


@pytest.fixture(scope="module")
def http_client():
    return HttpClient("https://a.b.c.com")


def test_get_token(client, http_client):
    response = mock(httpx.Response)
    when(response).raise_for_status().thenReturn(None)
    when(response).json().thenReturn(
        {"access_token": "example_token", "expires_in": 42, "token_type": "Bearer"}
    )
    when(http_client).post(
        "/multipass/api/oauth2/token",
        data={
            "client_id": "client_id",
            "client_secret": "client_secret",
            "grant_type": "client_credentials",
            "scope": "scope1 scope2 offline_access",
        },
    ).thenReturn(response)
    token = client.get_token(http_client)
    expect(token.access_token).to(equal("example_token"))
    expect(token.token_type).to(equal("Bearer"))
    unstub()


def test_get_token_throws_when_unsuccessful(client, http_client):
    response = mock(httpx.Response)
    when(response).raise_for_status().thenRaise(
        httpx.HTTPStatusError(
            "Foo",
            request=httpx.Request("GET", "/foo/bar"),
            response=httpx.Response(200),
        ),
    )
    when(http_client).post(
        "/multipass/api/oauth2/token",
        data={
            "client_id": "client_id",
            "client_secret": "client_secret",
            "grant_type": "client_credentials",
            "scope": "scope1 scope2 offline_access",
        },
    ).thenReturn(response)

    with pytest.raises(httpx.HTTPStatusError):
        client.get_token(http_client)

    unstub()


def test_revoke_token(client, http_client):
    response = mock(httpx.Response)
    when(response).raise_for_status().thenReturn(None)
    when(http_client).post(
        "/multipass/api/oauth2/revoke_token",
        data={
            "client_id": "client_id",
            "client_secret": "client_secret",
            "token": "token_to_be_revoked",
        },
    ).thenReturn(response)
    client.revoke_token(http_client, "token_to_be_revoked")
    unstub()


def test_get_scopes(client):
    expect(client.get_scopes()).to(equal(["scope1", "scope2", "offline_access"]))
