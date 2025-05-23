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


from typing import Any
from typing import AsyncIterator
from typing import Optional

import pytest

from foundry_sdk._core.page_iterator import AsyncPageIterator
from foundry_sdk._core.page_iterator import PageIterator


def create_page_func(total_items: int, default_page_size: int):
    def page_function(page_size: Optional[int], next_page_token: Optional[str]):
        page_size = page_size or default_page_size
        next_page_token_int = int(next_page_token or "0")

        items = list(range(next_page_token_int, min(next_page_token_int + page_size, total_items)))
        next_page_token = (
            str(next_page_token_int + page_size)
            if next_page_token_int + page_size < total_items
            else None
        )

        return (next_page_token, items)

    return page_function


def create_async_page_func(total_items: int, default_page_size: int):
    async def page_function(page_size: Optional[int], next_page_token: Optional[str]):
        page_size = page_size or default_page_size
        next_page_token_int = int(next_page_token or "0")

        items = list(range(next_page_token_int, min(next_page_token_int + page_size, total_items)))
        next_page_token = (
            str(next_page_token_int + page_size)
            if next_page_token_int + page_size < total_items
            else None
        )

        return (next_page_token, items)

    return page_function


def create_iterator(total_items: int, default_page_size: int):
    return PageIterator[int](create_page_func(total_items, default_page_size))


def create_async_iterator(total_items: int, default_page_size: int):
    return AsyncPageIterator[int](create_async_page_func(total_items, default_page_size))


def test_empty_iterator():
    iterator = create_iterator(0, 5)
    assert iterator.data == []
    assert iterator.next_page_token is None
    assert list(iterator) == []


def test_iterator_with_one_item():
    iterator = create_iterator(1, 5)
    assert iterator.data == [0]
    assert iterator.next_page_token is None
    assert list(iterator) == []


def test_iterator_with_5_pages_of_5():
    iterator = create_iterator(25, 5)

    assert iterator.data == [0, 1, 2, 3, 4]
    assert iterator.next_page_token == "5"
    assert next(iterator) == [0, 1, 2, 3, 4]
    assert iterator.next_page_token == "10"

    assert next(iterator) == [5, 6, 7, 8, 9]
    assert iterator.next_page_token == "15"

    # Make sure it finishes the last 2 pages
    assert len(list(iterator)) == 2

    # And then confirm there is nothing left
    with pytest.raises(StopIteration):
        next(iterator)


async def alist(iterator: AsyncIterator[Any]) -> Any:
    return [gen async for gen in iterator]


@pytest.mark.asyncio(scope="session")
async def test_empty_async_iterator():
    iterator = create_async_iterator(0, 5)
    assert await iterator.get_data() == []
    assert await iterator.get_next_page_token() is None
    assert await alist(iterator) == [[]]


@pytest.mark.asyncio(scope="session")
async def test_async_iterator_with_one_item():
    iterator = create_async_iterator(1, 5)
    assert await iterator.get_data() == [0]
    assert await iterator.get_next_page_token() is None
    assert await alist(iterator) == [[0]]


@pytest.mark.asyncio(scope="session")
async def test_async_iterator_with_5_pages_of_5():
    iterator = create_async_iterator(25, 5)

    assert await iterator.get_data() == [0, 1, 2, 3, 4]
    assert await iterator.get_next_page_token() == "5"
    assert await iterator.__anext__() == [0, 1, 2, 3, 4]
    assert await iterator.get_next_page_token() == "5"

    assert await iterator.__anext__() == [5, 6, 7, 8, 9]
    assert await iterator.get_next_page_token() == "10"

    # Make sure it finishes the last 3 pages
    assert len(await alist(iterator)) == 3

    # And then confirm there is nothing left
    with pytest.raises(StopAsyncIteration):
        await iterator.__anext__()
