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
from typing import Any
from typing import ClassVar
from typing import Dict
from typing import Set

from pydantic import BaseModel
from pydantic import Field


from foundry.models._dataset_name import DatasetName
from foundry.models._dataset_rid import DatasetRid
from foundry.models._folder_rid import FolderRid


class Dataset(BaseModel):
    """Dataset"""

    rid: DatasetRid = Field()
    """The Resource Identifier (RID) of a Dataset. Example: `ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da`."""

    name: DatasetName = Field()
    """DatasetName"""

    parent_folder_rid: FolderRid = Field(alias="parentFolderRid")
    """FolderRid"""

    _properties: ClassVar[Set[str]] = set(["rid", "name", "parentFolderRid"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "Dataset":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)
