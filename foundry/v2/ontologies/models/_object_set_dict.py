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

from typing import List
from typing import Literal
from typing import Union

from pydantic import Field
from pydantic import StrictStr
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry.v2.ontologies.models._link_type_api_name import LinkTypeApiName
from foundry.v2.ontologies.models._object_set_base_type_dict import ObjectSetBaseTypeDict  # NOQA
from foundry.v2.ontologies.models._object_set_interface_base_type_dict import (
    ObjectSetInterfaceBaseTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_reference_type_dict import (
    ObjectSetReferenceTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_set_static_type_dict import (
    ObjectSetStaticTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._search_json_query_v2_dict import SearchJsonQueryV2Dict  # NOQA


class ObjectSetFilterTypeDict(TypedDict):
    """ObjectSetFilterType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    where: SearchJsonQueryV2Dict

    type: Literal["filter"]


class ObjectSetSearchAroundTypeDict(TypedDict):
    """ObjectSetSearchAroundType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    link: LinkTypeApiName

    type: Literal["searchAround"]


class ObjectSetIntersectionTypeDict(TypedDict):
    """ObjectSetIntersectionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSets: List[ObjectSetDict]

    type: Literal["intersect"]


class ObjectSetAsBaseObjectTypesTypeDict(TypedDict):
    """
    Casts the objects in the object set to their base type and thus ensures objects are returned with all of their
    properties in the resulting object set, not just the properties that implement interface properties. This is
    currently unsupported and an exception will be thrown if used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    type: Literal["asBaseObjectTypes"]


class ObjectSetSubtractTypeDict(TypedDict):
    """ObjectSetSubtractType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSets: List[ObjectSetDict]

    type: Literal["subtract"]


class ObjectSetUnionTypeDict(TypedDict):
    """ObjectSetUnionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSets: List[ObjectSetDict]

    type: Literal["union"]


class ObjectSetAsTypeTypeDict(TypedDict):
    """ObjectSetAsTypeType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    entityType: StrictStr
    """
    An object type or interface type API name to cast the object set to. Any object whose object type does not 
    match the object type provided or implement the interface type provided will be dropped from the resulting 
    object set. This is currently unsupported and an exception will be thrown if used.
    """

    objectSet: ObjectSetDict

    type: Literal["asType"]


ObjectSetDict = Annotated[
    Union[
        ObjectSetReferenceTypeDict,
        ObjectSetFilterTypeDict,
        ObjectSetSearchAroundTypeDict,
        ObjectSetInterfaceBaseTypeDict,
        ObjectSetStaticTypeDict,
        ObjectSetIntersectionTypeDict,
        ObjectSetAsBaseObjectTypesTypeDict,
        ObjectSetSubtractTypeDict,
        ObjectSetUnionTypeDict,
        ObjectSetAsTypeTypeDict,
        ObjectSetBaseTypeDict,
    ],
    Field(discriminator="type"),
]
"""Represents the definition of an `ObjectSet` in the `Ontology`."""
