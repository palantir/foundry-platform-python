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


import warnings

import pytest

from foundry_sdk import UserTokenAuth


def test_missing_token_raises_type_error():
    assert pytest.raises(TypeError, lambda: UserTokenAuth())  # type: ignore


def test_warns_if_given_hostname():
    with warnings.catch_warnings(record=True) as w:
        UserTokenAuth(hostname="foo", token="bar")
        assert len(w) == 1
