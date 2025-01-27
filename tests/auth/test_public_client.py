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
from foundry._core.oauth_utils import AuthorizeRequest
from foundry._core.public_client_auth import PublicClientAuth
from foundry._errors.not_authenticated import NotAuthenticated


def test_public_client_instantiate():
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    assert auth._client_id == "client_id"
    assert auth._redirect_url == "redirect_url"
    assert auth._hostname == "https://a.b.c.com"
    assert auth._token == None
    assert auth.url == "a.b.c.com"
    assert auth._should_refresh == True


@pytest.mark.asyncio
async def test_public_client_sign_in():
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    auth_request = mock(AuthorizeRequest)
    auth_request.url = "auth_request url"
    auth_request.state = "random string"
    auth_request.code_verifier = "random string"
    when(auth._server_oauth_flow_provider).generate_auth_request().thenReturn(auth_request)

    expect(auth.sign_in()).to(equal("auth_request url"))
    expect(auth._auth_request).to(equal(auth_request))
    unstub()


@pytest.mark.asyncio
async def test_public_client_set_token():
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    auth._auth_request = AuthorizeRequest(url="", state="", code_verifier="")
    token = mock(Token)
    token.access_token = "access_token"
    token.expires_in = 3600
    when(auth._server_oauth_flow_provider).get_token(code="", code_verifier="").thenReturn(token)
    auth.set_token(code="", state="")
    expect(auth._token).to(equal(token))
    unstub()


def test_public_client_get_token():
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    token = mock(Token)
    token.access_token = "access_token"
    token.expires_in = 3600
    auth._token = token
    expect(auth.get_token()).to(equal(token))


def test_public_client_sign_out():
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
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


def test_public_client_get_token_throws_if_not_signed_in():
    # pylint: disable=unnecessary-lambda
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    expect(lambda: auth.get_token()).to(
        raise_error(NotAuthenticated, "Client has not been authenticated.")
    )


def test_public_client_execute_with_token_successful_method():
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    token = mock(Token)
    token.access_token = "token"
    token.expires_in = 3600
    auth._token = token
    auth = spy(auth)
    expect(auth.execute_with_token(lambda _: "success")).to(equal("success"))
    verify(auth, times=0)._refresh_token()


def test_public_client_execute_with_token_failing_method():
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=True,
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
    unstub()


def _test_public_client_execute_with_token_method_raises_401():
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=True,
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
    unstub()
