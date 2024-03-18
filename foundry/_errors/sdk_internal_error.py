import functools
import sys
from typing import Any
from typing import Callable
from typing import TypeVar

from pydantic import __version__ as __pydantic__version__
from pydantic import ValidationError
from pydantic_core import __version__ as __pydantic_core_version__
from requests import __version__ as __requests_version__
from requests.exceptions import ConnectionError

from foundry._errors.palantir_rpc_exception import PalantirRPCException
from foundry._versions import __version__
from foundry._versions import __openapi_document_version__
from foundry._versions import __openapi_specification_version__


AnyCallableT = TypeVar("AnyCallableT", bound=Callable[..., Any])


def handle_unexpected(__func: AnyCallableT) -> AnyCallableT:
    @functools.wraps(__func)
    def validate(*args, **kwargs):
        try:
            return __func(*args, **kwargs)
        except (PalantirRPCException, ValidationError, ConnectionError) as e:
            # pass through these exceptions
            raise e
        except Exception as e:
            raise SDKInternalError(str(e)) from e

    return validate  # type: ignore


class SDKInternalError(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self):
        message = self.msg

        sys_version = sys.version.replace("\n", " ")
        message += (
            "\n\nThis is an unexpected issue and should be reported. "
            "When filing an issue, make sure to copy the package information "
            "listed below.\n\n"
            f"OS: {sys.platform}\n"
            f"Python Version: {sys_version}\n"
            f"SDK Version: {__version__}\n"
            f"OpenAPI Document Version: {__openapi_document_version__}\n"
            f"OpenAPI Specification Version: {__openapi_specification_version__}\n"
            f"Pydantic Version: {__pydantic__version__}\n"
            f"Pydantic Core Version: {__pydantic_core_version__}\n"
            f"Requests Version: {__requests_version__}\n"
        )

        return message
