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
from typing import List
from typing import Optional
from typing import Set

from pydantic import BaseModel
from pydantic import Field


from foundry.models._ontology_object import OntologyObject
from foundry.models._page_token import PageToken


class ListLinkedObjectsResponse(BaseModel):
    """ListLinkedObjectsResponse"""

    next_page_token: Optional[PageToken] = Field(alias="nextPageToken", default=None)
    """
    The page token indicates where to start paging. This should be omitted from the first page's request.
    To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response
    and populate the next request's `pageToken` field with it.
    """

    data: Optional[List[OntologyObject]] = Field(default=None)

    _properties: ClassVar[Set[str]] = set(["nextPageToken", "data"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "ListLinkedObjectsResponse":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)
