import warnings

import pytest

from foundry._core.utils import maybe_ignore_preview
from foundry._core.utils import remove_prefixes


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
        my_func_without_preview(preview=True)
