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
                "url": "https://example.palantirfoundry.com/api/v1/ontologies/{ontologyRid}",
                "path_params": {
                    "ontologyRid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                },
                "json": None,
                "response": {
                    "status": 200,
                    "json": {
                        "apiName": "default-ontology",
                        "displayName": "Ontology",
                        "description": "The default ontology",
                        "rid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                    },
                    "content_type": "application/json",
                },
            }
        ]
    ):
        ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
        try:
            response = client_v1.ontologies.Ontology.get(
                ontology_rid,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with getOntology") from e

        assert serialize_response(response) == {
            "apiName": "default-ontology",
            "displayName": "Ontology",
            "description": "The default ontology",
            "rid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
        }


def test_list(client_v1):
    with mock_requests(
        [
            {
                "method": "GET",
                "url": "https://example.palantirfoundry.com/api/v1/ontologies",
                "path_params": {},
                "json": None,
                "response": {
                    "status": 200,
                    "json": {
                        "data": [
                            {
                                "apiName": "default-ontology",
                                "displayName": "Ontology",
                                "description": "The default ontology",
                                "rid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                            },
                            {
                                "apiName": "shared-ontology",
                                "displayName": "Shared ontology",
                                "description": "The ontology shared with our suppliers",
                                "rid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                            },
                        ]
                    },
                    "content_type": "application/json",
                },
            }
        ]
    ):
        try:
            response = client_v1.ontologies.Ontology.list()
        except ValidationError as e:
            raise Exception("There was a validation error with listOntologies") from e

        assert serialize_response(response) == {
            "data": [
                {
                    "apiName": "default-ontology",
                    "displayName": "Ontology",
                    "description": "The default ontology",
                    "rid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                },
                {
                    "apiName": "shared-ontology",
                    "displayName": "Shared ontology",
                    "description": "The ontology shared with our suppliers",
                    "rid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                },
            ]
        }
