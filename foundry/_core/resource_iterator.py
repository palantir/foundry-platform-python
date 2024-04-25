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


from typing import Generic
from typing import Optional
from typing import TypeVar

from .page_iterator import PageFunction
from .page_iterator import PageIterator

T = TypeVar("T")


class ResourceIterator(Generic[T]):
    """A generic class for iterating over paged responses."""

    def __init__(self, paged_func: PageFunction[T], page_size: Optional[int] = None) -> None:
        self._page_iterator = PageIterator(paged_func, page_size)
        self._data = []
        self._index = 0

    @property
    def page_iterator(self):
        return self._page_iterator

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            self._get_data()

        obj = self._data[self._index]
        self._index += 1
        return obj

    def _get_data(self):
        try:
            self._data = next(self._page_iterator)
            self._index = 0
        except StopIteration:
            raise StopIteration("End of iteration reached")
