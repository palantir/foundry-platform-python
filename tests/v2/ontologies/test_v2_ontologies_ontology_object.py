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


def test_count(client_v2):
    with mock_requests(
        [
            {
                "method": "POST",
                "url": "https://example.palantirfoundry.com/api/v2/ontologies/{ontology}/objects/{objectType}/count",
                "path_params": {
                    "ontology": "palantir",
                    "objectType": "employee",
                },
                "json": None,
                "response": {
                    "status": 200,
                    "json": {"count": 100},
                    "content_type": "application/json",
                },
            }
        ]
    ):
        ontology = "palantir"
        object_type = "employee"
        artifact_repository = None
        package_name = None
        try:
            response = client_v2.ontologies.OntologyObject.count(
                ontology,
                object_type,
                artifact_repository=artifact_repository,
                package_name=package_name,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with countObjects") from e

        assert serialize_response(response) == {"count": 100}
