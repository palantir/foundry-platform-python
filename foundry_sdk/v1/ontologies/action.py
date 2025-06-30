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
from foundry_sdk.v1.ontologies import models as ontologies_models


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
        ontology_rid: ontologies_models.OntologyRid,
        action_type: ontologies_models.ActionTypeApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ApplyActionResponse:
        """
        Applies an action using the given parameters.

        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param action_type: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action_type: ActionTypeApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ApplyActionResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/actions/{actionType}/apply",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "actionType": action_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            ontologies_models.ParameterId,
                            typing.Optional[ontologies_models.DataValue],
                        ],
                    },
                ),
                response_type=ontologies_models.ApplyActionResponse,
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
        ontology_rid: ontologies_models.OntologyRid,
        action_type: ontologies_models.ActionTypeApiName,
        *,
        requests: typing.List[ontologies_models.ApplyActionRequest],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.BatchApplyActionResponse:
        """
        Applies multiple actions (of the same Action Type) using the given parameters.
        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
        call Functions may receive a higher limit.

        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) and
        [notifications](https://palantir.com/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param action_type: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action_type: ActionTypeApiName
        :param requests:
        :type requests: List[ApplyActionRequest]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.BatchApplyActionResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/actions/{actionType}/applyBatch",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "actionType": action_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "requests": requests,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "requests": typing.List[ontologies_models.ApplyActionRequest],
                    },
                ),
                response_type=ontologies_models.BatchApplyActionResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def validate(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        action_type: ontologies_models.ActionTypeApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ValidateActionResponse:
        """
        Validates if an action can be run with the given set of parameters.
        The response contains the evaluation of parameters and **submission criteria**
        that determine if the request is `VALID` or `INVALID`.
        For performance reasons, validations will not consider existing objects or other data in Foundry.
        For example, the uniqueness of a primary key or the existence of a user ID will not be checked.
        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint. Unspecified parameters will be given a default value of `null`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param action_type: The API name of the action to validate. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action_type: ActionTypeApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ValidateActionResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/actions/{actionType}/validate",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "actionType": action_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            ontologies_models.ParameterId,
                            typing.Optional[ontologies_models.DataValue],
                        ],
                    },
                ),
                response_type=ontologies_models.ValidateActionResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ActionClientRaw:
    def __init__(self, client: ActionClient) -> None:
        def apply(_: ontologies_models.ApplyActionResponse): ...
        def apply_batch(_: ontologies_models.BatchApplyActionResponse): ...
        def validate(_: ontologies_models.ValidateActionResponse): ...

        self.apply = core.with_raw_response(apply, client.apply)
        self.apply_batch = core.with_raw_response(apply_batch, client.apply_batch)
        self.validate = core.with_raw_response(validate, client.validate)


class _ActionClientStreaming:
    def __init__(self, client: ActionClient) -> None:
        def apply(_: ontologies_models.ApplyActionResponse): ...
        def apply_batch(_: ontologies_models.BatchApplyActionResponse): ...
        def validate(_: ontologies_models.ValidateActionResponse): ...

        self.apply = core.with_streaming_response(apply, client.apply)
        self.apply_batch = core.with_streaming_response(apply_batch, client.apply_batch)
        self.validate = core.with_streaming_response(validate, client.validate)


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
        ontology_rid: ontologies_models.OntologyRid,
        action_type: ontologies_models.ActionTypeApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ApplyActionResponse]:
        """
        Applies an action using the given parameters.

        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param action_type: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action_type: ActionTypeApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ApplyActionResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/actions/{actionType}/apply",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "actionType": action_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            ontologies_models.ParameterId,
                            typing.Optional[ontologies_models.DataValue],
                        ],
                    },
                ),
                response_type=ontologies_models.ApplyActionResponse,
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
        ontology_rid: ontologies_models.OntologyRid,
        action_type: ontologies_models.ActionTypeApiName,
        *,
        requests: typing.List[ontologies_models.ApplyActionRequest],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.BatchApplyActionResponse]:
        """
        Applies multiple actions (of the same Action Type) using the given parameters.
        Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
        Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

        Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
        call Functions may receive a higher limit.

        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) and
        [notifications](https://palantir.com/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param action_type: The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action_type: ActionTypeApiName
        :param requests:
        :type requests: List[ApplyActionRequest]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.BatchApplyActionResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/actions/{actionType}/applyBatch",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "actionType": action_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "requests": requests,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "requests": typing.List[ontologies_models.ApplyActionRequest],
                    },
                ),
                response_type=ontologies_models.BatchApplyActionResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def validate(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        action_type: ontologies_models.ActionTypeApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ValidateActionResponse]:
        """
        Validates if an action can be run with the given set of parameters.
        The response contains the evaluation of parameters and **submission criteria**
        that determine if the request is `VALID` or `INVALID`.
        For performance reasons, validations will not consider existing objects or other data in Foundry.
        For example, the uniqueness of a primary key or the existence of a user ID will not be checked.
        Note that [parameter default values](https://palantir.com/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint. Unspecified parameters will be given a default value of `null`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the action. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param action_type: The API name of the action to validate. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**.
        :type action_type: ActionTypeApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ValidateActionResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/actions/{actionType}/validate",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "actionType": action_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            ontologies_models.ParameterId,
                            typing.Optional[ontologies_models.DataValue],
                        ],
                    },
                ),
                response_type=ontologies_models.ValidateActionResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncActionClientRaw:
    def __init__(self, client: AsyncActionClient) -> None:
        def apply(_: ontologies_models.ApplyActionResponse): ...
        def apply_batch(_: ontologies_models.BatchApplyActionResponse): ...
        def validate(_: ontologies_models.ValidateActionResponse): ...

        self.apply = core.async_with_raw_response(apply, client.apply)
        self.apply_batch = core.async_with_raw_response(apply_batch, client.apply_batch)
        self.validate = core.async_with_raw_response(validate, client.validate)


class _AsyncActionClientStreaming:
    def __init__(self, client: AsyncActionClient) -> None:
        def apply(_: ontologies_models.ApplyActionResponse): ...
        def apply_batch(_: ontologies_models.BatchApplyActionResponse): ...
        def validate(_: ontologies_models.ValidateActionResponse): ...

        self.apply = core.async_with_streaming_response(apply, client.apply)
        self.apply_batch = core.async_with_streaming_response(apply_batch, client.apply_batch)
        self.validate = core.async_with_streaming_response(validate, client.validate)
