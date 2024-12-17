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


import warnings
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar

from .page_iterator import PageFunction
from .page_iterator import PageIterator

T = TypeVar("T")


class ResourceIterator(Generic[T]):
    """A generic class for iterating over paged responses."""

    def __init__(self, paged_func: PageFunction[T], page_size: Optional[int] = None) -> None:
        self._page_iterator = PageIterator(paged_func, page_size)
        self._index = 0

    @property
    def data(self) -> List[T]:
        return self._page_iterator.data

    @property
    def next_page_token(self) -> Optional[str]:
        return self._page_iterator.next_page_token

    @property
    def page_iterator(self):
        warnings.warn(
            "Accessing the page_iterator directly is deprecated. You can now access data and next_page_token directly on the ResourceIterator.",
            DeprecationWarning,
        )
        return self._page_iterator

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._page_iterator.data):
            self._get_data()

        obj = self._page_iterator.data[self._index]
        self._index += 1
        return obj

    def _get_data(self):
        try:
            next(self._page_iterator)
            self._index = 0
        except StopIteration:
            raise StopIteration("End of iteration reached")
