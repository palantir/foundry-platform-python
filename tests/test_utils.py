import sys
import types
import typing
import warnings
from datetime import datetime
from datetime import timedelta
from datetime import timezone

import pytest
import typing_extensions
from pydantic import BaseModel
from pydantic import ValidationError

from foundry_sdk._core.utils import RID
from foundry_sdk._core.utils import UUID
from foundry_sdk._core.utils import AwareDatetime
from foundry_sdk._core.utils import Long
from foundry_sdk._core.utils import maybe_ignore_preview
from foundry_sdk._core.utils import remove_prefixes
from foundry_sdk._core.utils import resolve_forward_references


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
    resolved_A = resolve_forward_references(A, globals(), locals())

    # Check the structure is correct rather than exact equality
    assert typing.get_origin(resolved_A) in (dict, typing.Dict)
    args = typing.get_args(resolved_A)
    assert len(args) == 2
    assert args[0] == str
    assert args[1] == str


def test_resolve_annotated_union_forward_references():
    A = typing_extensions.Annotated[typing.Union["B", "C"], "Foo Bar"]
    B = str
    C = int

    resolved_A = resolve_forward_references(A, globals(), locals())

    # Check the structure is correct rather than exact equality
    assert typing.get_origin(resolved_A) == typing_extensions.Annotated
    args = typing.get_args(resolved_A)
    assert len(args) == 2
    assert args[1] == "Foo Bar"

    # First arg is the union
    union_type = args[0]
    union_origin = typing.get_origin(union_type)
    assert union_origin in (typing.Union, types_union := getattr(types, "Union", None))
    union_args = typing.get_args(union_type)
    assert len(union_args) == 2
    assert str in union_args
    assert int in union_args


def test_resolve_duplicate_forward_references():
    A = typing.List["C"]
    B = typing.List["C"]
    C = typing.List[float]

    resolved_B = resolve_forward_references(B, globals(), locals())
    resolved_A = resolve_forward_references(A, globals(), locals())

    # Python 3.9 and Python 3.13+ differ in how they represent nested types
    # In Python 3.9, it's typing.List[typing.List[float]]
    # In Python 3.13+, it's typing.List[list[float]] or list[list[float]]
    # We check the structure instead of exact equality
    inner_type = typing.get_args(resolved_A)[0]
    assert typing.get_origin(inner_type) in (list, typing.List)
    assert typing.get_args(inner_type)[0] == float


def test_resolve_double_forward_reference():
    A = typing.List[typing.List["B"]]
    B = float

    resolved_A = resolve_forward_references(A, globals(), locals())

    # Python 3.9 and Python 3.13+ differ in how they represent nested types
    # In Python 3.9, it's typing.List[typing.List[float]]
    # In Python 3.13+, it's typing.List[list[float]] or list[list[float]]
    # We check the structure instead of exact equality
    inner_type = typing.get_args(resolved_A)[0]
    assert typing.get_origin(inner_type) in (list, typing.List)
    assert typing.get_args(inner_type)[0] == float
