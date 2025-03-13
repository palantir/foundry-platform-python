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

import typing
from datetime import datetime

import pydantic
import typing_extensions

from foundry import _core as core


class AgentProxyRuntime(pydantic.BaseModel):
    """
    The [agent proxy runtime](/docs/foundry/data-connection/core-concepts/#agent-proxy-runtime) is used to connect
    to data sources not accessible over the Internet. The agent acts as an inverting network proxy, forwarding
    network traffic originating in Foundry into the network where the agent is deployed, and relaying traffic
    back to Foundry. This allows capabilities in Foundry to work almost exactly the same as when using a
    direct connection but without requiring you to allow inbound network traffic to your systems originating
    from Foundry's IP addresses.
    """

    agent_rids: typing.List[AgentRid] = pydantic.Field(alias=str("agentRids"))  # type: ignore[literal-required]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: typing.Literal["agentProxyRuntime"] = "agentProxyRuntime"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AgentProxyRuntimeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AgentProxyRuntimeDict, self.model_dump(by_alias=True, exclude_none=True))


class AgentProxyRuntimeDict(typing_extensions.TypedDict):
    """
    The [agent proxy runtime](/docs/foundry/data-connection/core-concepts/#agent-proxy-runtime) is used to connect
    to data sources not accessible over the Internet. The agent acts as an inverting network proxy, forwarding
    network traffic originating in Foundry into the network where the agent is deployed, and relaying traffic
    back to Foundry. This allows capabilities in Foundry to work almost exactly the same as when using a
    direct connection but without requiring you to allow inbound network traffic to your systems originating
    from Foundry's IP addresses.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRids: typing.List[AgentRid]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: typing.Literal["agentProxyRuntime"]


AgentRid = core.RID
"""The Resource Identifier (RID) of an Agent."""


class AgentWorkerRuntime(pydantic.BaseModel):
    """
    The [agent worker runtime](/docs/foundry/data-connection/core-concepts/#agent-worker-runtime) is used to
    connect to data sources not accessible over the Internet. An agent worker should only be used when the desired
    connector does not support the agent proxy runtime. Agent worker runtimes are associated with a single or
    multiple agents that store the source configuration and credentials locally in an encrypted format,
    and run source capabilities on the agent itself.
    """

    agent_rids: typing.List[AgentRid] = pydantic.Field(alias=str("agentRids"))  # type: ignore[literal-required]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: typing.Literal["agentWorkerRuntime"] = "agentWorkerRuntime"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AgentWorkerRuntimeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AgentWorkerRuntimeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AgentWorkerRuntimeDict(typing_extensions.TypedDict):
    """
    The [agent worker runtime](/docs/foundry/data-connection/core-concepts/#agent-worker-runtime) is used to
    connect to data sources not accessible over the Internet. An agent worker should only be used when the desired
    connector does not support the agent proxy runtime. Agent worker runtimes are associated with a single or
    multiple agents that store the source configuration and credentials locally in an encrypted format,
    and run source capabilities on the agent itself.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRids: typing.List[AgentRid]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: typing.Literal["agentWorkerRuntime"]


class ApiKeyAuthentication(pydantic.BaseModel):
    """
    The API key used to authenticate to the external system.
    This can be configured as a header or query parameter.
    """

    location: RestRequestApiKeyLocation
    """The location of the API key in the request."""

    api_key: EncryptedProperty = pydantic.Field(alias=str("apiKey"))  # type: ignore[literal-required]
    """The value of the API key."""

    type: typing.Literal["apiKey"] = "apiKey"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ApiKeyAuthenticationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ApiKeyAuthenticationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ApiKeyAuthenticationDict(typing_extensions.TypedDict):
    """
    The API key used to authenticate to the external system.
    This can be configured as a header or query parameter.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    location: RestRequestApiKeyLocationDict
    """The location of the API key in the request."""

    apiKey: EncryptedPropertyDict
    """The value of the API key."""

    type: typing.Literal["apiKey"]


class AsPlaintextValue(pydantic.BaseModel):
    """AsPlaintextValue"""

    value: PlaintextValue
    type: typing.Literal["asPlaintextValue"] = "asPlaintextValue"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AsPlaintextValueDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AsPlaintextValueDict, self.model_dump(by_alias=True, exclude_none=True))


class AsPlaintextValueDict(typing_extensions.TypedDict):
    """AsPlaintextValue"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: PlaintextValue
    type: typing.Literal["asPlaintextValue"]


class AsSecretName(pydantic.BaseModel):
    """AsSecretName"""

    value: SecretName
    type: typing.Literal["asSecretName"] = "asSecretName"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AsSecretNameDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AsSecretNameDict, self.model_dump(by_alias=True, exclude_none=True))


class AsSecretNameDict(typing_extensions.TypedDict):
    """AsSecretName"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: SecretName
    type: typing.Literal["asSecretName"]


class AwsAccessKey(pydantic.BaseModel):
    """
    [Access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) are long-term
    credentials for an IAM user or the AWS account root user.
    Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and a secret access
    key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY). You must use both the access key ID and
    secret access key together to authenticate your requests.
    """

    access_key_id: str = pydantic.Field(alias=str("accessKeyId"))  # type: ignore[literal-required]
    secret_access_key: EncryptedProperty = pydantic.Field(alias=str("secretAccessKey"))  # type: ignore[literal-required]
    type: typing.Literal["awsAccessKey"] = "awsAccessKey"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AwsAccessKeyDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AwsAccessKeyDict, self.model_dump(by_alias=True, exclude_none=True))


class AwsAccessKeyDict(typing_extensions.TypedDict):
    """
    [Access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) are long-term
    credentials for an IAM user or the AWS account root user.
    Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and a secret access
    key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY). You must use both the access key ID and
    secret access key together to authenticate your requests.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    accessKeyId: str
    secretAccessKey: EncryptedPropertyDict
    type: typing.Literal["awsAccessKey"]


class BasicCredentials(pydantic.BaseModel):
    """BasicCredentials"""

    username: str
    password: EncryptedProperty
    type: typing.Literal["basic"] = "basic"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BasicCredentialsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(BasicCredentialsDict, self.model_dump(by_alias=True, exclude_none=True))


class BasicCredentialsDict(typing_extensions.TypedDict):
    """BasicCredentials"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    username: str
    password: EncryptedPropertyDict
    type: typing.Literal["basic"]


class BearerToken(pydantic.BaseModel):
    """The bearer token used to authenticate to the external system."""

    bearer_token: EncryptedProperty = pydantic.Field(alias=str("bearerToken"))  # type: ignore[literal-required]
    type: typing.Literal["bearerToken"] = "bearerToken"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BearerTokenDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(BearerTokenDict, self.model_dump(by_alias=True, exclude_none=True))


class BearerTokenDict(typing_extensions.TypedDict):
    """The bearer token used to authenticate to the external system."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    bearerToken: EncryptedPropertyDict
    type: typing.Literal["bearerToken"]


class CloudIdentity(pydantic.BaseModel):
    """
    [Cloud identities](/docs/foundry/administration/configure-cloud-identities/) allow you to authenticate to
    cloud provider resources without the use of static credentials.
    """

    cloud_identity_rid: CloudIdentityRid = pydantic.Field(alias=str("cloudIdentityRid"))  # type: ignore[literal-required]
    type: typing.Literal["cloudIdentity"] = "cloudIdentity"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CloudIdentityDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(CloudIdentityDict, self.model_dump(by_alias=True, exclude_none=True))


class CloudIdentityDict(typing_extensions.TypedDict):
    """
    [Cloud identities](/docs/foundry/administration/configure-cloud-identities/) allow you to authenticate to
    cloud provider resources without the use of static credentials.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    cloudIdentityRid: CloudIdentityRid
    type: typing.Literal["cloudIdentity"]


CloudIdentityRid = core.RID
"""The Resource Identifier (RID) of a Cloud Identity."""


class Connection(pydantic.BaseModel):
    """Connection"""

    rid: ConnectionRid
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    display_name: ConnectionDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the Connection. The display name must not be blank."""

    runtime_platform: RuntimePlatform = pydantic.Field(alias=str("runtimePlatform"))  # type: ignore[literal-required]
    configuration: ConnectionConfiguration
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ConnectionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ConnectionDict, self.model_dump(by_alias=True, exclude_none=True))


ConnectionConfiguration = typing_extensions.Annotated[
    typing.Union[
        "S3ConnectionConfiguration", "RestConnectionConfiguration", "JdbcConnectionConfiguration"
    ],
    pydantic.Field(discriminator="type"),
]
"""ConnectionConfiguration"""


