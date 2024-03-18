from datetime import date, datetime, timezone
from pydantic import TypeAdapter, ValidationError
from pydantic_core import ValidationError
import pytest
from foundry._core.utils import RFC3339Date
from foundry._core.utils import RFC3339DateTime

date_ta = TypeAdapter(RFC3339Date)
datetime_ta = TypeAdapter(RFC3339DateTime)


def test_date_can_be_string():
    date_ta.validate_python("2024-01-01")


def test_date_rejected_invalid_string():
    assert pytest.raises(ValidationError, lambda: date_ta.validate_python("2024-01-0133"))
    assert pytest.raises(ValidationError, lambda: date_ta.validate_python("2024-01-1"))
    assert pytest.raises(ValidationError, lambda: date_ta.validate_python("2024-0101"))


def test_date_can_be_date():
    assert date_ta.validate_python(date(2024, 1, 1)) == "2024-01-01"


def test_datetime_can_be_string():
    assert datetime_ta.validate_python("1996-12-19T16:39:57-08:00") == "1996-12-19T16:39:57-08:00"
    assert datetime_ta.validate_python("1990-12-31T23:59:59Z") == "1990-12-31T23:59:59Z"
    assert datetime_ta.validate_python("1990-12-31T15:59:59-08:00") == "1990-12-31T15:59:59-08:00"
    assert (
        datetime_ta.validate_python("1937-01-01T12:00:27.87+00:20")
        == "1937-01-01T12:00:27.87+00:20"
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
    assert (
        date_ta.validate_python(datetime(2024, 1, 1, tzinfo=timezone.utc))
        == "2024-01-01T00:00:00+00:00"
    )
