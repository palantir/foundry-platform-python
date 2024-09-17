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


from pydantic import ValidationError

from tests.utils import client_v1
from tests.utils import mock_requests
from tests.utils import serialize_response


def test_create(client_v1):
    with mock_requests(
        [
            {
                "method": "POST",
                "url": "https://example.palantirfoundry.com/api/v1/datasets/{datasetRid}/branches",
                "path_params": {
                    "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
                },
                "json": {"branchId": "my-branch"},
                "response": {
                    "status": 200,
                    "json": {"branchId": "my-branch"},
                    "content_type": "application/json",
                },
            }
        ]
    ):
        dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
        branch_id = "my-branch"
        transaction_rid = None
        try:
            response = client_v1.datasets.Dataset.Branch.create(
                dataset_rid,
                branch_id=branch_id,
                transaction_rid=transaction_rid,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with createBranch") from e

        assert serialize_response(response) == {"branchId": "my-branch"}


def test_delete(client_v1):
    with mock_requests(
        [
            {
                "method": "DELETE",
                "url": "https://example.palantirfoundry.com/api/v1/datasets/{datasetRid}/branches/{branchId}",
                "path_params": {
                    "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
                    "branchId": "my-branch",
                },
                "json": None,
                "response": {
                    "status": 200,
                    "json": None,
                    "content_type": "None",
                },
            }
        ]
    ):
        dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
        branch_id = "my-branch"
        try:
            response = client_v1.datasets.Dataset.Branch.delete(
                dataset_rid,
                branch_id,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with deleteBranch") from e

        assert serialize_response(response) == None


def test_get(client_v1):
    with mock_requests(
        [
            {
                "method": "GET",
                "url": "https://example.palantirfoundry.com/api/v1/datasets/{datasetRid}/branches/{branchId}",
                "path_params": {
                    "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
                    "branchId": "master",
                },
                "json": None,
                "response": {
                    "status": 200,
                    "json": {
                        "branchId": "master",
                        "transactionRid": "ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4",
                    },
                    "content_type": "application/json",
                },
            }
        ]
    ):
        dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
        branch_id = "master"
        try:
            response = client_v1.datasets.Dataset.Branch.get(
                dataset_rid,
                branch_id,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with getBranch") from e

        assert serialize_response(response) == {
            "branchId": "master",
            "transactionRid": "ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4",
        }


def test_page(client_v1):
    with mock_requests(
        [
            {
                "method": "GET",
                "url": "https://example.palantirfoundry.com/api/v1/datasets/{datasetRid}/branches",
                "path_params": {
                    "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
                },
                "json": None,
                "response": {
                    "status": 200,
                    "json": {
                        "nextPageToken": "v1.VGhlcmUgaXMgc28gbXVjaCBsZWZ0IHRvIGJ1aWxkIC0gcGFsYW50aXIuY29tL2NhcmVlcnMv",
                        "data": [
                            {
                                "branchId": "master",
                                "transactionRid": "ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4",
                            },
                            {
                                "branchId": "test-v2",
                                "transactionRid": "ri.foundry.main.transaction.fc9feb4b-34e4-4bfd-9e4f-b6425fbea85f",
                            },
                            {"branchId": "my-branch"},
                        ],
                    },
                    "content_type": "application/json",
                },
            }
        ]
    ):
        dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
        page_size = None
        page_token = None
        try:
            response = client_v1.datasets.Dataset.Branch.page(
                dataset_rid,
                page_size=page_size,
                page_token=page_token,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with pageBranches") from e

        assert serialize_response(response) == {
            "nextPageToken": "v1.VGhlcmUgaXMgc28gbXVjaCBsZWZ0IHRvIGJ1aWxkIC0gcGFsYW50aXIuY29tL2NhcmVlcnMv",
            "data": [
                {
                    "branchId": "master",
                    "transactionRid": "ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4",
                },
                {
                    "branchId": "test-v2",
                    "transactionRid": "ri.foundry.main.transaction.fc9feb4b-34e4-4bfd-9e4f-b6425fbea85f",
                },
                {"branchId": "my-branch"},
            ],
        }
