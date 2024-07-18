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

from typing import Any

import pytest
from foundry import FoundryClient
from foundry.models import Branch
from foundry.models import CreateBranchRequest
from pydantic import ValidationError

from ..utils import client  # type: ignore
from ..utils import mock_responses

TEST_RID = "ri.foundry.main.dataset.abc"


def mock_create_branch(monkeypatch: Any, dataset_rid: str, branch_id: str):
    mock_responses(
        monkeypatch,
        [
            (
                {
                    "method": "POST",
                    "url": f"https://test.com/api/v2/datasets/{dataset_rid}/branches",
                    "json": {"branchId": branch_id},
                    "params": {},
                },
                {
                    "status": 200,
                    "json": {"branchId": branch_id},
                    "content": None,
                },
            )
        ],
    )


def test_create_branch_fails_no_body(client: FoundryClient):
    with pytest.raises(ValueError):
        client.datasets.Dataset.Branch.create("test", create_branch_request=None)  # type: ignore


def test_create_branch_fails_bad_body(client: FoundryClient):
    with pytest.raises(ValidationError):
        client.datasets.Dataset.Branch.create(
            dataset_rid=TEST_RID,
            create_branch_request={"branchId": "123", "transactionRid": 123},  # type: ignore
        )


def test_works_with_extra_property(client: FoundryClient, monkeypatch: Any):
    dataset_rid = TEST_RID
    mock_create_branch(
        monkeypatch,
        dataset_rid=dataset_rid,
        branch_id="branch_test",
    )

    # Just making sure this works
    client.datasets.Dataset.Branch.create(
        dataset_rid=dataset_rid,
        create_branch_request={"branchId": "branch_test"},
    )

    # This ensures we don't fail if the user passes in an extra property
    client.datasets.Dataset.Branch.create(
        dataset_rid=dataset_rid,
        create_branch_request={"branchId": "branch_test", "foo": "bar"},  # type: ignore
    )


def test_create_branch_with_dict(client: FoundryClient, monkeypatch: Any):
    dataset_rid = TEST_RID
    mock_create_branch(
        monkeypatch,
        dataset_rid=dataset_rid,
        branch_id="branch_test",
    )

    res = client.datasets.Dataset.Branch.create(
        dataset_rid,
        create_branch_request={
            "branchId": "branch_test",
        },
    )

    assert isinstance(res, Branch)
    assert res.branch_id == "branch_test"
    assert res.transaction_rid is None


def test_create_branch_with_model(client: FoundryClient, monkeypatch: Any):
    mock_create_branch(
        monkeypatch,
        dataset_rid=TEST_RID,
        branch_id="branch_test",
    )

    res = client.datasets.Dataset.Branch.create(
        TEST_RID,
        create_branch_request=CreateBranchRequest(
            branchId="branch_test",
        ),
    )

    assert isinstance(res, Branch)
    assert res.branch_id == "branch_test"
    assert res.transaction_rid is None


def test_create_branch_doesnt_fail_extra_property(client: FoundryClient, monkeypatch: Any):
    """
    We want to make sure that additional properties don't cause a failure when the extra
    properties come from the server.
    """
    dataset_rid = TEST_RID
    mock_create_branch(
        monkeypatch,
        dataset_rid=dataset_rid,
        branch_id="branch_test",
    )

    res = client.datasets.Dataset.Branch.create(
        dataset_rid=dataset_rid,
        create_branch_request={"branchId": "branch_test"},
    )

    assert res.branch_id == "branch_test"


def mock_data_read(monkeypatch: Any, data: bytes):
    mock_responses(
        monkeypatch,
        [
            (
                {
                    "method": "GET",
                    "url": f"https://test.com/api/v2/datasets/{TEST_RID}/readTable",
                    "params": {"format": "CSV", "columns": []},
                    "json": None,
                },
                {
                    "status": 200,
                    "json": None,
                    "content": data,
                },
            )
        ],
    )


def test_read_table_can_pass_in_str(client: FoundryClient, monkeypatch: Any):
    mock_data_read(monkeypatch, data=b"hello")
    res = client.datasets.Dataset.read_table(format="CSV", dataset_rid=TEST_RID, columns=[])
    assert res == b"hello"
