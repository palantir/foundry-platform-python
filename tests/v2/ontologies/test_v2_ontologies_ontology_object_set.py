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


def test_create_temporary(client_v2):
    with mock_requests(
        [
            {
                "method": "POST",
                "url": "https://example.palantirfoundry.com/api/v2/ontologies/{ontology}/objectSets/createTemporary",
                "path_params": {
                    "ontology": "palantir",
                },
                "json": {"objectSet": {"type": "base", "objectType": "Employee"}},
                "response": {
                    "status": 200,
                    "json": {
                        "objectSetRid": "ri.object-set.main.object-set.c32ccba5-1a55-4cfe-ad71-160c4c77a053"
                    },
                    "content_type": "application/json",
                },
            }
        ]
    ):
        ontology = "palantir"
        object_set = {"type": "base", "objectType": "Employee"}
        try:
            response = client_v2.ontologies.OntologyObjectSet.create_temporary(
                ontology,
                object_set=object_set,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with createTemporaryObjectSetV2") from e

        assert serialize_response(response) == {
            "objectSetRid": "ri.object-set.main.object-set.c32ccba5-1a55-4cfe-ad71-160c4c77a053"
        }