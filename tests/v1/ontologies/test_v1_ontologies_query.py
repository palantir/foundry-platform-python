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


def test_execute(client_v1):
    with mock_requests(
        [
            {
                "method": "POST",
                "url": "https://example.palantirfoundry.com/api/v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute",
                "path_params": {
                    "ontologyRid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                    "queryApiName": "getEmployeesInCity",
                },
                "json": {"parameters": {"city": "New York"}},
                "response": {
                    "status": 200,
                    "json": {"value": ["EMP546", "EMP609", "EMP989"]},
                    "content_type": "application/json",
                },
            }
        ]
    ):
        ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
        query_api_name = "getEmployeesInCity"
        parameters = {"city": "New York"}
        try:
            response = client_v1.ontologies.Query.execute(
                ontology_rid,
                query_api_name,
                parameters=parameters,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with executeQuery") from e

        assert serialize_response(response) == {"value": ["EMP546", "EMP609", "EMP989"]}
