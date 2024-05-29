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

from datetime import date
from datetime import datetime
from datetime import timezone

import pytest
from foundry._core.utils import Date
from foundry._core.utils import DateTime
from pydantic import BaseModel
from pydantic import TypeAdapter
from pydantic import ValidationError
from pydantic_core import ValidationError

date_ta = TypeAdapter(Date)  # type: ignore
datetime_ta = TypeAdapter(DateTime)  # type: ignore


def test_date_can_be_string():
    assert date_ta.validate_python("2024-01-01") == date(2024, 1, 1)


def test_date_rejected_invalid_string():
    assert pytest.raises(ValidationError, lambda: date_ta.validate_python("2024-01-0133"))
    assert pytest.raises(ValidationError, lambda: date_ta.validate_python("2024-01-1"))
    assert pytest.raises(ValidationError, lambda: date_ta.validate_python("2024-0101"))


def test_date_rejects_datetime():
    assert pytest.raises(ValidationError, lambda: date_ta.validate_python(datetime(2024, 1, 1)))


def test_date_can_be_date():
    assert date_ta.validate_python(date(2024, 1, 1)) == date(2024, 1, 1)


def test_datetime_can_be_string():
    assert datetime_ta.validate_python("1996-12-19T16:39:57-08:00") == datetime.fromisoformat(
        "1996-12-19T16:39:57-08:00"
    )
    assert datetime_ta.validate_python("1990-12-31T15:59:59-08:00") == datetime.fromisoformat(
        "1990-12-31T15:59:59-08:00"
    )


def test_reject_invalid_dateime():
    assert pytest.raises(
        ValidationError, lambda: datetime_ta.validate_python("1996-12-19T16:39:69-08:00")
    )

    assert pytest.raises(
        ValidationError, lambda: datetime_ta.validate_python("1990-12-31T23:59:59..Z")
    )

    assert pytest.raises(
        ValidationError, lambda: datetime_ta.validate_python("1990-12-31T15:59:59-24:00")
    )

    assert pytest.raises(
        ValidationError, lambda: datetime_ta.validate_python("1937-0101T12:00:27.87+00:20")
    )


def test_datetime_can_be_datetime():
    assert datetime_ta.validate_python(datetime(2024, 1, 1, tzinfo=timezone.utc)) == datetime(
        2024, 1, 1, tzinfo=timezone.utc
    )


class MyObject(BaseModel):
    datetime: DateTime
    date: Date


def test_can_construct_object_with_strings():
    my_object = MyObject(date="2024-01-01", datetime="2024-01-01T00:00:00")  # type: ignore
    assert my_object.date == date(2024, 1, 1)
    assert my_object.datetime == datetime(2024, 1, 1, 0, 0, 0)


def test_can_dump_object_to_json():
    my_object = MyObject(date="2024-01-01", datetime="2024-01-01T00:00:00")  # type: ignore
    assert my_object.model_dump_json()
