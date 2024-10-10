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
from mockito import spy
from mockito import unstub
from mockito import verify
from mockito import when

from foundry._core.auth_utils import Token
from foundry._core.confidential_client_auth import ConfidentialClientAuth
from foundry._core.oauth import SignInResponse
from foundry._errors.not_authenticated import NotAuthenticated


def test_confidential_client_instantiate():
    auth = ConfidentialClientAuth(
        client_id="client_id",
        client_secret="client_secret",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    assert auth._client_id == "client_id"
    assert auth._client_secret == "client_secret"
    assert auth._hostname == "https://a.b.c.com"
    assert auth._token == None
    assert auth.url == "a.b.c.com"
    assert auth._should_refresh == True


@pytest.mark.asyncio
async def test_confidential_client_sign_in_as_service_user():
    auth = ConfidentialClientAuth(
        client_id="client_id",
        client_secret="client_secret",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    token = mock(Token)
    token.access_token = "token"
    token.expires_in = 3600
    when(auth._server_oauth_flow_provider).get_token().thenReturn(token)
    expect(auth.sign_in_as_service_user()).to(
        equal(SignInResponse(session={"accessToken": "token", "expiresIn": 3600}))
    )
    expect(auth.get_token()).to(equal(token))
    unstub()


def test_confidential_client_get_token():
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    token = mock(Token)
    token.access_token = "token"
    token.expires_in = 3600
    when(auth._server_oauth_flow_provider).get_token().thenReturn(token)
    auth.sign_in_as_service_user()
    expect(auth.get_token()).to(equal(token))
    unstub()


def test_confidential_client_sign_out():
    auth = ConfidentialClientAuth(
        client_id="client_id",
        client_secret="client_secret",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    token = mock(Token)
    token.access_token = "access_token"
    token.expires_in = 3600
    auth._token = token
    when(auth._server_oauth_flow_provider).revoke_token("access_token").thenReturn(None)
    auth.sign_out()
    expect(auth._token).to(equal(None))
    expect(auth._stop_refresh_event._flag).to(equal(True))
    unstub()


def test_confidential_client_get_token_throws_if_not_signed_in():
    # pylint: disable=unnecessary-lambda
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    expect(lambda: auth.get_token()).to(raise_error(NotAuthenticated))


def test_confidential_client_execute_with_token_successful_method():
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    token = mock(Token)
    token.access_token = "token"
    token.expires_in = 3600
    auth._token = token
    auth = spy(auth)
    expect(auth.execute_with_token(lambda _: "success")).to(equal("success"))
    verify(auth, times=0)._refresh_token()


def test_confidential_client_execute_with_token_failing_method():
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    token = mock(Token)
    token.access_token = "token"
    token.expires_in = 3600
    auth._token = token
    when(auth).sign_out().thenReturn(None)

    def raise_(ex):
        raise ex

    expect(lambda: auth.execute_with_token(lambda _: raise_(ValueError("Oops!")))).to(
        raise_error(ValueError)
    )
    verify(auth, times=0)._refresh_token()
    verify(auth, times=0).sign_out()
    unstub()


def test_confidential_client_execute_with_token_method_raises_401():
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    token = mock(Token)
    token.access_token = "access_token"
    token.expires_in = 3600
    auth._token = token
    when(auth).sign_out().thenReturn(None)
    when(auth)._refresh_token().thenReturn(token)

    def raise_401():
        e = requests.HTTPError()
        e.response = requests.Response()
        e.response.status_code = 401
        raise e

    expect(lambda: auth.execute_with_token(lambda _: raise_401())).to(
        raise_error(requests.HTTPError)
    )
    verify(auth, times=1)._refresh_token()
    verify(auth, times=1).sign_out()
    unstub()
