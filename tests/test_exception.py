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


import json
import re

import pytest

from foundry._errors.palantir_rpc_exception import PalantirRPCException
from foundry._errors.sdk_internal_error import SDKInternalError
from foundry._errors.sdk_internal_error import handle_unexpected


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
Requests Version: \d+\.\d+\.\d+
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


def test_handle_unexpected_ignores_known_exception():
    @handle_unexpected
    def raises_known_exception():
        raise PalantirRPCException({"errorName": "", "parameters": "", "errorInstanceId": ""})

    with pytest.raises(PalantirRPCException) as error:
        raises_known_exception()

    assert str(error.value) == json.dumps(
        {
            "errorInstanceId": "",
            "errorName": "",
            "parameters": "",
        },
        indent=4,
    )
