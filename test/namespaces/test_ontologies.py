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

from foundry.v2 import FoundryV2Client

# from foundry.models.search_json_query_v2 import EqualsQuery
# from foundry.models.search_json_query_v2 import SearchJsonQueryV2
from ..utils import client_v2  # type: ignore
from ..utils import mock_responses


def mock_list_ontologies(monkeypatch: Any):
    mock_responses(
        monkeypatch,
        [
            (
                {
                    "method": "GET",
                    "url": "https://test.com/api/v2/ontologies/MyOntology/objectTypes",
                    "json": None,
                    "params": None,
                },
                {
                    "status": 200,
                    "json": {
                        "nextPageToken": None,
                        "data": [
                            {
                                "rid": "ri.a.b.c.d",
                                "displayName": "TEST",
                                "pluralDisplayName": "TEST",
                                "apiName": "API",
                                "status": "ACTIVE",
                                "primaryKey": "123",
                                "primaryKey": "abc",
                                "titleProperty": "abc",
                                "properties": {},
                                "icon": {"type": "blueprint", "name": "test", "color": "test"},
                            }
                        ],
                    },
                    "content": None,
                },
            )
        ],
    )


def test_can_list_object_types(client_v2: FoundryV2Client, monkeypatch: Any):
    mock_list_ontologies(monkeypatch)

    result = client_v2.ontologies.Ontology.ObjectType.list(
        ontology="MyOntology",
    )

    assert len(list(result)) == 1


# def mock_search_query(monkeypatch):
#     mock_responses(
#         monkeypatch,
#         [
#             (
#                 {
#                     "method": "POST",
#                     "url": "https://test.com/api/v2/ontologies/MyOntology/objects/MyObjectType/search",
#                     "body": {"where": {"field": "myProp", "type": "eq", "value": 21}},
#                 },
#                 {"status": 200, "body": {"nextPageToken": None, "data": [{}]}},
#             )
#         ],
#     )


# def test_can_search_using_classes(client_v2: FoundryV2Client, monkeypatch):
#     mock_search_query(monkeypatch)

#     result = client_v2.ontologies.search_objects(
#         ontology="MyOntology",
#         object_type="MyObjectType",
#         search_objects_request_v2=SearchObjectsRequestV2(
#             where=EqualsQuery(
#                 type="eq",
#                 field="myProp",
#                 value=21,
#             )
#         ),
#     )

#     assert result.data is not None and len(result.data) == 1


# def test_can_search_with_dict(client_v2: FoundryV2Client, monkeypatch):
#     mock_search_query(monkeypatch)

#     _ = client_v2.ontologies.search_objects(
#         ontology="MyOntology",
#         object_type="MyObjectType",
#         search_objects_request_v2={"where": {"field": "myProp", "type": "eq", "value": 21}},  # type: ignore
#     )


# def test_can_search_with_query_builder(client_v2: FoundryV2Client, monkeypatch):
#     mock_search_query(monkeypatch)

#     _ = client_v2.ontologies.search_objects(
#         ontology="MyOntology",
#         object_type="MyObjectType",
#         search_objects_request_v2=SearchObjectsRequestV2(
#             where=SearchQuery.eq(field="myProp", value=21)
#         ),
# )
