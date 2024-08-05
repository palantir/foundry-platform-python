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

from datetime import datetime
from datetime import timezone

from foundry.models import Transaction


def test_model_validate_with_z():
    r = Transaction.model_validate(
        {
            "rid": "ri.foundry.main.transaction.00000024-065b-a1ba-9d5c-805d236318ad",
            "transactionType": "SNAPSHOT",
            "status": "OPEN",
            "createdTime": "2024-08-01T17:28:58.796Z",
        }
    )
    assert r.transaction_type == "SNAPSHOT"
    assert r.status == "OPEN"
    assert r.created_time == datetime(2024, 8, 1, 17, 28, 58, 796000, tzinfo=timezone.utc)


def test_model_validate_with_two_digit_milli():
    r = Transaction.model_validate(
        {
            "rid": "ri.foundry.main.transaction.00000024-065b-a1ba-9d5c-805d236318ad",
            "transactionType": "SNAPSHOT",
            "status": "OPEN",
            "createdTime": "2024-08-02T20:19:30.93+00:00",
        }
    )
    assert r.transaction_type == "SNAPSHOT"
    assert r.status == "OPEN"
    assert r.created_time == datetime(2024, 8, 2, 20, 19, 30, 930000, tzinfo=timezone.utc)
