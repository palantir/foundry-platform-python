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

from typing import Literal

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.connectivity.models._s3_authentication_mode_dict import (
    S3AuthenticationModeDict,
)  # NOQA


class S3ConnectionConfigurationDict(TypedDict):
    """
    The configuration needed to connect to an [AWS S3 external system (or any other S3-like external systems that
    implement the s3a protocol)](/docs/foundry/available-connectors/amazon-s3/#amazon-s3).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    bucketUrl: str
    """The URL of the S3 bucket. The URL should contain a trailing slash."""

    authenticationMode: NotRequired[S3AuthenticationModeDict]
    """
    The authentication mode to use to connect to the S3 external system. No authentication mode is required
    to connect to publicly accessible AWS S3 buckets.
    """

    type: Literal["s3"]
