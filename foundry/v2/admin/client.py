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


from __future__ import annotations

from foundry._core import Auth
from foundry.v2.admin.enrollment import EnrollmentClient
from foundry.v2.admin.group import GroupClient
from foundry.v2.admin.marking import MarkingClient
from foundry.v2.admin.marking_category import MarkingCategoryClient
from foundry.v2.admin.user import UserClient


class AdminClient:
    def __init__(self, auth: Auth, hostname: str):
        self.Enrollment = EnrollmentClient(auth=auth, hostname=hostname)
        self.Group = GroupClient(auth=auth, hostname=hostname)
        self.Marking = MarkingClient(auth=auth, hostname=hostname)
        self.MarkingCategory = MarkingCategoryClient(auth=auth, hostname=hostname)
        self.User = UserClient(auth=auth, hostname=hostname)
