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


import logging
from abc import ABC
from abc import abstractmethod
from enum import Enum
from functools import cache

log = logging.getLogger(__name__)


class EndpointType(Enum):
    GENERIC = "GENERIC"
    HIGH_SCALE = "HIGH_SCALE"
    AUTH = "AUTH"


class HostnameSupplier(ABC):
    @abstractmethod
    def get_hostname(self) -> str:
        """Return the base hostname (e.g., 'https://example.com')."""
        ...

    @abstractmethod
    def get_endpoint(self, endpoint_type: EndpointType) -> str:
        """Return a base URL including scheme for an endpoint-specific URL."""
        ...

    @property
    @abstractmethod
    def is_user_supplied(self) -> bool:
        """Return True if the user explicitly provided their own hostname."""
        ...


class StaticHostnameSupplier(HostnameSupplier):
    def __init__(self, base_url: str, is_user_supplied: bool) -> None:
        self._base_url = base_url
        self._api_gateway_url = base_url + "/api"
        self._multipass_url = base_url + "/multipass/api"
        self._stream_proxy_url = base_url + "/api"
        self._is_user_supplied = is_user_supplied

    def get_hostname(self) -> str:
        return self._base_url

    def get_endpoint(self, endpoint_type: EndpointType) -> str:
        if endpoint_type == EndpointType.GENERIC:
            return self._api_gateway_url
        elif endpoint_type == EndpointType.AUTH:
            return self._multipass_url
        elif endpoint_type == EndpointType.HIGH_SCALE:
            return self._stream_proxy_url

        raise ValueError(f"Unsupported endpoint type: {endpoint_type}")

    @property
    def is_user_supplied(self) -> bool:
        return self._is_user_supplied


class ServiceDiscoveryHostnameSupplier(HostnameSupplier):
    def __init__(
        self, services: dict[str, list[str]], fallback_supplier: HostnameSupplier | None = None
    ) -> None:
        self._services = services
        self._fallback_supplier = fallback_supplier

    def get_hostname(self) -> str:
        if self._fallback_supplier is not None:
            return self._fallback_supplier.get_hostname()
        raise ValueError(
            "Unable to provide hostname. Please provide a hostname parameter to the client."
        )

    @cache
    def get_endpoint(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, endpoint_type: EndpointType
    ) -> str:
        service_name = None
        if endpoint_type == EndpointType.GENERIC:
            service_name = "api-gateway"
        elif endpoint_type == EndpointType.AUTH:
            service_name = "multipass"
        elif endpoint_type == EndpointType.HIGH_SCALE:
            service_name = "stream-proxy"

        if service_name is None:
            raise ValueError(f"Unsupported endpoint type: {endpoint_type}")

        url = self._find_service_url(service_name)
        if url is not None:
            return url

        if self._fallback_supplier is not None:
            return self._fallback_supplier.get_endpoint(endpoint_type)
        raise ValueError(f"Unable to discover service '{service_name}'.")

    @property
    def is_user_supplied(self) -> bool:
        return False

    def _find_service_url(self, service_name: str) -> str | None:
        # Functions swaps hyphens for underscores in service names
        alt_service_name = service_name.replace("-", "_")
        service_names = [service_name, alt_service_name]
        for name in service_names:
            urls = self._services.get(name)
            if urls:
                return urls[0]

        return None
