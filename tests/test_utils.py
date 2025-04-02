import typing
import warnings
from datetime import datetime
from datetime import timedelta
from datetime import timezone

import pytest
import typing_extensions
from pydantic import BaseModel
from pydantic import ValidationError

from foundry._core.utils import RID
from foundry._core.utils import UUID
from foundry._core.utils import AwareDatetime
from foundry._core.utils import Long
from foundry._core.utils import maybe_ignore_preview
from foundry._core.utils import remove_prefixes
from foundry._core.utils import resolve_forward_references


def test_remove_prefixes():
    assert remove_prefixes("http://example.com", ["https://", "http://"]) == "example.com"
    assert remove_prefixes("https://example.com", ["https://", "http://"]) == "example.com"
    assert remove_prefixes("example.com", ["https://", "http://"]) == "example.com"


def test_no_warning_when_preview_not_passed():
    @maybe_ignore_preview
    def my_func_without_preview(preview: bool = False):
        pass

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        my_func_without_preview()
        assert len(w) == 0  # No warnings should be emitted


def test_no_warning_when_expected_preview():
    @maybe_ignore_preview
    def my_func_without_preview(preview: bool = False):
        pass

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        my_func_without_preview(preview=True)
        assert len(w) == 0  # No warnings should be emitted


def test_warns_about_unexpected_preview():
    @maybe_ignore_preview
    def my_func_without_preview():
        pass

    with pytest.warns(
        UserWarning,
        match=r'The "preview" argument is not required when calling my_func_without_preview\(\) since the endpoint is not in beta.',
    ):
        my_func_without_preview(preview=True)  # type: ignore


def test_accepts_valid_rid():
    class WithRid(BaseModel):
        rid: RID

    WithRid.model_validate({"rid": "ri.a.b.c.d"})
    WithRid.model_validate({"rid": "ri.foundry.main.dataset.b737e24d-6b19-43aa-93d5-da9fc4073f6"})


def test_rejects_invalid_rid():
    class WithRid(BaseModel):
        rid: RID

    with pytest.raises(ValidationError):
        WithRid.model_validate({"rid": "ri.a.b.c"})

    with pytest.raises(ValidationError):
        WithRid.model_validate({"rid": "ri.foundry.main.0.b737e24d-6b19-43aa-93d5-da9fc4073f6"})


def test_accepts_valid_uuid():
    class WithUuid(BaseModel):
        uuid: UUID

    WithUuid.model_validate({"uuid": "b737e24d-6b19-43aa-93d5-da9fc4073f6e"})


def test_rejects_invalid_uuid():
    class WithUuid(BaseModel):
        uuid: UUID

    with pytest.raises(ValidationError):
        WithUuid.model_validate({"uuid": "c"})

    with pytest.raises(ValidationError):
        WithUuid.model_validate({"uuid": "621f9a07-69e2-46c7-8015-c3bb8ee422e"})


def test_accepts_valid_long():
    class WithLong(BaseModel):
        long: Long

    WithLong.model_validate({"long": "1234"})
    WithLong.model_validate({"long": 1234})


def test_rejects_invalid_long():
    class WithLong(BaseModel):
        long: Long

    with pytest.raises(ValidationError):
        WithLong.model_validate({"long": "a1234"})


def test_long_serializes_to_string():
    class WithLong(BaseModel):
        long: Long

    assert WithLong(long=123).model_dump_json() == '{"long":"123"}'


def test_accepts_valid_datetime():
    class WithDatetime(BaseModel):
        datetime: AwareDatetime

    WithDatetime.model_validate({"datetime": datetime.now(timezone.utc)})


def test_rejects_invalid_datetime():
    class WithDatetime(BaseModel):
        datetime: AwareDatetime

    with pytest.raises(ValidationError):
        WithDatetime.model_validate({"datetime": datetime.now()})


def test_datetime_serializes_to_string():
    class WithDatetime(BaseModel):
        datetime: AwareDatetime

    t = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert WithDatetime(datetime=t).model_dump_json() == '{"datetime":"2023-10-01T12:00:00+00:00"}'


def test_non_utc_datetime_serializes_to_utc_string():
    class WithDatetime(BaseModel):
        datetime: AwareDatetime

    t = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=2)))
    assert WithDatetime(datetime=t).model_dump_json() == '{"datetime":"2023-10-01T10:00:00+00:00"}'


def test_resolve_dict_forward_references():
    A = typing.Dict[str, "B"]
    B = str

    assert A == typing.Dict[str, "B"]
    resolve_forward_references(A, globals(), locals())
    assert A == typing.Dict[str, str]


def test_resolve_annotated_union_forward_references():
    A = typing_extensions.Annotated[typing.Union["B", "C"], "Foo Bar"]
    B = str
    C = int

    resolve_forward_references(A, globals(), locals())
    assert A == typing_extensions.Annotated[typing.Union[str, int], "Foo Bar"]
