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


from foundry._namespaces.datasets.dataset import DatasetResource
from foundry._namespaces.datasets.branch import BranchResource
from foundry._namespaces.datasets.transaction import TransactionResource
from foundry._namespaces.datasets.file import FileResource
from foundry._namespaces.ontologies.ontology import OntologyResource
from foundry._namespaces.ontologies.objecttype import ObjectTypeResource
from foundry._namespaces.ontologies.actiontype import ActionTypeResource
from foundry._namespaces.ontologies.querytype import QueryTypeResource
from foundry._namespaces.ontologies.ontologyobject import OntologyObjectResource
from foundry._namespaces.ontologies.attachment import AttachmentResource
from foundry.api_client import ApiClient


class Datasets:
    def __init__(self, api_client: ApiClient):
        self.Dataset = DatasetResource(api_client=api_client)
        self.Branch = BranchResource(api_client=api_client)
        self.Transaction = TransactionResource(api_client=api_client)
        self.File = FileResource(api_client=api_client)


class Ontologies:
    def __init__(self, api_client: ApiClient):
        self.Ontology = OntologyResource(api_client=api_client)
        self.ObjectType = ObjectTypeResource(api_client=api_client)
        self.ActionType = ActionTypeResource(api_client=api_client)
        self.QueryType = QueryTypeResource(api_client=api_client)
        self.OntologyObject = OntologyObjectResource(api_client=api_client)
        self.Attachment = AttachmentResource(api_client=api_client)
