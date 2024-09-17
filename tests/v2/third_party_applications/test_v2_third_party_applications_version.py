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


def test_delete(client_v2):
    with mock_requests(
        [
            {
                "method": "DELETE",
                "url": "https://example.palantirfoundry.com/api/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion}",
                "path_params": {
                    "thirdPartyApplicationRid": "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6",
                    "versionVersion": "1.2.0",
                },
                "json": None,
                "response": {
                    "status": 200,
                    "json": None,
                    "content_type": "None",
                },
            }
        ]
    ):
        third_party_application_rid = (
            "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
        )
        version_version = "1.2.0"
        preview = None
        try:
            response = (
                client_v2.third_party_applications.ThirdPartyApplication.Website.Version.delete(
                    third_party_application_rid,
                    version_version,
                    preview=preview,
                )
            )
        except ValidationError as e:
            raise Exception("There was a validation error with deleteVersion") from e

        assert serialize_response(response) == None


def test_get(client_v2):
    with mock_requests(
        [
            {
                "method": "GET",
                "url": "https://example.palantirfoundry.com/api/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion}",
                "path_params": {
                    "thirdPartyApplicationRid": "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6",
                    "versionVersion": "1.2.0",
                },
                "json": None,
                "response": {
                    "status": 200,
                    "json": {"version": "1.2.0"},
                    "content_type": "application/json",
                },
            }
        ]
    ):
        third_party_application_rid = (
            "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
        )
        version_version = "1.2.0"
        preview = None
        try:
            response = client_v2.third_party_applications.ThirdPartyApplication.Website.Version.get(
                third_party_application_rid,
                version_version,
                preview=preview,
            )
        except ValidationError as e:
            raise Exception("There was a validation error with getVersion") from e

        assert serialize_response(response) == {"version": "1.2.0"}