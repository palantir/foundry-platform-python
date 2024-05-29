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


def test_can_get_user_groups(client: FoundryClient, monkeypatch: Any):
    user_id = "176a8ce7-1f63-4942-b89e-208f5f3d4380"
    group_id = "186a8ce7-1f63-4942-b89e-208f5f3d4380"

    mock_responses(
        monkeypatch,
        [
            (
                {
                    "method": "GET",
                    "url": f"https://test.com/api/v2/security/users/{user_id}/groupMemberships",
                    "json": None,
                    "params": {},
                },
                {
                    "status": 200,
                    "json": {
                        "nextPageToken": "123",
                        "data": [{"groupId": group_id}],
                    },
                    "content": None,
                },
            )
        ],
    )

    result = client.security.User.GroupMembership.page(user_id)
    assert result.next_page_token == "123"
    assert len(result.data) == 1
    assert result.data[0].group_id == group_id
    assert result.data[0].to_dict() == {"groupId": group_id}