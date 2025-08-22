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
        branch: typing.Optional[core_models.FoundryBranch] = None,
        options: typing.Optional[ontologies_models.ApplyActionRequestOptions] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.SyncApplyActionResponseV2:
        """
        Applies an action using the given parameters.

        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Note that a 200 HTTP status code only indicates that the request was received and processed by the server.
        See the validation result in the response body to determine if the action was applied successfully.

        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param action: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action: ActionTypeApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param branch: The Foundry branch to apply the action against. If not specified, the default branch is used.
        :type branch: Optional[FoundryBranch]
        :param options:
        :type options: Optional[ApplyActionRequestOptions]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
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
                    "branch": branch,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
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
        branch: typing.Optional[core_models.FoundryBranch] = None,
        options: typing.Optional[ontologies_models.BatchApplyActionRequestOptions] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
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

        :param ontology:
        :type ontology: OntologyIdentifier
        :param action: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action: ActionTypeApiName
        :param requests:
        :type requests: List[BatchApplyActionRequestItem]
        :param branch: The Foundry branch to apply the action against. If not specified, the default branch is used.
        :type branch: Optional[FoundryBranch]
        :param options:
        :type options: Optional[BatchApplyActionRequestOptions]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
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
                    "branch": branch,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
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
        branch: typing.Optional[core_models.FoundryBranch] = None,
        options: typing.Optional[ontologies_models.ApplyActionRequestOptions] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.SyncApplyActionResponseV2]:
        """
        Applies an action using the given parameters.

        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Note that a 200 HTTP status code only indicates that the request was received and processed by the server.
        See the validation result in the response body to determine if the action was applied successfully.

        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param action: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action: ActionTypeApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param branch: The Foundry branch to apply the action against. If not specified, the default branch is used.
        :type branch: Optional[FoundryBranch]
        :param options:
        :type options: Optional[ApplyActionRequestOptions]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
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
                    "branch": branch,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
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
        branch: typing.Optional[core_models.FoundryBranch] = None,
        options: typing.Optional[ontologies_models.BatchApplyActionRequestOptions] = None,
        sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid] = None,
        sdk_version: typing.Optional[ontologies_models.SdkVersion] = None,
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

        :param ontology:
        :type ontology: OntologyIdentifier
        :param action: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action: ActionTypeApiName
        :param requests:
        :type requests: List[BatchApplyActionRequestItem]
        :param branch: The Foundry branch to apply the action against. If not specified, the default branch is used.
        :type branch: Optional[FoundryBranch]
        :param options:
        :type options: Optional[BatchApplyActionRequestOptions]
        :param sdk_package_rid: The package rid of the generated SDK.
        :type sdk_package_rid: Optional[SdkPackageRid]
        :param sdk_version: The version of the generated SDK.
        :type sdk_version: Optional[SdkVersion]
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
                    "branch": branch,
                    "sdkPackageRid": sdk_package_rid,
                    "sdkVersion": sdk_version,
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
