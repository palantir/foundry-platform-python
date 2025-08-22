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
from foundry_sdk.v2.ontologies import models as ontologies_models


class CipherTextPropertyClient:
    """
    The API client for the CipherTextProperty Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

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
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.DecryptionResult
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/decrypt",
                query_params={},
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
                body_type=None,
                response_type=ontologies_models.DecryptionResult,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _CipherTextPropertyClientRaw:
    def __init__(self, client: CipherTextPropertyClient) -> None:
        def decrypt(_: ontologies_models.DecryptionResult): ...

        self.decrypt = core.with_raw_response(decrypt, client.decrypt)


class _CipherTextPropertyClientStreaming:
    def __init__(self, client: CipherTextPropertyClient) -> None:
        def decrypt(_: ontologies_models.DecryptionResult): ...

        self.decrypt = core.with_streaming_response(decrypt, client.decrypt)


class AsyncCipherTextPropertyClient:
    """
    The API client for the CipherTextProperty Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

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
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.DecryptionResult]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/decrypt",
                query_params={},
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
                body_type=None,
                response_type=ontologies_models.DecryptionResult,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncCipherTextPropertyClientRaw:
    def __init__(self, client: AsyncCipherTextPropertyClient) -> None:
        def decrypt(_: ontologies_models.DecryptionResult): ...

        self.decrypt = core.async_with_raw_response(decrypt, client.decrypt)


class _AsyncCipherTextPropertyClientStreaming:
    def __init__(self, client: AsyncCipherTextPropertyClient) -> None:
        def decrypt(_: ontologies_models.DecryptionResult): ...

        self.decrypt = core.async_with_streaming_response(decrypt, client.decrypt)
