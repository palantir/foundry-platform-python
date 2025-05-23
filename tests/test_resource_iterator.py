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
from typing import Optional

import pytest

from foundry_sdk._core.resource_iterator import AsyncResourceIterator
from foundry_sdk._core.resource_iterator import ResourceIterator
from tests.test_page_iterator import alist
from tests.test_page_iterator import create_async_page_func
from tests.test_page_iterator import create_page_func


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
