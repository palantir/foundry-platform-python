from typing import Any

from foundry.foundry_client import FoundryClient

# from foundry.models.search_json_query_v2 import EqualsQuery
# from foundry.models.search_json_query_v2 import SearchJsonQueryV2
from ..utils import client  # type: ignore
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
                                "apiName": "API",
                                "status": "ACTIVE",
                                "primaryKey": "123",
                                "primaryKey": "abc",
                                "titleProperty": "abc",
                                "properties": {},
                            }
                        ],
                    },
                    "content": None,
                },
            )
        ],
    )


def test_can_list_object_types(client: FoundryClient, monkeypatch: Any):
    mock_list_ontologies(monkeypatch)

    result = client.ontologies.Ontology.ObjectType.list(
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


# def test_can_search_using_classes(client: FoundryClient, monkeypatch):
#     mock_search_query(monkeypatch)

#     result = client.ontologies.search_objects(
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


# def test_can_search_with_dict(client: FoundryClient, monkeypatch):
#     mock_search_query(monkeypatch)

#     _ = client.ontologies.search_objects(
#         ontology="MyOntology",
#         object_type="MyObjectType",
#         search_objects_request_v2={"where": {"field": "myProp", "type": "eq", "value": 21}},  # type: ignore
#     )


# def test_can_search_with_query_builder(client: FoundryClient, monkeypatch):
#     mock_search_query(monkeypatch)

#     _ = client.ontologies.search_objects(
#         ontology="MyOntology",
#         object_type="MyObjectType",
#         search_objects_request_v2=SearchObjectsRequestV2(
#             where=SearchQuery.eq(field="myProp", value=21)
#         ),
# )
