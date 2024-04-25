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

from typing import Annotated
from typing import Union

from pydantic import Field

from foundry.models._attachment_v2 import AttachmentV2
from foundry.models._list_attachments_response_v2 import ListAttachmentsResponseV2

AttachmentMetadataResponse = Annotated[
    Union[AttachmentV2, ListAttachmentsResponseV2], Field(discriminator="type")
]
"""The attachment metadata response"""
