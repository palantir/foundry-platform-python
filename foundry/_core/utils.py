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


from typing import List

import pydantic
from typing_extensions import Annotated

RID = Annotated[
    pydantic.StrictStr,
    pydantic.StringConstraints(
        pattern=r"^ri\.[a-z][a-z0-9-]*\.([a-z0-9][a-z0-9\-]*)?\.[a-z][a-z0-9-]*\.[a-zA-Z0-9._-]+$",
    ),
]


UUID = Annotated[
    pydantic.StrictStr,
    pydantic.StringConstraints(
        pattern=r"^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$",
    ),
]


def remove_prefixes(text: str, prefixes: List[str]):
    for prefix in prefixes:
        if text.startswith(prefix):
            text = text[len(prefix) :]
    return text
