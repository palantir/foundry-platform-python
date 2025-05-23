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


from typing import Awaitable
from typing import Generic
from typing import List
from typing import Optional
from typing import Protocol
from typing import Tuple
from typing import TypeVar

T = TypeVar("T")


class PageFunction(Generic[T], Protocol):
    def __call__(
        self, page_size: Optional[int], next_page_token: Optional[str]
    ) -> Tuple[Optional[str], List[T]]: ...


class AsyncPageFunction(Generic[T], Protocol):
    def __call__(
        self, page_size: Optional[int], next_page_token: Optional[str]
    ) -> Awaitable[Tuple[Optional[str], List[T]]]: ...


class PageIterator(Generic[T]):
    """A generic class for iterating over paged responses."""

    def __init__(
        self,
        paged_func: PageFunction[T],
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> None:
        self._page_size: Optional[int] = page_size
        self._paged_func: PageFunction[T] = paged_func
        self._next_page_token: Optional[str] = page_token
        self._has_next = True
        self._data: List[T] = []
        self._get_data()

    @property
    def next_page_token(self):
        return self._next_page_token

    @property
    def data(self):
        return self._data

    def __iter__(self):
        return self

    def __next__(self):
        if self._data == [] or not self._has_next:
            raise StopIteration("End of iteration reached")

        data = self._data
        self._get_data()
        return data

    def _get_data(self):
        if self._has_next:
            self._next_page_token, self._data = self._paged_func(
                page_size=self._page_size, next_page_token=self._next_page_token
            )
            self._has_next = self._next_page_token is not None
        else:
            self._data = []


class AsyncPageIterator(Generic[T]):
    """A generic class for iterating over paged responses."""

    def __init__(
        self,
        paged_func: AsyncPageFunction[T],
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> None:
        self._page_size: Optional[int] = page_size
        self._paged_func: AsyncPageFunction[T] = paged_func
        self._next_page_token: Optional[str] = page_token
        self._yielded_first = False
        self._data: Optional[List[T]] = None

    async def get_next_page_token(self):
        """
        Get the next page token. If the first page has not been fetched, it will be
        loaded first.
        """
        await self.get_data()
        return self._next_page_token

    async def get_data(self):
        """
        Get the current page of data. If the first page has not been fetched, it will be
        loaded first.
        """
        if self._data is None:
            await self._get_data()

        # This should never be None, but mypy doesn't know that
        assert self._data is not None
        return self._data

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._yielded_first and self._next_page_token is None:
            raise StopAsyncIteration("End of iteration reached")

        if not self._yielded_first:
            self._yielded_first = True

            # Unlike the PageIterator, the AsyncPageIterator cannot
            # fetch data in the constructor because it is async
            if self._data is None:
                await self._get_data()
        else:
            await self._get_data()

        # This should never be None, but mypy doesn't know that
        assert self._data is not None
        return self._data

    async def _get_data(self):
        self._next_page_token, self._data = await self._paged_func(
            page_size=self._page_size,
            next_page_token=self._next_page_token,
        )
