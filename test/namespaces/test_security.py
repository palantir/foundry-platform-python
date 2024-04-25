from typing import Any

from foundry.foundry_client import FoundryClient

# from foundry.models.search_json_query import EqualsQuery
from ..utils import client  # type: ignore
from ..utils import mock_responses


def test_can_get_user(client: FoundryClient, monkeypatch: Any):
    user_id = "176a8ce7-1f63-4942-b89e-208f5f3d4380"

    mock_responses(
        monkeypatch,
        [
            (
                {
                    "method": "GET",
                    "url": f"https://test.com/api/v2/security/users/{user_id}",
                    "json": None,
                    "params": {},
                },
                {
                    "status": 200,
                    "json": {
                        "id": user_id,
                        "username": "test-username",
                        "givenName": None,
                        "familyName": None,
                        "email": None,
                        "realm": "Palantir",
                        "organization": "ri.a.b.c.d",
                        "attributes": {},
                    },
                    "content": None,
                },
            )
        ],
    )

    user = client.security.User.get(user_id)
    assert user.id == user_id
    assert user.username == "test-username"
