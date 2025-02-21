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

from dataclasses import dataclass
from typing import Literal

from typing_extensions import TypedDict

from foundry._errors import NotFoundError
from foundry.v2.core.models._file_path import FilePath
from foundry.v2.datasets.models._dataset_rid import DatasetRid


class FileNotFoundParameters(TypedDict):
    """The given File could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: DatasetRid

    filePath: FilePath


@dataclass
class FileNotFound(NotFoundError):
    name: Literal["FileNotFound"]
    parameters: FileNotFoundParameters
    error_instance_id: str


__all__ = ["FileNotFound"]
