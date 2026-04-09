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

"""Tests that FoundryClient hostname is correctly propagated to OAuth auth objects
even when environment variables would otherwise provide a hostname."""

import os
from unittest.mock import patch

import pytest

from foundry_sdk._core.confidential_client_auth import ConfidentialClientAuth
from foundry_sdk._core.hostname_supplier import EndpointType
from foundry_sdk._core.hostname_supplier import StaticHostnameSupplier


class TestOAuthHostnameParameterize:
    """Regression tests for hostname propagation from FoundryClient to OAuth auth objects."""

    def test_parameterize_sets_hostname_when_no_hostname_provided(self):
        """When auth is created without a hostname, _parameterize should set it."""
        auth = ConfidentialClientAuth(
            client_id="my-client-id",
            client_secret="my-client-secret",
        )
        assert auth._hostname_supplier is None

        supplier = StaticHostnameSupplier("https://correct.host.com")
        auth._parameterize(supplier, None)

        assert auth._hostname_supplier is supplier
        assert auth._get_base_url() == "https://correct.host.com/multipass/api"

    def test_parameterize_preserves_explicit_hostname(self):
        """When auth is created with an explicit hostname, _parameterize should not override it."""
        auth = ConfidentialClientAuth(
            client_id="my-client-id",
            client_secret="my-client-secret",
            hostname="https://explicit.host.com",
        )
        assert auth._hostname_supplier is not None

        supplier = StaticHostnameSupplier("https://other.host.com")
        auth._parameterize(supplier, None)

        # The explicit hostname should be preserved (not overridden)
        assert auth._get_base_url() == "https://explicit.host.com/multipass/api"

    def test_parameterize_overrides_env_hostname(self):
        """Regression test: when FOUNDRY_HOSTNAME env var is set but auth has no explicit hostname,
        _parameterize from FoundryClient should take precedence over the env var.

        Previously, OAuth.__init__ eagerly resolved the env var into _hostname_supplier,
        which caused _parameterize to skip setting the FoundryClient's hostname.
        """
        with patch.dict(os.environ, {"FOUNDRY_HOSTNAME": "https://env.host.com"}):
            auth = ConfidentialClientAuth(
                client_id="my-client-id",
                client_secret="my-client-secret",
            )
            # hostname_supplier should be None because no explicit hostname was given
            assert auth._hostname_supplier is None

            # Simulate what FoundryClient does: call _parameterize with its own hostname
            foundry_client_supplier = StaticHostnameSupplier("https://foundryclient.host.com")
            auth._parameterize(foundry_client_supplier, None)

            # The FoundryClient hostname should win, NOT the env var
            assert auth._hostname_supplier is foundry_client_supplier
            assert auth._get_base_url() == "https://foundryclient.host.com/multipass/api"

    def test_standalone_auth_falls_back_to_env_var(self):
        """When auth is used standalone (no FoundryClient, no _parameterize call),
        it should lazily resolve the hostname from environment variables."""
        with patch.dict(os.environ, {"FOUNDRY_HOSTNAME": "https://env.host.com"}):
            auth = ConfidentialClientAuth(
                client_id="my-client-id",
                client_secret="my-client-secret",
            )
            assert auth._hostname_supplier is None

            # Calling _get_base_url without _parameterize should lazily resolve from env
            base_url = auth._get_base_url()
            assert base_url == "https://env.host.com/multipass/api"

    def test_standalone_auth_raises_without_hostname_or_env(self):
        """When auth is used standalone with no hostname and no env vars,
        _get_base_url should raise ValueError."""
        with patch.dict(os.environ, {}, clear=True):
            auth = ConfidentialClientAuth(
                client_id="my-client-id",
                client_secret="my-client-secret",
            )
            with pytest.raises(ValueError, match="hostname must be provided"):
                auth._get_base_url()
