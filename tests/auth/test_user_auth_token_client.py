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


import pytest

from foundry_sdk._core.user_token_auth_client import UserTokenAuth


def test_invalid_token_raises_appropriate_error():
    assert pytest.raises(TypeError, lambda: UserTokenAuth())  # type: ignore
    assert pytest.raises(TypeError, lambda: UserTokenAuth(1))  # type: ignore
    assert pytest.raises(TypeError, lambda: UserTokenAuth(None))  # type: ignore
    assert pytest.raises(ValueError, lambda: UserTokenAuth(""))
