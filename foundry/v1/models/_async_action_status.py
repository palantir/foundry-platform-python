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

AsyncActionStatus = Literal[
    "RUNNING_SUBMISSION_CHECKS",
    "EXECUTING_WRITE_BACK_WEBHOOK",
    "COMPUTING_ONTOLOGY_EDITS",
    "COMPUTING_FUNCTION",
    "WRITING_ONTOLOGY_EDITS",
    "EXECUTING_SIDE_EFFECT_WEBHOOK",
    "SENDING_NOTIFICATIONS",
]
"""AsyncActionStatus"""
