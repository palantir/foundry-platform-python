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


import os

from foundry_sdk import ConfidentialClientAuth, Config, FoundryClient
from foundry_sdk._core.hostname_supplier import StaticHostnameSupplier


def test_client_passes_hostname_supplier():
    auth = ConfidentialClientAuth(client_id="abc123", client_secret="xyz789")
    assert auth._hostname_supplier is None

    client = FoundryClient(auth=auth, hostname="https://example.palantirfoundry.com")
    # The auth object is not parameterized until the API clients are initialized via the property call
    client.datasets.Dataset._auth

    assert isinstance(auth._hostname_supplier, StaticHostnameSupplier)
    assert auth._hostname_supplier._base_url == "https://example.palantirfoundry.com"


def test_client_overrides_inferred_hostname_supplier():
    os.environ["FOUNDRY_HOSTNAME"] = "https://example2.palantirfoundry.com"

    auth = ConfidentialClientAuth(client_id="abc123", client_secret="xyz789")
    assert auth._hostname_supplier is not None
    assert isinstance(auth._hostname_supplier, StaticHostnameSupplier)
    assert auth._hostname_supplier._base_url == "https://example2.palantirfoundry.com"
    assert not auth._hostname_supplier.is_user_supplied

    client = FoundryClient(auth=auth, hostname="https://example.palantirfoundry.com")
    # The auth object is not parameterized until the API clients are initialized via the property call
    client.datasets.Dataset._auth

    assert isinstance(auth._hostname_supplier, StaticHostnameSupplier)
    assert auth._hostname_supplier._base_url == "https://example.palantirfoundry.com"
    assert auth._hostname_supplier.is_user_supplied


def test_client_does_not_override_user_supplied_hostname():
    auth = ConfidentialClientAuth(
        client_id="abc123", client_secret="xyz789", hostname="https://example3.palantirfoundry.com"
    )
    assert auth._hostname_supplier is not None
    assert isinstance(auth._hostname_supplier, StaticHostnameSupplier)
    assert auth._hostname_supplier._base_url == "https://example3.palantirfoundry.com"
    assert auth._hostname_supplier.is_user_supplied

    config = Config(default_headers={"test": "test"})
    client = FoundryClient(auth=auth, hostname="https://example.palantirfoundry.com", config=config)
    # The auth object is not parameterized until the API clients are initialized via the property call
    client.datasets.Dataset._auth

    assert isinstance(auth._hostname_supplier, StaticHostnameSupplier)
    # Hostname is unchanged
    assert auth._hostname_supplier._base_url == "https://example3.palantirfoundry.com"
    assert auth._hostname_supplier.is_user_supplied
    # Config still successfully parameterized
    assert auth._config == config
