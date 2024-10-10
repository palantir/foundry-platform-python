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

from datetime import datetime
from typing import Literal

from typing_extensions import NotRequired
from typing_extensions import TypedDict


class FileLastModifiedAfterFilterDict(TypedDict):
    """Only import files that have been modified after a specified timestamp"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    afterTimestamp: NotRequired[datetime]
    """
    Timestamp threshold, specified in ISO-8601 format.
    If not specified, defaults to the timestamp the file import is executed.
    """

    type: Literal["lastModifiedAfterFilter"]
