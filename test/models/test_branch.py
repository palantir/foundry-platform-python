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

from pydantic import ValidationError
import pytest
from foundry.models import Branch


def test_from_dict():
    r = Branch.from_dict(
        {
            "branchId": "123",
            "transactionRid": "ri.a.b.c.d",
        }
    )
    assert r.branch_id == "123"
    assert r.transaction_rid == "ri.a.b.c.d"


def test_from_dict_extra():
    with pytest.raises(ValidationError) as error:
        # Expect extra property to be forbidden to be default
        r = Branch.from_dict(
            {
                "branchId": "123",
                "DOES_NOT_EXIST": "FOO",
            },
        )

    r = Branch.from_dict(
        {
            "branchId": "123",
            "DOES_NOT_EXIST": "FOO",
        },
        allow_extra=True,
    )

    assert r.branch_id == "123"
