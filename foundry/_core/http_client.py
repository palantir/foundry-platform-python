import functools
import os
import sys
from typing import Optional
from typing import Union

import httpx

from foundry._core.config import Config
from foundry._core.utils import AnyCallableT
from foundry._core.utils import remove_prefixes
from foundry._versions import __version__


def type_safe_cache(func: AnyCallableT) -> AnyCallableT:
    """A type safe version of @functools.cache"""
    return functools.cache(func)  # type: ignore


@type_safe_cache
def _get_transport(verify: Union[bool, str], proxy: Optional[httpx.Proxy]) -> httpx.BaseTransport:
    """Create a shared transport. Because verify is at the transport level, we have to create a
    transport for each different configuration.
    """
    return httpx.HTTPTransport(verify=verify, proxy=proxy)


class HttpClient(httpx.Client):
    def __init__(self, hostname: str, config: Optional[Config] = None):
        config = config or Config()

        hostname = remove_prefixes(hostname.strip("/"), ["https://", "http://"])
        verify = config.verify

        # If verity is set to True, then merge with env vars
        # This is the same behavior as requests (although
        # requests does not check for SSL_CERT_FILE)
        if verify is True:
            verify = (
                # For historical reasons, we continue to support REQUESTS_CA_BUNDLE
                os.environ.get("REQUESTS_CA_BUNDLE")
                or os.environ.get("SSL_CERT_FILE")
                or True
            )

        # Expose this for testing, otherwise it is hard to access
        self._verify = verify

        super().__init__(
            headers={
                "User-Agent": f"python-foundry-platform-sdk/{__version__} python/{sys.version_info.major}.{sys.version_info.minor}",
                **(config.default_headers or {}),
            },
            params=config.default_params,
            transport=_get_transport(verify=verify, proxy=None),
            mounts={
                scheme + "://": _get_transport(verify=verify, proxy=httpx.Proxy(url=proxy_url))
                for scheme, proxy_url in (config.proxies or {}).items()
            },
            # Unlike requests, HTTPX does not follow redirects by default
            # If you access an endpoint with a missing trailing slash, the server could redirect
            # the user to the URL with the trailing slash. For example, accessing `/example` might
            # redirect to `/example/`.
            follow_redirects=True,
            base_url=f"{config.scheme}://{hostname}",
            timeout=config.timeout,
        )
