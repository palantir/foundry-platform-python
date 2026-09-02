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

from foundry_sdk import _errors as errors
from foundry_sdk.v3.endpoints import models as endpoints_models


class EndpointSetEndpointNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    endpointRid: endpoints_models.EndpointSetEndpointRid
    endpointSetRid: endpoints_models.EndpointSetRid


@dataclass
class EndpointSetEndpointNotFound(errors.NotFoundError):
    name: typing.Literal["EndpointSetEndpointNotFound"]
    parameters: EndpointSetEndpointNotFoundParameters
    error_instance_id: str


class EndpointSetNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    endpointSetRid: endpoints_models.EndpointSetRid


@dataclass
class EndpointSetNotFound(errors.NotFoundError):
    name: typing.Literal["EndpointSetNotFound"]
    parameters: EndpointSetNotFoundParameters
    error_instance_id: str


class EndpointSetVersionNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    versionId: endpoints_models.EndpointSetVersionId
    endpointSetRid: endpoints_models.EndpointSetRid


@dataclass
class EndpointSetVersionNotFound(errors.NotFoundError):
    name: typing.Literal["EndpointSetVersionNotFound"]
    parameters: EndpointSetVersionNotFoundParameters
    error_instance_id: str


__all__ = [
    "EndpointSetEndpointNotFound",
    "EndpointSetNotFound",
    "EndpointSetVersionNotFound",
]
