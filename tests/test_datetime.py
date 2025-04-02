from datetime import datetime
from datetime import timezone

import pydantic
import pytest


class Model(pydantic.BaseModel):
    datetype: pydantic.AwareDatetime


def test_init_fails_without_timezone():
    with pytest.raises(pydantic.ValidationError):
        Model(datetype=datetime.now())


def test_validate_python_fails_without_timezone():
    with pytest.raises(pydantic.ValidationError):
        Model.model_validate({"datetype": "2022-01-01T00:00:00"})


def test_init_passes_with_timezone():
    Model(datetype=datetime.now(tz=timezone.utc))


def test_validate_python_passes_with_timezone():
    Model.model_validate({"datetype": "2022-01-01T00:00:00Z"})
