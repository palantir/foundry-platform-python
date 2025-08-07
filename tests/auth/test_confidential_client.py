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
from mockito import spy
from mockito import unstub
from mockito import verify
from mockito import when

from foundry_sdk._core.confidential_client_auth import ConfidentialClientAuth
from foundry_sdk._core.oauth_utils import SignInResponse

RESPONSE = {
    "access_token": "access_token",
    "token_type": "foo",
    "expires_in": 3600,
}


@contextlib.contextmanager
def stubbed_auth(should_refresh=True, token_response=RESPONSE):
    auth = ConfidentialClientAuth(
        client_id="client_id",
        client_secret="client_secret",
        hostname="https://a.b.c.com",
        should_refresh=should_refresh,
    )

    response = httpx.Response(
        request=httpx.Request("GET", "foo"), status_code=200, json=token_response
    )
    when(auth._get_client()).post("/multipass/api/oauth2/token", data=any()).thenReturn(response)

    response = httpx.Response(request=httpx.Request("GET", "foo"), status_code=200)
    when(auth._get_client()).post("/multipass/api/oauth2/revoke_token", data=any()).thenReturn(
        response
    )

    when(auth)._try_refresh_token().thenCallOriginalImplementation()
    when(auth).sign_out().thenCallOriginalImplementation()

    yield auth
    unstub()


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


def test_confidential_client_url():
    assert (
        ConfidentialClientAuth(client_id="1", client_secret="1", hostname="https://a.b.c.com").url
        == "a.b.c.com"
    )
    assert (
        ConfidentialClientAuth(client_id="1", client_secret="1", hostname="http://a.b.c.com").url
        == "a.b.c.com"
    )
    assert (
        ConfidentialClientAuth(client_id="1", client_secret="1", hostname="a.b.c.com/").url
        == "a.b.c.com"
    )


def test_confidential_client_get_token():
    with stubbed_auth() as auth:
        assert auth.get_token().access_token == "access_token"


def test_confidential_client_sign_out():
    with stubbed_auth() as auth:
        auth.get_token()
        assert auth._token is not None
        auth.sign_out()
        assert auth._token is None
        assert auth._stop_refresh_event._flag == True  # type: ignore


def test_confidential_client_execute_with_token_successful_method():
    with stubbed_auth() as auth:
        assert auth.execute_with_token(lambda _: httpx.Response(200)).status_code == 200
        verify(auth, times=0)._refresh_token()


def test_confidential_client_execute_with_token_failing_method():
    with stubbed_auth() as auth:

        def raise_(ex):
            raise ex

        with pytest.raises(ValueError):
            auth.execute_with_token(lambda _: raise_(ValueError("Oops!")))

        verify(auth, times=0)._refresh_token()
        verify(auth, times=0).sign_out()


def test_confidential_client_execute_with_token_method_raises_401():
    with stubbed_auth() as auth:

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
        verify(auth, times=1).sign_out()


def test_invalid_client_id_raises_appropriate_error():
    assert pytest.raises(TypeError, lambda: ConfidentialClientAuth())  # type: ignore
    assert pytest.raises(TypeError, lambda: ConfidentialClientAuth(1, "1"))  # type: ignore
    assert pytest.raises(TypeError, lambda: ConfidentialClientAuth(None, "1"))  # type: ignore
    assert pytest.raises(ValueError, lambda: ConfidentialClientAuth("", "1"))


def test_invalid_client_secret_raises_appropriate_error():
    assert pytest.raises(TypeError, lambda: ConfidentialClientAuth("1"))  # type: ignore
    assert pytest.raises(TypeError, lambda: ConfidentialClientAuth("1", 1))  # type: ignore
    assert pytest.raises(TypeError, lambda: ConfidentialClientAuth("1", None))  # type: ignore
    assert pytest.raises(ValueError, lambda: ConfidentialClientAuth("1", ""))


def test_invalid_hostname_raises_appropriate_error():
    assert pytest.raises(TypeError, lambda: ConfidentialClientAuth("1", "1", 1))  # type: ignore
    assert pytest.raises(ValueError, lambda: ConfidentialClientAuth("1", "1", ""))  # type: ignore


def test_invalid_scopes_raises_appropriate_error():
    assert pytest.raises(TypeError, lambda: ConfidentialClientAuth("1", "1", scopes=1))  # type: ignore
