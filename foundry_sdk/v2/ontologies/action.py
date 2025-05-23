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


class ActionClient:
    """
    The API client for the Action Resource.

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

        self.with_streaming_response = _ActionClientStreaming(self)
        self.with_raw_response = _ActionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def apply(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        action: ontologies_models.ActionTypeApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        options: typing.Optional[ontologies_models.ApplyActionRequestOptions] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.SyncApplyActionResponseV2:
        """
        Applies an action using the given parameters.

        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param action: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action: ActionTypeApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param options:
        :type options: Optional[ApplyActionRequestOptions]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.SyncApplyActionResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actions/{action}/apply",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "action": action,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "options": options,
                    "parameters": parameters,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "options": typing.Optional[ontologies_models.ApplyActionRequestOptions],
                        "parameters": typing.Dict[
                            ontologies_models.ParameterId,
                            typing.Optional[ontologies_models.DataValue],
                        ],
                    },
                ),
                response_type=ontologies_models.SyncApplyActionResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def apply_batch(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        action: ontologies_models.ActionTypeApiName,
        *,
        requests: typing.List[ontologies_models.BatchApplyActionRequestItem],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        options: typing.Optional[ontologies_models.BatchApplyActionRequestOptions] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.BatchApplyActionResponseV2:
        """
        Applies multiple actions (of the same Action Type) using the given parameters.

        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
        call Functions may receive a higher limit.

        Note that [notifications](https://palantir.com/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param action: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action: ActionTypeApiName
        :param requests:
        :type requests: List[BatchApplyActionRequestItem]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param options:
        :type options: Optional[BatchApplyActionRequestOptions]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.BatchApplyActionResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actions/{action}/applyBatch",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "action": action,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "options": options,
                    "requests": requests,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "options": typing.Optional[
                            ontologies_models.BatchApplyActionRequestOptions
                        ],
                        "requests": typing.List[ontologies_models.BatchApplyActionRequestItem],
                    },
                ),
                response_type=ontologies_models.BatchApplyActionResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ActionClientRaw:
    def __init__(self, client: ActionClient) -> None:
        def apply(_: ontologies_models.SyncApplyActionResponseV2): ...
        def apply_batch(_: ontologies_models.BatchApplyActionResponseV2): ...

        self.apply = core.with_raw_response(apply, client.apply)
        self.apply_batch = core.with_raw_response(apply_batch, client.apply_batch)


class _ActionClientStreaming:
    def __init__(self, client: ActionClient) -> None:
        def apply(_: ontologies_models.SyncApplyActionResponseV2): ...
        def apply_batch(_: ontologies_models.BatchApplyActionResponseV2): ...

        self.apply = core.with_streaming_response(apply, client.apply)
        self.apply_batch = core.with_streaming_response(apply_batch, client.apply_batch)


class AsyncActionClient:
    """
    The API client for the Action Resource.

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

        self.with_streaming_response = _AsyncActionClientStreaming(self)
        self.with_raw_response = _AsyncActionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def apply(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        action: ontologies_models.ActionTypeApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        options: typing.Optional[ontologies_models.ApplyActionRequestOptions] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.SyncApplyActionResponseV2]:
        """
        Applies an action using the given parameters.

        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param action: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action: ActionTypeApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param options:
        :type options: Optional[ApplyActionRequestOptions]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.SyncApplyActionResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actions/{action}/apply",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "action": action,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "options": options,
                    "parameters": parameters,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "options": typing.Optional[ontologies_models.ApplyActionRequestOptions],
                        "parameters": typing.Dict[
                            ontologies_models.ParameterId,
                            typing.Optional[ontologies_models.DataValue],
                        ],
                    },
                ),
                response_type=ontologies_models.SyncApplyActionResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def apply_batch(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        action: ontologies_models.ActionTypeApiName,
        *,
        requests: typing.List[ontologies_models.BatchApplyActionRequestItem],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        options: typing.Optional[ontologies_models.BatchApplyActionRequestOptions] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.BatchApplyActionResponseV2]:
        """
        Applies multiple actions (of the same Action Type) using the given parameters.

        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
        call Functions may receive a higher limit.

        Note that [notifications](https://palantir.com/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param action: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action: ActionTypeApiName
        :param requests:
        :type requests: List[BatchApplyActionRequestItem]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param options:
        :type options: Optional[BatchApplyActionRequestOptions]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.BatchApplyActionResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actions/{action}/applyBatch",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "action": action,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "options": options,
                    "requests": requests,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "options": typing.Optional[
                            ontologies_models.BatchApplyActionRequestOptions
                        ],
                        "requests": typing.List[ontologies_models.BatchApplyActionRequestItem],
                    },
                ),
                response_type=ontologies_models.BatchApplyActionResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncActionClientRaw:
    def __init__(self, client: AsyncActionClient) -> None:
        def apply(_: ontologies_models.SyncApplyActionResponseV2): ...
        def apply_batch(_: ontologies_models.BatchApplyActionResponseV2): ...

        self.apply = core.async_with_raw_response(apply, client.apply)
        self.apply_batch = core.async_with_raw_response(apply_batch, client.apply_batch)


class _AsyncActionClientStreaming:
    def __init__(self, client: AsyncActionClient) -> None:
        def apply(_: ontologies_models.SyncApplyActionResponseV2): ...
        def apply_batch(_: ontologies_models.BatchApplyActionResponseV2): ...

        self.apply = core.async_with_streaming_response(apply, client.apply)
        self.apply_batch = core.async_with_streaming_response(apply_batch, client.apply_batch)
