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


from typing import Iterator


class BinaryStream(Iterator[bytes]):
    """A generic class for streaming binary data."""

    def __init__(self, iterator: Iterator[bytes]):
        self._iterator = iterator

    def __next__(self) -> bytes:
        return next(self._iterator)

    def __iter__(self) -> Iterator[bytes]:
        return self

    def read_all(self) -> bytes:
        """Read and concatenate all remaining chunks."""
        return b"".join(self._iterator)
