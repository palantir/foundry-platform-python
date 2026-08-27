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

    @cached_property
    def Action(self):
        from foundry_sdk.v2.ontologies.action import ActionClient

        return ActionClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def ActionTypeFullMetadata(self):
        from foundry_sdk.v2.ontologies.action_type_full_metadata import (
            ActionTypeFullMetadataClient,
        )

        return ActionTypeFullMetadataClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def Attachment(self):
        from foundry_sdk.v2.ontologies.attachment import AttachmentClient

        return AttachmentClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def AttachmentProperty(self):
        from foundry_sdk.v2.ontologies.attachment_property import (
            AttachmentPropertyClient,
        )

        return AttachmentPropertyClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def CipherTextProperty(self):
        from foundry_sdk.v2.ontologies.cipher_text_property import (
            CipherTextPropertyClient,
        )

        return CipherTextPropertyClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def GeotemporalSeriesProperty(self):
        from foundry_sdk.v2.ontologies.geotemporal_series_property import (
            GeotemporalSeriesPropertyClient,
        )

        return GeotemporalSeriesPropertyClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def LinkedObject(self):
        from foundry_sdk.v2.ontologies.linked_object import LinkedObjectClient

        return LinkedObjectClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def MediaReferenceProperty(self):
        from foundry_sdk.v2.ontologies.media_reference_property import (
            MediaReferencePropertyClient,
        )

        return MediaReferencePropertyClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def Ontology(self):
        from foundry_sdk.v2.ontologies.ontology import OntologyClient

        return OntologyClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def OntologyInterface(self):
        from foundry_sdk.v2.ontologies.ontology_interface import OntologyInterfaceClient

        return OntologyInterfaceClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def OntologyObject(self):
        from foundry_sdk.v2.ontologies.ontology_object import OntologyObjectClient

        return OntologyObjectClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def OntologyObjectSet(self):
        from foundry_sdk.v2.ontologies.ontology_object_set import (
            OntologyObjectSetClient,
        )

        return OntologyObjectSetClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def OntologyScenario(self):
        from foundry_sdk.v2.ontologies.ontology_scenario import OntologyScenarioClient

        return OntologyScenarioClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def OntologyTransaction(self):
        from foundry_sdk.v2.ontologies.ontology_transaction import (
            OntologyTransactionClient,
        )

        return OntologyTransactionClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def OntologyValueType(self):
        from foundry_sdk.v2.ontologies.ontology_value_type import (
            OntologyValueTypeClient,
        )

        return OntologyValueTypeClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def Query(self):
        from foundry_sdk.v2.ontologies.query import QueryClient

        return QueryClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def TimeSeriesPropertyV2(self):
        from foundry_sdk.v2.ontologies.time_series_property_v2 import (
            TimeSeriesPropertyV2Client,
        )

        return TimeSeriesPropertyV2Client(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @cached_property
    def TimeSeriesValueBankProperty(self):
        from foundry_sdk.v2.ontologies.time_series_value_bank_property import (
            TimeSeriesValueBankPropertyClient,
        )

        return TimeSeriesValueBankPropertyClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )


class AsyncOntologiesClient:
    """
    The Async API client for the Ontologies Namespace.

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
        from foundry_sdk.v2.ontologies.action import AsyncActionClient
        from foundry_sdk.v2.ontologies.action_type_full_metadata import (
            AsyncActionTypeFullMetadataClient,
        )
        from foundry_sdk.v2.ontologies.attachment import AsyncAttachmentClient
        from foundry_sdk.v2.ontologies.attachment_property import (
            AsyncAttachmentPropertyClient,
        )
        from foundry_sdk.v2.ontologies.cipher_text_property import (
            AsyncCipherTextPropertyClient,
        )
        from foundry_sdk.v2.ontologies.geotemporal_series_property import (
            AsyncGeotemporalSeriesPropertyClient,
        )
        from foundry_sdk.v2.ontologies.linked_object import AsyncLinkedObjectClient
        from foundry_sdk.v2.ontologies.media_reference_property import (
            AsyncMediaReferencePropertyClient,
        )
        from foundry_sdk.v2.ontologies.ontology import AsyncOntologyClient
        from foundry_sdk.v2.ontologies.ontology_interface import (
            AsyncOntologyInterfaceClient,
        )
        from foundry_sdk.v2.ontologies.ontology_object import AsyncOntologyObjectClient
        from foundry_sdk.v2.ontologies.ontology_object_set import (
            AsyncOntologyObjectSetClient,
        )
        from foundry_sdk.v2.ontologies.ontology_scenario import (
            AsyncOntologyScenarioClient,
        )
        from foundry_sdk.v2.ontologies.ontology_transaction import (
            AsyncOntologyTransactionClient,
        )
        from foundry_sdk.v2.ontologies.ontology_value_type import (
            AsyncOntologyValueTypeClient,
        )
        from foundry_sdk.v2.ontologies.query import AsyncQueryClient
        from foundry_sdk.v2.ontologies.time_series_property_v2 import (
            AsyncTimeSeriesPropertyV2Client,
        )
        from foundry_sdk.v2.ontologies.time_series_value_bank_property import (
            AsyncTimeSeriesValueBankPropertyClient,
        )

        self.Action = AsyncActionClient(auth=auth, hostname=hostname, config=config)

        self.ActionTypeFullMetadata = AsyncActionTypeFullMetadataClient(
            auth=auth, hostname=hostname, config=config
        )

        self.Attachment = AsyncAttachmentClient(auth=auth, hostname=hostname, config=config)

        self.AttachmentProperty = AsyncAttachmentPropertyClient(
            auth=auth, hostname=hostname, config=config
        )

        self.CipherTextProperty = AsyncCipherTextPropertyClient(
            auth=auth, hostname=hostname, config=config
        )

        self.GeotemporalSeriesProperty = AsyncGeotemporalSeriesPropertyClient(
            auth=auth, hostname=hostname, config=config
        )

        self.LinkedObject = AsyncLinkedObjectClient(auth=auth, hostname=hostname, config=config)

        self.MediaReferenceProperty = AsyncMediaReferencePropertyClient(
            auth=auth, hostname=hostname, config=config
        )

        self.Ontology = AsyncOntologyClient(auth=auth, hostname=hostname, config=config)

        self.OntologyInterface = AsyncOntologyInterfaceClient(
            auth=auth, hostname=hostname, config=config
        )

        self.OntologyObject = AsyncOntologyObjectClient(auth=auth, hostname=hostname, config=config)

        self.OntologyObjectSet = AsyncOntologyObjectSetClient(
            auth=auth, hostname=hostname, config=config
        )

        self.OntologyScenario = AsyncOntologyScenarioClient(
            auth=auth, hostname=hostname, config=config
        )

        self.OntologyTransaction = AsyncOntologyTransactionClient(
            auth=auth, hostname=hostname, config=config
        )

        self.OntologyValueType = AsyncOntologyValueTypeClient(
            auth=auth, hostname=hostname, config=config
        )

        self.Query = AsyncQueryClient(auth=auth, hostname=hostname, config=config)

        self.TimeSeriesPropertyV2 = AsyncTimeSeriesPropertyV2Client(
            auth=auth, hostname=hostname, config=config
        )

        self.TimeSeriesValueBankProperty = AsyncTimeSeriesValueBankPropertyClient(
            auth=auth, hostname=hostname, config=config
        )
