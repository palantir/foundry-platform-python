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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry._core.utils import DateTime
from foundry.models._transaction_rid import TransactionRid
from foundry.models._transaction_status import TransactionStatus
from foundry.models._transaction_type import TransactionType


class TransactionDict(TypedDict):
    """An operation that modifies the files within a dataset."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: TransactionRid

    transactionType: TransactionType

    status: TransactionStatus

    createdTime: DateTime
    """The timestamp when the transaction was created, in ISO 8601 timestamp format."""

    closedTime: NotRequired[DateTime]
    """The timestamp when the transaction was closed, in ISO 8601 timestamp format."""
