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

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.ontologies import models as ontologies_models


class CipherTextPropertyClient:
    """
    The API client for the CipherTextProperty Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _CipherTextPropertyClientStreaming(self)
        self.with_raw_response = _CipherTextPropertyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def decrypt(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.DecryptionResult:
        """
        Decrypt the value of a ciphertext property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the CipherText property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param branch: The Foundry branch to read from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.DecryptionResult
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/decrypt",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.DecryptionResult,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def encrypt(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        plaintext: ontologies_models.Plaintext,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        cipher_channel_strategy: typing.Optional[ontologies_models.CipherChannelStrategy] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.EncryptionResult:
        """
        Encrypt a plaintext value into a CipherText value for the given object's CipherText property.

        The Cipher Channel used is resolved based on the supplied `cipherChannelStrategy`, using the channel of the
        object's existing ciphertext value and/or the default channel configured for the property in ontology metadata.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the CipherText property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param plaintext:
        :type plaintext: Plaintext
        :param branch: The Foundry branch to read from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param cipher_channel_strategy: The strategy controlling which Cipher Channel is used to encrypt the value. If not specified, defaults to `PREFER_EXISTING`.
        :type cipher_channel_strategy: Optional[CipherChannelStrategy]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.EncryptionResult
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/encrypt",
                query_params={
                    "branch": branch,
                    "cipherChannelStrategy": cipher_channel_strategy,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.EncryptionRequest(
                    plaintext=plaintext,
                ),
                response_type=ontologies_models.EncryptionResult,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def encrypt_with_default_channel(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        property: ontologies_models.PropertyApiName,
        *,
        plaintext: ontologies_models.Plaintext,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.EncryptionResult:
        """
        Encrypt a plaintext value into a CipherText value for the given object type property.

        The Cipher Channel used is the default channel configured for the property in ontology metadata. This
        endpoint requires the CipherText property to have a configured `defaultCipherChannelRid`; if none is
        configured an error will be thrown. To encrypt against the channel of an existing object's value, use the
        **Encrypt** endpoint that accepts a `primaryKey` instead.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param property: The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param plaintext:
        :type plaintext: Plaintext
        :param branch: The Foundry branch to read from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.EncryptionResult
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/ciphertexts/{property}/encrypt",
                query_params={
                    "branch": branch,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "property": property,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.EncryptionRequest(
                    plaintext=plaintext,
                ),
                response_type=ontologies_models.EncryptionResult,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _CipherTextPropertyClientRaw:
    def __init__(self, client: CipherTextPropertyClient) -> None:
        def decrypt(_: ontologies_models.DecryptionResult): ...
        def encrypt(_: ontologies_models.EncryptionResult): ...
        def encrypt_with_default_channel(_: ontologies_models.EncryptionResult): ...

        self.decrypt = core.with_raw_response(decrypt, client.decrypt)
        self.encrypt = core.with_raw_response(encrypt, client.encrypt)
        self.encrypt_with_default_channel = core.with_raw_response(
            encrypt_with_default_channel, client.encrypt_with_default_channel
        )


class _CipherTextPropertyClientStreaming:
    def __init__(self, client: CipherTextPropertyClient) -> None:
        def decrypt(_: ontologies_models.DecryptionResult): ...
        def encrypt(_: ontologies_models.EncryptionResult): ...
        def encrypt_with_default_channel(_: ontologies_models.EncryptionResult): ...

        self.decrypt = core.with_streaming_response(decrypt, client.decrypt)
        self.encrypt = core.with_streaming_response(encrypt, client.encrypt)
        self.encrypt_with_default_channel = core.with_streaming_response(
            encrypt_with_default_channel, client.encrypt_with_default_channel
        )


class AsyncCipherTextPropertyClient:
    """
    The API client for the CipherTextProperty Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncCipherTextPropertyClientStreaming(self)
        self.with_raw_response = _AsyncCipherTextPropertyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def decrypt(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.DecryptionResult]:
        """
        Decrypt the value of a ciphertext property.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the CipherText property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param branch: The Foundry branch to read from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.DecryptionResult]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/decrypt",
                query_params={
                    "branch": branch,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=ontologies_models.DecryptionResult,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def encrypt(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        property: ontologies_models.PropertyApiName,
        *,
        plaintext: ontologies_models.Plaintext,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        cipher_channel_strategy: typing.Optional[ontologies_models.CipherChannelStrategy] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.EncryptionResult]:
        """
        Encrypt a plaintext value into a CipherText value for the given object's CipherText property.

        The Cipher Channel used is resolved based on the supplied `cipherChannelStrategy`, using the channel of the
        object's existing ciphertext value and/or the default channel configured for the property in ontology metadata.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object with the CipherText property.
        :type primary_key: PropertyValueEscapedString
        :param property: The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param plaintext:
        :type plaintext: Plaintext
        :param branch: The Foundry branch to read from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param cipher_channel_strategy: The strategy controlling which Cipher Channel is used to encrypt the value. If not specified, defaults to `PREFER_EXISTING`.
        :type cipher_channel_strategy: Optional[CipherChannelStrategy]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.EncryptionResult]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/encrypt",
                query_params={
                    "branch": branch,
                    "cipherChannelStrategy": cipher_channel_strategy,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.EncryptionRequest(
                    plaintext=plaintext,
                ),
                response_type=ontologies_models.EncryptionResult,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def encrypt_with_default_channel(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        object_type: ontologies_models.ObjectTypeApiName,
        property: ontologies_models.PropertyApiName,
        *,
        plaintext: ontologies_models.Plaintext,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.EncryptionResult]:
        """
        Encrypt a plaintext value into a CipherText value for the given object type property.

        The Cipher Channel used is the default channel configured for the property in ontology metadata. This
        endpoint requires the CipherText property to have a configured `defaultCipherChannelRid`; if none is
        configured an error will be thrown. To encrypt against the channel of an existing object's value, use the
        **Encrypt** endpoint that accepts a `primaryKey` instead.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param property: The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.
        :type property: PropertyApiName
        :param plaintext:
        :type plaintext: Plaintext
        :param branch: The Foundry branch to read from. If not specified, the default branch will be used.
        :type branch: Optional[FoundryBranch]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.EncryptionResult]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/ciphertexts/{property}/encrypt",
                query_params={
                    "branch": branch,
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "property": property,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=ontologies_models.EncryptionRequest(
                    plaintext=plaintext,
                ),
                response_type=ontologies_models.EncryptionResult,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncCipherTextPropertyClientRaw:
    def __init__(self, client: AsyncCipherTextPropertyClient) -> None:
        def decrypt(_: ontologies_models.DecryptionResult): ...
        def encrypt(_: ontologies_models.EncryptionResult): ...
        def encrypt_with_default_channel(_: ontologies_models.EncryptionResult): ...

        self.decrypt = core.async_with_raw_response(decrypt, client.decrypt)
        self.encrypt = core.async_with_raw_response(encrypt, client.encrypt)
        self.encrypt_with_default_channel = core.async_with_raw_response(
            encrypt_with_default_channel, client.encrypt_with_default_channel
        )


class _AsyncCipherTextPropertyClientStreaming:
    def __init__(self, client: AsyncCipherTextPropertyClient) -> None:
        def decrypt(_: ontologies_models.DecryptionResult): ...
        def encrypt(_: ontologies_models.EncryptionResult): ...
        def encrypt_with_default_channel(_: ontologies_models.EncryptionResult): ...

        self.decrypt = core.async_with_streaming_response(decrypt, client.decrypt)
        self.encrypt = core.async_with_streaming_response(encrypt, client.encrypt)
        self.encrypt_with_default_channel = core.async_with_streaming_response(
            encrypt_with_default_channel, client.encrypt_with_default_channel
        )
