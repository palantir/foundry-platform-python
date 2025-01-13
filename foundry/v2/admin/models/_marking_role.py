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

from typing import Literal

MarkingRole = Literal["ADMINISTER", "DECLASSIFY", "USE"]
"""
Represents the operations that a user can perform with regards to a Marking.
  * ADMINISTER: The user can add and remove members from the Marking, update Marking Role Assignments, and change Marking metadata.
  * DECLASSIFY: The user can remove the Marking from resources in the platform and stop the propagation of the Marking during a transform.
  * USE: The user can apply the marking to resources in the platform.
"""
