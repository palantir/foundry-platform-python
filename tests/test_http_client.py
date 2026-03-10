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


from foundry_sdk._core.config import Config
from foundry_sdk._core.http_client import _prepare_client_data


class TestPrepareClientDataScheme:
    def test_bare_hostname_defaults_to_https(self):
        config, hostname, _, _ = _prepare_client_data("myhost.example.com", None)
        assert config.scheme == "https"
        assert hostname == "myhost.example.com"

    def test_https_prefix_uses_https(self):
        config, hostname, _, _ = _prepare_client_data("https://myhost.example.com", None)
        assert config.scheme == "https"
        assert hostname == "myhost.example.com"

    def test_https_prefix_overrides_config_http(self):
        original_config = Config(scheme="http")
        config, hostname, _, _ = _prepare_client_data("https://myhost.example.com", original_config)
        assert config.scheme == "https"
        assert hostname == "myhost.example.com"

    def test_http_prefix_overrides_config_https(self):
        original_config = Config(scheme="https")
        config, hostname, _, _ = _prepare_client_data("http://localhost:8080", original_config)
        assert config.scheme == "http"
        assert hostname == "localhost:8080"

    def test_bare_hostname_respects_config_http(self):
        config, hostname, _, _ = _prepare_client_data("localhost:8080", Config(scheme="http"))
        assert config.scheme == "http"
        assert hostname == "localhost:8080"

    def test_does_not_mutate_original_config(self):
        original_config = Config(scheme="https")
        config, _, _, _ = _prepare_client_data("http://localhost:8080", original_config)
        assert config.scheme == "http"
        assert original_config.scheme == "https"

    def test_https_prefix_with_path(self):
        config, hostname, _, _ = _prepare_client_data("https://myhost.example.com/api/v1", None)
        assert config.scheme == "https"
        assert hostname == "myhost.example.com/api/v1"
