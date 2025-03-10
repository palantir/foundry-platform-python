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

from foundry import _core as core


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
        from foundry.v2.ontologies.action import ActionClient

        return ActionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Attachment(self):
        from foundry.v2.ontologies.attachment import AttachmentClient

        return AttachmentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def AttachmentProperty(self):
        from foundry.v2.ontologies.attachment_property import AttachmentPropertyClient

        return AttachmentPropertyClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def LinkedObject(self):
        from foundry.v2.ontologies.linked_object import LinkedObjectClient

        return LinkedObjectClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Ontology(self):
        from foundry.v2.ontologies.ontology import OntologyClient

        return OntologyClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def OntologyInterface(self):
        from foundry.v2.ontologies.ontology_interface import OntologyInterfaceClient

        return OntologyInterfaceClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def OntologyObject(self):
        from foundry.v2.ontologies.ontology_object import OntologyObjectClient

        return OntologyObjectClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def OntologyObjectSet(self):
        from foundry.v2.ontologies.ontology_object_set import OntologyObjectSetClient

        return OntologyObjectSetClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Query(self):
        from foundry.v2.ontologies.query import QueryClient

        return QueryClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def TimeSeriesPropertyV2(self):
        from foundry.v2.ontologies.time_series_property_v2 import TimeSeriesPropertyV2Client  # NOQA

        return TimeSeriesPropertyV2Client(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )
