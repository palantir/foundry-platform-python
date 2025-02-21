import warnings

import pytest

from foundry import PalantirRPCException
from foundry._errors.utils import deserialize_error
from foundry.v1.datasets.errors import AbortTransactionPermissionDenied
from foundry.v1.datasets.errors import BranchNotFound

ERRORS_MAP = {
    "AbortTransactionPermissionDenied": AbortTransactionPermissionDenied,
    "BranchNotFound": BranchNotFound,
}


def test_correctly_deserializes_to_branch_not_found():
    error = deserialize_error(
        {
            "errorName": "BranchNotFound",
            "errorInstanceId": "123",
            "parameters": {
                "datasetRid": "ri.a.b.c.d",
                "branchId": "main",
            },
        },
        ERRORS_MAP,
    )

    assert isinstance(error, PalantirRPCException)
    assert isinstance(error, BranchNotFound)
    assert error.name == "BranchNotFound"
    assert error.error_instance_id == "123"
    assert error.parameters["datasetRid"] == "ri.a.b.c.d"
    assert error.parameters["branchId"] == "main"


def test_falls_back_to_standard_if_parsing_fails():
    with warnings.catch_warnings(record=True) as w:
        error = deserialize_error(
            {
                "errorName": "BranchNotFound",
                "errorInstanceId": "123",
                "parameters": {
                    "datasetRid": "ri.a.b.c.d",
                    "branchId": 123,
                },
            },
            {
                "AbortTransactionPermissionDenied": AbortTransactionPermissionDenied,
                "BranchNotFound": BranchNotFound,
            },
        )

        assert len(w) == 1
        assert error is None
