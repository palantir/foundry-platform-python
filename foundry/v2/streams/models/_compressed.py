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

import pydantic

Compressed = pydantic.StrictBool
"""
Compression helps reduce the size of the data being sent, resulting in lower network usage and
storage, at the cost of some additional CPU usage for compression and decompression. This stream type
is only recommended if your stream contains a high volume of repetitive strings and is experiencing poor
network bandwidth symptoms like non-zero lag, lower than expected throughput, or dropped records.
"""
