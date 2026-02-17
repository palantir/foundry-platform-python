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


import contextlib

import httpx
import pytest
from mockito import any
from mockito import unstub
from mockito import verify
from mockito import when

from foundry_sdk._core.auth_utils import Token
from foundry_sdk._core.public_client_auth import PublicClientAuth
from foundry_sdk._errors.not_authenticated import NotAuthenticated

RESPONSE = {
    "access_token": "access_token",
    "token_type": "foo",
    "expires_in": 3600,
    "refresh_token": "bar",
}


@contextlib.contextmanager
def stubbed_auth(should_refresh=True, token_response=RESPONSE):
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=should_refresh,
    )

    response = httpx.Response(
        request=httpx.Request("GET", "foo"), status_code=200, json=token_response
    )
    when(auth._get_client()).post(
        "/multipass/api/oauth2/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=any(),
    ).thenReturn(response)

    response = httpx.Response(request=httpx.Request("GET", "foo"), status_code=200)
    when(auth._get_client()).post("/multipass/api/oauth2/revoke_token", data=any()).thenReturn(
        response
    )

    when(auth)._try_refresh_token().thenCallOriginalImplementation()
    when(auth).sign_out().thenCallOriginalImplementation()

    yield auth
    unstub()


def _sign_in(auth: PublicClientAuth):
    auth.sign_in()
    assert auth._auth_request is not None
    auth.set_token(code="", state=auth._auth_request.state)


def test_public_client_instantiate():
    auth = PublicClientAuth(
        client_id="client_id",
        redirect_url="redirect_url",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    assert auth._client_id == "client_id"
    assert auth._redirect_url == "redirect_url"
    assert auth._token is None
    assert auth.url == "a.b.c.com"
    assert auth._should_refresh


def test_public_client_sign_in():
    with stubbed_auth() as auth:
        assert auth.sign_in().startswith("https://a.b.c.com/multipass/api/oauth2/authorize?")
        assert auth._auth_request is not None


def test_public_client_set_token():
    with stubbed_auth() as auth:
        auth.sign_in()
        assert auth._auth_request is not None

        auth.set_token(code="", state=auth._auth_request.state)
        assert auth._token is not None
        assert auth._token.access_token == "access_token"


def test_public_client_url():
    assert (
        PublicClientAuth(client_id="", redirect_url="", hostname="https://a.b.c.com").url
        == "a.b.c.com"
    )
    assert (
        PublicClientAuth(client_id="", redirect_url="", hostname="http://a.b.c.com").url
        == "a.b.c.com"
    )
    assert PublicClientAuth(client_id="", redirect_url="", hostname="a.b.c.com/").url == "a.b.c.com"


def test_public_client_get_token():
    with stubbed_auth() as auth:
        _sign_in(auth)
        assert isinstance(auth.get_token(), Token)


def test_public_client_sign_out():
    with stubbed_auth() as auth:
        _sign_in(auth)
        assert auth._token is not None

        auth.sign_out()
        assert auth._token is None
        assert auth._stop_refresh_event._flag


def test_public_client_get_token_throws_if_not_signed_in():
    with stubbed_auth() as auth:
        with pytest.raises(NotAuthenticated) as e:
            auth.get_token()

        assert str(e.value) == "Client has not been authenticated."


def test_public_client_execute_with_token_successful_method():
    with stubbed_auth() as auth:
        _sign_in(auth)
        assert auth.execute_with_token(lambda _: httpx.Response(200)).status_code == 200
        verify(auth, times=0)._refresh_token()


def test_public_client_execute_with_token_failing_method():
    with stubbed_auth() as auth:
        _sign_in(auth)

        def raise_(ex):
            raise ex

        with pytest.raises(ValueError):
            auth.execute_with_token(lambda _: raise_(ValueError("Oops!")))

        verify(auth, times=0)._refresh_token()


def test_public_client_execute_with_token_method_raises_401():
    with stubbed_auth() as auth:
        _sign_in(auth)

        def raise_401():
            e = httpx.HTTPStatusError(
                "foo",
                request=httpx.Request("foo", url="foo"),
                response=httpx.Response(status_code=401),
            )
            raise e

        with pytest.raises(httpx.HTTPStatusError):
            auth.execute_with_token(lambda _: raise_401())

        verify(auth, times=1)._try_refresh_token()
