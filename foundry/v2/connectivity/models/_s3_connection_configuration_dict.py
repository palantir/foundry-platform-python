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

from foundry._core.utils import Long
from foundry.v2.connectivity.models._region import Region
from foundry.v2.connectivity.models._s3_authentication_mode_dict import (
    S3AuthenticationModeDict,
)  # NOQA
from foundry.v2.connectivity.models._s3_kms_configuration_dict import S3KmsConfigurationDict  # NOQA
from foundry.v2.connectivity.models._s3_proxy_configuration_dict import (
    S3ProxyConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._sts_role_configuration_dict import (
    StsRoleConfigurationDict,
)  # NOQA


class S3ConnectionConfigurationDict(TypedDict):
    """
    The configuration needed to connect to an [AWS S3 external system (or any other S3-like external systems that
    implement the s3a protocol)](/docs/foundry/available-connectors/amazon-s3/#amazon-s3).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    bucketUrl: str
    """The URL of the S3 bucket. The URL should contain a trailing slash."""

    s3Endpoint: NotRequired[str]
    """
    The endpoint of the S3 service. This is used to connect to a custom S3 service that is not AWS S3.
    If not specified, defaults to the [AWS S3 endpoint](https://docs.aws.amazon.com/general/latest/gr/s3.html).
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    region: NotRequired[Region]
    """
    The region representing the location of the S3 bucket.
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    authenticationMode: NotRequired[S3AuthenticationModeDict]
    """
    The authentication mode to use to connect to the S3 external system. No authentication mode is required
    to connect to publicly accessible AWS S3 buckets.
    """

    s3EndpointSigningRegion: NotRequired[Region]
    """
    The region used when constructing the S3 client using a custom endpoint.
    This is often not required and would only be needed if you are using the S3 connector with an S3-compliant third-party API,
    and are also setting a custom endpoint that requires a non-default region.
    """

    clientKmsConfiguration: NotRequired[S3KmsConfigurationDict]
    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    stsRoleConfiguration: NotRequired[StsRoleConfigurationDict]
    """The configuration needed to assume a role to connect to the S3 external system."""

    proxyConfiguration: NotRequired[S3ProxyConfigurationDict]
    """The configuration needed to connect to the S3 external system through a proxy."""

    maxConnections: NotRequired[int]
    """
    The maximum number of HTTP connections to the S3 service per sync.
    If not specified, defaults to 50 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_MAX_CONNECTIONS).
    """

    connectionTimeoutMillis: NotRequired[Long]
    """
    The amount of time (in milliseconds) to wait when initially establishing a connection before giving up and timing out.
    If not specified, defaults to 10000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_CONNECTION_TIMEOUT).
    """

    socketTimeoutMillis: NotRequired[Long]
    """
    The amount of time (in milliseconds) to wait for data to be transferred over an established, open connection.
    If not specified, defaults to 50000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_SOCKET_TIMEOUT).
    """

    maxErrorRetry: NotRequired[int]
    """
    The maximum number of retry attempts for failed requests to the S3 service.
    If not specified, defaults to 3 as defined by the [AWS SDK default](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html#retry-strategies).
    """

    matchSubfolderExactly: NotRequired[bool]
    """
    If true, only files in the subfolder specified in the bucket URL will be synced.
    If false, all files in the bucket will be synced.
    If not specified, defaults to false.
    """

    enableRequesterPays: NotRequired[bool]
    """
    Defaults to false, unless set and overwritten.
    If true, includes the [requester pays header](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html)
    in requests, allowing reads from requester pays buckets.
    """

    type: Literal["s3"]
