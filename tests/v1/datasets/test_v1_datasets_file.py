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


def test_delete(client_v1):
    with mock_requests(
        [
            {
                "method": "DELETE",
                "url": "https://example.palantirfoundry.com/api/v1/datasets/{datasetRid}/files/{filePath}",
                "path_params": {
                    "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
                    "filePath": "q3-data%2fmy-file.csv",
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
        file_path = "q3-data%2fmy-file.csv"
        branch_id = None
        transaction_rid = None
        try:
            response = client_v1.datasets.Dataset.File.delete(
                dataset_rid,
                file_path,
                branch_id=branch_id,
                transaction_rid=transaction_rid,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with deleteFile") from e

        assert serialize_response(response) == None
