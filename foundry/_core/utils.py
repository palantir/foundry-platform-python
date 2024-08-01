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


from datetime import date
from datetime import datetime
from typing import Annotated
from typing import Union

from pydantic import BeforeValidator
from pydantic import Strict
from pydantic import StrictStr
from pydantic import StringConstraints
from pydantic.functional_serializers import PlainSerializer
from pydantic_core import PydanticCustomError

RID = Annotated[
    StrictStr,
    StringConstraints(
        pattern=r"^ri\.[a-z][a-z0-9-]*\.([a-z0-9][a-z0-9\-]*)?\.[a-z][a-z0-9-]*\.[a-zA-Z0-9._-]+$",
    ),
]


UUID = Annotated[
    StrictStr,
    StringConstraints(
        pattern=r"^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$",
    ),
]


def validate_datetime(value: Union[str, datetime]):
    if isinstance(value, str):
        try:
            # In Python 3.11, fromisoformat handles the Z shorthand
            # In 3.10 and below, this shorthand throws an error
            # The easiest solution is to just replace "Z" with a +00:00
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError as e:
            raise PydanticCustomError(
                "iso_8601", "Invalid ISO 8601 datetime value", {"value": value}
            ) from e

    return value


def validate_date(value: Union[str, date]):
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError as e:
            raise PydanticCustomError(
                "iso_8601", "Invalid ISO 8601 format", {"value": value}
            ) from e

    return value


DateTime = Annotated[
    Annotated[datetime, Strict()],
    BeforeValidator(validate_datetime),
    PlainSerializer(
        lambda ts: ts.isoformat(timespec="microseconds"),
        return_type=str,
        # Important: This ensures that the to_dict() methods on the models dumps
        # the model according to the TypeDict representation
        when_used="json",
    ),
]


Date = Annotated[
    Annotated[date, Strict()],
    BeforeValidator(validate_date),
    PlainSerializer(
        lambda dt: dt.isoformat(),
        return_type=str,
        # Important: This ensures that the to_dict() methods on the models dumps
        # the model according to the TypeDict representation
        when_used="json",
    ),
]
