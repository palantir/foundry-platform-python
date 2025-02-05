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
from typing import Optional
from typing import cast

import pydantic

from foundry._core.utils import Long
from foundry.v2.connectivity.models._region import Region
from foundry.v2.connectivity.models._s3_authentication_mode import S3AuthenticationMode
from foundry.v2.connectivity.models._s3_connection_configuration_dict import (
    S3ConnectionConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._s3_kms_configuration import S3KmsConfiguration
from foundry.v2.connectivity.models._s3_proxy_configuration import S3ProxyConfiguration
from foundry.v2.connectivity.models._sts_role_configuration import StsRoleConfiguration


class S3ConnectionConfiguration(pydantic.BaseModel):
    """
    The configuration needed to connect to an [AWS S3 external system (or any other S3-like external systems that
    implement the s3a protocol)](/docs/foundry/available-connectors/amazon-s3/#amazon-s3).
    """

    bucket_url: str = pydantic.Field(alias=str("bucketUrl"))  # type: ignore[literal-required]

    """The URL of the S3 bucket. The URL should contain a trailing slash."""

    s3_endpoint: Optional[str] = pydantic.Field(alias=str("s3Endpoint"), default=None)  # type: ignore[literal-required]

    """
    The endpoint of the S3 service. This is used to connect to a custom S3 service that is not AWS S3.
    If not specified, defaults to the [AWS S3 endpoint](https://docs.aws.amazon.com/general/latest/gr/s3.html).
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    region: Optional[Region] = None

    """
    The region representing the location of the S3 bucket.
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    authentication_mode: Optional[S3AuthenticationMode] = pydantic.Field(alias=str("authenticationMode"), default=None)  # type: ignore[literal-required]

    """
    The authentication mode to use to connect to the S3 external system. No authentication mode is required
    to connect to publicly accessible AWS S3 buckets.
    """

    s3_endpoint_signing_region: Optional[Region] = pydantic.Field(alias=str("s3EndpointSigningRegion"), default=None)  # type: ignore[literal-required]

    """
    The region used when constructing the S3 client using a custom endpoint.
    This is often not required and would only be needed if you are using the S3 connector with an S3-compliant third-party API,
    and are also setting a custom endpoint that requires a non-default region.
    """

    client_kms_configuration: Optional[S3KmsConfiguration] = pydantic.Field(alias=str("clientKmsConfiguration"), default=None)  # type: ignore[literal-required]

    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    sts_role_configuration: Optional[StsRoleConfiguration] = pydantic.Field(alias=str("stsRoleConfiguration"), default=None)  # type: ignore[literal-required]

    """The configuration needed to assume a role to connect to the S3 external system."""

    proxy_configuration: Optional[S3ProxyConfiguration] = pydantic.Field(alias=str("proxyConfiguration"), default=None)  # type: ignore[literal-required]

    """The configuration needed to connect to the S3 external system through a proxy."""

    max_connections: Optional[int] = pydantic.Field(alias=str("maxConnections"), default=None)  # type: ignore[literal-required]

    """
    The maximum number of HTTP connections to the S3 service per sync.
    If not specified, defaults to 50 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_MAX_CONNECTIONS).
    """

    connection_timeout_millis: Optional[Long] = pydantic.Field(alias=str("connectionTimeoutMillis"), default=None)  # type: ignore[literal-required]

    """
    The amount of time (in milliseconds) to wait when initially establishing a connection before giving up and timing out.
    If not specified, defaults to 10000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_CONNECTION_TIMEOUT).
    """

    socket_timeout_millis: Optional[Long] = pydantic.Field(alias=str("socketTimeoutMillis"), default=None)  # type: ignore[literal-required]

    """
    The amount of time (in milliseconds) to wait for data to be transferred over an established, open connection.
    If not specified, defaults to 50000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_SOCKET_TIMEOUT).
    """

    max_error_retry: Optional[int] = pydantic.Field(alias=str("maxErrorRetry"), default=None)  # type: ignore[literal-required]

    """
    The maximum number of retry attempts for failed requests to the S3 service.
    If not specified, defaults to 3 as defined by the [AWS SDK default](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html#retry-strategies).
    """

    match_subfolder_exactly: Optional[bool] = pydantic.Field(alias=str("matchSubfolderExactly"), default=None)  # type: ignore[literal-required]

    """
    If true, only files in the subfolder specified in the bucket URL will be synced.
    If false, all files in the bucket will be synced.
    If not specified, defaults to false.
    """

    enable_requester_pays: Optional[bool] = pydantic.Field(alias=str("enableRequesterPays"), default=None)  # type: ignore[literal-required]

    """
    Defaults to false, unless set and overwritten.
    If true, includes the [requester pays header](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html)
    in requests, allowing reads from requester pays buckets.
    """

    type: Literal["s3"] = "s3"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> S3ConnectionConfigurationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            S3ConnectionConfigurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )
