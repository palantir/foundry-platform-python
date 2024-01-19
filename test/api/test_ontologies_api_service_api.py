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
from foundry.foundry_client import FoundryClient

# from foundry.models.search_json_query import EqualsQuery
from test.utils import mock_responses
from test.utils import client


def mock_list_ontologies(monkeypatch):
    mock_responses(
        monkeypatch,
        [
            (
                {
                    "method": "GET",
                    "url": "https://test.com/api/v1/ontologies/MyOntology/objectTypes",
                },
                {
                    "status": 200,
                    "body": {
                        "nextPageToken": None,
                        "data": [{"rid": "123", "apiName": "API", "status": "ACTIVE"}],
                    },
                },
            )
        ],
    )


def test_can_list_object_types(client: FoundryClient, monkeypatch):
    mock_list_ontologies(monkeypatch)

    result = client.ontologies.list_object_types(
        ontology_rid="MyOntology",
    )

    assert result.data is not None and len(result.data) == 1


# def mock_search_query(monkeypatch):
#     mock_responses(
#         monkeypatch,
#         [
#             (
#                 {
#                     "method": "POST",
#                     "url": "https://test.com/api/v1/ontologies/MyOntology/objects/MyObjectType/search",
#                     "body": {"query": {"field": "myProp", "type": "eq", "value": 21}},
#                 },
#                 {
#                     "status": 200,
#                     "body": {
#                         "nextPageToken": None,
#                         "data": [{"properties": {}, "rid": ""}],
#                     },
#                 },
#             )
#         ],
#     )


# def test_can_search_using_classes(client: FoundryClient, monkeypatch):
#     mock_search_query(monkeypatch)

#     result = client.ontologies.search_objects(
#         ontology_rid="MyOntology",
#         object_type="MyObjectType",
#         search_objects_request=SearchObjectsRequest(
#             query=EqualsQuery(
#                 type="eq",
#                 field="myProp",
#                 value=21,
#             )
#         ),
#     )

#     assert result.data is not None and len(result.data) == 1


# def test_can_search_with_dict(client: FoundryClient, monkeypatch):
#     mock_search_query(monkeypatch)

#     _ = client.ontologies.search_objects(
#         ontology_rid="MyOntology",
#         object_type="MyObjectType",
#         search_objects_request={"query": {"field": "myProp", "type": "eq", "value": 21}},  # type: ignore
#     )


# def test_can_search_with_query_builder(client: FoundryClient, monkeypatch):
#     mock_search_query(monkeypatch)

#     _ = client.ontologies.search_objects(
#         ontology_rid="MyOntology",
#         object_type="MyObjectType",
#         search_objects_request=SearchObjectsRequest(query=SearchQuery.eq(field="myProp", value=21)),
#     )