ConnectionConfigurationDict = typing_extensions.Annotated[
    typing.Union[
        "S3ConnectionConfigurationDict",
        "RestConnectionConfigurationDict",
        "JdbcConnectionConfigurationDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""ConnectionConfiguration"""


class ConnectionDict(typing_extensions.TypedDict):
    """Connection"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ConnectionRid
    parentFolderRid: filesystem_models.FolderRid
    displayName: ConnectionDisplayName
    """The display name of the Connection. The display name must not be blank."""

    runtimePlatform: RuntimePlatformDict
    configuration: ConnectionConfigurationDict


ConnectionDisplayName = str
"""The display name of the Connection. The display name must not be blank."""


ConnectionRid = core.RID
"""The Resource Identifier (RID) of a Connection (also known as a source)."""


class CreateConnectionRequestAgentProxyRuntime(pydantic.BaseModel):
    """CreateConnectionRequestAgentProxyRuntime"""

    agent_rids: typing.List[AgentRid] = pydantic.Field(alias=str("agentRids"))  # type: ignore[literal-required]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: typing.Literal["agentProxyRuntime"] = "agentProxyRuntime"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateConnectionRequestAgentProxyRuntimeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateConnectionRequestAgentProxyRuntimeDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateConnectionRequestAgentProxyRuntimeDict(typing_extensions.TypedDict):
    """CreateConnectionRequestAgentProxyRuntime"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRids: typing.List[AgentRid]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: typing.Literal["agentProxyRuntime"]


class CreateConnectionRequestAgentWorkerRuntime(pydantic.BaseModel):
    """CreateConnectionRequestAgentWorkerRuntime"""

    agent_rids: typing.List[AgentRid] = pydantic.Field(alias=str("agentRids"))  # type: ignore[literal-required]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: typing.Literal["agentWorkerRuntime"] = "agentWorkerRuntime"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateConnectionRequestAgentWorkerRuntimeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateConnectionRequestAgentWorkerRuntimeDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateConnectionRequestAgentWorkerRuntimeDict(typing_extensions.TypedDict):
    """CreateConnectionRequestAgentWorkerRuntime"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRids: typing.List[AgentRid]
    """
    The RIDs of the [agents](/docs/foundry/data-connection/set-up-agent/) configured on the connection.
    These agents are used to provide network connectivity to the external systems or APIs configured on the
    connection.
    """

    type: typing.Literal["agentWorkerRuntime"]


CreateConnectionRequestConnectionConfiguration = typing_extensions.Annotated[
    typing.Union[
        "CreateConnectionRequestS3ConnectionConfiguration",
        "CreateConnectionRequestRestConnectionConfiguration",
        "CreateConnectionRequestJdbcConnectionConfiguration",
    ],
    pydantic.Field(discriminator="type"),
]
"""CreateConnectionRequestConnectionConfiguration"""


CreateConnectionRequestConnectionConfigurationDict = typing_extensions.Annotated[
    typing.Union[
        "CreateConnectionRequestS3ConnectionConfigurationDict",
        "CreateConnectionRequestRestConnectionConfigurationDict",
        "CreateConnectionRequestJdbcConnectionConfigurationDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""CreateConnectionRequestConnectionConfiguration"""


class CreateConnectionRequestDirectConnectionRuntime(pydantic.BaseModel):
    """CreateConnectionRequestDirectConnectionRuntime"""

    network_egress_policy_rids: typing.List[NetworkEgressPolicyRid] = pydantic.Field(alias=str("networkEgressPolicyRids"))  # type: ignore[literal-required]
    """
    The RIDs of the [network egress policies](/docs/foundry/administration/configure-egress/#network-egress-policies) 
    configured on the connection.
    These network egress policies represent the set of external destinations that the connection is allowed
    to egress to from a Foundry enrollment
    """

    type: typing.Literal["directConnectionRuntime"] = "directConnectionRuntime"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateConnectionRequestDirectConnectionRuntimeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateConnectionRequestDirectConnectionRuntimeDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateConnectionRequestDirectConnectionRuntimeDict(typing_extensions.TypedDict):
    """CreateConnectionRequestDirectConnectionRuntime"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    networkEgressPolicyRids: typing.List[NetworkEgressPolicyRid]
    """
    The RIDs of the [network egress policies](/docs/foundry/administration/configure-egress/#network-egress-policies) 
    configured on the connection.
    These network egress policies represent the set of external destinations that the connection is allowed
    to egress to from a Foundry enrollment
    """

    type: typing.Literal["directConnectionRuntime"]


class CreateConnectionRequestJdbcConnectionConfiguration(pydantic.BaseModel):
    """CreateConnectionRequestJdbcConnectionConfiguration"""

    credentials: typing.Optional[BasicCredentials] = None
    driver_class: str = pydantic.Field(alias=str("driverClass"))  # type: ignore[literal-required]
    """The fully-qualified driver class name that is used to connect to the database."""

    jdbc_properties: typing.Dict[str, str] = pydantic.Field(alias=str("jdbcProperties"))  # type: ignore[literal-required]
    """
    The list of [properties](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Properties.html) passed 
    to the JDBC driver to configure behavior. Refer to the documentation of your specific connection for additional 
    available JDBC properties to add to your connection configuration.
    """

    url: str
    """The URL that the JDBC driver uses to connect to a database."""

    type: typing.Literal["jdbc"] = "jdbc"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateConnectionRequestJdbcConnectionConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateConnectionRequestJdbcConnectionConfigurationDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateConnectionRequestJdbcConnectionConfigurationDict(typing_extensions.TypedDict):
    """CreateConnectionRequestJdbcConnectionConfiguration"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    credentials: typing_extensions.NotRequired[BasicCredentialsDict]
    driverClass: str
    """The fully-qualified driver class name that is used to connect to the database."""

    jdbcProperties: typing.Dict[str, str]
    """
    The list of [properties](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Properties.html) passed 
    to the JDBC driver to configure behavior. Refer to the documentation of your specific connection for additional 
    available JDBC properties to add to your connection configuration.
    """

    url: str
    """The URL that the JDBC driver uses to connect to a database."""

    type: typing.Literal["jdbc"]


class CreateConnectionRequestRestConnectionConfiguration(pydantic.BaseModel):
    """CreateConnectionRequestRestConnectionConfiguration"""

    additional_secrets: typing.Optional[RestConnectionAdditionalSecrets] = pydantic.Field(alias=str("additionalSecrets"), default=None)  # type: ignore[literal-required]
    """
    Additional secrets that can be referenced in code and webhook configurations.
    If not provided, no additional secrets will be created.
    """

    oauth2_client_rid: typing.Optional[core.RID] = pydantic.Field(alias=str("oauth2ClientRid"), default=None)  # type: ignore[literal-required]
    """
    The RID of the [Outbound application](/docs/foundry/administration/configure-outbound-applications) that is used to authenticate to the external system via OAuth2.
    Currently, a connection may use only one outbound application for OAuth 2.0 authentication.
    Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization.
    """

    domains: typing.List[Domain]
    """
    The domains that the connection is allowed to access.
    At least one domain must be specified.
    """

    type: typing.Literal["rest"] = "rest"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateConnectionRequestRestConnectionConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateConnectionRequestRestConnectionConfigurationDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateConnectionRequestRestConnectionConfigurationDict(typing_extensions.TypedDict):
    """CreateConnectionRequestRestConnectionConfiguration"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    additionalSecrets: typing_extensions.NotRequired[RestConnectionAdditionalSecretsDict]
    """
    Additional secrets that can be referenced in code and webhook configurations.
    If not provided, no additional secrets will be created.
    """

    oauth2ClientRid: typing_extensions.NotRequired[core.RID]
    """
    The RID of the [Outbound application](/docs/foundry/administration/configure-outbound-applications) that is used to authenticate to the external system via OAuth2.
    Currently, a connection may use only one outbound application for OAuth 2.0 authentication.
    Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization.
    """

    domains: typing.List[DomainDict]
    """
    The domains that the connection is allowed to access.
    At least one domain must be specified.
    """

    type: typing.Literal["rest"]


CreateConnectionRequestRuntimePlatform = typing_extensions.Annotated[
    typing.Union[
        "CreateConnectionRequestDirectConnectionRuntime",
        "CreateConnectionRequestAgentProxyRuntime",
        "CreateConnectionRequestAgentWorkerRuntime",
    ],
    pydantic.Field(discriminator="type"),
]
"""
[The runtime of a Connection](/docs/foundry/data-connection/core-concepts/#runtimes), which defines the
networking configuration and where capabilities are executed.
"""


CreateConnectionRequestRuntimePlatformDict = typing_extensions.Annotated[
    typing.Union[
        "CreateConnectionRequestDirectConnectionRuntimeDict",
        "CreateConnectionRequestAgentProxyRuntimeDict",
        "CreateConnectionRequestAgentWorkerRuntimeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""
[The runtime of a Connection](/docs/foundry/data-connection/core-concepts/#runtimes), which defines the
networking configuration and where capabilities are executed.
"""


class CreateConnectionRequestS3ConnectionConfiguration(pydantic.BaseModel):
    """CreateConnectionRequestS3ConnectionConfiguration"""

    connection_timeout_millis: typing.Optional[core.Long] = pydantic.Field(alias=str("connectionTimeoutMillis"), default=None)  # type: ignore[literal-required]
    """
    The amount of time (in milliseconds) to wait when initially establishing a connection before giving up and timing out.
    If not specified, defaults to 10000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_CONNECTION_TIMEOUT).
    """

    max_error_retry: typing.Optional[int] = pydantic.Field(alias=str("maxErrorRetry"), default=None)  # type: ignore[literal-required]
    """
    The maximum number of retry attempts for failed requests to the S3 service.
    If not specified, defaults to 3 as defined by the [AWS SDK default](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html#retry-strategies).
    """

    bucket_url: str = pydantic.Field(alias=str("bucketUrl"))  # type: ignore[literal-required]
    """The URL of the S3 bucket. The URL should contain a trailing slash."""

    client_kms_configuration: typing.Optional[S3KmsConfiguration] = pydantic.Field(alias=str("clientKmsConfiguration"), default=None)  # type: ignore[literal-required]
    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    match_subfolder_exactly: typing.Optional[bool] = pydantic.Field(alias=str("matchSubfolderExactly"), default=None)  # type: ignore[literal-required]
    """
    If true, only files in the subfolder specified in the bucket URL will be synced.
    If false, all files in the bucket will be synced.
    If not specified, defaults to false.
    """

    sts_role_configuration: typing.Optional[StsRoleConfiguration] = pydantic.Field(alias=str("stsRoleConfiguration"), default=None)  # type: ignore[literal-required]
    """The configuration needed to assume a role to connect to the S3 external system."""

    s3_endpoint: typing.Optional[str] = pydantic.Field(alias=str("s3Endpoint"), default=None)  # type: ignore[literal-required]
    """
    The endpoint of the S3 service. This is used to connect to a custom S3 service that is not AWS S3.
    If not specified, defaults to the [AWS S3 endpoint](https://docs.aws.amazon.com/general/latest/gr/s3.html).
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    socket_timeout_millis: typing.Optional[core.Long] = pydantic.Field(alias=str("socketTimeoutMillis"), default=None)  # type: ignore[literal-required]
    """
    The amount of time (in milliseconds) to wait for data to be transferred over an established, open connection.
    If not specified, defaults to 50000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_SOCKET_TIMEOUT).
    """

    enable_requester_pays: typing.Optional[bool] = pydantic.Field(alias=str("enableRequesterPays"), default=None)  # type: ignore[literal-required]
    """
    Defaults to false, unless set and overwritten.
    If true, includes the [requester pays header](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html)
    in requests, allowing reads from requester pays buckets.
    """

    s3_endpoint_signing_region: typing.Optional[Region] = pydantic.Field(alias=str("s3EndpointSigningRegion"), default=None)  # type: ignore[literal-required]
    """
    The region used when constructing the S3 client using a custom endpoint.
    This is often not required and would only be needed if you are using the S3 connector with an S3-compliant third-party API,
    and are also setting a custom endpoint that requires a non-default region.
    """

    region: typing.Optional[Region] = None
    """
    The region representing the location of the S3 bucket.
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    authentication_mode: typing.Optional[S3AuthenticationMode] = pydantic.Field(alias=str("authenticationMode"), default=None)  # type: ignore[literal-required]
    """
    The authentication mode to use to connect to the S3 external system. No authentication mode is required
    to connect to publicly accessible AWS S3 buckets.
    """

    proxy_configuration: typing.Optional[S3ProxyConfiguration] = pydantic.Field(alias=str("proxyConfiguration"), default=None)  # type: ignore[literal-required]
    """The configuration needed to connect to the S3 external system through a proxy."""

    max_connections: typing.Optional[int] = pydantic.Field(alias=str("maxConnections"), default=None)  # type: ignore[literal-required]
    """
    The maximum number of HTTP connections to the S3 service per sync.
    If not specified, defaults to 50 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_MAX_CONNECTIONS).
    """

    type: typing.Literal["s3"] = "s3"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateConnectionRequestS3ConnectionConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateConnectionRequestS3ConnectionConfigurationDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateConnectionRequestS3ConnectionConfigurationDict(typing_extensions.TypedDict):
    """CreateConnectionRequestS3ConnectionConfiguration"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionTimeoutMillis: typing_extensions.NotRequired[core.Long]
    """
    The amount of time (in milliseconds) to wait when initially establishing a connection before giving up and timing out.
    If not specified, defaults to 10000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_CONNECTION_TIMEOUT).
    """

    maxErrorRetry: typing_extensions.NotRequired[int]
    """
    The maximum number of retry attempts for failed requests to the S3 service.
    If not specified, defaults to 3 as defined by the [AWS SDK default](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html#retry-strategies).
    """

    bucketUrl: str
    """The URL of the S3 bucket. The URL should contain a trailing slash."""

    clientKmsConfiguration: typing_extensions.NotRequired[S3KmsConfigurationDict]
    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    matchSubfolderExactly: typing_extensions.NotRequired[bool]
    """
    If true, only files in the subfolder specified in the bucket URL will be synced.
    If false, all files in the bucket will be synced.
    If not specified, defaults to false.
    """

    stsRoleConfiguration: typing_extensions.NotRequired[StsRoleConfigurationDict]
    """The configuration needed to assume a role to connect to the S3 external system."""

    s3Endpoint: typing_extensions.NotRequired[str]
    """
    The endpoint of the S3 service. This is used to connect to a custom S3 service that is not AWS S3.
    If not specified, defaults to the [AWS S3 endpoint](https://docs.aws.amazon.com/general/latest/gr/s3.html).
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    socketTimeoutMillis: typing_extensions.NotRequired[core.Long]
    """
    The amount of time (in milliseconds) to wait for data to be transferred over an established, open connection.
    If not specified, defaults to 50000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_SOCKET_TIMEOUT).
    """

    enableRequesterPays: typing_extensions.NotRequired[bool]
    """
    Defaults to false, unless set and overwritten.
    If true, includes the [requester pays header](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html)
    in requests, allowing reads from requester pays buckets.
    """

    s3EndpointSigningRegion: typing_extensions.NotRequired[Region]
    """
    The region used when constructing the S3 client using a custom endpoint.
    This is often not required and would only be needed if you are using the S3 connector with an S3-compliant third-party API,
    and are also setting a custom endpoint that requires a non-default region.
    """

    region: typing_extensions.NotRequired[Region]
    """
    The region representing the location of the S3 bucket.
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    authenticationMode: typing_extensions.NotRequired[S3AuthenticationModeDict]
    """
    The authentication mode to use to connect to the S3 external system. No authentication mode is required
    to connect to publicly accessible AWS S3 buckets.
    """

    proxyConfiguration: typing_extensions.NotRequired[S3ProxyConfigurationDict]
    """The configuration needed to connect to the S3 external system through a proxy."""

    maxConnections: typing_extensions.NotRequired[int]
    """
    The maximum number of HTTP connections to the S3 service per sync.
    If not specified, defaults to 50 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_MAX_CONNECTIONS).
    """

    type: typing.Literal["s3"]


class CreateTableImportRequestJdbcImportConfig(pydantic.BaseModel):
    """CreateTableImportRequestJdbcImportConfig"""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["jdbcImportConfig"] = "jdbcImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateTableImportRequestJdbcImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateTableImportRequestJdbcImportConfigDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateTableImportRequestJdbcImportConfigDict(typing_extensions.TypedDict):
    """CreateTableImportRequestJdbcImportConfig"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["jdbcImportConfig"]


class CreateTableImportRequestMicrosoftAccessImportConfig(pydantic.BaseModel):
    """CreateTableImportRequestMicrosoftAccessImportConfig"""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["microsoftAccessImportConfig"] = "microsoftAccessImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateTableImportRequestMicrosoftAccessImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateTableImportRequestMicrosoftAccessImportConfigDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateTableImportRequestMicrosoftAccessImportConfigDict(typing_extensions.TypedDict):
    """CreateTableImportRequestMicrosoftAccessImportConfig"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["microsoftAccessImportConfig"]


class CreateTableImportRequestMicrosoftSqlServerImportConfig(pydantic.BaseModel):
    """CreateTableImportRequestMicrosoftSqlServerImportConfig"""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["microsoftSqlServerImportConfig"] = "microsoftSqlServerImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateTableImportRequestMicrosoftSqlServerImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateTableImportRequestMicrosoftSqlServerImportConfigDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateTableImportRequestMicrosoftSqlServerImportConfigDict(typing_extensions.TypedDict):
    """CreateTableImportRequestMicrosoftSqlServerImportConfig"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["microsoftSqlServerImportConfig"]


class CreateTableImportRequestOracleImportConfig(pydantic.BaseModel):
    """CreateTableImportRequestOracleImportConfig"""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["oracleImportConfig"] = "oracleImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateTableImportRequestOracleImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateTableImportRequestOracleImportConfigDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateTableImportRequestOracleImportConfigDict(typing_extensions.TypedDict):
    """CreateTableImportRequestOracleImportConfig"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["oracleImportConfig"]


class CreateTableImportRequestPostgreSqlImportConfig(pydantic.BaseModel):
    """CreateTableImportRequestPostgreSqlImportConfig"""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["postgreSqlImportConfig"] = "postgreSqlImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateTableImportRequestPostgreSqlImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateTableImportRequestPostgreSqlImportConfigDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateTableImportRequestPostgreSqlImportConfigDict(typing_extensions.TypedDict):
    """CreateTableImportRequestPostgreSqlImportConfig"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["postgreSqlImportConfig"]


CreateTableImportRequestTableImportConfig = typing_extensions.Annotated[
    typing.Union[
        "CreateTableImportRequestJdbcImportConfig",
        "CreateTableImportRequestMicrosoftSqlServerImportConfig",
        "CreateTableImportRequestPostgreSqlImportConfig",
        "CreateTableImportRequestMicrosoftAccessImportConfig",
        "CreateTableImportRequestOracleImportConfig",
    ],
    pydantic.Field(discriminator="type"),
]
"""The import configuration for a specific [connector type](docs/foundry/data-integration/source-type-overview)."""


CreateTableImportRequestTableImportConfigDict = typing_extensions.Annotated[
    typing.Union[
        "CreateTableImportRequestJdbcImportConfigDict",
        "CreateTableImportRequestMicrosoftSqlServerImportConfigDict",
        "CreateTableImportRequestPostgreSqlImportConfigDict",
        "CreateTableImportRequestMicrosoftAccessImportConfigDict",
        "CreateTableImportRequestOracleImportConfigDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""The import configuration for a specific [connector type](docs/foundry/data-integration/source-type-overview)."""


class DirectConnectionRuntime(pydantic.BaseModel):
    """
    [Direct connections](/docs/foundry/data-connection/core-concepts/#direct-connection) enable users to connect
    to data sources accessible over the Internet without needing to set up an agent. If your Foundry stack is
    hosted on-premises, you can also connect to data sources within your on-premises network.

    This is the preferred source connection method if the data source is accessible over the Internet.
    """

    network_egress_policy_rids: typing.List[NetworkEgressPolicyRid] = pydantic.Field(alias=str("networkEgressPolicyRids"))  # type: ignore[literal-required]
    """
    The RIDs of the [network egress policies](/docs/foundry/administration/configure-egress/#network-egress-policies) 
    configured on the connection.
    These network egress policies represent the set of external destinations that the connection is allowed
    to egress to from a Foundry enrollment
    """

    type: typing.Literal["directConnectionRuntime"] = "directConnectionRuntime"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DirectConnectionRuntimeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            DirectConnectionRuntimeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class DirectConnectionRuntimeDict(typing_extensions.TypedDict):
    """
    [Direct connections](/docs/foundry/data-connection/core-concepts/#direct-connection) enable users to connect
    to data sources accessible over the Internet without needing to set up an agent. If your Foundry stack is
    hosted on-premises, you can also connect to data sources within your on-premises network.

    This is the preferred source connection method if the data source is accessible over the Internet.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    networkEgressPolicyRids: typing.List[NetworkEgressPolicyRid]
    """
    The RIDs of the [network egress policies](/docs/foundry/administration/configure-egress/#network-egress-policies) 
    configured on the connection.
    These network egress policies represent the set of external destinations that the connection is allowed
    to egress to from a Foundry enrollment
    """

    type: typing.Literal["directConnectionRuntime"]


class Domain(pydantic.BaseModel):
    """The domain that the connection is allowed to access."""

    scheme: typing.Optional[UriScheme] = None
    """
    The scheme of the domain that the connection is allowed to access.
    If not specified, defaults to HTTPS.
    """

    host: str
    """The domain name, IPv4, or IPv6 address."""

    port: typing.Optional[int] = None
    """The port number of the domain that the connection is allowed to access."""

    auth: typing.Optional[RestAuthenticationMode] = None
    """
    The URI scheme must be HTTPS if using any authentication.
    If not specified, no authentication is required.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DomainDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DomainDict, self.model_dump(by_alias=True, exclude_none=True))


class DomainDict(typing_extensions.TypedDict):
    """The domain that the connection is allowed to access."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    scheme: typing_extensions.NotRequired[UriScheme]
    """
    The scheme of the domain that the connection is allowed to access.
    If not specified, defaults to HTTPS.
    """

    host: str
    """The domain name, IPv4, or IPv6 address."""

    port: typing_extensions.NotRequired[int]
    """The port number of the domain that the connection is allowed to access."""

    auth: typing_extensions.NotRequired[RestAuthenticationModeDict]
    """
    The URI scheme must be HTTPS if using any authentication.
    If not specified, no authentication is required.
    """


EncryptedProperty = typing_extensions.Annotated[
    typing.Union["AsSecretName", "AsPlaintextValue"], pydantic.Field(discriminator="type")
]
"""
When reading an encrypted property, the secret name representing the encrypted value will be returned.
When writing to an encrypted property:
- If a plaintext value is passed as an input, the plaintext value will be encrypted and saved to the property.
- If a secret name is passed as an input, the secret name must match the existing secret name of the property
  and the property will retain its previously encrypted value.
"""


EncryptedPropertyDict = typing_extensions.Annotated[
    typing.Union["AsSecretNameDict", "AsPlaintextValueDict"], pydantic.Field(discriminator="type")
]
"""
When reading an encrypted property, the secret name representing the encrypted value will be returned.
When writing to an encrypted property:
- If a plaintext value is passed as an input, the plaintext value will be encrypted and saved to the property.
- If a secret name is passed as an input, the secret name must match the existing secret name of the property
  and the property will retain its previously encrypted value.
"""


class FileAnyPathMatchesFilter(pydantic.BaseModel):
    """If any file has a relative path matching the regular expression, sync all files in the subfolder that are not otherwise filtered."""

    regex: str
    """The regular expression for the relative path to match against."""

    type: typing.Literal["anyPathMatchesFilter"] = "anyPathMatchesFilter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FileAnyPathMatchesFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FileAnyPathMatchesFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FileAnyPathMatchesFilterDict(typing_extensions.TypedDict):
    """If any file has a relative path matching the regular expression, sync all files in the subfolder that are not otherwise filtered."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    regex: str
    """The regular expression for the relative path to match against."""

    type: typing.Literal["anyPathMatchesFilter"]


class FileAtLeastCountFilter(pydantic.BaseModel):
    """Import all filtered files only if there are at least the specified number of files remaining."""

    min_files_count: int = pydantic.Field(alias=str("minFilesCount"))  # type: ignore[literal-required]
    """
    The minimum number of files remaining expected.
    The value specified must be greater than 0.
    """

    type: typing.Literal["atLeastCountFilter"] = "atLeastCountFilter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FileAtLeastCountFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FileAtLeastCountFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FileAtLeastCountFilterDict(typing_extensions.TypedDict):
    """Import all filtered files only if there are at least the specified number of files remaining."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    minFilesCount: int
    """
    The minimum number of files remaining expected.
    The value specified must be greater than 0.
    """

    type: typing.Literal["atLeastCountFilter"]


class FileChangedSinceLastUploadFilter(pydantic.BaseModel):
    """
    Only import files that have changed or been added since the last import run. Whether or not a file is considered to be changed is determined by the specified file properties.
    This will exclude files uploaded in any previous imports, regardless of the file import mode used. A SNAPSHOT file import mode does not reset the filter.
    """

    file_properties: typing.List[FileProperty] = pydantic.Field(alias=str("fileProperties"))  # type: ignore[literal-required]
    """
    The criteria on which to determine whether a file has been changed or not since the last import. 
    If any of the specified criteria have changed, the file is consider changed. The criteria include:

    LAST_MODIFIED: The file's last modified timestamp has changed since the last import.
    SIZE: The file's size has changed since the last import.

    If no criteria are specified, only newly added files will be imported.
    """

    type: typing.Literal["changedSinceLastUploadFilter"] = "changedSinceLastUploadFilter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FileChangedSinceLastUploadFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FileChangedSinceLastUploadFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FileChangedSinceLastUploadFilterDict(typing_extensions.TypedDict):
    """
    Only import files that have changed or been added since the last import run. Whether or not a file is considered to be changed is determined by the specified file properties.
    This will exclude files uploaded in any previous imports, regardless of the file import mode used. A SNAPSHOT file import mode does not reset the filter.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileProperties: typing.List[FileProperty]
    """
    The criteria on which to determine whether a file has been changed or not since the last import. 
    If any of the specified criteria have changed, the file is consider changed. The criteria include:

    LAST_MODIFIED: The file's last modified timestamp has changed since the last import.
    SIZE: The file's size has changed since the last import.

    If no criteria are specified, only newly added files will be imported.
    """

    type: typing.Literal["changedSinceLastUploadFilter"]


class FileImport(pydantic.BaseModel):
    """FileImport"""

    rid: FileImportRid
    connection_rid: ConnectionRid = pydantic.Field(alias=str("connectionRid"))  # type: ignore[literal-required]
    """The RID of the Connection (also known as a source) that the File Import uses to import data."""

    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the output dataset."""

    branch_name: typing.Optional[datasets_models.BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]
    """The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments."""

    display_name: FileImportDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    file_import_filters: typing.List[FileImportFilter] = pydantic.Field(alias=str("fileImportFilters"))  # type: ignore[literal-required]
    """Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)"""

    import_mode: FileImportMode = pydantic.Field(alias=str("importMode"))  # type: ignore[literal-required]
    subfolder: typing.Optional[str] = None
    """A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FileImportDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FileImportDict, self.model_dump(by_alias=True, exclude_none=True))


class FileImportCustomFilter(pydantic.BaseModel):
    """
    A custom file import filter. Custom file import filters can be fetched but cannot currently be used
    when creating or updating file imports.
    """

    config: typing.Any
    type: typing.Literal["customFilter"] = "customFilter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FileImportCustomFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FileImportCustomFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FileImportCustomFilterDict(typing_extensions.TypedDict):
    """
    A custom file import filter. Custom file import filters can be fetched but cannot currently be used
    when creating or updating file imports.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    config: typing.Any
    type: typing.Literal["customFilter"]


class FileImportDict(typing_extensions.TypedDict):
    """FileImport"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: FileImportRid
    connectionRid: ConnectionRid
    """The RID of the Connection (also known as a source) that the File Import uses to import data."""

    datasetRid: datasets_models.DatasetRid
    """The RID of the output dataset."""

    branchName: typing_extensions.NotRequired[datasets_models.BranchName]
    """The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments."""

    displayName: FileImportDisplayName
    fileImportFilters: typing.List[FileImportFilterDict]
    """Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)"""

    importMode: FileImportMode
    subfolder: typing_extensions.NotRequired[str]
    """A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system."""


FileImportDisplayName = str
"""FileImportDisplayName"""


FileImportFilter = typing_extensions.Annotated[
    typing.Union[
        "FilePathNotMatchesFilter",
        "FileAnyPathMatchesFilter",
        "FilesCountLimitFilter",
        "FileChangedSinceLastUploadFilter",
        "FileImportCustomFilter",
        "FileLastModifiedAfterFilter",
        "FilePathMatchesFilter",
        "FileAtLeastCountFilter",
        "FileSizeFilter",
    ],
    pydantic.Field(discriminator="type"),
]
"""
[Filters](/docs/foundry/data-connection/file-based-syncs/#filters) allow you to filter source files
before they are imported into Foundry.
"""


FileImportFilterDict = typing_extensions.Annotated[
    typing.Union[
        "FilePathNotMatchesFilterDict",
        "FileAnyPathMatchesFilterDict",
        "FilesCountLimitFilterDict",
        "FileChangedSinceLastUploadFilterDict",
        "FileImportCustomFilterDict",
        "FileLastModifiedAfterFilterDict",
        "FilePathMatchesFilterDict",
        "FileAtLeastCountFilterDict",
        "FileSizeFilterDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""
[Filters](/docs/foundry/data-connection/file-based-syncs/#filters) allow you to filter source files
before they are imported into Foundry.
"""


FileImportMode = typing.Literal["SNAPSHOT", "APPEND", "UPDATE"]
"""
Import mode governs how raw files are read from an external system, and written into a Foundry dataset. 

SNAPSHOT: Defines a new dataset state consisting only of files from a particular import execution.
APPEND: Purely additive and yields data from previous import executions in addition to newly added files.
UPDATE: Replaces existing files from previous import executions based on file names.
"""


FileImportRid = core.RID
"""The Resource Identifier (RID) of a FileImport (also known as a batch sync)."""


class FileLastModifiedAfterFilter(pydantic.BaseModel):
    """Only import files that have been modified after a specified timestamp"""

    after_timestamp: typing.Optional[datetime] = pydantic.Field(alias=str("afterTimestamp"), default=None)  # type: ignore[literal-required]
    """
    Timestamp threshold, specified in ISO-8601 format.
    If not specified, defaults to the timestamp the filter is added to the file import.
    """

    type: typing.Literal["lastModifiedAfterFilter"] = "lastModifiedAfterFilter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FileLastModifiedAfterFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FileLastModifiedAfterFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FileLastModifiedAfterFilterDict(typing_extensions.TypedDict):
    """Only import files that have been modified after a specified timestamp"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    afterTimestamp: typing_extensions.NotRequired[datetime]
    """
    Timestamp threshold, specified in ISO-8601 format.
    If not specified, defaults to the timestamp the filter is added to the file import.
    """

    type: typing.Literal["lastModifiedAfterFilter"]


class FilePathMatchesFilter(pydantic.BaseModel):
    """
    Only import files whose path (relative to the root of the source) matches the regular expression.

    **Example**
    Suppose we are importing files from `relative/subfolder`.
    `relative/subfolder` contains:
    - `relative/subfolder/include-file.txt`
    - `relative/subfolder/exclude-file.txt`
    - `relative/subfolder/other-file.txt`

    With the `relative/subfolder/include-.*.txt` regex, only `relative/subfolder/include-file.txt` will be imported.
    """

    regex: str
    """Must be written to match the paths relative to the root of the source, even if a subfolder is specified."""

    type: typing.Literal["pathMatchesFilter"] = "pathMatchesFilter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FilePathMatchesFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FilePathMatchesFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FilePathMatchesFilterDict(typing_extensions.TypedDict):
    """
    Only import files whose path (relative to the root of the source) matches the regular expression.

    **Example**
    Suppose we are importing files from `relative/subfolder`.
    `relative/subfolder` contains:
    - `relative/subfolder/include-file.txt`
    - `relative/subfolder/exclude-file.txt`
    - `relative/subfolder/other-file.txt`

    With the `relative/subfolder/include-.*.txt` regex, only `relative/subfolder/include-file.txt` will be imported.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    regex: str
    """Must be written to match the paths relative to the root of the source, even if a subfolder is specified."""

    type: typing.Literal["pathMatchesFilter"]


class FilePathNotMatchesFilter(pydantic.BaseModel):
    """
    Only import files whose path (relative to the root of the source) does not match the regular expression.

    **Example**
    Suppose we are importing files from `relative/subfolder`.
    `relative/subfolder` contains:
    - `relative/subfolder/include-file.txt`
    - `relative/subfolder/exclude-file.txt`
    - `relative/subfolder/other-file.txt`

    With the `relative/subfolder/exclude-.*.txt` regex, both `relative/subfolder/include-file.txt` and `relative/subfolder/other-file.txt` will be imported,
    and `relative/subfolder/exclude-file.txt` will be excluded from the import.
    """

    regex: str
    """Must be written to match the paths relative to the root of the source, even if a subfolder is specified."""

    type: typing.Literal["pathNotMatchesFilter"] = "pathNotMatchesFilter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FilePathNotMatchesFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FilePathNotMatchesFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FilePathNotMatchesFilterDict(typing_extensions.TypedDict):
    """
    Only import files whose path (relative to the root of the source) does not match the regular expression.

    **Example**
    Suppose we are importing files from `relative/subfolder`.
    `relative/subfolder` contains:
    - `relative/subfolder/include-file.txt`
    - `relative/subfolder/exclude-file.txt`
    - `relative/subfolder/other-file.txt`

    With the `relative/subfolder/exclude-.*.txt` regex, both `relative/subfolder/include-file.txt` and `relative/subfolder/other-file.txt` will be imported,
    and `relative/subfolder/exclude-file.txt` will be excluded from the import.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    regex: str
    """Must be written to match the paths relative to the root of the source, even if a subfolder is specified."""

    type: typing.Literal["pathNotMatchesFilter"]


FileProperty = typing.Literal["LAST_MODIFIED", "SIZE"]
"""FileProperty"""


class FileSizeFilter(pydantic.BaseModel):
    """
    Only import files whose size is between the specified minimum and maximum values.
    At least one of `gt` or `lt` should be present.
    If both are present, the value specified for `gt` must be strictly less than `lt - 1`.
    """

    gt: typing.Optional[core_models.SizeBytes] = None
    """
    File size must be greater than this number for it to be imported.
    The value specified cannot be a negative number.
    """

    lt: typing.Optional[core_models.SizeBytes] = None
    """
    File size must be less than this number for it to be imported.
    The value specified must be at least 1 byte.
    """

    type: typing.Literal["fileSizeFilter"] = "fileSizeFilter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FileSizeFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FileSizeFilterDict, self.model_dump(by_alias=True, exclude_none=True))


class FileSizeFilterDict(typing_extensions.TypedDict):
    """
    Only import files whose size is between the specified minimum and maximum values.
    At least one of `gt` or `lt` should be present.
    If both are present, the value specified for `gt` must be strictly less than `lt - 1`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    gt: typing_extensions.NotRequired[core_models.SizeBytes]
    """
    File size must be greater than this number for it to be imported.
    The value specified cannot be a negative number.
    """

    lt: typing_extensions.NotRequired[core_models.SizeBytes]
    """
    File size must be less than this number for it to be imported.
    The value specified must be at least 1 byte.
    """

    type: typing.Literal["fileSizeFilter"]


class FilesCountLimitFilter(pydantic.BaseModel):
    """
    Only retain `filesCount` number of files in each transaction.
    The choice of files to retain is made without any guarantee of order.
    This option can increase the reliability of incremental syncs.
    """

    files_count: int = pydantic.Field(alias=str("filesCount"))  # type: ignore[literal-required]
    """The number of files to import in the transaction. The value specified must be positive."""

    type: typing.Literal["filesCountLimitFilter"] = "filesCountLimitFilter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FilesCountLimitFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            FilesCountLimitFilterDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class FilesCountLimitFilterDict(typing_extensions.TypedDict):
    """
    Only retain `filesCount` number of files in each transaction.
    The choice of files to retain is made without any guarantee of order.
    This option can increase the reliability of incremental syncs.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    filesCount: int
    """The number of files to import in the transaction. The value specified must be positive."""

    type: typing.Literal["filesCountLimitFilter"]


class HeaderApiKey(pydantic.BaseModel):
    """HeaderApiKey"""

    header_name: str = pydantic.Field(alias=str("headerName"))  # type: ignore[literal-required]
    """The name of the header that the API key is passed in."""

    type: typing.Literal["header"] = "header"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "HeaderApiKeyDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(HeaderApiKeyDict, self.model_dump(by_alias=True, exclude_none=True))


class HeaderApiKeyDict(typing_extensions.TypedDict):
    """HeaderApiKey"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    headerName: str
    """The name of the header that the API key is passed in."""

    type: typing.Literal["header"]


class JdbcConnectionConfiguration(pydantic.BaseModel):
    """The configuration needed to connect to an external system using the JDBC protocol."""

    url: str
    """The URL that the JDBC driver uses to connect to a database."""

    driver_class: str = pydantic.Field(alias=str("driverClass"))  # type: ignore[literal-required]
    """The fully-qualified driver class name that is used to connect to the database."""

    jdbc_properties: typing.Dict[str, str] = pydantic.Field(alias=str("jdbcProperties"))  # type: ignore[literal-required]
    """
    The list of [properties](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Properties.html) passed 
    to the JDBC driver to configure behavior. Refer to the documentation of your specific connection for additional 
    available JDBC properties to add to your connection configuration.
    """

    credentials: typing.Optional[BasicCredentials] = None
    type: typing.Literal["jdbc"] = "jdbc"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "JdbcConnectionConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            JdbcConnectionConfigurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class JdbcConnectionConfigurationDict(typing_extensions.TypedDict):
    """The configuration needed to connect to an external system using the JDBC protocol."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    url: str
    """The URL that the JDBC driver uses to connect to a database."""

    driverClass: str
    """The fully-qualified driver class name that is used to connect to the database."""

    jdbcProperties: typing.Dict[str, str]
    """
    The list of [properties](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Properties.html) passed 
    to the JDBC driver to configure behavior. Refer to the documentation of your specific connection for additional 
    available JDBC properties to add to your connection configuration.
    """

    credentials: typing_extensions.NotRequired[BasicCredentialsDict]
    type: typing.Literal["jdbc"]


class JdbcImportConfig(pydantic.BaseModel):
    """The import configuration for a [custom JDBC connection](docs/foundry/available-connectors/custom-jdbc-sources)."""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["jdbcImportConfig"] = "jdbcImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "JdbcImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(JdbcImportConfigDict, self.model_dump(by_alias=True, exclude_none=True))


class JdbcImportConfigDict(typing_extensions.TypedDict):
    """The import configuration for a [custom JDBC connection](docs/foundry/available-connectors/custom-jdbc-sources)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["jdbcImportConfig"]


class ListFileImportsResponse(pydantic.BaseModel):
    """ListFileImportsResponse"""

    data: typing.List[FileImport]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListFileImportsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListFileImportsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListFileImportsResponseDict(typing_extensions.TypedDict):
    """ListFileImportsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[FileImportDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListTableImportsResponse(pydantic.BaseModel):
    """ListTableImportsResponse"""

    data: typing.List[TableImport]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListTableImportsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListTableImportsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListTableImportsResponseDict(typing_extensions.TypedDict):
    """ListTableImportsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[TableImportDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class MicrosoftAccessImportConfig(pydantic.BaseModel):
    """The import configuration for a [Microsoft Access connection](docs/foundry/available-connectors/microsoft-access)."""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["microsoftAccessImportConfig"] = "microsoftAccessImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MicrosoftAccessImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            MicrosoftAccessImportConfigDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class MicrosoftAccessImportConfigDict(typing_extensions.TypedDict):
    """The import configuration for a [Microsoft Access connection](docs/foundry/available-connectors/microsoft-access)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["microsoftAccessImportConfig"]


class MicrosoftSqlServerImportConfig(pydantic.BaseModel):
    """The import configuration for a [Microsoft SQL Server connection](docs/foundry/available-connectors/microsoft-sql-server)."""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["microsoftSqlServerImportConfig"] = "microsoftSqlServerImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MicrosoftSqlServerImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            MicrosoftSqlServerImportConfigDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class MicrosoftSqlServerImportConfigDict(typing_extensions.TypedDict):
    """The import configuration for a [Microsoft SQL Server connection](docs/foundry/available-connectors/microsoft-sql-server)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["microsoftSqlServerImportConfig"]


NetworkEgressPolicyRid = core.RID
"""The Resource Identifier (RID) of a Network Egress Policy."""


class Oidc(pydantic.BaseModel):
    """
    [OpenID Connect (OIDC)](/docs/foundry/data-connection/oidc/) is an open authentication protocol that allows
    you to authenticate to external system resources without the use of static credentials.
    """

    audience: str
    """The configured audience that identifies the external system."""

    issuer_url: str = pydantic.Field(alias=str("issuerUrl"))  # type: ignore[literal-required]
    """The URL that identifies Foundry as an OIDC identity provider."""

    subject: ConnectionRid
    """The RID of the Connection that is connecting to the external system."""

    type: typing.Literal["oidc"] = "oidc"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OidcDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OidcDict, self.model_dump(by_alias=True, exclude_none=True))


class OidcDict(typing_extensions.TypedDict):
    """
    [OpenID Connect (OIDC)](/docs/foundry/data-connection/oidc/) is an open authentication protocol that allows
    you to authenticate to external system resources without the use of static credentials.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    audience: str
    """The configured audience that identifies the external system."""

    issuerUrl: str
    """The URL that identifies Foundry as an OIDC identity provider."""

    subject: ConnectionRid
    """The RID of the Connection that is connecting to the external system."""

    type: typing.Literal["oidc"]


class OracleImportConfig(pydantic.BaseModel):
    """The import configuration for an Oracle Database 21 connection."""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["oracleImportConfig"] = "oracleImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OracleImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OracleImportConfigDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OracleImportConfigDict(typing_extensions.TypedDict):
    """The import configuration for an Oracle Database 21 connection."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["oracleImportConfig"]


PlaintextValue = str
"""PlaintextValue"""


class PostgreSqlImportConfig(pydantic.BaseModel):
    """The import configuration for a [PostgreSQL connection](docs/foundry/available-connectors/postgresql)."""

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["postgreSqlImportConfig"] = "postgreSqlImportConfig"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "PostgreSqlImportConfigDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            PostgreSqlImportConfigDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class PostgreSqlImportConfigDict(typing_extensions.TypedDict):
    """The import configuration for a [PostgreSQL connection](docs/foundry/available-connectors/postgresql)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: str
    """
    A single SQL query can be executed per sync, which should output a data table 
    and avoid operations like invoking stored procedures. 
    The query results are saved to the output dataset in Foundry.
    """

    type: typing.Literal["postgreSqlImportConfig"]


Protocol = typing.Literal["HTTP", "HTTPS"]
"""Protocol to establish a connection with another system."""


class QueryParameterApiKey(pydantic.BaseModel):
    """QueryParameterApiKey"""

    query_parameter_name: str = pydantic.Field(alias=str("queryParameterName"))  # type: ignore[literal-required]
    """The name of the query parameter that the API key is passed in."""

    type: typing.Literal["queryParameter"] = "queryParameter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryParameterApiKeyDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            QueryParameterApiKeyDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class QueryParameterApiKeyDict(typing_extensions.TypedDict):
    """QueryParameterApiKey"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryParameterName: str
    """The name of the query parameter that the API key is passed in."""

    type: typing.Literal["queryParameter"]


Region = str
"""The region of the external system."""


RestAuthenticationMode = typing_extensions.Annotated[
    typing.Union["BearerToken", "ApiKeyAuthentication", "BasicCredentials", "RestConnectionOAuth2"],
    pydantic.Field(discriminator="type"),
]
"""The method of authentication for connecting to an external REST system."""


RestAuthenticationModeDict = typing_extensions.Annotated[
    typing.Union[
        "BearerTokenDict",
        "ApiKeyAuthenticationDict",
        "BasicCredentialsDict",
        "RestConnectionOAuth2Dict",
    ],
    pydantic.Field(discriminator="type"),
]
"""The method of authentication for connecting to an external REST system."""


RestConnectionAdditionalSecrets = typing_extensions.Annotated[
    typing.Union["SecretsWithPlaintextValues", "SecretsNames"], pydantic.Field(discriminator="type")
]
"""
When creating or updating additional secrets, use SecretsWithPlaintextValues.
When fetching the RestConnectionConfiguration, SecretsNames will be provided.
"""


RestConnectionAdditionalSecretsDict = typing_extensions.Annotated[
    typing.Union["SecretsWithPlaintextValuesDict", "SecretsNamesDict"],
    pydantic.Field(discriminator="type"),
]
"""
When creating or updating additional secrets, use SecretsWithPlaintextValues.
When fetching the RestConnectionConfiguration, SecretsNames will be provided.
"""


class RestConnectionConfiguration(pydantic.BaseModel):
    """The configuration needed to connect to a [REST external system](/docs/foundry/available-connectors/rest-apis)."""

    domains: typing.List[Domain]
    """
    The domains that the connection is allowed to access.
    At least one domain must be specified.
    """

    additional_secrets: typing.Optional[RestConnectionAdditionalSecrets] = pydantic.Field(alias=str("additionalSecrets"), default=None)  # type: ignore[literal-required]
    """
    Additional secrets that can be referenced in code and webhook configurations.
    If not provided, no additional secrets will be created.
    """

    oauth2_client_rid: typing.Optional[core.RID] = pydantic.Field(alias=str("oauth2ClientRid"), default=None)  # type: ignore[literal-required]
    """
    The RID of the [Outbound application](/docs/foundry/administration/configure-outbound-applications) that is used to authenticate to the external system via OAuth2.
    Currently, a connection may use only one outbound application for OAuth 2.0 authentication.
    Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization.
    """

    type: typing.Literal["rest"] = "rest"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "RestConnectionConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            RestConnectionConfigurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class RestConnectionConfigurationDict(typing_extensions.TypedDict):
    """The configuration needed to connect to a [REST external system](/docs/foundry/available-connectors/rest-apis)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    domains: typing.List[DomainDict]
    """
    The domains that the connection is allowed to access.
    At least one domain must be specified.
    """

    additionalSecrets: typing_extensions.NotRequired[RestConnectionAdditionalSecretsDict]
    """
    Additional secrets that can be referenced in code and webhook configurations.
    If not provided, no additional secrets will be created.
    """

    oauth2ClientRid: typing_extensions.NotRequired[core.RID]
    """
    The RID of the [Outbound application](/docs/foundry/administration/configure-outbound-applications) that is used to authenticate to the external system via OAuth2.
    Currently, a connection may use only one outbound application for OAuth 2.0 authentication.
    Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization.
    """

    type: typing.Literal["rest"]


class RestConnectionOAuth2(pydantic.BaseModel):
    """
    In order to use OAuth2 you must have an Outbound application configured in the [Foundry Control Panel Organization settings](/docs/foundry/administration/configure-outbound-applications#create-an-outbound-application).
    The RID of the Outbound application must be configured in the RestConnectionConfiguration in the `oauth2ClientRid` field.
    """

    type: typing.Literal["oauth2"] = "oauth2"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "RestConnectionOAuth2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            RestConnectionOAuth2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class RestConnectionOAuth2Dict(typing_extensions.TypedDict):
    """
    In order to use OAuth2 you must have an Outbound application configured in the [Foundry Control Panel Organization settings](/docs/foundry/administration/configure-outbound-applications#create-an-outbound-application).
    The RID of the Outbound application must be configured in the RestConnectionConfiguration in the `oauth2ClientRid` field.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["oauth2"]


RestRequestApiKeyLocation = typing_extensions.Annotated[
    typing.Union["HeaderApiKey", "QueryParameterApiKey"], pydantic.Field(discriminator="type")
]
"""The location of the API key in the request."""


RestRequestApiKeyLocationDict = typing_extensions.Annotated[
    typing.Union["HeaderApiKeyDict", "QueryParameterApiKeyDict"],
    pydantic.Field(discriminator="type"),
]
"""The location of the API key in the request."""


RuntimePlatform = typing_extensions.Annotated[
    typing.Union["DirectConnectionRuntime", "AgentProxyRuntime", "AgentWorkerRuntime"],
    pydantic.Field(discriminator="type"),
]
"""
[The runtime of a Connection](/docs/foundry/data-connection/core-concepts/#runtimes), which defines the
networking configuration and where capabilities are executed.
"""


RuntimePlatformDict = typing_extensions.Annotated[
    typing.Union["DirectConnectionRuntimeDict", "AgentProxyRuntimeDict", "AgentWorkerRuntimeDict"],
    pydantic.Field(discriminator="type"),
]
"""
[The runtime of a Connection](/docs/foundry/data-connection/core-concepts/#runtimes), which defines the
networking configuration and where capabilities are executed.
"""


S3AuthenticationMode = typing_extensions.Annotated[
    typing.Union["AwsAccessKey", "CloudIdentity", "Oidc"], pydantic.Field(discriminator="type")
]
"""S3AuthenticationMode"""


S3AuthenticationModeDict = typing_extensions.Annotated[
    typing.Union["AwsAccessKeyDict", "CloudIdentityDict", "OidcDict"],
    pydantic.Field(discriminator="type"),
]
"""S3AuthenticationMode"""


class S3ConnectionConfiguration(pydantic.BaseModel):
    """
    The configuration needed to connect to an [AWS S3 external system (or any other S3-like external systems that
    implement the s3a protocol)](/docs/foundry/available-connectors/amazon-s3/#amazon-s3).
    """

    bucket_url: str = pydantic.Field(alias=str("bucketUrl"))  # type: ignore[literal-required]
    """The URL of the S3 bucket. The URL should contain a trailing slash."""

    s3_endpoint: typing.Optional[str] = pydantic.Field(alias=str("s3Endpoint"), default=None)  # type: ignore[literal-required]
    """
    The endpoint of the S3 service. This is used to connect to a custom S3 service that is not AWS S3.
    If not specified, defaults to the [AWS S3 endpoint](https://docs.aws.amazon.com/general/latest/gr/s3.html).
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    region: typing.Optional[Region] = None
    """
    The region representing the location of the S3 bucket.
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    authentication_mode: typing.Optional[S3AuthenticationMode] = pydantic.Field(alias=str("authenticationMode"), default=None)  # type: ignore[literal-required]
    """
    The authentication mode to use to connect to the S3 external system. No authentication mode is required
    to connect to publicly accessible AWS S3 buckets.
    """

    s3_endpoint_signing_region: typing.Optional[Region] = pydantic.Field(alias=str("s3EndpointSigningRegion"), default=None)  # type: ignore[literal-required]
    """
    The region used when constructing the S3 client using a custom endpoint.
    This is often not required and would only be needed if you are using the S3 connector with an S3-compliant third-party API,
    and are also setting a custom endpoint that requires a non-default region.
    """

    client_kms_configuration: typing.Optional[S3KmsConfiguration] = pydantic.Field(alias=str("clientKmsConfiguration"), default=None)  # type: ignore[literal-required]
    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    sts_role_configuration: typing.Optional[StsRoleConfiguration] = pydantic.Field(alias=str("stsRoleConfiguration"), default=None)  # type: ignore[literal-required]
    """The configuration needed to assume a role to connect to the S3 external system."""

    proxy_configuration: typing.Optional[S3ProxyConfiguration] = pydantic.Field(alias=str("proxyConfiguration"), default=None)  # type: ignore[literal-required]
    """The configuration needed to connect to the S3 external system through a proxy."""

    max_connections: typing.Optional[int] = pydantic.Field(alias=str("maxConnections"), default=None)  # type: ignore[literal-required]
    """
    The maximum number of HTTP connections to the S3 service per sync.
    If not specified, defaults to 50 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_MAX_CONNECTIONS).
    """

    connection_timeout_millis: typing.Optional[core.Long] = pydantic.Field(alias=str("connectionTimeoutMillis"), default=None)  # type: ignore[literal-required]
    """
    The amount of time (in milliseconds) to wait when initially establishing a connection before giving up and timing out.
    If not specified, defaults to 10000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_CONNECTION_TIMEOUT).
    """

    socket_timeout_millis: typing.Optional[core.Long] = pydantic.Field(alias=str("socketTimeoutMillis"), default=None)  # type: ignore[literal-required]
    """
    The amount of time (in milliseconds) to wait for data to be transferred over an established, open connection.
    If not specified, defaults to 50000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_SOCKET_TIMEOUT).
    """

    max_error_retry: typing.Optional[int] = pydantic.Field(alias=str("maxErrorRetry"), default=None)  # type: ignore[literal-required]
    """
    The maximum number of retry attempts for failed requests to the S3 service.
    If not specified, defaults to 3 as defined by the [AWS SDK default](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html#retry-strategies).
    """

    match_subfolder_exactly: typing.Optional[bool] = pydantic.Field(alias=str("matchSubfolderExactly"), default=None)  # type: ignore[literal-required]
    """
    If true, only files in the subfolder specified in the bucket URL will be synced.
    If false, all files in the bucket will be synced.
    If not specified, defaults to false.
    """

    enable_requester_pays: typing.Optional[bool] = pydantic.Field(alias=str("enableRequesterPays"), default=None)  # type: ignore[literal-required]
    """
    Defaults to false, unless set and overwritten.
    If true, includes the [requester pays header](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html)
    in requests, allowing reads from requester pays buckets.
    """

    type: typing.Literal["s3"] = "s3"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "S3ConnectionConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            S3ConnectionConfigurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class S3ConnectionConfigurationDict(typing_extensions.TypedDict):
    """
    The configuration needed to connect to an [AWS S3 external system (or any other S3-like external systems that
    implement the s3a protocol)](/docs/foundry/available-connectors/amazon-s3/#amazon-s3).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    bucketUrl: str
    """The URL of the S3 bucket. The URL should contain a trailing slash."""

    s3Endpoint: typing_extensions.NotRequired[str]
    """
    The endpoint of the S3 service. This is used to connect to a custom S3 service that is not AWS S3.
    If not specified, defaults to the [AWS S3 endpoint](https://docs.aws.amazon.com/general/latest/gr/s3.html).
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    region: typing_extensions.NotRequired[Region]
    """
    The region representing the location of the S3 bucket.
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    authenticationMode: typing_extensions.NotRequired[S3AuthenticationModeDict]
    """
    The authentication mode to use to connect to the S3 external system. No authentication mode is required
    to connect to publicly accessible AWS S3 buckets.
    """

    s3EndpointSigningRegion: typing_extensions.NotRequired[Region]
    """
    The region used when constructing the S3 client using a custom endpoint.
    This is often not required and would only be needed if you are using the S3 connector with an S3-compliant third-party API,
    and are also setting a custom endpoint that requires a non-default region.
    """

    clientKmsConfiguration: typing_extensions.NotRequired[S3KmsConfigurationDict]
    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    stsRoleConfiguration: typing_extensions.NotRequired[StsRoleConfigurationDict]
    """The configuration needed to assume a role to connect to the S3 external system."""

    proxyConfiguration: typing_extensions.NotRequired[S3ProxyConfigurationDict]
    """The configuration needed to connect to the S3 external system through a proxy."""

    maxConnections: typing_extensions.NotRequired[int]
    """
    The maximum number of HTTP connections to the S3 service per sync.
    If not specified, defaults to 50 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_MAX_CONNECTIONS).
    """

    connectionTimeoutMillis: typing_extensions.NotRequired[core.Long]
    """
    The amount of time (in milliseconds) to wait when initially establishing a connection before giving up and timing out.
    If not specified, defaults to 10000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_CONNECTION_TIMEOUT).
    """

    socketTimeoutMillis: typing_extensions.NotRequired[core.Long]
    """
    The amount of time (in milliseconds) to wait for data to be transferred over an established, open connection.
    If not specified, defaults to 50000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_SOCKET_TIMEOUT).
    """

    maxErrorRetry: typing_extensions.NotRequired[int]
    """
    The maximum number of retry attempts for failed requests to the S3 service.
    If not specified, defaults to 3 as defined by the [AWS SDK default](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html#retry-strategies).
    """

    matchSubfolderExactly: typing_extensions.NotRequired[bool]
    """
    If true, only files in the subfolder specified in the bucket URL will be synced.
    If false, all files in the bucket will be synced.
    If not specified, defaults to false.
    """

    enableRequesterPays: typing_extensions.NotRequired[bool]
    """
    Defaults to false, unless set and overwritten.
    If true, includes the [requester pays header](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html)
    in requests, allowing reads from requester pays buckets.
    """

    type: typing.Literal["s3"]


class S3KmsConfiguration(pydantic.BaseModel):
    """S3KmsConfiguration"""

    kms_key: str = pydantic.Field(alias=str("kmsKey"))  # type: ignore[literal-required]
    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    kms_region: typing.Optional[Region] = pydantic.Field(alias=str("kmsRegion"), default=None)  # type: ignore[literal-required]
    """
    The region of the client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key region for the bucket is used.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "S3KmsConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            S3KmsConfigurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class S3KmsConfigurationDict(typing_extensions.TypedDict):
    """S3KmsConfiguration"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    kmsKey: str
    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    kmsRegion: typing_extensions.NotRequired[Region]
    """
    The region of the client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key region for the bucket is used.
    """


class S3ProxyConfiguration(pydantic.BaseModel):
    """S3ProxyConfiguration"""

    host: str
    """
    Domain name, IPv4, or IPv6 address. 
    `protocol` and `port` must be specified separately.
    """

    port: int
    non_proxy_hosts: typing.Optional[typing.List[str]] = pydantic.Field(alias=str("nonProxyHosts"), default=None)  # type: ignore[literal-required]
    """A list of hosts that can bypass the proxy, such as those used for STS Role. You can also use "*" wildcards."""

    protocol: typing.Optional[Protocol] = None
    """If defined, must be "HTTP" or "HTTPS". Defaults to "HTTPS"."""

    credentials: typing.Optional[BasicCredentials] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "S3ProxyConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            S3ProxyConfigurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class S3ProxyConfigurationDict(typing_extensions.TypedDict):
    """S3ProxyConfiguration"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    host: str
    """
    Domain name, IPv4, or IPv6 address. 
    `protocol` and `port` must be specified separately.
    """

    port: int
    nonProxyHosts: typing_extensions.NotRequired[typing.List[str]]
    """A list of hosts that can bypass the proxy, such as those used for STS Role. You can also use "*" wildcards."""

    protocol: typing_extensions.NotRequired[Protocol]
    """If defined, must be "HTTP" or "HTTPS". Defaults to "HTTPS"."""

    credentials: typing_extensions.NotRequired[BasicCredentialsDict]


SecretName = str
"""SecretName"""


class SecretsNames(pydantic.BaseModel):
    """
    A list of secret names that can be referenced in code and webhook configurations.
    This will be provided to the client when fetching the RestConnectionConfiguration.
    """

    secret_names: typing.List[SecretName] = pydantic.Field(alias=str("secretNames"))  # type: ignore[literal-required]
    """The names of the additional secrets that can be referenced in code and webhook configurations."""

    type: typing.Literal["asSecretsNames"] = "asSecretsNames"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SecretsNamesDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SecretsNamesDict, self.model_dump(by_alias=True, exclude_none=True))


class SecretsNamesDict(typing_extensions.TypedDict):
    """
    A list of secret names that can be referenced in code and webhook configurations.
    This will be provided to the client when fetching the RestConnectionConfiguration.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    secretNames: typing.List[SecretName]
    """The names of the additional secrets that can be referenced in code and webhook configurations."""

    type: typing.Literal["asSecretsNames"]


class SecretsWithPlaintextValues(pydantic.BaseModel):
    """
    A map representing secret name to plaintext secret value pairs.
    This should be used when creating or updating additional secrets for a REST connection.
    """

    secrets: typing.Dict[SecretName, PlaintextValue]
    """The additional secrets that can be referenced in code and webhook configurations."""

    type: typing.Literal["asSecretsWithPlaintextValues"] = "asSecretsWithPlaintextValues"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SecretsWithPlaintextValuesDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SecretsWithPlaintextValuesDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SecretsWithPlaintextValuesDict(typing_extensions.TypedDict):
    """
    A map representing secret name to plaintext secret value pairs.
    This should be used when creating or updating additional secrets for a REST connection.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    secrets: typing.Dict[SecretName, PlaintextValue]
    """The additional secrets that can be referenced in code and webhook configurations."""

    type: typing.Literal["asSecretsWithPlaintextValues"]


class StsRoleConfiguration(pydantic.BaseModel):
    """StsRoleConfiguration"""

    role_arn: str = pydantic.Field(alias=str("roleArn"))  # type: ignore[literal-required]
    """
    The Amazon Resource Name (ARN) of the role to assume.
    For more information, see the official [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-arn-format).
    """

    role_session_name: str = pydantic.Field(alias=str("roleSessionName"))  # type: ignore[literal-required]
    """
    An identifier for the assumed role session.
    The value can be any string that you assume will be unique within the AWS account.
    For more information, see the official [AWS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html#API_AssumeRole_RequestParameters).
    """

    role_session_duration: typing.Optional[core_models.Duration] = pydantic.Field(alias=str("roleSessionDuration"), default=None)  # type: ignore[literal-required]
    """
    The duration of the role session.
    The value specified can range from 900 seconds (15 minutes) up to the maximum session duration set for the role.
    The maximum session duration setting can have a value from 1 hour to 12 hours. For more details see the official [AWS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html#API_AssumeRole_RequestParameters).
    """

    external_id: typing.Optional[str] = pydantic.Field(alias=str("externalId"), default=None)  # type: ignore[literal-required]
    """
    A unique identifier that is used by third parties when assuming roles in their customers' accounts.
    For more information, see the official [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).
    """

    sts_endpoint: typing.Optional[str] = pydantic.Field(alias=str("stsEndpoint"), default=None)  # type: ignore[literal-required]
    """
    By default, the AWS Security Token Service (AWS STS) is available as a global service, and all AWS STS requests go to a single endpoint at https://sts.amazonaws.com.
    AWS recommends using Regional AWS STS endpoints instead of the global endpoint to reduce latency, build in redundancy, and increase session token validity.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "StsRoleConfigurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            StsRoleConfigurationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class StsRoleConfigurationDict(typing_extensions.TypedDict):
    """StsRoleConfiguration"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    roleArn: str
    """
    The Amazon Resource Name (ARN) of the role to assume.
    For more information, see the official [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-arn-format).
    """

    roleSessionName: str
    """
    An identifier for the assumed role session.
    The value can be any string that you assume will be unique within the AWS account.
    For more information, see the official [AWS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html#API_AssumeRole_RequestParameters).
    """

    roleSessionDuration: typing_extensions.NotRequired[core_models.DurationDict]
    """
    The duration of the role session.
    The value specified can range from 900 seconds (15 minutes) up to the maximum session duration set for the role.
    The maximum session duration setting can have a value from 1 hour to 12 hours. For more details see the official [AWS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html#API_AssumeRole_RequestParameters).
    """

    externalId: typing_extensions.NotRequired[str]
    """
    A unique identifier that is used by third parties when assuming roles in their customers' accounts.
    For more information, see the official [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).
    """

    stsEndpoint: typing_extensions.NotRequired[str]
    """
    By default, the AWS Security Token Service (AWS STS) is available as a global service, and all AWS STS requests go to a single endpoint at https://sts.amazonaws.com.
    AWS recommends using Regional AWS STS endpoints instead of the global endpoint to reduce latency, build in redundancy, and increase session token validity.
    """


class TableImport(pydantic.BaseModel):
    """TableImport"""

    rid: TableImportRid
    connection_rid: ConnectionRid = pydantic.Field(alias=str("connectionRid"))  # type: ignore[literal-required]
    """The RID of the Connection (also known as a source) that the Table Import uses to import data."""

    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the output dataset."""

    branch_name: typing.Optional[datasets_models.BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]
    """The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments."""

    display_name: TableImportDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    import_mode: TableImportMode = pydantic.Field(alias=str("importMode"))  # type: ignore[literal-required]
    allow_schema_changes: TableImportAllowSchemaChanges = pydantic.Field(alias=str("allowSchemaChanges"))  # type: ignore[literal-required]
    """Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports."""

    config: TableImportConfig
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "TableImportDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(TableImportDict, self.model_dump(by_alias=True, exclude_none=True))


TableImportAllowSchemaChanges = bool
"""Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports."""


TableImportConfig = typing_extensions.Annotated[
    typing.Union[
        "JdbcImportConfig",
        "MicrosoftSqlServerImportConfig",
        "PostgreSqlImportConfig",
        "MicrosoftAccessImportConfig",
        "OracleImportConfig",
    ],
    pydantic.Field(discriminator="type"),
]
"""The import configuration for a specific [connector type](docs/foundry/data-integration/source-type-overview)."""


TableImportConfigDict = typing_extensions.Annotated[
    typing.Union[
        "JdbcImportConfigDict",
        "MicrosoftSqlServerImportConfigDict",
        "PostgreSqlImportConfigDict",
        "MicrosoftAccessImportConfigDict",
        "OracleImportConfigDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""The import configuration for a specific [connector type](docs/foundry/data-integration/source-type-overview)."""


class TableImportDict(typing_extensions.TypedDict):
    """TableImport"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: TableImportRid
    connectionRid: ConnectionRid
    """The RID of the Connection (also known as a source) that the Table Import uses to import data."""

    datasetRid: datasets_models.DatasetRid
    """The RID of the output dataset."""

    branchName: typing_extensions.NotRequired[datasets_models.BranchName]
    """The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments."""

    displayName: TableImportDisplayName
    importMode: TableImportMode
    allowSchemaChanges: TableImportAllowSchemaChanges
    """Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports."""

    config: TableImportConfigDict


TableImportDisplayName = str
"""TableImportDisplayName"""


TableImportMode = typing.Literal["SNAPSHOT", "APPEND"]
"""
Import mode governs how data is read from an external system, and written into a Foundry dataset. 

SNAPSHOT: Defines a new dataset state consisting only of data from a particular import execution.
APPEND: Purely additive and yields data from previous import executions in addition to newly added data.
"""


TableImportRid = core.RID
"""The Resource Identifier (RID) of a TableImport (also known as a batch sync)."""


UriScheme = typing.Literal["HTTP", "HTTPS"]
"""Defines supported URI schemes to be used for external connections."""


from foundry.v2.core import models as core_models  # noqa: E402
from foundry.v2.datasets import models as datasets_models  # noqa: E402
from foundry.v2.filesystem import models as filesystem_models  # noqa: E402

__all__ = [
    "AgentProxyRuntime",
    "AgentProxyRuntimeDict",
    "AgentRid",
    "AgentWorkerRuntime",
    "AgentWorkerRuntimeDict",
    "ApiKeyAuthentication",
    "ApiKeyAuthenticationDict",
    "AsPlaintextValue",
    "AsPlaintextValueDict",
    "AsSecretName",
    "AsSecretNameDict",
    "AwsAccessKey",
    "AwsAccessKeyDict",
    "BasicCredentials",
    "BasicCredentialsDict",
    "BearerToken",
    "BearerTokenDict",
    "CloudIdentity",
    "CloudIdentityDict",
    "CloudIdentityRid",
    "Connection",
    "ConnectionConfiguration",
    "ConnectionConfigurationDict",
    "ConnectionDict",
    "ConnectionDisplayName",
    "ConnectionRid",
    "CreateConnectionRequestAgentProxyRuntime",
    "CreateConnectionRequestAgentProxyRuntimeDict",
    "CreateConnectionRequestAgentWorkerRuntime",
    "CreateConnectionRequestAgentWorkerRuntimeDict",
    "CreateConnectionRequestConnectionConfiguration",
    "CreateConnectionRequestConnectionConfigurationDict",
    "CreateConnectionRequestDirectConnectionRuntime",
    "CreateConnectionRequestDirectConnectionRuntimeDict",
    "CreateConnectionRequestJdbcConnectionConfiguration",
    "CreateConnectionRequestJdbcConnectionConfigurationDict",
    "CreateConnectionRequestRestConnectionConfiguration",
    "CreateConnectionRequestRestConnectionConfigurationDict",
    "CreateConnectionRequestRuntimePlatform",
    "CreateConnectionRequestRuntimePlatformDict",
    "CreateConnectionRequestS3ConnectionConfiguration",
    "CreateConnectionRequestS3ConnectionConfigurationDict",
    "CreateTableImportRequestJdbcImportConfig",
    "CreateTableImportRequestJdbcImportConfigDict",
    "CreateTableImportRequestMicrosoftAccessImportConfig",
    "CreateTableImportRequestMicrosoftAccessImportConfigDict",
    "CreateTableImportRequestMicrosoftSqlServerImportConfig",
    "CreateTableImportRequestMicrosoftSqlServerImportConfigDict",
    "CreateTableImportRequestOracleImportConfig",
    "CreateTableImportRequestOracleImportConfigDict",
    "CreateTableImportRequestPostgreSqlImportConfig",
    "CreateTableImportRequestPostgreSqlImportConfigDict",
    "CreateTableImportRequestTableImportConfig",
    "CreateTableImportRequestTableImportConfigDict",
    "DirectConnectionRuntime",
    "DirectConnectionRuntimeDict",
    "Domain",
    "DomainDict",
    "EncryptedProperty",
    "EncryptedPropertyDict",
    "FileAnyPathMatchesFilter",
    "FileAnyPathMatchesFilterDict",
    "FileAtLeastCountFilter",
    "FileAtLeastCountFilterDict",
    "FileChangedSinceLastUploadFilter",
    "FileChangedSinceLastUploadFilterDict",
    "FileImport",
    "FileImportCustomFilter",
    "FileImportCustomFilterDict",
    "FileImportDict",
    "FileImportDisplayName",
    "FileImportFilter",
    "FileImportFilterDict",
    "FileImportMode",
    "FileImportRid",
    "FileLastModifiedAfterFilter",
    "FileLastModifiedAfterFilterDict",
    "FilePathMatchesFilter",
    "FilePathMatchesFilterDict",
    "FilePathNotMatchesFilter",
    "FilePathNotMatchesFilterDict",
    "FileProperty",
    "FileSizeFilter",
    "FileSizeFilterDict",
    "FilesCountLimitFilter",
    "FilesCountLimitFilterDict",
    "HeaderApiKey",
    "HeaderApiKeyDict",
    "JdbcConnectionConfiguration",
    "JdbcConnectionConfigurationDict",
    "JdbcImportConfig",
    "JdbcImportConfigDict",
    "ListFileImportsResponse",
    "ListFileImportsResponseDict",
    "ListTableImportsResponse",
    "ListTableImportsResponseDict",
    "MicrosoftAccessImportConfig",
    "MicrosoftAccessImportConfigDict",
    "MicrosoftSqlServerImportConfig",
    "MicrosoftSqlServerImportConfigDict",
    "NetworkEgressPolicyRid",
    "Oidc",
    "OidcDict",
    "OracleImportConfig",
    "OracleImportConfigDict",
    "PlaintextValue",
    "PostgreSqlImportConfig",
    "PostgreSqlImportConfigDict",
    "Protocol",
    "QueryParameterApiKey",
    "QueryParameterApiKeyDict",
    "Region",
    "RestAuthenticationMode",
    "RestAuthenticationModeDict",
    "RestConnectionAdditionalSecrets",
    "RestConnectionAdditionalSecretsDict",
    "RestConnectionConfiguration",
    "RestConnectionConfigurationDict",
    "RestConnectionOAuth2",
    "RestConnectionOAuth2Dict",
    "RestRequestApiKeyLocation",
    "RestRequestApiKeyLocationDict",
    "RuntimePlatform",
    "RuntimePlatformDict",
    "S3AuthenticationMode",
    "S3AuthenticationModeDict",
    "S3ConnectionConfiguration",
    "S3ConnectionConfigurationDict",
    "S3KmsConfiguration",
    "S3KmsConfigurationDict",
    "S3ProxyConfiguration",
    "S3ProxyConfigurationDict",
    "SecretName",
    "SecretsNames",
    "SecretsNamesDict",
    "SecretsWithPlaintextValues",
    "SecretsWithPlaintextValuesDict",
    "StsRoleConfiguration",
    "StsRoleConfigurationDict",
    "TableImport",
    "TableImportAllowSchemaChanges",
    "TableImportConfig",
    "TableImportConfigDict",
    "TableImportDict",
    "TableImportDisplayName",
    "TableImportMode",
    "TableImportRid",
    "UriScheme",
]
