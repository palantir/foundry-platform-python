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

ObjectState = Literal["ADDED_OR_UPDATED", "REMOVED"]
"""
Represents the state of the object within the object set. ADDED_OR_UPDATED indicates that the object was 
added to the set or the object has updated and was previously in the set. REMOVED indicates that the object 
was removed from the set due to the object being deleted or the object no longer meets the object set 
definition.
"""
