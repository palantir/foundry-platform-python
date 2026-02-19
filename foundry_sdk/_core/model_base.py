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


import json
import warnings
from typing import Any
from typing import Dict
from typing import Hashable
from typing import Optional
from typing import cast

import pydantic


class ModelBase(pydantic.BaseModel):
    """
    Base class for all model objects in the SDK.

    This base model supports being used as a dictionary key while preserving mutability.
    It tracks if it has been used as a hash key and warns if mutation occurs after hashing.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def __init__(self, **data):
        super().__init__(**data)
        self._hash_called = False
        self._hash_value: Optional[int] = None

    def __hash__(self) -> int:
        """
        Generate a hash based on class identity and attribute values.
        """
        if self._hash_value is None:
            self._hash_called = True

            def make_hashable(value: Any) -> Hashable:
                if isinstance(value, dict):
                    return tuple((k, make_hashable(v)) for k, v in sorted(value.items()))
                elif isinstance(value, (list, set)):
                    return tuple(make_hashable(v) for v in value)
                else:
                    return value

            # Include class type in the hash
            class_identifier = self.__class__.__name__

            # Create hashable representations of all fields
            hash_fields = tuple(
                (field, make_hashable(getattr(self, field))) for field in self.model_fields
            )

            # Hash combination of class identifier and field values
            self._hash_value = hash((class_identifier, hash_fields))

        return self._hash_value

    def __setattr__(self, name: str, value: Any) -> None:
        """
        Track attribute mutations and warn if the model has been hashed.

        Once a model has been used as a dictionary key, modifying it could cause
        unexpected behavior, as the dictionary location is determined by the hash
        value at insertion time.
        """
        # Check if we're setting special attributes used by this class
        if name in ("_hash_called", "_hash_value"):
            super().__setattr__(name, value)
            return

        # If hash has been called, warn about the mutation and reset the hash
        if self._hash_called:
            warnings.warn(
                f"Modifying {self.__class__.__name__} after it has been used as a dictionary key "
                "may lead to unexpected behavior.",
                UserWarning,
                stacklevel=2,
            )
            # Reset the hash value since the object has changed
            self._hash_value = None

        super().__setattr__(name, value)

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(Dict[str, Any], self.model_dump(by_alias=True, exclude_none=True))
