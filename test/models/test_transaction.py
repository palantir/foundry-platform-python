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
from datetime import datetime
from datetime import timezone
from typing import Union

from foundry.v2.models import Transaction


def validate(created_time: Union[str, datetime]):
    return Transaction.model_validate(
        {
            "rid": "ri.foundry.main.transaction.00000024-065b-a1ba-9d5c-805d236318ad",
            "transactionType": "SNAPSHOT",
            "status": "OPEN",
            "createdTime": created_time,
        }
    )


def test_model_validate_with_z():
    assert validate("2024-08-01T17:28:58.796Z").created_time == datetime(
        2024, 8, 1, 17, 28, 58, 796000, tzinfo=timezone.utc
    )


def test_model_validate_with_two_digit_milli():
    assert validate("2024-08-02T20:19:30.93+00:00").created_time == datetime(
        2024, 8, 2, 20, 19, 30, 930000, tzinfo=timezone.utc
    )


def test_model_validate_with_no_milli():
    assert validate("1990-12-31T15:59:59-08:00").created_time == datetime.fromisoformat(
        "1990-12-31T15:59:59-08:00"
    )


def test_model_validate_with_datetime():
    assert validate(datetime(2024, 1, 1, tzinfo=timezone.utc)).created_time == datetime(
        2024, 1, 1, tzinfo=timezone.utc
    )


def test_model_can_dump_to_dict():
    transaction = validate("2024-01-01T00:00:00")
    assert transaction.to_dict()["createdTime"] == datetime(2024, 1, 1, 0, 0)


def test_model_can_dump_to_json():
    transaction = validate("2024-01-01T00:00:00")
    assert (
        json.loads(transaction.model_dump_json(by_alias=True))["createdTime"]
        == "2024-01-01T00:00:00"
    )
