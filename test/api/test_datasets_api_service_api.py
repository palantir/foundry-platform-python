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
from unittest.mock import Mock
from pydantic import ValidationError
import pytest
from urllib3 import PoolManager
from foundry import FoundryClient
from foundry.models.branch import Branch
from foundry.models.create_branch_request import CreateBranchRequest
from foundry.models.table_export_format import TableExportFormat
from test.utils import mock_responses
from test.utils import client


def mock_create_branch(monkeypatch, dataset_rid: str, branch_id: str):
    mock_responses(
        monkeypatch,
        [
            (
                {
                    "method": "POST",
                    "url": f"https://test.com/api/v1/datasets/{dataset_rid}/branches",
                    "body": {"branchId": branch_id},
                },
                {
                    "status": 200,
                    "body": {"branchId": branch_id},
                },
            )
        ],
    )


def test_create_branch_fails_no_body(client: FoundryClient):
    with pytest.raises(ValueError):
        client.datasets.create_branch("test", create_branch_request=None)  # type: ignore


def test_create_branch_fails_bad_body(client: FoundryClient):
    with pytest.raises(ValidationError):
        client.datasets.create_branch(
            "ri.foundry.main.dataset.abc",
            create_branch_request=CreateBranchRequest(
                branchId="123", transactionRid=123  # type: ignore
            ),
        )


def test_fails_with_extra_property(client: FoundryClient, monkeypatch):
    dataset_rid = "ri.foundry.main.dataset.123"
    mock_create_branch(
        monkeypatch,
        dataset_rid=dataset_rid,
        branch_id="branch_test",
    )

    # Just making sure this works
    client.datasets.create_branch(
        dataset_rid,
        create_branch_request={"branchId": "branch_test"},  # type: ignore
    )

    with pytest.raises(ValidationError):
        # This ensures we fail if the user passes in an extra property
        client.datasets.create_branch(
            dataset_rid,
            create_branch_request={"branchId": "branch_test", "foo": "bar"},  # type: ignore
        )


def test_create_branch_can_create_branch(client: FoundryClient, monkeypatch):
    dataset_rid = "ri.foundry.main.dataset.123"
    mock_create_branch(
        monkeypatch,
        dataset_rid=dataset_rid,
        branch_id="branch_test",
    )

    res = client.datasets.create_branch(
        dataset_rid,
        create_branch_request=CreateBranchRequest(
            branchId="branch_test",
        ),
    )

    assert isinstance(res, Branch)
    assert res.branch_id == "branch_test"
    assert res.transaction_rid is None

    res = client.datasets.create_branch(
        dataset_rid,
        create_branch_request={
            "branchId": "branch_test",
        },  # type: ignore
    )

    assert isinstance(res, Branch)
    assert res.branch_id == "branch_test"
    assert res.transaction_rid is None


def test_create_branch_doesnt_fail_extra_property(client: FoundryClient, monkeypatch):
    """
    We want to make sure that additional properties don't cause a failure when the extra
    properties come from the server.
    """
    dataset_rid = "ri.foundry.main.dataset.123"
    mock_create_branch(
        monkeypatch,
        dataset_rid=dataset_rid,
        branch_id="branch_test",
    )

    res = client.datasets.create_branch(
        dataset_rid,
        create_branch_request=CreateBranchRequest(branchId="branch_test"),
    )

    assert res.branch_id == "branch_test"


def mock_data_read(monkeypatch, data: bytes):
    mock_responses(
        monkeypatch,
        [
            (
                {
                    "method": "GET",
                    "url": "https://test.com/api/v1/datasets/test.rid/readTable?format=CSV",
                },
                {
                    "status": 200,
                    "data": data,
                },
            )
        ],
    )


def test_read_table_can_pass_in_str(client: FoundryClient, monkeypatch):
    mock_data_read(monkeypatch, data=b"hello")
    res = client.datasets.read_table(format="CSV", dataset_rid="test.rid")  # type: ignore
    assert res == b"hello"


def test_read_table_can_pass_enum(client: FoundryClient, monkeypatch):
    mock_data_read(monkeypatch, data=b"hello")
    res = client.datasets.read_table(format=TableExportFormat.CSV, dataset_rid="test.rid")
    assert res == b"hello"
