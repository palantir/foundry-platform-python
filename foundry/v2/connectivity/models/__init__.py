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


from foundry.v2.connectivity.models._agent_proxy_runtime import AgentProxyRuntime
from foundry.v2.connectivity.models._agent_proxy_runtime_dict import AgentProxyRuntimeDict  # NOQA
from foundry.v2.connectivity.models._agent_rid import AgentRid
from foundry.v2.connectivity.models._agent_worker_runtime import AgentWorkerRuntime
from foundry.v2.connectivity.models._agent_worker_runtime_dict import AgentWorkerRuntimeDict  # NOQA
from foundry.v2.connectivity.models._api_key_authentication import ApiKeyAuthentication
from foundry.v2.connectivity.models._api_key_authentication_dict import (
    ApiKeyAuthenticationDict,
)  # NOQA
from foundry.v2.connectivity.models._as_plaintext_value import AsPlaintextValue
from foundry.v2.connectivity.models._as_plaintext_value_dict import AsPlaintextValueDict
from foundry.v2.connectivity.models._as_secret_name import AsSecretName
from foundry.v2.connectivity.models._as_secret_name_dict import AsSecretNameDict
from foundry.v2.connectivity.models._aws_access_key import AwsAccessKey
from foundry.v2.connectivity.models._aws_access_key_dict import AwsAccessKeyDict
from foundry.v2.connectivity.models._basic_credentials import BasicCredentials
from foundry.v2.connectivity.models._basic_credentials_dict import BasicCredentialsDict
from foundry.v2.connectivity.models._bearer_token import BearerToken
from foundry.v2.connectivity.models._bearer_token_dict import BearerTokenDict
from foundry.v2.connectivity.models._cloud_identity import CloudIdentity
from foundry.v2.connectivity.models._cloud_identity_dict import CloudIdentityDict
from foundry.v2.connectivity.models._cloud_identity_rid import CloudIdentityRid
from foundry.v2.connectivity.models._connection import Connection
from foundry.v2.connectivity.models._connection_configuration import ConnectionConfiguration  # NOQA
from foundry.v2.connectivity.models._connection_configuration_dict import (
    ConnectionConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._connection_dict import ConnectionDict
from foundry.v2.connectivity.models._connection_display_name import ConnectionDisplayName  # NOQA
from foundry.v2.connectivity.models._connection_rid import ConnectionRid
from foundry.v2.connectivity.models._create_connection_request_agent_proxy_runtime import (
    CreateConnectionRequestAgentProxyRuntime,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_agent_proxy_runtime_dict import (
    CreateConnectionRequestAgentProxyRuntimeDict,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_agent_worker_runtime import (
    CreateConnectionRequestAgentWorkerRuntime,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_agent_worker_runtime_dict import (
    CreateConnectionRequestAgentWorkerRuntimeDict,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_connection_configuration import (
    CreateConnectionRequestConnectionConfiguration,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_connection_configuration_dict import (
    CreateConnectionRequestConnectionConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_direct_connection_runtime import (
    CreateConnectionRequestDirectConnectionRuntime,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_direct_connection_runtime_dict import (
    CreateConnectionRequestDirectConnectionRuntimeDict,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_rest_connection_configuration import (
    CreateConnectionRequestRestConnectionConfiguration,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_rest_connection_configuration_dict import (
    CreateConnectionRequestRestConnectionConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_runtime_platform import (
    CreateConnectionRequestRuntimePlatform,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_runtime_platform_dict import (
    CreateConnectionRequestRuntimePlatformDict,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_s3_connection_configuration import (
    CreateConnectionRequestS3ConnectionConfiguration,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_s3_connection_configuration_dict import (
    CreateConnectionRequestS3ConnectionConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_jdbc_import_config import (
    CreateTableImportRequestJdbcImportConfig,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_jdbc_import_config_dict import (
    CreateTableImportRequestJdbcImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_microsoft_access_import_config import (
    CreateTableImportRequestMicrosoftAccessImportConfig,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_microsoft_access_import_config_dict import (
    CreateTableImportRequestMicrosoftAccessImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_microsoft_sql_server_import_config import (
    CreateTableImportRequestMicrosoftSqlServerImportConfig,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_microsoft_sql_server_import_config_dict import (
    CreateTableImportRequestMicrosoftSqlServerImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_oracle_import_config import (
    CreateTableImportRequestOracleImportConfig,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_oracle_import_config_dict import (
    CreateTableImportRequestOracleImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_postgre_sql_import_config import (
    CreateTableImportRequestPostgreSqlImportConfig,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_postgre_sql_import_config_dict import (
    CreateTableImportRequestPostgreSqlImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_table_import_config import (
    CreateTableImportRequestTableImportConfig,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_table_import_config_dict import (
    CreateTableImportRequestTableImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._direct_connection_runtime import (
    DirectConnectionRuntime,
)  # NOQA
from foundry.v2.connectivity.models._direct_connection_runtime_dict import (
    DirectConnectionRuntimeDict,
)  # NOQA
from foundry.v2.connectivity.models._domain import Domain
from foundry.v2.connectivity.models._domain_dict import DomainDict
from foundry.v2.connectivity.models._encrypted_property import EncryptedProperty
from foundry.v2.connectivity.models._encrypted_property_dict import EncryptedPropertyDict  # NOQA
from foundry.v2.connectivity.models._file_any_path_matches_filter import (
    FileAnyPathMatchesFilter,
)  # NOQA
from foundry.v2.connectivity.models._file_any_path_matches_filter_dict import (
    FileAnyPathMatchesFilterDict,
)  # NOQA
from foundry.v2.connectivity.models._file_at_least_count_filter import (
    FileAtLeastCountFilter,
)  # NOQA
from foundry.v2.connectivity.models._file_at_least_count_filter_dict import (
    FileAtLeastCountFilterDict,
)  # NOQA
from foundry.v2.connectivity.models._file_changed_since_last_upload_filter import (
    FileChangedSinceLastUploadFilter,
)  # NOQA
from foundry.v2.connectivity.models._file_changed_since_last_upload_filter_dict import (
    FileChangedSinceLastUploadFilterDict,
)  # NOQA
from foundry.v2.connectivity.models._file_import import FileImport
from foundry.v2.connectivity.models._file_import_custom_filter import FileImportCustomFilter  # NOQA
from foundry.v2.connectivity.models._file_import_custom_filter_dict import (
    FileImportCustomFilterDict,
)  # NOQA
from foundry.v2.connectivity.models._file_import_dict import FileImportDict
from foundry.v2.connectivity.models._file_import_display_name import FileImportDisplayName  # NOQA
from foundry.v2.connectivity.models._file_import_filter import FileImportFilter
from foundry.v2.connectivity.models._file_import_filter_dict import FileImportFilterDict
from foundry.v2.connectivity.models._file_import_mode import FileImportMode
from foundry.v2.connectivity.models._file_import_rid import FileImportRid
from foundry.v2.connectivity.models._file_last_modified_after_filter import (
    FileLastModifiedAfterFilter,
)  # NOQA
from foundry.v2.connectivity.models._file_last_modified_after_filter_dict import (
    FileLastModifiedAfterFilterDict,
)  # NOQA
from foundry.v2.connectivity.models._file_path_matches_filter import FilePathMatchesFilter  # NOQA
from foundry.v2.connectivity.models._file_path_matches_filter_dict import (
    FilePathMatchesFilterDict,
)  # NOQA
from foundry.v2.connectivity.models._file_path_not_matches_filter import (
    FilePathNotMatchesFilter,
)  # NOQA
from foundry.v2.connectivity.models._file_path_not_matches_filter_dict import (
    FilePathNotMatchesFilterDict,
)  # NOQA
from foundry.v2.connectivity.models._file_property import FileProperty
from foundry.v2.connectivity.models._file_size_filter import FileSizeFilter
from foundry.v2.connectivity.models._file_size_filter_dict import FileSizeFilterDict
from foundry.v2.connectivity.models._files_count_limit_filter import FilesCountLimitFilter  # NOQA
from foundry.v2.connectivity.models._files_count_limit_filter_dict import (
    FilesCountLimitFilterDict,
)  # NOQA
from foundry.v2.connectivity.models._header_api_key import HeaderApiKey
from foundry.v2.connectivity.models._header_api_key_dict import HeaderApiKeyDict
from foundry.v2.connectivity.models._jdbc_import_config import JdbcImportConfig
from foundry.v2.connectivity.models._jdbc_import_config_dict import JdbcImportConfigDict
from foundry.v2.connectivity.models._list_file_imports_response import (
    ListFileImportsResponse,
)  # NOQA
from foundry.v2.connectivity.models._list_file_imports_response_dict import (
    ListFileImportsResponseDict,
)  # NOQA
from foundry.v2.connectivity.models._list_table_imports_response import (
    ListTableImportsResponse,
)  # NOQA
from foundry.v2.connectivity.models._list_table_imports_response_dict import (
    ListTableImportsResponseDict,
)  # NOQA
from foundry.v2.connectivity.models._microsoft_access_import_config import (
    MicrosoftAccessImportConfig,
)  # NOQA
from foundry.v2.connectivity.models._microsoft_access_import_config_dict import (
    MicrosoftAccessImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._microsoft_sql_server_import_config import (
    MicrosoftSqlServerImportConfig,
)  # NOQA
from foundry.v2.connectivity.models._microsoft_sql_server_import_config_dict import (
    MicrosoftSqlServerImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._network_egress_policy_rid import NetworkEgressPolicyRid  # NOQA
from foundry.v2.connectivity.models._oidc import Oidc
from foundry.v2.connectivity.models._oidc_dict import OidcDict
from foundry.v2.connectivity.models._oracle_import_config import OracleImportConfig
from foundry.v2.connectivity.models._oracle_import_config_dict import OracleImportConfigDict  # NOQA
from foundry.v2.connectivity.models._plaintext_value import PlaintextValue
from foundry.v2.connectivity.models._postgre_sql_import_config import PostgreSqlImportConfig  # NOQA
from foundry.v2.connectivity.models._postgre_sql_import_config_dict import (
    PostgreSqlImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._protocol import Protocol
from foundry.v2.connectivity.models._query_parameter_api_key import QueryParameterApiKey
from foundry.v2.connectivity.models._query_parameter_api_key_dict import (
    QueryParameterApiKeyDict,
)  # NOQA
from foundry.v2.connectivity.models._region import Region
from foundry.v2.connectivity.models._rest_authentication_mode import RestAuthenticationMode  # NOQA
from foundry.v2.connectivity.models._rest_authentication_mode_dict import (
    RestAuthenticationModeDict,
)  # NOQA
from foundry.v2.connectivity.models._rest_connection_additional_secrets import (
    RestConnectionAdditionalSecrets,
)  # NOQA
from foundry.v2.connectivity.models._rest_connection_additional_secrets_dict import (
    RestConnectionAdditionalSecretsDict,
)  # NOQA
from foundry.v2.connectivity.models._rest_connection_configuration import (
    RestConnectionConfiguration,
)  # NOQA
from foundry.v2.connectivity.models._rest_connection_configuration_dict import (
    RestConnectionConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._rest_connection_o_auth2 import RestConnectionOAuth2
from foundry.v2.connectivity.models._rest_connection_o_auth2_dict import (
    RestConnectionOAuth2Dict,
)  # NOQA
from foundry.v2.connectivity.models._rest_request_api_key_location import (
    RestRequestApiKeyLocation,
)  # NOQA
from foundry.v2.connectivity.models._rest_request_api_key_location_dict import (
    RestRequestApiKeyLocationDict,
)  # NOQA
from foundry.v2.connectivity.models._runtime_platform import RuntimePlatform
from foundry.v2.connectivity.models._runtime_platform_dict import RuntimePlatformDict
from foundry.v2.connectivity.models._s3_authentication_mode import S3AuthenticationMode
from foundry.v2.connectivity.models._s3_authentication_mode_dict import (
    S3AuthenticationModeDict,
)  # NOQA
from foundry.v2.connectivity.models._s3_connection_configuration import (
    S3ConnectionConfiguration,
)  # NOQA
from foundry.v2.connectivity.models._s3_connection_configuration_dict import (
    S3ConnectionConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._s3_kms_configuration import S3KmsConfiguration
from foundry.v2.connectivity.models._s3_kms_configuration_dict import S3KmsConfigurationDict  # NOQA
from foundry.v2.connectivity.models._s3_proxy_configuration import S3ProxyConfiguration
from foundry.v2.connectivity.models._s3_proxy_configuration_dict import (
    S3ProxyConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._secret_name import SecretName
from foundry.v2.connectivity.models._secrets_names import SecretsNames
from foundry.v2.connectivity.models._secrets_names_dict import SecretsNamesDict
from foundry.v2.connectivity.models._secrets_with_plaintext_values import (
    SecretsWithPlaintextValues,
)  # NOQA
from foundry.v2.connectivity.models._secrets_with_plaintext_values_dict import (
    SecretsWithPlaintextValuesDict,
)  # NOQA
from foundry.v2.connectivity.models._sts_role_configuration import StsRoleConfiguration
from foundry.v2.connectivity.models._sts_role_configuration_dict import (
    StsRoleConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._table_import import TableImport
from foundry.v2.connectivity.models._table_import_allow_schema_changes import (
    TableImportAllowSchemaChanges,
)  # NOQA
from foundry.v2.connectivity.models._table_import_config import TableImportConfig
from foundry.v2.connectivity.models._table_import_config_dict import TableImportConfigDict  # NOQA
from foundry.v2.connectivity.models._table_import_dict import TableImportDict
from foundry.v2.connectivity.models._table_import_display_name import TableImportDisplayName  # NOQA
from foundry.v2.connectivity.models._table_import_mode import TableImportMode
from foundry.v2.connectivity.models._table_import_rid import TableImportRid
from foundry.v2.connectivity.models._uri_scheme import UriScheme

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
