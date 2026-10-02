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
import tempfile

from foundry_sdk import ConfidentialClientAuth
from foundry_sdk import Config
from foundry_sdk import FoundryClient
from foundry_sdk._core.hostname_supplier import EndpointType
from foundry_sdk._core.hostname_supplier import ServiceDiscoveryHostnameSupplier
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


def test_client_builds_from_service_discovery_alone():
    """Regression test: in a service-discovered environment (a Compute Module, for example) there
    is no FOUNDRY_HOSTNAME and no hostname argument. Construction must succeed, and each endpoint
    type must resolve to its own discovered service rather than to one shared hostname."""
    previous_hostname = os.environ.pop("FOUNDRY_HOSTNAME", None)
    with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as discovery_file:
        discovery_file.write(
            "api-gateway:\n"
            "  - https://api-gateway.example.com:8443/api\n"
            "multipass:\n"
            "  - https://multipass.example.com:8443/multipass/api\n"
            "stream-proxy:\n"
            "  - https://stream-proxy.example.com:8443/api\n"
        )
        discovery_file.flush()
        os.environ["FOUNDRY_SERVICE_DISCOVERY_V2"] = discovery_file.name

        try:
            auth = ConfidentialClientAuth(client_id="abc123", client_secret="xyz789")
            client = FoundryClient(auth=auth)
            # The auth object is not parameterized until the API clients are initialized via the property call
            client.datasets.Dataset._auth

            assert isinstance(auth._hostname_supplier, ServiceDiscoveryHostnameSupplier)
            # Auth goes to multipass, not to the api-gateway or to a single flattened hostname
            assert auth._get_base_url() == "https://multipass.example.com:8443/multipass/api"
            supplier = auth._hostname_supplier
            assert (
                supplier.get_endpoint(EndpointType.GENERIC)
                == "https://api-gateway.example.com:8443/api"
            )
            assert (
                supplier.get_endpoint(EndpointType.HIGH_SCALE)
                == "https://stream-proxy.example.com:8443/api"
            )
        finally:
            del os.environ["FOUNDRY_SERVICE_DISCOVERY_V2"]
            if previous_hostname is not None:
                os.environ["FOUNDRY_HOSTNAME"] = previous_hostname
