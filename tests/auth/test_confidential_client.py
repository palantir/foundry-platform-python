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
from mockito import spy
from mockito import unstub
from mockito import verify
from mockito import when

from foundry._core.confidential_client_auth import ConfidentialClientAuth
from foundry._core.oauth import SignInResponse
from foundry._core.oauth_utils import OAuthToken
from foundry._core.oauth_utils import OAuthTokenResponse
from foundry._errors.not_authenticated import NotAuthenticated


def create_token(access_token="access_token", expired_in=3600) -> OAuthToken:
    return OAuthToken(
        OAuthTokenResponse(
            {
                "access_token": access_token,
                "token_type": "foo",
                "expires_in": expired_in,
            }
        )
    )


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


def test_confidential_client_sign_in_as_service_user():
    auth = ConfidentialClientAuth(
        client_id="client_id",
        client_secret="client_secret",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    token = create_token()
    when(auth._server_oauth_flow_provider).get_token().thenReturn(token)
    assert auth.sign_in_as_service_user() == SignInResponse(
        session={"accessToken": "access_token", "expiresIn": 3600}
    )
    assert auth.get_token() == token
    unstub()


def test_confidential_client_url():
    assert (
        ConfidentialClientAuth(client_id="", client_secret="", hostname="https://a.b.c.com").url
        == "a.b.c.com"
    )
    assert (
        ConfidentialClientAuth(client_id="", client_secret="", hostname="http://a.b.c.com").url
        == "a.b.c.com"
    )
    assert (
        ConfidentialClientAuth(client_id="", client_secret="", hostname="a.b.c.com/").url
        == "a.b.c.com"
    )


def test_confidential_client_get_token():
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    token = create_token()
    when(auth._server_oauth_flow_provider).get_token().thenReturn(token)
    auth.sign_in_as_service_user()
    assert auth.get_token() == token
    unstub()


def test_confidential_client_sign_out():
    auth = ConfidentialClientAuth(
        client_id="client_id",
        client_secret="client_secret",
        hostname="https://a.b.c.com",
        should_refresh=True,
    )
    token = create_token()
    auth._token = token
    when(auth._server_oauth_flow_provider).revoke_token("access_token").thenReturn(None)
    auth.sign_out()
    assert auth._token == None
    assert auth._stop_refresh_event._flag == True  # type: ignore
    unstub()


def test_confidential_client_get_token_throws_if_not_signed_in():
    # pylint: disable=unnecessary-lambda
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    with pytest.raises(NotAuthenticated):
        auth.get_token()


def test_confidential_client_execute_with_token_successful_method():
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    token = create_token()
    auth._token = token
    auth = spy(auth)
    assert auth.execute_with_token(lambda _: "success") == "success"
    verify(auth, times=0)._refresh_token()


def test_confidential_client_execute_with_token_failing_method():
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    token = create_token()
    auth._token = token
    when(auth).sign_out().thenReturn(None)

    def raise_(ex):
        raise ex

    with pytest.raises(ValueError):
        auth.execute_with_token(lambda _: raise_(ValueError("Oops!")))

    verify(auth, times=0)._refresh_token()
    verify(auth, times=0).sign_out()
    unstub()


def test_confidential_client_execute_with_token_method_raises_401():
    auth = ConfidentialClientAuth(
        client_id="client_id", client_secret="client_secret", hostname="https://a.b.c.com"
    )
    token = create_token()
    auth._token = token
    when(auth).sign_out().thenReturn(None)
    when(auth)._refresh_token().thenReturn(token)

    def raise_401():
        e = httpx.HTTPStatusError(
            "foo",
            request=httpx.Request("foo", url="foo"),
            response=httpx.Response(status_code=401),
        )
        raise e

    with pytest.raises(httpx.HTTPStatusError):
        auth.execute_with_token(lambda _: raise_401())

    verify(auth, times=1)._refresh_token()
    verify(auth, times=1).sign_out()
    unstub()
