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


import inspect
import typing
import warnings
from datetime import timezone
from functools import wraps
from typing import Any
from typing import Callable
from typing import ForwardRef
from typing import List
from typing import TypeVar

import pydantic
from typing_extensions import Annotated

RID = Annotated[
    str,
    pydantic.StringConstraints(
        pattern=r"^ri\.[a-z][a-z0-9-]*\.([a-z0-9][a-z0-9\-]*)?\.[a-z][a-z0-9-]*\.[a-zA-Z0-9._-]+$",
    ),
]


UUID = Annotated[
    str,
    pydantic.StringConstraints(
        pattern=r"^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$",
    ),
]


Long = Annotated[
    int,
    pydantic.PlainSerializer(
        lambda value: str(value),
        return_type=str,
        # Important: This ensures the value is not serialized when using to_dict()
        # We only want to serialize when dumping to a JSON string
        when_used="json",
    ),
]
"""A long integer that is serialized to a string in JSON."""


AwareDatetime = Annotated[
    pydantic.AwareDatetime,
    pydantic.PlainSerializer(
        lambda value: value.astimezone(timezone.utc).isoformat(),
        return_type=str,
        # Important: This ensures the value is not serialized when using to_dict()
        # We only want to serialize when dumping to a JSON string
        when_used="json",
    ),
]
"""A datetime object that enforces timezones and is always serialized to UTC."""


Timeout = Annotated[int, pydantic.Field(gt=0)]


def remove_prefixes(text: str, prefixes: List[str]):
    for prefix in prefixes:
        if text.startswith(prefix):
            text = text[len(prefix) :]
    return text


AnyCallableT = TypeVar("AnyCallableT", bound=Callable[..., Any])


def maybe_ignore_preview(func: AnyCallableT) -> AnyCallableT:
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if "preview" in kwargs and "preview" not in sig.parameters:
            warnings.warn(
                f'The "preview" argument is not required when calling {func.__name__}() since the endpoint is not in beta.',
                UserWarning,
            )
            kwargs.pop("preview")
        return func(*args, **kwargs)

    return wrapper  # type: ignore


def resolve_forward_references(type_obj: Any, globalns: dict, localns: dict) -> Any:
    if typing.get_origin(type_obj) is None:
        return type_obj

    args = tuple(
        (
            typing._eval_type(arg, globalns, localns)  # type: ignore
            if isinstance(arg, ForwardRef)
            else resolve_forward_references(arg, globalns, localns)
        )
        for arg in typing.get_args(type_obj)  # type: ignore
    )

    setattr(type_obj, "__args__", args)
    return type_obj


def assert_non_empty_string(value: str, name: str) -> None:
    if not isinstance(value, str):
        raise TypeError(f"The {name} must be a string, not {type(value)}.")

    if not value:
        raise ValueError(f"The {name} cannot be empty.")
