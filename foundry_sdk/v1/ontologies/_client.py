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
from functools import cached_property

from foundry_sdk import _core as core


class OntologiesClient:
    """
    The API client for the Ontologies Namespace.

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

    @cached_property
    def Action(self):
        from foundry_sdk.v1.ontologies.action import ActionClient

        return ActionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Attachment(self):
        from foundry_sdk.v1.ontologies.attachment import AttachmentClient

        return AttachmentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Ontology(self):
        from foundry_sdk.v1.ontologies.ontology import OntologyClient

        return OntologyClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def OntologyObject(self):
        from foundry_sdk.v1.ontologies.ontology_object import OntologyObjectClient

        return OntologyObjectClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Query(self):
        from foundry_sdk.v1.ontologies.query import QueryClient

        return QueryClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )


class AsyncOntologiesClient:
    """
    The Async API client for the Ontologies Namespace.

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
        from foundry_sdk.v1.ontologies.action import AsyncActionClient
        from foundry_sdk.v1.ontologies.attachment import AsyncAttachmentClient
        from foundry_sdk.v1.ontologies.ontology import AsyncOntologyClient
        from foundry_sdk.v1.ontologies.ontology_object import AsyncOntologyObjectClient
        from foundry_sdk.v1.ontologies.query import AsyncQueryClient

        self.Action = AsyncActionClient(auth=auth, hostname=hostname, config=config)

        self.Attachment = AsyncAttachmentClient(auth=auth, hostname=hostname, config=config)

        self.Ontology = AsyncOntologyClient(auth=auth, hostname=hostname, config=config)

        self.OntologyObject = AsyncOntologyObjectClient(auth=auth, hostname=hostname, config=config)

        self.Query = AsyncQueryClient(auth=auth, hostname=hostname, config=config)
