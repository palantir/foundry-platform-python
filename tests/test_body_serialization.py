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


import json
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

import pydantic
import pytest

from foundry_sdk._core.api_client import BaseApiClient


# Test models for serialization
class SimpleModel(pydantic.BaseModel):
    name: str
    count: int


class ComplexModel(pydantic.BaseModel):
    id: str
    date: datetime
    nested: SimpleModel
    tags: List[str] = []
    optional_field: Optional[int] = None


class ModelWithArray(pydantic.BaseModel):
    id: str
    items: List[SimpleModel]


class ModelWithOptionalArray(pydantic.BaseModel):
    id: str
    items: Optional[List[SimpleModel]] = None


class ModelWithNestedArrays(pydantic.BaseModel):
    id: str
    matrix: List[List[SimpleModel]]


# Create a test client for serialization tests
class TestApiClient(BaseApiClient):
    """A minimal implementation for testing the serialization logic"""

    def __init__(self):
        pass  # Skip the standard initialization


# Helper function to serialize and then deserialize back to verify correctness
def serialize_and_deserialize(client: TestApiClient, data: Any) -> Any:
    """
    Serialize data using the client's _serialize method and then deserialize it back to a generic Python object (e.g., dict or list).
    Note: This does NOT reconstruct the original input type if it was a custom class.
    """
    serialized = client._serialize(data)
    # If None is returned, it means the data was None
    if serialized is None:
        return None
    # Decode the bytes and parse as JSON
    return json.loads(serialized.decode("utf-8"))


# ----- Basic Serialization Tests -----


def test_serialize_none():
    """Test serializing None value."""
    client = TestApiClient()
    result = client._serialize(None)
    assert result is None


def test_serialize_bytes():
    """Test that bytes are passed through as-is."""
    client = TestApiClient()
    raw_bytes = b"raw byte content"
    result = client._serialize(raw_bytes)
    assert result is raw_bytes  # Should return the same bytes object


def test_serialize_primitive_types():
    """Test serializing primitive JSON types."""
    client = TestApiClient()

    # String
    assert json.loads((client._serialize("test string") or b"").decode()) == "test string"

    # Number
    assert json.loads((client._serialize(42) or b"").decode()) == 42
    assert json.loads((client._serialize(3.14) or b"").decode()) == 3.14

    # Boolean
    assert json.loads((client._serialize(True) or b"").decode())
    assert not json.loads((client._serialize(False) or b"").decode())

    # Array of primitives
    assert json.loads((client._serialize([1, 2, 3]) or b"").decode()) == [1, 2, 3]

    # Object of primitives
    assert json.loads((client._serialize({"key": "value"}) or b"").decode()) == {"key": "value"}


# ----- Pydantic BaseModel Serialization Tests -----


def test_serialize_simple_model():
    """Test serializing a single simple Pydantic model."""
    client = TestApiClient()
    model = SimpleModel(name="test", count=42)

    result = serialize_and_deserialize(client, model)
    assert result == {"name": "test", "count": 42}


def test_serialize_complex_model():
    """Test serializing a complex Pydantic model with nested objects."""
    client = TestApiClient()

    now = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    model = ComplexModel(
        id="test-id", date=now, nested=SimpleModel(name="nested", count=10), tags=["tag1", "tag2"]
    )

    result = serialize_and_deserialize(client, model)
    assert result == {
        "id": "test-id",
        "date": "2023-01-01T12:00:00+00:00",
        "nested": {"name": "nested", "count": 10},
        "tags": ["tag1", "tag2"],
    }

    # Optional fields that are None should be excluded
    assert "optional_field" not in result


def test_serialize_model_with_none_fields():
    """Test that None fields are properly excluded from serialization."""
    client = TestApiClient()

    model = ComplexModel(
        id="test-id",
        date=datetime(2023, 1, 1, tzinfo=timezone.utc),
        nested=SimpleModel(name="nested", count=10),
        optional_field=None,
    )

    result = serialize_and_deserialize(client, model)
    assert "optional_field" not in result


# ----- Array Serialization Tests -----


def test_serialize_array_of_models():
    """Test serializing an array of Pydantic models."""
    client = TestApiClient()

    models = [
        SimpleModel(name="item1", count=1),
        SimpleModel(name="item2", count=2),
        SimpleModel(name="item3", count=3),
    ]

    result = serialize_and_deserialize(client, models)
    assert result == [
        {"name": "item1", "count": 1},
        {"name": "item2", "count": 2},
        {"name": "item3", "count": 3},
    ]


def test_serialize_empty_array():
    """Test serializing an empty array."""
    client = TestApiClient()
    result = serialize_and_deserialize(client, [])
    assert result == []


def test_serialize_array_with_none():
    """Test serializing an array containing None values."""
    client = TestApiClient()

    # Array with None values
    data = [SimpleModel(name="item1", count=1), None, SimpleModel(name="item3", count=3)]

    result = serialize_and_deserialize(client, data)
    assert result == [{"name": "item1", "count": 1}, None, {"name": "item3", "count": 3}]


