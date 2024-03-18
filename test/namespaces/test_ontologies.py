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
from ..utils import mock_responses
from ..utils import client


def mock_list_ontologies(monkeypatch):
    mock_responses(
        monkeypatch,
        [
            (
                {
                    "method": "GET",
                    "url": "https://test.com/api/v1/ontologies/ri.a.b.c.d/objectTypes",
                    "json": None,
                    "params": None,
                },
                {
                    "status": 200,
                    "json": {
                        "nextPageToken": None,
                        "data": [{"rid": "ri.a.b.c.d", "apiName": "API", "status": "ACTIVE"}],
                    },
                    "content": None,
                },
            )
        ],
    )


def test_can_list_object_types(client: FoundryClient, monkeypatch):
    mock_list_ontologies(monkeypatch)

    result = client.ontologies.ObjectType.iterator(
        ontology_rid="ri.a.b.c.d",
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
