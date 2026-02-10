import warnings

import pytest

from foundry_sdk import PalantirRPCException
from foundry_sdk._errors.utils import deserialize_error
from foundry_sdk.v1.datasets.errors import BranchNotFound


class MockError(PalantirRPCException):
    def __init__(self, name):
        super().__init__(name)


ERRORS_MAP = {
    "MockError": MockError,
    "BranchNotFound": BranchNotFound,
}


def test_correctly_deserializes_error():
    error = deserialize_error(
        {
            "errorName": "BranchNotFound",
            "errorInstanceId": "123",
            "parameters": {"datasetRid": "ri.a.b.c.d", "branchId": "main"},
        },
        ERRORS_MAP,
    )

    assert isinstance(error, PalantirRPCException)
    assert isinstance(error, BranchNotFound)
    assert error.name == "BranchNotFound"
    assert error.error_instance_id == "123"
    assert error.parameters == {"datasetRid": "ri.a.b.c.d", "branchId": "main"}


def test_falls_back_to_standard_if_parsing_fails():
    with warnings.catch_warnings(record=True) as w:
        error = deserialize_error(
            {
                "errorName": "BranchNotFound",
                "errorInstanceId": "123",
                "parameters": {"datasetRid": "ri.a.b.c.d", "branchId": 123},
            },
            ERRORS_MAP,
        )

        assert len(w) == 1
        assert error is None