def test_serialize_mixed_array():
    """Test serializing a mixed array with different types including models."""
    client = TestApiClient()

    data = ["string", 42, {"key": "value"}, SimpleModel(name="model", count=1), [1, 2, 3]]

    result = serialize_and_deserialize(client, data)
    assert result == ["string", 42, {"key": "value"}, {"name": "model", "count": 1}, [1, 2, 3]]


# ----- Nested Structure Serialization Tests -----


def test_serialize_model_with_array():
    """Test serializing a model that contains an array of models."""
    client = TestApiClient()

    model = ModelWithArray(
        id="test-id", items=[SimpleModel(name="item1", count=1), SimpleModel(name="item2", count=2)]
    )

    result = serialize_and_deserialize(client, model)
    assert result == {
        "id": "test-id",
        "items": [{"name": "item1", "count": 1}, {"name": "item2", "count": 2}],
    }


def test_serialize_model_with_optional_array_present():
    """Test serializing a model with an optional array that is present."""
    client = TestApiClient()

    model = ModelWithOptionalArray(id="test-id", items=[SimpleModel(name="item", count=1)])

    result = serialize_and_deserialize(client, model)
    assert result == {"id": "test-id", "items": [{"name": "item", "count": 1}]}


def test_serialize_model_with_optional_array_none():
    """Test serializing a model with an optional array that is None."""
    client = TestApiClient()

    model = ModelWithOptionalArray(id="test-id")  # items defaults to None

    result = serialize_and_deserialize(client, model)
    assert result == {"id": "test-id"}
    assert "items" not in result


def test_serialize_model_with_nested_arrays():
    """Test serializing a model with nested arrays of models."""
    client = TestApiClient()

    model = ModelWithNestedArrays(
        id="test-id",
        matrix=[
            [SimpleModel(name="1,1", count=11), SimpleModel(name="1,2", count=12)],
            [SimpleModel(name="2,1", count=21), SimpleModel(name="2,2", count=22)],
        ],
    )

    result = serialize_and_deserialize(client, model)
    assert result == {
        "id": "test-id",
        "matrix": [
            [{"name": "1,1", "count": 11}, {"name": "1,2", "count": 12}],
            [{"name": "2,1", "count": 21}, {"name": "2,2", "count": 22}],
        ],
    }


def test_serialize_deeply_nested_structure():
    """Test serializing a deeply nested structure with models at various levels."""
    client = TestApiClient()

    data = {
        "top_level": SimpleModel(name="top", count=1),
        "nested": {
            "model": SimpleModel(name="nested", count=2),
            "list": [SimpleModel(name="list1", count=3), SimpleModel(name="list2", count=4)],
        },
        "matrix": [
            [SimpleModel(name="m11", count=11), SimpleModel(name="m12", count=12)],
            [SimpleModel(name="m21", count=21), SimpleModel(name="m22", count=22)],
        ],
        "mixed": [
            {"model": SimpleModel(name="mixed", count=5)},
            [SimpleModel(name="array", count=6)],
        ],
    }

    result = serialize_and_deserialize(client, data)
    assert result == {
        "top_level": {"name": "top", "count": 1},
        "nested": {
            "model": {"name": "nested", "count": 2},
            "list": [{"name": "list1", "count": 3}, {"name": "list2", "count": 4}],
        },
        "matrix": [
            [{"name": "m11", "count": 11}, {"name": "m12", "count": 12}],
            [{"name": "m21", "count": 21}, {"name": "m22", "count": 22}],
        ],
        "mixed": [{"model": {"name": "mixed", "count": 5}}, [{"name": "array", "count": 6}]],
    }


# ----- Dictionary Serialization Tests -----


def test_serialize_dict_with_model_values():
    """Test serializing a dictionary with model values."""
    client = TestApiClient()

    data = {
        "model1": SimpleModel(name="first", count=1),
        "model2": SimpleModel(name="second", count=2),
    }

    result = serialize_and_deserialize(client, data)
    assert result == {
        "model1": {"name": "first", "count": 1},
        "model2": {"name": "second", "count": 2},
    }


def test_serialize_dict_with_mixed_values():
    """Test serializing a dictionary with a mix of model and non-model values."""
    client = TestApiClient()

    data = {
        "model": SimpleModel(name="model", count=1),
        "string": "text value",
        "number": 42,
        "boolean": True,
        "array": [1, 2, 3],
        "nested_array": [SimpleModel(name="nested", count=2)],
    }

    result = serialize_and_deserialize(client, data)
    assert result == {
        "model": {"name": "model", "count": 1},
        "string": "text value",
        "number": 42,
        "boolean": True,
        "array": [1, 2, 3],
        "nested_array": [{"name": "nested", "count": 2}],
    }


