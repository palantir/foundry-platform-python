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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry import _errors as errors
from foundry.v2.admin import models as admin_models


class MarkingCategoryNotFoundParameters(typing_extensions.TypedDict):
    """The given MarkingCategory could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingCategoryId: admin_models.MarkingCategoryId


@dataclass
class MarkingCategoryNotFound(errors.NotFoundError):
    name: typing.Literal["MarkingCategoryNotFound"]
    parameters: MarkingCategoryNotFoundParameters
    error_instance_id: str


__all__ = ["MarkingCategoryNotFound"]
