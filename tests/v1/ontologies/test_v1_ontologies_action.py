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


def test_apply(client_v1):
    with mock_requests(
        [
            {
                "method": "POST",
                "url": "https://example.palantirfoundry.com/api/v1/ontologies/{ontologyRid}/actions/{actionType}/apply",
                "path_params": {
                    "ontologyRid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                    "actionType": "rename-employee",
                },
                "json": {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}},
                "response": {
                    "status": 200,
                    "json": {},
                    "content_type": "application/json",
                },
            }
        ]
    ):
        ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
        action_type = "rename-employee"
        parameters = {"id": 80060, "newName": "Anna Smith-Doe"}
        try:
            response = client_v1.ontologies.Action.apply(
                ontology_rid,
                action_type,
                parameters=parameters,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with applyAction") from e

        assert serialize_response(response) == {}


def test_apply_batch(client_v1):
    with mock_requests(
        [
            {
                "method": "POST",
                "url": "https://example.palantirfoundry.com/api/v1/ontologies/{ontologyRid}/actions/{actionType}/applyBatch",
                "path_params": {
                    "ontologyRid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                    "actionType": "rename-employee",
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
        ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
        action_type = "rename-employee"
        requests = [
            {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}},
            {"parameters": {"id": 80061, "newName": "Joe Bloggs"}},
        ]
        try:
            response = client_v1.ontologies.Action.apply_batch(
                ontology_rid,
                action_type,
                requests=requests,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with applyActionBatch") from e

        assert serialize_response(response) == {}


def test_validate(client_v1):
    with mock_requests(
        [
            {
                "method": "POST",
                "url": "https://example.palantirfoundry.com/api/v1/ontologies/{ontologyRid}/actions/{actionType}/validate",
                "path_params": {
                    "ontologyRid": "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367",
                    "actionType": "rename-employee",
                },
                "json": {
                    "parameters": {
                        "id": "2",
                        "firstName": "Chuck",
                        "lastName": "Jones",
                        "age": 17,
                        "date": "2021-05-01",
                        "numbers": [1, 2, 3],
                        "hasObjectSet": True,
                        "objectSet": "ri.object-set.main.object-set.39a9f4bd-f77e-45ce-9772-70f25852f623",
                        "reference": "Chuck",
                        "percentage": 41.3,
                        "differentObjectId": "2",
                    }
                },
                "response": {
                    "status": 200,
                    "json": {
                        "result": "INVALID",
                        "submissionCriteria": [
                            {
                                "configuredFailureMessage": "First name can not match the first name of the referenced object.",
                                "result": "INVALID",
                            }
                        ],
                        "parameters": {
                            "age": {
                                "result": "INVALID",
                                "evaluatedConstraints": [{"type": "range", "gte": 18}],
                                "required": True,
                            },
                            "id": {"result": "VALID", "evaluatedConstraints": [], "required": True},
                            "date": {
                                "result": "VALID",
                                "evaluatedConstraints": [],
                                "required": True,
                            },
                            "lastName": {
                                "result": "VALID",
                                "evaluatedConstraints": [
                                    {
                                        "type": "oneOf",
                                        "options": [
                                            {"displayName": "Doe", "value": "Doe"},
                                            {"displayName": "Smith", "value": "Smith"},
                                            {"displayName": "Adams", "value": "Adams"},
                                            {"displayName": "Jones", "value": "Jones"},
                                        ],
                                        "otherValuesAllowed": True,
                                    }
                                ],
                                "required": True,
                            },
                            "numbers": {
                                "result": "VALID",
                                "evaluatedConstraints": [{"type": "arraySize", "lte": 4, "gte": 2}],
                                "required": True,
                            },
                            "differentObjectId": {
                                "result": "VALID",
                                "evaluatedConstraints": [{"type": "objectPropertyValue"}],
                                "required": False,
                            },
                            "firstName": {
                                "result": "VALID",
                                "evaluatedConstraints": [],
                                "required": True,
                            },
                            "reference": {
                                "result": "VALID",
                                "evaluatedConstraints": [{"type": "objectQueryResult"}],
                                "required": False,
                            },
                            "percentage": {
                                "result": "VALID",
                                "evaluatedConstraints": [{"type": "range", "lt": 100, "gte": 0}],
                                "required": True,
                            },
                            "objectSet": {
                                "result": "VALID",
                                "evaluatedConstraints": [],
                                "required": True,
                            },
                            "attachment": {
                                "result": "VALID",
                                "evaluatedConstraints": [],
                                "required": False,
                            },
                            "hasObjectSet": {
                                "result": "VALID",
                                "evaluatedConstraints": [],
                                "required": False,
                            },
                            "multipleAttachments": {
                                "result": "VALID",
                                "evaluatedConstraints": [{"type": "arraySize", "gte": 0}],
                                "required": False,
                            },
                        },
                    },
                    "content_type": "application/json",
                },
            }
        ]
    ):
        ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
        action_type = "rename-employee"
        parameters = {
            "id": "2",
            "firstName": "Chuck",
            "lastName": "Jones",
            "age": 17,
            "date": "2021-05-01",
            "numbers": [1, 2, 3],
            "hasObjectSet": True,
            "objectSet": "ri.object-set.main.object-set.39a9f4bd-f77e-45ce-9772-70f25852f623",
            "reference": "Chuck",
            "percentage": 41.3,
            "differentObjectId": "2",
        }
        try:
            response = client_v1.ontologies.Action.validate(
                ontology_rid,
                action_type,
                parameters=parameters,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with validateAction") from e

        assert serialize_response(response) == {
            "result": "INVALID",
            "submissionCriteria": [
                {
                    "configuredFailureMessage": "First name can not match the first name of the referenced object.",
                    "result": "INVALID",
                }
            ],
            "parameters": {
                "age": {
                    "result": "INVALID",
                    "evaluatedConstraints": [{"type": "range", "gte": 18}],
                    "required": True,
                },
                "id": {"result": "VALID", "evaluatedConstraints": [], "required": True},
                "date": {"result": "VALID", "evaluatedConstraints": [], "required": True},
                "lastName": {
                    "result": "VALID",
                    "evaluatedConstraints": [
                        {
                            "type": "oneOf",
                            "options": [
                                {"displayName": "Doe", "value": "Doe"},
                                {"displayName": "Smith", "value": "Smith"},
                                {"displayName": "Adams", "value": "Adams"},
                                {"displayName": "Jones", "value": "Jones"},
                            ],
                            "otherValuesAllowed": True,
                        }
                    ],
                    "required": True,
                },
                "numbers": {
                    "result": "VALID",
                    "evaluatedConstraints": [{"type": "arraySize", "lte": 4, "gte": 2}],
                    "required": True,
                },
                "differentObjectId": {
                    "result": "VALID",
                    "evaluatedConstraints": [{"type": "objectPropertyValue"}],
                    "required": False,
                },
                "firstName": {"result": "VALID", "evaluatedConstraints": [], "required": True},
                "reference": {
                    "result": "VALID",
                    "evaluatedConstraints": [{"type": "objectQueryResult"}],
                    "required": False,
                },
                "percentage": {
                    "result": "VALID",
                    "evaluatedConstraints": [{"type": "range", "lt": 100, "gte": 0}],
                    "required": True,
                },
                "objectSet": {"result": "VALID", "evaluatedConstraints": [], "required": True},
                "attachment": {"result": "VALID", "evaluatedConstraints": [], "required": False},
                "hasObjectSet": {"result": "VALID", "evaluatedConstraints": [], "required": False},
                "multipleAttachments": {
                    "result": "VALID",
                    "evaluatedConstraints": [{"type": "arraySize", "gte": 0}],
                    "required": False,
                },
            },
        }
