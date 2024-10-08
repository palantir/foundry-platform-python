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


import json
from typing import Any
from typing import Dict


def format_error_message(fields: Dict[str, Any]) -> str:
    return json.dumps(fields, sort_keys=True, indent=4, default=str)


class PalantirRPCException(Exception):
    def __init__(self, error_metadata: Dict[str, Any]):
        super().__init__(format_error_message(error_metadata))
        self.name = error_metadata.get("errorName")
        self.parameters = error_metadata.get("parameters")
        self.error_instance_id = error_metadata.get("errorInstanceId")
