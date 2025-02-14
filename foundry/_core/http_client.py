import functools
import os
import ssl
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
def _get_transport(verify: Union[bool, str], proxy_url: Optional[str]) -> httpx.BaseTransport:
    """Create a shared transport. Because verify is at the transport level, we have to create a
    transport for each different configuration.
    """
    # If verify is a string, we need to create an SSL context ourself
    # since httpx has deprecated strings as inputs
    # This logic to check whether the path is a file or directory is
    # the same logic as both httpx (before they deprecated string paths) and requests
    # Otherwise, we let httpx create the SSL context for us from a True/False value
    if isinstance(verify, str):
        if os.path.isdir(verify):
            ssl_context = ssl.create_default_context(capath=verify)
        else:
            ssl_context = ssl.create_default_context(cafile=verify)
    else:
        ssl_context = httpx.create_ssl_context(verify=verify)

    proxy: Optional[httpx.Proxy] = None
    if proxy_url is not None:
        if not proxy_url.startswith(("http://", "https://")):
            raise ValueError(f"Proxy URL must start with http:// or https://: {proxy_url}")

        # We shold only pass the SSL context to the proxy iff the proxy is HTTPS
        # Otherwise, httpx will throw an error
        if proxy_url.startswith("https://"):
            proxy = httpx.Proxy(url=proxy_url, ssl_context=ssl_context)
        else:
            proxy = httpx.Proxy(url=proxy_url)

    return httpx.HTTPTransport(verify=ssl_context, proxy=proxy)


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
            transport=_get_transport(verify=verify, proxy_url=None),
            mounts={
                scheme + "://": _get_transport(verify=verify, proxy_url=proxy_url)
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
