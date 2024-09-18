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

from foundry._core import Auth
from foundry.v1.ontologies.action import ActionClient
from foundry.v1.ontologies.ontology import OntologyClient
from foundry.v1.ontologies.ontology_object import OntologyObjectClient
from foundry.v1.ontologies.query import QueryClient


class OntologiesClient:
    def __init__(self, auth: Auth, hostname: str):
        self.Action = ActionClient(auth=auth, hostname=hostname)
        self.Ontology = OntologyClient(auth=auth, hostname=hostname)
        self.OntologyObject = OntologyObjectClient(auth=auth, hostname=hostname)
        self.Query = QueryClient(auth=auth, hostname=hostname)
