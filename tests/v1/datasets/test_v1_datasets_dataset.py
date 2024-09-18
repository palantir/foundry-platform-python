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


def test_get(client_v1):
    with mock_requests(
        [
            {
                "method": "GET",
                "url": "https://example.palantirfoundry.com/api/v1/datasets/{datasetRid}",
                "path_params": {
                    "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
                },
                "json": None,
                "response": {
                    "status": 200,
                    "json": {
                        "rid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
                        "name": "My Dataset",
                        "parentFolderRid": "ri.foundry.main.folder.bfe58487-4c56-4c58-aba7-25defd6163c4",
                    },
                    "content_type": "application/json",
                },
            }
        ]
    ):
        dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
        try:
            response = client_v1.datasets.Dataset.get(
                dataset_rid,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with getDataset") from e

        assert serialize_response(response) == {
            "rid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
            "name": "My Dataset",
            "parentFolderRid": "ri.foundry.main.folder.bfe58487-4c56-4c58-aba7-25defd6163c4",
        }
