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


class OntologyTransactionClient:
    """
    The API client for the OntologyTransaction Resource.

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

        self.with_streaming_response = _OntologyTransactionClientStreaming(self)
        self.with_raw_response = _OntologyTransactionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def post_edits(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        transaction_rid: ontologies_models.OntologyTransactionRid,
        *,
        edits: typing.List[ontologies_models.TransactionEdit],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.PostTransactionEditsResponse:
        """
        Applies a set of edits to a transaction in order.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param transaction_rid: The RID of the transaction to apply edits to.
        :type transaction_rid: OntologyTransactionRid
        :param edits:
        :type edits: List[TransactionEdit]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.PostTransactionEditsResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/transactions/{transactionRid}/edits",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "edits": edits,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "edits": typing.List[ontologies_models.TransactionEdit],
                    },
                ),
                response_type=ontologies_models.PostTransactionEditsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OntologyTransactionClientRaw:
    def __init__(self, client: OntologyTransactionClient) -> None:
        def post_edits(_: ontologies_models.PostTransactionEditsResponse): ...

        self.post_edits = core.with_raw_response(post_edits, client.post_edits)


class _OntologyTransactionClientStreaming:
    def __init__(self, client: OntologyTransactionClient) -> None:
        def post_edits(_: ontologies_models.PostTransactionEditsResponse): ...

        self.post_edits = core.with_streaming_response(post_edits, client.post_edits)


class AsyncOntologyTransactionClient:
    """
    The API client for the OntologyTransaction Resource.

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

        self.with_streaming_response = _AsyncOntologyTransactionClientStreaming(self)
        self.with_raw_response = _AsyncOntologyTransactionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def post_edits(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        transaction_rid: ontologies_models.OntologyTransactionRid,
        *,
        edits: typing.List[ontologies_models.TransactionEdit],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.PostTransactionEditsResponse]:
        """
        Applies a set of edits to a transaction in order.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param transaction_rid: The RID of the transaction to apply edits to.
        :type transaction_rid: OntologyTransactionRid
        :param edits:
        :type edits: List[TransactionEdit]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.PostTransactionEditsResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/transactions/{transactionRid}/edits",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "edits": edits,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "edits": typing.List[ontologies_models.TransactionEdit],
                    },
                ),
                response_type=ontologies_models.PostTransactionEditsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOntologyTransactionClientRaw:
    def __init__(self, client: AsyncOntologyTransactionClient) -> None:
        def post_edits(_: ontologies_models.PostTransactionEditsResponse): ...

        self.post_edits = core.async_with_raw_response(post_edits, client.post_edits)


class _AsyncOntologyTransactionClientStreaming:
    def __init__(self, client: AsyncOntologyTransactionClient) -> None:
        def post_edits(_: ontologies_models.PostTransactionEditsResponse): ...

        self.post_edits = core.async_with_streaming_response(post_edits, client.post_edits)
