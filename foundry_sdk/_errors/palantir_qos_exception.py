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


from collections.abc import Mapping
from enum import Enum
from typing import Final, Optional

from foundry_sdk._errors.palantir_exception import PalantirException

QOS_RETRY_HINT_HEADER: Final = "QoS-Retry-Hint"
QOS_DUE_TO_HEADER: Final = "QoS-Due-To"


class QoSRetryHint(Enum):
    DO_NOT_RETRY = "do-not-retry"

    @staticmethod
    def from_headers(headers: Mapping[str, str]) -> Optional["QoSRetryHint"]:
        retry_hint_value = headers.get(QOS_RETRY_HINT_HEADER)
        if retry_hint_value is not None:
            try:
                return QoSRetryHint(retry_hint_value)
            except ValueError:
                # If the value in the header is not a valid QoSRetryHint, we can choose to either
                # return None or raise an exception. Here, we choose to return None.
                return None
        return None


class QoSDueTo(Enum):
    CUSTOM = "custom"

    @staticmethod
    def from_headers(headers: Mapping[str, str]) -> Optional["QoSDueTo"]:
        due_to_value = headers.get(QOS_DUE_TO_HEADER)
        if due_to_value is not None:
            try:
                return QoSDueTo(due_to_value)
            except ValueError:
                # If the value in the header is not a valid QoSDueTo, we can choose to either
                # return None or raise an exception. Here, we choose to return None.
                return None
        return None


class PalantirQoSException(PalantirException):
    """The root exception class for all QoS related exceptions."""

    def __init__(
        self,
        message: str,
        reason: str,
        retry_hint: Optional[QoSRetryHint] = None,
        due_to: Optional[QoSDueTo] = None,
    ) -> None:
        super().__init__(message)
        self.reason = reason
        self.retry_hint = retry_hint
        self.due_to = due_to

    reason: str
    retry_hint: Optional[QoSRetryHint]
    due_to: Optional[QoSDueTo]


class RateLimitError(PalantirQoSException):
    """
    The service is experiencing too many requests. Reduce your request rate and retry your
    request shortly. This error is thrown if a 429 status code is returned.
    """


class ServiceUnavailable(PalantirQoSException):
    """
    The service is currently unavailable. Retry your request shortly. This error is thrown if a
    503 status code is returned.
    """
