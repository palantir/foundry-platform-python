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
import json
import re
import sys
from types import ModuleType
from typing import List
from typing import Type

import pydantic
import pytest

from foundry_sdk import _errors
from foundry_sdk._errors.palantir_rpc_exception import PalantirRPCException
from foundry_sdk._errors.sdk_internal_error import PalantirException
from foundry_sdk._errors.sdk_internal_error import SDKInternalError
from foundry_sdk._errors.sdk_internal_error import handle_unexpected


def find_exception_subclasses(module: ModuleType) -> List[Type[Exception]]:
    exception_subclasses = []

    # Get all members of the module
    members = inspect.getmembers(module)

    for name, obj in members:
        # Check if the member is a class
        if inspect.isclass(obj):
            # Check if the class is a subclass of Exception
            if issubclass(obj, Exception):
                exception_subclasses.append(obj)

    return exception_subclasses


def test_sdk_internal_error():
    with pytest.raises(SDKInternalError) as error:
        raise SDKInternalError("test")

    assert (
        re.match(
            r"""^test\n
This is an unexpected issue and should be reported. When filing an issue, make sure to copy the package information listed below.\n
OS: \w+
Python Version: \d+\.\d+\.\d+[^\n]+
SDK Version: \d+\.\d+\.\d+
OpenAPI Document Version: \d+\.\d+\.\d+
Pydantic Version: \d+\.\d+\.\d+
Pydantic Core Version: \d+\.\d+\.\d+
Httpx Version: \d+\.\d+\.\d+
$""",
            str(error.value),
        )
        is not None
    ), "Mismatch with text: " + str(error.value)


def test_handle_unexpected_fails_for_unkonwn_exception():
    @handle_unexpected
    def raises_unknown_exception():
        raise ValueError("test")

    with pytest.raises(SDKInternalError) as error:
        raises_unknown_exception()

    assert error.value.msg == "test"


def test_all_errors_subclass_palantir_exception():
    classes = find_exception_subclasses(_errors)
    assert len(classes) >= 5  # sanity check we are finding the classes
    for klass in find_exception_subclasses(_errors):
        assert issubclass(klass, PalantirException)


def test_handle_unexpected_ignores_palantir_exception():
    @handle_unexpected
    def raises_known_exception():
        raise PalantirException("Foo")

    with pytest.raises(PalantirException):
        raises_known_exception()


def test_handle_unexpected_ignores_validation_error():
    class Model(pydantic.BaseModel):
        foo: str

    @handle_unexpected
    def raises_known_exception():
        Model.model_validate({"foo": 123})

    with pytest.raises(pydantic.ValidationError):
        raises_known_exception()
