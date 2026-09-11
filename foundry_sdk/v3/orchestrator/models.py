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

import typing

import pydantic
import typing_extensions

from foundry_sdk import _core as core


class CompleteProcessExecutionSignalRequest(core.ModelBase):
    """The data to attach to a signal completion."""

    payload: typing.Optional[typing.Any] = None
    """
    Arbitrary JSON passed to the process execution that consumes the signal. Empty when the completion
    carries no payload.
    """


ProcessExecutionId: typing_extensions.TypeAlias = str
"""Identifies a single execution of a durable process run by the platform."""


SignalId: typing_extensions.TypeAlias = str
"""Identifies a signal on a process execution."""


core.resolve_forward_references_in_module(__name__)

__all__ = [
    "CompleteProcessExecutionSignalRequest",
    "ProcessExecutionId",
    "SignalId",
]
