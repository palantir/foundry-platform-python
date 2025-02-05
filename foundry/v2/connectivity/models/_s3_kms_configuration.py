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
from typing import cast

import pydantic

from foundry.v2.connectivity.models._region import Region
from foundry.v2.connectivity.models._s3_kms_configuration_dict import S3KmsConfigurationDict  # NOQA


class S3KmsConfiguration(pydantic.BaseModel):
    """S3KmsConfiguration"""

    kms_key: str = pydantic.Field(alias=str("kmsKey"))  # type: ignore[literal-required]

    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    kms_region: Optional[Region] = pydantic.Field(alias=str("kmsRegion"), default=None)  # type: ignore[literal-required]

    """
    The region of the client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key region for the bucket is used.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> S3KmsConfigurationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(S3KmsConfigurationDict, self.model_dump(by_alias=True, exclude_none=True))
