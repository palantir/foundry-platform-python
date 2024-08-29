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

from foundry.api_client import ApiClient
from foundry.v2._namespaces.admin.group import GroupResource
from foundry.v2._namespaces.admin.user import UserResource
from foundry.v2._namespaces.datasets.dataset import DatasetResource
from foundry.v2._namespaces.ontologies.action import ActionResource
from foundry.v2._namespaces.ontologies.attachment import AttachmentResource
from foundry.v2._namespaces.ontologies.attachment_property import AttachmentPropertyResource  # NOQA
from foundry.v2._namespaces.ontologies.linked_object import LinkedObjectResource
from foundry.v2._namespaces.ontologies.ontology import OntologyResource
from foundry.v2._namespaces.ontologies.ontology_interface import OntologyInterfaceResource  # NOQA
from foundry.v2._namespaces.ontologies.ontology_object import OntologyObjectResource
from foundry.v2._namespaces.ontologies.ontology_object_set import OntologyObjectSetResource  # NOQA
from foundry.v2._namespaces.ontologies.query import QueryResource
from foundry.v2._namespaces.ontologies.time_series_property_v2 import (
    TimeSeriesPropertyV2Resource,
)  # NOQA
from foundry.v2._namespaces.orchestration.build import BuildResource
from foundry.v2._namespaces.orchestration.schedule import ScheduleResource
from foundry.v2._namespaces.thirdpartyapplications.third_party_application import (
    ThirdPartyApplicationResource,
)  # NOQA


class Admin:
    def __init__(self, api_client: ApiClient):
        self.Group = GroupResource(api_client=api_client)
        self.User = UserResource(api_client=api_client)


class Datasets:
    def __init__(self, api_client: ApiClient):
        self.Dataset = DatasetResource(api_client=api_client)


class Ontologies:
    def __init__(self, api_client: ApiClient):
        self.Action = ActionResource(api_client=api_client)
        self.Attachment = AttachmentResource(api_client=api_client)
        self.AttachmentProperty = AttachmentPropertyResource(api_client=api_client)
        self.LinkedObject = LinkedObjectResource(api_client=api_client)
        self.Ontology = OntologyResource(api_client=api_client)
        self.OntologyInterface = OntologyInterfaceResource(api_client=api_client)
        self.OntologyObject = OntologyObjectResource(api_client=api_client)
        self.OntologyObjectSet = OntologyObjectSetResource(api_client=api_client)
        self.Query = QueryResource(api_client=api_client)
        self.TimeSeriesPropertyV2 = TimeSeriesPropertyV2Resource(api_client=api_client)


class Orchestration:
    def __init__(self, api_client: ApiClient):
        self.Build = BuildResource(api_client=api_client)
        self.Schedule = ScheduleResource(api_client=api_client)


class ThirdPartyApplications:
    def __init__(self, api_client: ApiClient):
        self.ThirdPartyApplication = ThirdPartyApplicationResource(api_client=api_client)
