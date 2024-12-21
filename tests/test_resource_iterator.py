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

from foundry._core.resource_iterator import ResourceIterator


def test_empty_iterator():
    iterator = ResourceIterator[int](lambda page_size, next_page_token: (None, []))
    assert iterator.data == []
    assert iterator.next_page_token is None
    assert list(iterator) == []


def test_iterator_with_one_item():
    iterator = ResourceIterator[int](lambda page_size, next_page_token: (None, [0]))
    assert iterator.data == [0]
    assert iterator.next_page_token is None
    assert list(iterator) == [0]


def test_iterator_with_5_pages_of_5():
    def page_function(page_size: Optional[int], next_page_token: Optional[str]):
        next_page_token_int = int(next_page_token or "0")
        return (
            str(next_page_token_int + 1) if next_page_token_int < 4 else None,
            [next_page_token_int * 5 + i for i in range(5)],
        )

    iterator = ResourceIterator[int](page_function)

    # Check it can traverse from page to page correctly
    # Page 1
    assert iterator.data == [0, 1, 2, 3, 4]
    assert iterator.next_page_token == "1"
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4
    assert iterator.data == [0, 1, 2, 3, 4]

    # Page 1
    assert next(iterator) == 5
    assert iterator.data == [5, 6, 7, 8, 9]
    assert iterator.next_page_token == "2"
    assert next(iterator) == 6
    assert next(iterator) == 7
    assert next(iterator) == 8
    assert next(iterator) == 9

    # Make sure it finishes the last 3 pages
    assert len(list(iterator)) == 15

    # And then confirm there is nothing left
    assert list(iterator) == []
    with pytest.raises(StopIteration):
        next(iterator)
