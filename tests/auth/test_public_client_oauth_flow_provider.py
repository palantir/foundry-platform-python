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
import requests
from expects import equal
from expects import expect
from expects import raise_error
from mockito import mock
from mockito import unstub
from mockito import when
from requests import HTTPError

from foundry._core.oauth_utils import OAuthUtils
from foundry._core.oauth_utils import PublicClientOAuthFlowProvider


@pytest.fixture(name="client", scope="module")
def instantiate_server_oauth_flow_provider():
    return PublicClientOAuthFlowProvider(
        client_id="client_id",
        redirect_url="redirect_url",
        url="https://a.b.c",
        multipass_context_path="/multipass",
        scopes=["scope1", "scope2"],
    )


def test_get_token(client):
    import foundry._core.oauth_utils as module_under_test

    when(PublicClientOAuthFlowProvider).get_scopes().thenReturn(["scope1", "scope2"])
    when(OAuthUtils).get_token_uri("https://a.b.c", "/multipass").thenReturn("token_url")
    response = mock(requests.Response)
    response.ok = True
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
        "scope": "scope1 scope2",
    }

    when(module_under_test.requests).post("token_url", data=params, headers=headers).thenReturn(
        response
    )
    token = client.get_token(code="code", code_verifier="code_verifier")
    expect(token.access_token).to(equal("example_token"))
    expect(token.token_type).to(equal("Bearer"))
    unstub()


def test_get_token_throws_when_unsuccessful(client):
    # pylint: disable=unnecessary-lambda
    import foundry._core.oauth_utils as module_under_test

    when(PublicClientOAuthFlowProvider).get_scopes().thenReturn(
        ["scope1", "scope2", "offline_access"]
    )
    when(OAuthUtils).get_token_uri("https://a.b.c", "/multipass").thenReturn("token_url")
    response = mock(requests.Response)
    when(response).raise_for_status().thenRaise(HTTPError)

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {
        "grant_type": "authorization_code",
        "code": "code",
        "redirect_uri": "redirect_url",
        "client_id": "client_id",
        "code_verifier": "code_verifier",
        "scope": "scope1 scope2 offline_access",
    }

    when(module_under_test.requests).post("token_url", data=params, headers=headers).thenReturn(
        response
    )
    expect(lambda: client.get_token(code="code", code_verifier="code_verifier")).to(
        raise_error(HTTPError)
    )
    unstub()


def test_refresh_token(client):
    import foundry._core.oauth_utils as module_under_test

    when(OAuthUtils).get_token_uri("https://a.b.c", "/multipass").thenReturn("token_url")
    response = mock(requests.Response)
    response.ok = True
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

    when(module_under_test.requests).post("token_url", data=params, headers=headers).thenReturn(
        response
    )
    token = client.refresh_token(refresh_token="refresh_token")
    expect(token.access_token).to(equal("example_token"))
    expect(token.token_type).to(equal("Bearer"))
    unstub()


def test_revoke_token(client):
    import foundry._core.oauth_utils as module_under_test

    when(OAuthUtils).get_revoke_uri("https://a.b.c", "/multipass").thenReturn("revoke_url")
    response = mock(requests.Response)
    when(response).raise_for_status().thenReturn(None)
    when(module_under_test.requests).post(
        "revoke_url", data={"client_id": "client_id", "token": "token_to_be_revoked"}
    ).thenReturn(response)
    client.revoke_token("token_to_be_revoked")
    unstub()


def test_get_scopes(client):
    expect(client.get_scopes()).to(equal(["scope1", "scope2", "offline_access"]))
