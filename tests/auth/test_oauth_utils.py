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


from expects import equal
from expects import expect
from mockito import unstub
from mockito import when

from foundry._core.oauth_utils import ConfidentialClientOAuthFlowProvider
from foundry._core.oauth_utils import OAuthToken
from foundry._core.oauth_utils import OAuthTokenResponse
from foundry._core.oauth_utils import OAuthUtils
from foundry._core.oauth_utils import PublicClientOAuthFlowProvider


def test_get_token_uri():
    expect(OAuthUtils.get_token_uri()).to(equal("/multipass/api/oauth2/token"))


def test_get_authorize_uri():
    expect(OAuthUtils.get_authorize_uri()).to(equal("/multipass/api/oauth2/authorize"))


def test_get_revoke_uri():
    expect(OAuthUtils.get_revoke_uri()).to(equal("/multipass/api/oauth2/revoke_token"))


def test_create_uri():
    expect(OAuthUtils.create_uri("/api/v2/datasets", "/abc")).to(equal("/api/v2/datasets/abc"))
    expect(OAuthUtils.create_uri("/api/v2/datasets", "/abc")).to(equal("/api/v2/datasets/abc"))


def test_confidential_client_no_scopes():
    provider = ConfidentialClientOAuthFlowProvider("CLIENT_ID", "CLIENT_SECRET", "URL", scopes=None)
    assert provider.get_scopes() == []

    provider.scopes = []
    assert provider.get_scopes() == []


def test_confidential_client_with_scopes():
    provider = ConfidentialClientOAuthFlowProvider(
        "CLIENT_ID", "CLIENT_SECRET", "URL", scopes=["test"]
    )
    assert provider.get_scopes() == ["test", "offline_access"]


def test_public_client_no_scopes():
    provider = PublicClientOAuthFlowProvider("CLIENT_ID", "REDIRECT_URL", "URL", scopes=None)
    assert provider.get_scopes() == []

    provider.scopes = []
    assert provider.get_scopes() == []


def test_public_client_with_scopes():
    provider = PublicClientOAuthFlowProvider("CLIENT_ID", "REDIRECT_URL", "URL", scopes=["test"])
    assert provider.get_scopes() == ["test", "offline_access"]


def test_token_from_dict():
    import foundry._core.oauth_utils as module_under_test

    when(module_under_test.time).time().thenReturn(123)
    token = OAuthToken(
        OAuthTokenResponse(
            {"access_token": "example_token", "expires_in": 42, "token_type": "Bearer"}
        )
    )
    expect(token.access_token).to(equal("example_token"))
    expect(token.token_type).to(equal("Bearer"))
    expect(token.expires_in).to(equal(42))
    expect(token.expires_at).to(equal(123 * 1000 + 42 * 1000))
    expect(token._calculate_expiration()).to(equal(123 * 1000 + 42 * 1000))
    unstub()
