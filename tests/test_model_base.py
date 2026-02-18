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
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

import pytest

from foundry_sdk._core import ModelBase


def test_can_be_used_as_dict_key() -> None:
    """Test that ModelBase objects can be used as dictionary keys."""

    class TestModel(ModelBase):
        name: str
        age: int

    model1 = TestModel(name="Alice", age=30)
    model2 = TestModel(name="Alice", age=30)  # Same data as model1
    model3 = TestModel(name="Bob", age=25)  # Different data

    # Models with same content should be equal
    assert model1 == model2
    assert model1 != model3

    # Models with same content should have same hash
    assert hash(model1) == hash(model2)
    assert hash(model1) != hash(model3)

    # Use models as dict keys
    data = {}
    data[model1] = "First model"
    data[model3] = "Third model"

    # Should retrieve by equivalent object
    assert data[model2] == "First model"
    assert len(data) == 2


def test_hash_value_cached() -> None:
    """Test that hash value is calculated only once and cached."""

    class SimpleModel(ModelBase):
        value: str

    model = SimpleModel(value="test")

    # Access hash first time - should calculate
    hash1 = hash(model)

    # Access hash second time - should use cached value
    hash2 = hash(model)

    assert hash1 == hash2
    assert model._hash_called is True
    assert model._hash_value == hash1


def test_warns_on_mutation_after_hash() -> None:
    """Test that a warning is issued when a model is modified after being hashed."""

    class MutableModel(ModelBase):
        value: str
        count: int = 0

    model = MutableModel(value="original")

    # Use as dict key to trigger hash calculation
    data = {model: "some value"}

    # Should warn when modified after hash
    with pytest.warns(
        UserWarning, match="Modifying MutableModel after it has been used as a dictionary key"
    ):
        model.value = "changed"

    # Hash value should be reset
    assert model._hash_value is None

    # Re-hashing should work
    _new_hash = hash(model)

    # But we can add it back
    data[model] = "updated value"
    assert data[model] == "updated value"


def test_hash_includes_class_identity() -> None:
    """Test that models with identical attributes but different classes have different hashes."""

    class UserModel(ModelBase):
        name: str
        age: int

    class PersonModel(ModelBase):
        name: str
        age: int

    user = UserModel(name="Alice", age=30)
    person = PersonModel(name="Alice", age=30)

    # Despite having identical attributes, hashes should differ due to class identity
    assert hash(user) != hash(person)

    # Dictionaries should treat them as separate keys
    data: dict[ModelBase, str] = {}
    data[user] = "User data"
    data[person] = "Person data"

    assert len(data) == 2
    assert data[user] == "User data"
    assert data[person] == "Person data"


def test_hash_with_different_data_structures() -> None:
    """Test that models with different data structures hash correctly."""

    class StructuredModel(ModelBase):
        tuple_field: Tuple[str, int]
        list_field: List[str]
        dict_field: Dict[str, Any]
        set_field: Set[int]

    model1 = StructuredModel(
        tuple_field=("hello", 42),
        list_field=["a", "b", "c"],
        dict_field={"key1": "value1", "key2": 123},
        set_field={1, 2, 3},
    )

    model2 = StructuredModel(
        tuple_field=("hello", 42),
        list_field=["a", "b", "c"],
        dict_field={"key1": "value1", "key2": 123},
        set_field={1, 2, 3},
    )

    # Models with identical content should have same hash
    assert hash(model1) == hash(model2)

    # Changing a tuple element should result in a different hash
    model3 = StructuredModel(
        tuple_field=("world", 42),  # Different first element
        list_field=["a", "b", "c"],
        dict_field={"key1": "value1", "key2": 123},
        set_field={1, 2, 3},
    )
    assert hash(model1) != hash(model3)

    # Changing list order should result in a different hash
    model4 = StructuredModel(
        tuple_field=("hello", 42),
        list_field=["a", "c", "b"],  # Different order
        dict_field={"key1": "value1", "key2": 123},
        set_field={1, 2, 3},
    )
    assert hash(model1) != hash(model4)

    # Adding a dict key should result in a different hash
    model5 = StructuredModel(
        tuple_field=("hello", 42),
        list_field=["a", "b", "c"],
        dict_field={"key1": "value1", "key2": 123, "key3": True},  # Additional key
        set_field={1, 2, 3},
    )
    assert hash(model1) != hash(model5)

    # Changing set elements should result in a different hash
    model6 = StructuredModel(
        tuple_field=("hello", 42),
        list_field=["a", "b", "c"],
        dict_field={"key1": "value1", "key2": 123},
        set_field={1, 2, 4},  # 3 replaced with 4
    )
    assert hash(model1) != hash(model6)


def test_hash_with_nested_models() -> None:
    """Test that models with nested model structures hash correctly."""

    class Address(ModelBase):
        street: str
        city: str
        postal_code: Optional[str] = None

    class Person(ModelBase):
        name: str
        address: Address
        tags: List[str]
        metadata: Dict[str, Any]

    # Create two models with identical nested structures
    address1 = Address(street="123 Main St", city="Springfield")
    person1 = Person(
        name="Alice",
        address=address1,
        tags=["employee", "manager"],
        metadata={"id": 123, "active": True},
    )

    address2 = Address(street="123 Main St", city="Springfield")
    person2 = Person(
        name="Alice",
        address=address2,
        tags=["employee", "manager"],
        metadata={"id": 123, "active": True},
    )

    # Different address object but same content
    assert address1 is not address2

    # Models with identical content (including nested structures) should have same hash
    assert hash(person1) == hash(person2)

    # Test a model with a different nested model
    person3 = Person(
        name="Alice",
        address=Address(street="456 Elm St", city="Springfield"),  # Different street
        tags=["employee", "manager"],
        metadata={"id": 123, "active": True},
    )

    assert hash(person1) != hash(person3)

    # Test a model with nullable nested fields
    address_with_postal = Address(street="123 Main St", city="Springfield", postal_code="12345")
    person_with_postal = Person(
        name="Alice",
        address=address_with_postal,
        tags=["employee", "manager"],
        metadata={"id": 123, "active": True},
    )

    assert hash(person1) != hash(person_with_postal)

    # Test with deeply nested structures
    deeply_nested_person = Person(
        name="Bob",
        address=address1,
        tags=["employee", "manager"],
        metadata={
            "id": 456,
            "active": True,
            "history": {
                "previous_roles": ["intern", "associate"],
                "performance": {"2022": "Excellent", "2023": "Outstanding"},
            },
        },
    )

    # Should be hashable despite complex nested structure
    hash_value = hash(deeply_nested_person)
    assert isinstance(hash_value, int)

    # Two identical deep structures should hash the same
    deeply_nested_person2 = Person(
        name="Bob",
        address=address1,
        tags=["employee", "manager"],
        metadata={
            "id": 456,
            "active": True,
            "history": {
                "previous_roles": ["intern", "associate"],
                "performance": {"2022": "Excellent", "2023": "Outstanding"},
            },
        },
    )

    assert hash(deeply_nested_person) == hash(deeply_nested_person2)