def test_serialize_dict_with_nested_dicts():
    """Test serializing a dictionary with nested dictionaries containing models."""
    client = TestApiClient()

    data = {"level1": {"level2": {"model": SimpleModel(name="deeply_nested", count=42)}}}

    result = serialize_and_deserialize(client, data)
    assert result == {"level1": {"level2": {"model": {"name": "deeply_nested", "count": 42}}}}


# ----- Special Cases and Edge Cases -----


def test_serialize_model_with_alias():
    """Test serializing a model with field aliases."""
    client = TestApiClient()

    class ModelWithAlias(pydantic.BaseModel):
        user_id: str = pydantic.Field(alias="userId")
        created_at: datetime = pydantic.Field(alias="createdAt")

    model = ModelWithAlias(userId="test-user", createdAt=datetime(2023, 1, 1, tzinfo=timezone.utc))

    result = serialize_and_deserialize(client, model)
    # Should use the aliases in the output JSON
    assert "userId" in result
    assert "createdAt" in result
    assert "user_id" not in result
    assert "created_at" not in result


def test_serialize_cyclic_references():
    """Test that serializing cyclic references raises an exception."""
    client = TestApiClient()

    # Create a cyclic reference
    a = {}
    b = {"a": a}
    a["b"] = b

    with pytest.raises((TypeError, ValueError)):
        client._serialize(a)


def test_serialize_datetime_values():
    """Test serializing datetime values in models."""
    client = TestApiClient()

    # UTC datetime
    utc_dt = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    model = ComplexModel(id="test", date=utc_dt, nested=SimpleModel(name="test", count=1))

    result = serialize_and_deserialize(client, model)
    assert result["date"] == "2023-01-01T12:00:00+00:00"

    # Non-UTC datetime
    est_tz = timezone(timedelta(hours=-5))
    est_dt = datetime(2023, 1, 1, 7, 0, 0, tzinfo=est_tz)
    model = ComplexModel(id="test", date=est_dt, nested=SimpleModel(name="test", count=1))

    result = serialize_and_deserialize(client, model)
    # Should be normalized to UTC in ISO format
    assert result["date"] == "2023-01-01T12:00:00+00:00"


def test_serialize_real_world_complex_payload():
    """Test serializing a complex real-world-like request payload."""
    client = TestApiClient()

    # Create a complex nested payload similar to what might be used in a real API
    class Address(pydantic.BaseModel):
        street: str
        city: str
        postal_code: str
        country: str

    class Contact(pydantic.BaseModel):
        email: str
        phone: Optional[str] = None

    class User(pydantic.BaseModel):
        id: str
        name: str
        address: Address
        contacts: List[Contact]
        is_active: bool = True
        created_at: datetime
        last_login: Optional[datetime] = None
        preferences: Dict[str, Any] = {}

    class OrderItem(pydantic.BaseModel):
        product_id: str = pydantic.Field(alias="productId")
        quantity: int
        unit_price: float = pydantic.Field(alias="unitPrice")

    class Order(pydantic.BaseModel):
        id: str
        user: User
        items: List[OrderItem]
        total_amount: float = pydantic.Field(alias="totalAmount")
        status: Literal["pending", "processing", "shipped", "delivered"]
        shipping_address: Optional[Address] = pydantic.Field(alias="shippingAddress", default=None)

    # Create an instance with deeply nested structure
    order = Order(
        id="order-123",
        user=User(
            id="user-456",
            name="John Doe",
            address=Address(
                street="123 Main St", city="Anytown", postal_code="12345", country="USA"
            ),
            contacts=[
                Contact(email="john@example.com", phone="+1234567890"),
                Contact(email="johndoe@work.com"),
            ],
            created_at=datetime(2022, 1, 1, tzinfo=timezone.utc),
            preferences={"theme": "dark", "notifications": True},
        ),
        items=[
            OrderItem(productId="prod-1", quantity=2, unitPrice=29.99),
            OrderItem(productId="prod-2", quantity=1, unitPrice=49.99),
        ],
        totalAmount=109.97,
        status="processing",
        shippingAddress=Address(
            street="456 Shipping Ave", city="Shipville", postal_code="54321", country="USA"
        ),
    )

    result = serialize_and_deserialize(client, order)

    # Validate the structure and content of the serialized data
    assert result["id"] == "order-123"
    assert result["user"]["name"] == "John Doe"
    assert result["user"]["address"]["city"] == "Anytown"
    assert result["user"]["contacts"][0]["email"] == "john@example.com"
    assert result["user"]["contacts"][1].get("phone") is None
    assert result["items"][0]["productId"] == "prod-1"
    assert result["totalAmount"] == 109.97
    assert result["status"] == "processing"
    assert result["shippingAddress"]["street"] == "456 Shipping Ave"

    # Check that aliases are properly used
    assert "productId" in result["items"][0]
    assert "product_id" not in result["items"][0]
    assert "totalAmount" in result
    assert "total_amount" not in result
    assert "shippingAddress" in result
    assert "shipping_address" not in result
