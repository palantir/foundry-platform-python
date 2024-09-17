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


def test_get_current(client_v2):
    with mock_requests(
        [
            {
                "method": "GET",
                "url": "https://example.palantirfoundry.com/api/v2/admin/users/getCurrent",
                "path_params": {},
                "json": None,
                "response": {
                    "status": 200,
                    "json": {
                        "givenName": "John",
                        "familyName": "Smith",
                        "organization": "ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa",
                        "realm": "palantir-internal-realm",
                        "attributes": {
                            "multipass:givenName": ["John"],
                            "multipass:familyName": ["Smith"],
                            "multipass:email:primary": ["jsmith@example.com"],
                            "multipass:realm": ["eab0a251-ca1a-4a84-a482-200edfb8026f"],
                            "multipass:organization-rid": [
                                "ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"
                            ],
                            "department": ["Finance"],
                            "jobTitle": ["Accountant"],
                        },
                        "id": "f05f8da4-b84c-4fca-9c77-8af0b13d11de",
                        "email": "jsmith@example.com",
                        "username": "jsmith",
                    },
                    "content_type": "application/json",
                },
            }
        ]
    ):
        preview = None
        try:
            response = client_v2.admin.User.get_current(
                preview=preview,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with getCurrentUser") from e

        assert serialize_response(response) == {
            "givenName": "John",
            "familyName": "Smith",
            "organization": "ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa",
            "realm": "palantir-internal-realm",
            "attributes": {
                "multipass:givenName": ["John"],
                "multipass:familyName": ["Smith"],
                "multipass:email:primary": ["jsmith@example.com"],
                "multipass:realm": ["eab0a251-ca1a-4a84-a482-200edfb8026f"],
                "multipass:organization-rid": [
                    "ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"
                ],
                "department": ["Finance"],
                "jobTitle": ["Accountant"],
            },
            "id": "f05f8da4-b84c-4fca-9c77-8af0b13d11de",
            "email": "jsmith@example.com",
            "username": "jsmith",
        }
