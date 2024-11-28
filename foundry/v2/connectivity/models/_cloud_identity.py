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

from typing import Literal
from typing import cast

import pydantic

from foundry.v2.connectivity.models._cloud_identity_dict import CloudIdentityDict
from foundry.v2.connectivity.models._cloud_identity_rid import CloudIdentityRid


class CloudIdentity(pydantic.BaseModel):
    """
    [Cloud identities](/docs/foundry/administration/configure-cloud-identities/) allow you to authenticate to
    cloud provider resources without the use of static credentials.
    """

    cloud_identity_rid: CloudIdentityRid = pydantic.Field(alias="cloudIdentityRid")

    type: Literal["cloudIdentity"] = "cloudIdentity"

    model_config = {"extra": "allow"}

    def to_dict(self) -> CloudIdentityDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(CloudIdentityDict, self.model_dump(by_alias=True, exclude_unset=True))
