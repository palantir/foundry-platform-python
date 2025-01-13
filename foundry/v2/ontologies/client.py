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


from __future__ import annotations

from typing import Optional

from foundry._core import Auth
from foundry._core import Config
from foundry.v2.ontologies.action import ActionClient
from foundry.v2.ontologies.attachment import AttachmentClient
from foundry.v2.ontologies.attachment_property import AttachmentPropertyClient
from foundry.v2.ontologies.linked_object import LinkedObjectClient
from foundry.v2.ontologies.ontology import OntologyClient
from foundry.v2.ontologies.ontology_interface import OntologyInterfaceClient
from foundry.v2.ontologies.ontology_object import OntologyObjectClient
from foundry.v2.ontologies.ontology_object_set import OntologyObjectSetClient
from foundry.v2.ontologies.query import QueryClient
from foundry.v2.ontologies.time_series_property_v2 import TimeSeriesPropertyV2Client


class OntologiesClient:
    """
    The API client for the OntologiesV2 Namespace.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com").
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self.Action = ActionClient(auth=auth, hostname=hostname, config=config)
        self.Attachment = AttachmentClient(auth=auth, hostname=hostname, config=config)
        self.AttachmentProperty = AttachmentPropertyClient(
            auth=auth, hostname=hostname, config=config
        )
        self.LinkedObject = LinkedObjectClient(auth=auth, hostname=hostname, config=config)
        self.OntologyInterface = OntologyInterfaceClient(
            auth=auth, hostname=hostname, config=config
        )
        self.OntologyObjectSet = OntologyObjectSetClient(
            auth=auth, hostname=hostname, config=config
        )
        self.OntologyObject = OntologyObjectClient(auth=auth, hostname=hostname, config=config)
        self.Ontology = OntologyClient(auth=auth, hostname=hostname, config=config)
        self.Query = QueryClient(auth=auth, hostname=hostname, config=config)
        self.TimeSeriesPropertyV2 = TimeSeriesPropertyV2Client(
            auth=auth, hostname=hostname, config=config
        )
