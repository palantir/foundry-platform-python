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


from abc import ABC
from abc import abstractmethod
from enum import Enum


class EndpointType(Enum):
    GENERIC = "GENERIC"
    HIGH_SCALE = "HIGH_SCALE"
    AUTH = "AUTH"


class HostnameSupplier(ABC):
    @abstractmethod
    def get_hostname(self, endpoint_type: EndpointType) -> str:
        """Return the full base URL including scheme (e.g., 'https://example.com')."""
        ...


class StaticHostnameSupplier(HostnameSupplier):
    def __init__(self, base_url: str) -> None:
        self._api_gateway_url = base_url + "/api"
        self._multipass_url = base_url + "/multipass/api"
        self._stream_proxy_url = base_url + "/stream-proxy/api"

    def get_hostname(self, endpoint_type: EndpointType) -> str:
        if endpoint_type == EndpointType.GENERIC:
            return self._api_gateway_url
        elif endpoint_type == EndpointType.AUTH:
            return self._multipass_url
        elif endpoint_type == EndpointType.HIGH_SCALE:
            return self._stream_proxy_url

        raise ValueError(f"Unsupported endpoint type: {endpoint_type}")


class ServiceDiscoveryHostnameSupplier(HostnameSupplier):
    def __init__(self, services: dict[str, list[str]]) -> None:
        self._services = services
        self._url_cache: dict[EndpointType, str] = {}

    def get_hostname(self, endpoint_type: EndpointType) -> str:
        if endpoint_type in self._url_cache:
            return self._url_cache[endpoint_type]

        if endpoint_type == EndpointType.GENERIC:
            url = self._find_service_url("api-gateway")
        elif endpoint_type == EndpointType.AUTH:
            url = self._find_service_url("multipass")
        elif endpoint_type == EndpointType.HIGH_SCALE:
            url = self._find_service_url("stream-proxy")
        else:
            raise ValueError(f"Unsupported endpoint type: {endpoint_type}")

        self._url_cache[endpoint_type] = url
        return url

    def _find_service_url(self, service_name: str) -> str:
        if service_name not in self._services:
            raise ValueError(f"Unable to discover service '{service_name}'.")

        urls = self._services[service_name]
        if not urls:
            raise ValueError(f"Unable to discover URLs for service '{service_name}'.")

        return urls[0]
