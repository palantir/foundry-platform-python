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

from foundry.v2.connectivity.models._aws_access_key_dict import AwsAccessKeyDict
from foundry.v2.connectivity.models._encrypted_property import EncryptedProperty


class AwsAccessKey(pydantic.BaseModel):
    """
    [Access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) are long-term
    credentials for an IAM user or the AWS account root user.
    Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and a secret access
    key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY). You must use both the access key ID and
    secret access key together to authenticate your requests.
    """

    access_key_id: str = pydantic.Field(alias=str("accessKeyId"))  # type: ignore[literal-required]

    secret_access_key: EncryptedProperty = pydantic.Field(alias=str("secretAccessKey"))  # type: ignore[literal-required]

    type: Literal["awsAccessKey"] = "awsAccessKey"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> AwsAccessKeyDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AwsAccessKeyDict, self.model_dump(by_alias=True, exclude_none=True))
