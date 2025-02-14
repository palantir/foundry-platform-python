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
import ssl
import sys
from typing import Any
from typing import Optional
from typing import Type
from typing import TypeVar
from unittest.mock import patch

import httpcore
import httpx
import pytest
from httpx._utils import URLPattern

from foundry._core.config import Config
from foundry._core.http_client import HttpClient
from foundry._versions import __version__


def assert_http_transport(transport: Optional[httpx.BaseTransport]) -> httpx.HTTPTransport:
    return assert_isinstance(transport, httpx.HTTPTransport)


def assert_http_proxy(pool: Optional[httpcore.ConnectionPool]) -> httpcore.HTTPProxy:
    return assert_isinstance(pool, httpcore.HTTPProxy)


T = TypeVar("T")


def assert_isinstance(instance: Any, type: Type[T]) -> T:
    if not isinstance(instance, type):
        raise Exception(f"Not an instance of {type}", instance)

    return instance


def create_client(config: Optional[Config] = None):
    config = config or Config()
    return HttpClient("localhost:8123", config=config)


def test_clean_hostname():
    assert HttpClient("http://example.com").base_url.host == "example.com"
    assert HttpClient("https://example.com").base_url.host == "example.com"
    assert HttpClient("example.com/").base_url.host == "example.com"
    assert HttpClient("example.com").base_url.host == "example.com"


@pytest.fixture
def tmp_cert(tmp_path):
    cert_file = tmp_path / "cert.pem"
    cert_file.write_text("cert")
    yield cert_file.as_posix()


@pytest.fixture
def tmp_cert_dupe(tmp_path):
    cert_file = tmp_path / "cert.pem"
    cert_file.write_text("cert")
    yield cert_file.as_posix()


@pytest.fixture
def patch_ssl_verify():
    with patch.object(ssl.SSLContext, "load_verify_locations") as mock_method:
        # You can specify a return value or a side effect if needed
        mock_method.return_value = None  # Example: make it do nothing
        yield mock_method


@pytest.fixture
def temp_os_env():
    old_environ = os.environ.copy()

    # Make sure to start with a clean slate
    for key in ["REQUESTS_CA_BUNDLE", "SSL_CERT_FILE"]:
        if key in os.environ:
            os.environ.pop(key)

    yield os.environ
    os.environ = old_environ


def test_requests_env_var(temp_os_env, patch_ssl_verify, tmp_cert: str):
    temp_os_env["REQUESTS_CA_BUNDLE"] = tmp_cert
    assert create_client(Config(verify=True))._verify == tmp_cert


def test_ssl_cert_file_env_var(temp_os_env, patch_ssl_verify, tmp_cert: str):
    temp_os_env["SSL_CERT_FILE"] = tmp_cert
    assert create_client(Config(verify=True))._verify == tmp_cert


def test_verify_false_env_var(temp_os_env, patch_ssl_verify, tmp_cert: str):
    temp_os_env["REQUESTS_CA_BUNDLE"] = tmp_cert
    assert create_client(Config(verify=False))._verify == False


def test_cert_path_takes_precedence(temp_os_env, patch_ssl_verify, tmp_cert: str, tmp_cert_dupe):
    temp_os_env["REQUESTS_CA_BUNDLE"] = tmp_cert
    assert create_client(Config(verify=tmp_cert_dupe))._verify == tmp_cert_dupe


def test_default_headers():
    """Test that the user agent is set correctly."""
    client = create_client()
    assert client.headers == {
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "User-Agent": f"python-foundry-platform-sdk/{__version__} python/3.{sys.version_info.minor}",
    }

    """Test that additional headers can be added."""
    client = create_client(Config(default_headers={"Foo": "Bar"}))
    assert client.headers == {
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Foo": "Bar",
        "User-Agent": f"python-foundry-platform-sdk/{__version__} python/3.{sys.version_info.minor}",
    }


def test_proxies():
    client = create_client(Config(proxies={"https": "https://foo.bar", "http": "http://foo.bar"}))

    transport = assert_http_transport(client._mounts[URLPattern("https://")])
    proxy = assert_http_proxy(transport._pool)
    assert proxy._ssl_context is not None
    assert proxy._ssl_context.verify_mode == ssl.VerifyMode.CERT_REQUIRED
    assert proxy._proxy_ssl_context is not None
    assert proxy._proxy_ssl_context.verify_mode == ssl.VerifyMode.CERT_REQUIRED
    assert proxy._proxy_url.scheme == b"https"
    assert proxy._proxy_url.host == b"foo.bar"

    transport = assert_http_transport(client._mounts[URLPattern("http://")])
    proxy = assert_http_proxy(transport._pool)
    assert proxy._ssl_context is not None
    assert proxy._ssl_context.verify_mode == ssl.VerifyMode.CERT_REQUIRED
    assert proxy._proxy_ssl_context is None
    assert proxy._proxy_url.scheme == b"http"
    assert proxy._proxy_url.host == b"foo.bar"


def test_bad_proxy_url():
    with pytest.raises(ValueError):
        create_client(Config(proxies={"https": "htts://foo.bar"}))


def test_timeout():
    client = create_client(config=Config(timeout=60))
    assert client.timeout == httpx.Timeout(60)


def test_verify_cofigures_transport():
    client = create_client()
    transport = assert_http_transport(client._transport)
    pool = assert_isinstance(transport._pool, httpcore.ConnectionPool)

    assert pool._ssl_context is not None
    assert pool._ssl_context.verify_mode == ssl.VerifyMode.CERT_REQUIRED

    client = create_client(Config(verify=False))
    transport = assert_http_transport(client._transport)
    pool = assert_isinstance(transport._pool, httpcore.ConnectionPool)

    assert pool._ssl_context is not None
    assert pool._ssl_context.verify_mode == ssl.VerifyMode.CERT_NONE


def test_default_params():
    client = create_client(Config(default_params={"foo": "bar"}))
    assert client.params._dict == {"foo": ["bar"]}


def test_scheme():
    client = create_client()
    assert str(client.base_url) == "https://localhost:8123"

    client = create_client(Config(scheme="http"))
    assert str(client.base_url) == "http://localhost:8123"
