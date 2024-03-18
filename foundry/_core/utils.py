from datetime import date
from datetime import datetime
from typing import Annotated
from typing import Union
from pydantic import BeforeValidator
from pydantic import StrictStr
from pydantic import StringConstraints
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
    if isinstance(value, datetime):
        value = value.isoformat(timespec="microseconds")
    else:
        try:
            datetime.fromisoformat(value)
        except ValueError as e:
            raise PydanticCustomError(
                "rfc_3339", "Invalid RFC 3339 datetime value", {"value": value}
            ) from e
    return value


def validate_date(value: Union[str, date]):
    if isinstance(value, date):
        value = value.isoformat()
    else:
        try:
            date.fromisoformat(value)
        except ValueError as e:
            raise PydanticCustomError(
                "rfc_3339", "Invalid RFC 3339 date value", {"value": value}
            ) from e
    return value


# Datetime type as defined by RFC 3339, section 5.6, for example, 2017-07-21T...
RFC3339DateTime = Annotated[
    Union[StrictStr, datetime],
    BeforeValidator(validate_datetime),
]


# Date type as defined by RFC 3339, section 5.6, for example, 2017-07-21
RFC3339Date = Annotated[
    Union[StrictStr, date],
    BeforeValidator(validate_date),
]
