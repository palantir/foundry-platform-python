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


from typing import Optional

import pytest

from foundry_sdk._core.resource_iterator import AsyncResourceIterator
from foundry_sdk._core.resource_iterator import ResourceIterator

from .test_page_iterator import alist
from .test_page_iterator import create_async_page_func
from .test_page_iterator import create_page_func


def create_iterator(total_items: int, default_page_size: int):
    return ResourceIterator[int](create_page_func(total_items, default_page_size))


def create_async_iterator(total_items: int, default_page_size: int):
    return AsyncResourceIterator[int](create_async_page_func(total_items, default_page_size))


def test_empty_iterator():
    iterator = create_iterator(0, 5)
    assert iterator.data == []
    assert iterator.next_page_token is None
    assert list(iterator) == []


def test_iterator_with_one_item():
    iterator = create_iterator(1, 5)
    assert iterator.data == [0]
    assert iterator.next_page_token is None
    assert list(iterator) == [0]


def test_iterator_with_5_pages_of_5():
    iterator = create_iterator(25, 5)

    # Check it can traverse from page to page correctly
    # Page 1
    assert iterator.data == [0, 1, 2, 3, 4]
    assert iterator.next_page_token == "5"
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4
    assert iterator.data == [0, 1, 2, 3, 4]

    # Page 1
    assert next(iterator) == 5
    assert iterator.data == [5, 6, 7, 8, 9]
    assert iterator.next_page_token == "10"
    assert next(iterator) == 6
    assert next(iterator) == 7
    assert next(iterator) == 8
    assert next(iterator) == 9

    # Make sure it finishes the last 3 pages
    assert len(list(iterator)) == 15

    # And then confirm there is nothing left
    with pytest.raises(StopIteration):
        next(iterator)


@pytest.mark.asyncio(scope="session")
async def test_empty_async_iterator():
    iterator = create_async_iterator(0, 5)
    assert await iterator._page_iterator.get_data() == []
    assert await iterator._page_iterator.get_next_page_token() is None
    assert await alist(iterator) == []


@pytest.mark.asyncio(scope="session")
async def test_async_iterator_with_one_item():
    iterator = create_async_iterator(1, 5)
    assert await iterator._page_iterator.get_data() == [0]
    assert await iterator._page_iterator.get_next_page_token() is None
    assert await alist(iterator) == [0]


@pytest.mark.asyncio(scope="session")
async def test_async_iterator_with_5_pages_of_5():
    iterator = create_async_iterator(25, 5)

    # Check it can traverse from page to page correctly
    # Page 1
    assert await iterator.__anext__() == 0
    assert await iterator.__anext__() == 1
    assert await iterator.__anext__() == 2
    assert await iterator.__anext__() == 3
    assert await iterator.__anext__() == 4
    assert await iterator._page_iterator.get_data() == [0, 1, 2, 3, 4]

    # Page 1
    assert await iterator.__anext__() == 5
    assert await iterator.__anext__() == 6
    assert await iterator.__anext__() == 7
    assert await iterator.__anext__() == 8
    assert await iterator.__anext__() == 9
    assert await iterator._page_iterator.get_data() == [5, 6, 7, 8, 9]

    # Make sure it finishes the last 3 pages
    assert len(await alist(iterator)) == 15

    # And then confirm there is nothing left
    with pytest.raises(StopAsyncIteration):
        await iterator.__anext__()


def test_iterator_with_empty_page_in_middle():
    def page_func_with_empty_page(page_size: Optional[int], next_page_token: Optional[str]):
        """Page function that returns: [0,1,2], [], [3,4,5], None"""
        page_token = next_page_token or "page1"

        if page_token == "page1":
            return ("page2", [0, 1, 2])
        elif page_token == "page2":
            # Empty page but pagination continues
            return ("page3", [])
        elif page_token == "page3":
            return (None, [3, 4, 5])
        else:
            return (None, [])

    iterator = ResourceIterator[int](page_func_with_empty_page)

    # Should successfully iterate through all items, skipping the empty page
    result = list(iterator)
    assert result == [0, 1, 2, 3, 4, 5]


@pytest.mark.asyncio(scope="session")
async def test_async_iterator_with_empty_page_in_middle():
    async def async_page_func_with_empty_page(
        page_size: Optional[int], next_page_token: Optional[str]
    ):
        """Async page function that returns: [0,1,2], [], [3,4,5], None"""
        page_token = next_page_token or "page1"

        if page_token == "page1":
            return ("page2", [0, 1, 2])
        elif page_token == "page2":
            # Empty page but pagination continues
            return ("page3", [])
        elif page_token == "page3":
            return (None, [3, 4, 5])
        else:
            return (None, [])

    iterator = AsyncResourceIterator[int](async_page_func_with_empty_page)

    # Should successfully iterate through all items, skipping the empty page
    result = await alist(iterator)
    assert result == [0, 1, 2, 3, 4, 5]


def test_iterator_with_initial_page_token():
    def page_func(page_size: Optional[int], next_page_token: Optional[str]):
        """Page function that returns different data based on page_token"""
        page_token = next_page_token or "page1"

        if page_token == "page1":
            return ("page2", [0, 1, 2])
        elif page_token == "page2":
            return ("page3", [3, 4, 5])
        elif page_token == "page3":
            return (None, [6, 7, 8])
        else:
            return (None, [])

    # Start from page2 instead of page1
    iterator = ResourceIterator[int](page_func, page_token="page2")

    # Should only get items from page2 onwards: [3, 4, 5, 6, 7, 8]
    result = list(iterator)
    assert result == [3, 4, 5, 6, 7, 8]


@pytest.mark.asyncio(scope="session")
async def test_async_iterator_with_initial_page_token():
    async def async_page_func(page_size: Optional[int], next_page_token: Optional[str]):
        """Async page function that returns different data based on page_token"""
        page_token = next_page_token or "page1"

        if page_token == "page1":
            return ("page2", [0, 1, 2])
        elif page_token == "page2":
            return ("page3", [3, 4, 5])
        elif page_token == "page3":
            return (None, [6, 7, 8])
        else:
            return (None, [])

    # Start from page2 instead of page1
    iterator = AsyncResourceIterator[int](async_page_func, page_token="page2")

    # Should only get items from page2 onwards: [3, 4, 5, 6, 7, 8]
    result = await alist(iterator)
    assert result == [3, 4, 5, 6, 7, 8]
