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

# coding: utf-8

"""
    Palantir OpenAPI

    The Palantir REST API. Please see https://www.palantir.com/docs for more details.

    The version of the OpenAPI document: 1.738.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TransactionStatus(str, Enum):
    """
    The status of a Transaction. 
    """

    """
    allowed enum values
    """
    ABORTED = 'ABORTED'
    COMMITTED = 'COMMITTED'
    OPEN = 'OPEN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionStatus from a JSON string"""
        return cls(json.loads(json_str))


