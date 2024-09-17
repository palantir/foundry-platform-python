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

from tests.utils import client_v2
from tests.utils import mock_requests
from tests.utils import serialize_response


def test_apply_batch(client_v2):
    with mock_requests(
        [
            {
                "method": "POST",
                "url": "https://example.palantirfoundry.com/api/v2/ontologies/{ontology}/actions/{action}/applyBatch",
                "path_params": {
                    "ontology": "palantir",
                    "action": "rename-employee",
                },
                "json": {
                    "requests": [
                        {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}},
                        {"parameters": {"id": 80061, "newName": "Joe Bloggs"}},
                    ]
                },
                "response": {
                    "status": 200,
                    "json": {},
                    "content_type": "application/json",
                },
            }
        ]
    ):
        ontology = "palantir"
        action = "rename-employee"
        requests = [
            {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}},
            {"parameters": {"id": 80061, "newName": "Joe Bloggs"}},
        ]
        artifact_repository = None
        options = None
        package_name = None
        try:
            response = client_v2.ontologies.Action.apply_batch(
                ontology,
                action,
                requests=requests,
                artifact_repository=artifact_repository,
                options=options,
                package_name=package_name,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with applyActionBatchV2") from e

        assert serialize_response(response) == {}
