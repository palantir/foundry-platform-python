import warnings

import pytest
from pydantic import BaseModel
from pydantic import ValidationError

from foundry._core.utils import RID
from foundry._core.utils import UUID
from foundry._core.utils import Long
from foundry._core.utils import clean_hostname
from foundry._core.utils import maybe_ignore_preview
from foundry._core.utils import remove_prefixes


def test_remove_prefixes():
    assert remove_prefixes("http://example.com", ["https://", "http://"]) == "example.com"
    assert remove_prefixes("https://example.com", ["https://", "http://"]) == "example.com"
    assert remove_prefixes("example.com", ["https://", "http://"]) == "example.com"


def test_clean_hostname():
    assert clean_hostname("http://example.com") == "example.com"
    assert clean_hostname("https://example.com") == "example.com"
    assert clean_hostname("example.com/") == "example.com"
    assert clean_hostname("example.com") == "example.com"


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
