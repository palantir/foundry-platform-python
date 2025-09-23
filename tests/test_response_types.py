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


import decimal
import json
from datetime import date
from datetime import datetime
from datetime import timezone
from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import Literal
from typing import Optional
from typing import TypeVar
from typing import Union

import httpx
import pydantic
import pytest
from typing_extensions import Annotated

from foundry_sdk._core import ApiResponse
from foundry_sdk._core import RequestInfo
from foundry_sdk._core.utils import RID
from foundry_sdk._core.utils import UUID
from foundry_sdk._core.utils import AwareDatetime
from foundry_sdk._core.utils import Long
from tests.server import FooBar


# Simple BaseModel types for testing
class SimpleModel(pydantic.BaseModel):
    value: str


class ModelWithAnnotation(pydantic.BaseModel):
    value: Annotated[str, pydantic.Field(min_length=3)]


# Union type with discriminator
class RunningStatus(pydantic.BaseModel):
    type: Literal["RUNNING"] = "RUNNING"
    percent_complete: int


class FailedStatus(pydantic.BaseModel):
    type: Literal["FAILED"] = "FAILED"
    error_message: str


class CompletedStatus(pydantic.BaseModel):
    type: Literal["COMPLETED"] = "COMPLETED"
    result: str


# Define Status using Annotated for discriminator
Status = Annotated[
    Union[RunningStatus, FailedStatus, CompletedStatus],
    pydantic.Field(discriminator="type"),
]

# Optional Annotated Union
OptionalStatus = Optional[Status]


def create_response(response_type: Any, json_content: Any) -> ApiResponse:
    """Helper function to create ApiResponse objects for testing."""
    return ApiResponse(
        RequestInfo.with_defaults("GET", "/test/endpoint", response_type=response_type),
        httpx.Response(200, content=json.dumps(json_content).encode()),
    )


def create_bytes_response(response_type: Any, content: bytes) -> ApiResponse:
    """Helper function to create ApiResponse objects with raw bytes for testing."""
    return ApiResponse(
        RequestInfo.with_defaults("GET", "/test/endpoint", response_type=response_type),
        httpx.Response(200, content=content),
    )


# ----- Tests for Simple Types -----


def test_decode_bytes():
    """Test decoding raw bytes."""
    response = create_bytes_response(bytes, b"raw bytes content")
    result = response.decode()
    assert result == b"raw bytes content"
    assert isinstance(result, bytes)


def test_decode_optional_bytes_present():
    """Test decoding Optional[bytes] when content is present."""
    response = create_bytes_response(Optional[bytes], b"optional bytes content")
    result = response.decode()
    assert result == b"optional bytes content"
    assert isinstance(result, bytes)


def test_decode_optional_bytes_empty():
    """Test decoding Optional[bytes] when content is empty."""
    response = create_bytes_response(Optional[bytes], b"")
    result = response.decode()
    assert result is None


def test_decode_none():
    response = create_response(None, "foo")
    result = response.decode()
    assert result is None


def test_decode_any_type():
    """Test decoding Any."""
    json_data = {"key": "value", "number": 42}
    response = create_response(Any, json_data)
    result = response.decode()
    assert result == json_data

    json_data = {"key": "value", "number": 42}
    response = create_response(Annotated[Any, pydantic.Field(description="test")], json_data)
    result = response.decode()
    assert result == json_data


def test_decode_string():
    """Test decoding a string."""
    json_data = "string value"
    response = create_response(str, json_data)
    result = response.decode()
    assert result == json_data
    assert isinstance(result, str)


def test_decode_integer():
    """Test decoding an integer."""
    json_data = 42
    response = create_response(int, json_data)
    result = response.decode()
    assert result == json_data
    assert isinstance(result, int)


def test_decode_float():
    """Test decoding a float."""
    json_data = 42.5
    response = create_response(float, json_data)
    result = response.decode()
    assert result == json_data
    assert isinstance(result, float)


def test_decode_boolean():
    """Test decoding a boolean."""
    json_data = True
    response = create_response(bool, json_data)
    result = response.decode()
    assert result == json_data
    assert isinstance(result, bool)


def test_decode_literal():
    """Test decoding a literal type."""
    json_data = "option1"
    response = create_response(Literal["option1", "option2", "option3"], json_data)
    result = response.decode()
    assert result == json_data
    assert result == "option1"


# ----- Tests for Collection Types -----


def test_decode_list():
    """Test decoding a list of values."""
    json_data = ["item1", "item2", "item3"]
    response = create_response(List[str], json_data)
    result = response.decode()
    assert result == json_data
    assert isinstance(result, list)
    assert all(isinstance(item, str) for item in result)


def test_decode_list_of_models():
    """Test decoding a list of models."""
    json_data = [{"value": "test1"}, {"value": "test2"}]
    response = create_response(List[SimpleModel], json_data)
    result = response.decode()
    assert isinstance(result, list)
    assert all(isinstance(item, SimpleModel) for item in result)
    assert result[0].value == "test1"
    assert result[1].value == "test2"


def test_decode_annotated_list():
    """Test decoding a list with length annotations."""
    json_data = ["item1", "item2", "item3"]
    response = create_response(
        Annotated[List[str], pydantic.Field(min_length=1, max_length=10)],
        json_data,
    )
    result = response.decode()
    assert result == json_data
    assert isinstance(result, list)
    assert all(isinstance(item, str) for item in result)


def test_decode_dict():
    """Test decoding a dictionary."""
    json_data = {"key1": "value1", "key2": "value2"}
    response = create_response(Dict[str, str], json_data)
    result = response.decode()
    assert result == json_data
    assert isinstance(result, dict)
    assert all(isinstance(key, str) and isinstance(value, str) for key, value in result.items())


def test_decode_dict_with_model_values():
    """Test decoding a dictionary with model values."""
    json_data = {"key1": {"value": "test1"}, "key2": {"value": "test2"}}
    response = create_response(Dict[str, SimpleModel], json_data)
    result = response.decode()
    assert isinstance(result, dict)
    assert all(
        isinstance(key, str) and isinstance(value, SimpleModel) for key, value in result.items()
    )
    assert result["key1"].value == "test1"
    assert result["key2"].value == "test2"


# ----- Tests for Special Types -----


def test_decode_decimal():
    """Test decoding a decimal.Decimal."""
    json_data = "123.456"  # Decimals are serialized as strings
    response = create_response(decimal.Decimal, json_data)
    result = response.decode()
    assert isinstance(result, decimal.Decimal)
    assert result == decimal.Decimal("123.456")


def test_decode_datetime():
    """Test decoding an AwareDatetime."""
    json_data = "2023-01-01T12:00:00Z"
    response = create_response(AwareDatetime, json_data)
    result = response.decode()
    assert isinstance(result, datetime)
    assert result.tzinfo is not None  # Ensure it's timezone aware
    assert result.year == 2023
    assert result.month == 1
    assert result.day == 1
    assert result.hour == 12


def test_decode_date():
    """Test decoding a date."""
    json_data = "2023-01-01"
    response = create_response(date, json_data)
    result = response.decode()
    assert isinstance(result, date)
    assert result.year == 2023
    assert result.month == 1
    assert result.day == 1


def test_decode_rid():
    """Test decoding a RID."""
    json_data = "ri.foundry.main.dataset.1234abcd"
    response = create_response(RID, json_data)
    result = response.decode()
    assert isinstance(result, str)
    assert result == json_data


def test_decode_uuid():
    """Test decoding a UUID."""
    json_data = "123e4567-e89b-12d3-a456-426614174000"
    response = create_response(UUID, json_data)
    result = response.decode()
    assert isinstance(result, str)
    assert result == json_data


def test_decode_long():
    """Test decoding a Long."""
    # Long values are typically integers that get serialized as strings in JSON
    json_data = "9223372036854775807"  # Max int64 value
    response = create_response(Long, json_data)
    result = response.decode()
    assert isinstance(result, int)
    assert result == 9223372036854775807


# ----- Tests for Pydantic Models -----


def test_decode_base_model():
    """Test decoding a simple BaseModel."""
    json_data = {"value": "test string"}
    response = create_response(SimpleModel, json_data)
    result = response.decode()
    assert isinstance(result, SimpleModel)
    assert result.value == "test string"


def test_decode_optional_base_model_present():
    """Test decoding Optional[BaseModel] when content is present."""
    json_data = {"value": "test string"}
    response = create_response(Optional[SimpleModel], json_data)
    result = response.decode()
    assert isinstance(result, SimpleModel)
    assert result.value == "test string"


def test_decode_optional_base_model_empty():
    """Test decoding Optional[BaseModel] when content is empty."""
    response = create_bytes_response(Optional[SimpleModel], b"")
    result = response.decode()
    assert result is None


def test_decode_annotated_base_model():
    """Test decoding an Annotated BaseModel."""
    json_data = {"value": "test string"}
    response = create_response(
        Annotated[SimpleModel, pydantic.Field(description="A test model")],
        json_data,
    )
    result = response.decode()
    assert isinstance(result, SimpleModel)
    assert result.value == "test string"


def test_decode_model_with_annotation():
    """Test decoding a model with annotated fields."""
    json_data = {"value": "test string"}
    response = create_response(ModelWithAnnotation, json_data)
    result = response.decode()
    assert isinstance(result, ModelWithAnnotation)
    assert result.value == "test string"


# ----- Tests for Union and Discriminated Types -----


def test_decode_union_with_discriminator_running():
    """Test decoding a union type with discriminator (running status)."""
    json_data = {"type": "RUNNING", "percent_complete": 75}
    response = create_response(Status, json_data)
    result = response.decode()
    assert isinstance(result, RunningStatus)
    assert result.type == "RUNNING"
    assert result.percent_complete == 75


def test_decode_union_with_discriminator_failed():
    """Test decoding a union type with discriminator (failed status)."""
    json_data = {"type": "FAILED", "error_message": "Something went wrong"}
    response = create_response(Status, json_data)
    result = response.decode()
    assert isinstance(result, FailedStatus)
    assert result.type == "FAILED"
    assert result.error_message == "Something went wrong"


def test_decode_union_with_discriminator_completed():
    """Test decoding a union type with discriminator (completed status)."""
    json_data = {"type": "COMPLETED", "result": "Success!"}
    response = create_response(Status, json_data)
    result = response.decode()
    assert isinstance(result, CompletedStatus)
    assert result.type == "COMPLETED"
    assert result.result == "Success!"


def test_decode_optional_union_with_discriminator_present():
    """Test decoding an Optional union type with discriminator when content is present."""
    json_data = {"type": "RUNNING", "percent_complete": 50}
    response = create_response(OptionalStatus, json_data)
    result = response.decode()
    assert isinstance(result, RunningStatus)
    assert result.type == "RUNNING"
    assert result.percent_complete == 50


def test_decode_optional_union_with_discriminator_empty():
    """Test decoding an Optional union type with discriminator when content is empty."""
    response = create_bytes_response(OptionalStatus, b"")
    result = response.decode()
    assert result is None


# ----- Tests for Nested and Complex Types -----


def test_decode_annotated_optional_base_model():
    """Test decoding an Annotated Optional BaseModel."""
    json_data = {"value": "test string"}
    response = create_response(
        Annotated[Optional[SimpleModel], pydantic.Field(description="Optional model")],
        json_data,
    )
    result = response.decode()
    assert isinstance(result, SimpleModel)
    assert result.value == "test string"


def test_decode_optional_annotated_base_model():
    """Test decoding an Optional Annotated BaseModel."""
    json_data = {"value": "test string"}
    response = create_response(
        Optional[Annotated[SimpleModel, pydantic.Field(description="Annotated model")]],
        json_data,
    )
    result = response.decode()
    assert isinstance(result, SimpleModel)
    assert result.value == "test string"


def test_decode_optional_annotated_base_model_empty():
    """Test decoding an Optional Annotated BaseModel when content is empty."""
    response = create_bytes_response(
        Optional[Annotated[SimpleModel, pydantic.Field(description="Annotated model")]],
        b"",
    )
    result = response.decode()
    assert result is None


def test_decode_annotated_optional_annotated_base_model():
    """Test decoding an Annotated Optional Annotated BaseModel (deeply nested)."""
    json_data = {"value": "test string"}
    response = create_response(
        Annotated[
            Optional[
                Annotated[
                    SimpleModel,
                    pydantic.Field(description="Inner annotation"),
                ]
            ],
            pydantic.Field(description="Outer annotation"),
        ],
        json_data,
    )
    result = response.decode()
    assert isinstance(result, SimpleModel)
    assert result.value == "test string"


def test_decode_nested_unions():
    """Test decoding nested Union types."""
    json_data = {"type": "RUNNING", "percent_complete": 25}
    nested_union = Union[Status, SimpleModel]
    response = create_response(nested_union, json_data)
    result = response.decode()
    assert isinstance(result, RunningStatus)
    assert result.type == "RUNNING"
    assert result.percent_complete == 25


def test_decode_list_of_optional_models():
    """Test decoding a list of optional models."""
    json_data = [{"value": "test1"}, None, {"value": "test3"}]
    response = create_response(List[Optional[SimpleModel]], json_data)
    result = response.decode()
    assert isinstance(result, list)
    assert isinstance(result[0], SimpleModel)
    assert result[1] is None
    assert isinstance(result[2], SimpleModel)
    assert result[0].value == "test1"
    assert result[2].value == "test3"


def test_decode_dict_with_complex_values():
    """Test decoding a dictionary with complex value types."""
    json_data = {
        "model": {"value": "test"},
        "list": [1, 2, 3],
        "nested": {"key": {"value": "nested value"}},
    }
    response = create_response(
        Dict[str, Union[SimpleModel, List[int], Dict[str, SimpleModel]]],
        json_data,
    )
    result = response.decode()
    assert isinstance(result, dict)
    assert isinstance(result["model"], SimpleModel)
    assert isinstance(result["list"], list)
    assert isinstance(result["nested"], dict)
    assert isinstance(result["nested"]["key"], SimpleModel)
    assert result["model"].value == "test"
    assert result["list"] == [1, 2, 3]
    assert result["nested"]["key"].value == "nested value"


# ----- Tests for Generic Types -----

T = TypeVar("T")


class GenericModel(pydantic.BaseModel, Generic[T]):
    """A generic model for testing."""

    value: T


def test_decode_generic_model():
    """Test decoding a generic model."""
    json_data = {"value": "test string"}
    response = create_response(GenericModel[str], json_data)
    result = response.decode()
    assert isinstance(result, GenericModel)
    assert result.value == "test string"

    json_data = {"value": 42}
    response = create_response(GenericModel[int], json_data)
    result = response.decode()
    assert isinstance(result, GenericModel)
    assert result.value == 42


# ----- Tests for Type Mismatches -----


def test_decode_string_when_int_expected():
    """Test decoding a string when an int was expected."""
    json_data = "not an integer"
    response = create_response(int, json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_int_when_string_expected():
    """Test decoding an int when a string was expected."""
    json_data = 42
    response = create_response(str, json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_wrong_union_discriminator_value():
    """Test decoding a union with a discriminator value that doesn't match any option."""
    json_data = {"type": "UNKNOWN", "some_field": "value"}
    response = create_response(Status, json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_missing_union_discriminator():
    """Test decoding a union with a missing discriminator field."""
    json_data = {"some_field": "value"}
    response = create_response(Status, json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_list_with_wrong_element_type():
    """Test decoding a list where elements don't match expected type."""
    json_data = ["string", 123, True]  # Mixed types
    response = create_response(List[int], json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_model_missing_required_fields():
    """Test decoding a model with missing required fields."""
    json_data = {}  # Missing required 'value' field
    response = create_response(SimpleModel, json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_non_json_as_model():
    """Test decoding non-JSON data as a model."""
    response = create_bytes_response(SimpleModel, b"Not a JSON object")
    with pytest.raises(json.JSONDecodeError):
        response.decode()


def test_decode_wrong_datetime_format():
    """Test decoding a datetime with wrong format."""
    json_data = "01/01/2023"  # Wrong format
    response = create_response(AwareDatetime, json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_invalid_rid():
    """Test decoding an invalid RID."""
    json_data = "not-a-valid-rid"
    response = create_response(RID, json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_dict_with_wrong_value_type():
    """Test decoding a dict with values of wrong type."""
    json_data = {"key1": 123, "key2": 456}  # Numbers instead of strings
    response = create_response(Dict[str, SimpleModel], json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_malformed_json_model():
    """Test decoding malformed JSON for a model."""
    json_data = {"value": {"nested": "object"}}  # Value should be string not object
    response = create_response(SimpleModel, json_data)
    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_validation_error():
    """Test validation error when decoding a model with invalid data."""
    # This should fail validation because the value is too short (min_length=3)
    json_data = {"value": "ab"}
    response = create_response(ModelWithAnnotation, json_data)

    with pytest.raises(pydantic.ValidationError):
        response.decode()


def test_decode_multiple_type_adapter_calls():
    """Test that the type adapter cache is working."""
    # Create multiple responses with the same type to test caching
    json_data1 = {"type": "RUNNING", "percent_complete": 25}
    json_data2 = {"type": "FAILED", "error_message": "Error message"}

    response1 = create_response(Status, json_data1)
    result1 = response1.decode()

    response2 = create_response(Status, json_data2)
    result2 = response2.decode()

    assert isinstance(result1, RunningStatus)
    assert isinstance(result2, FailedStatus)
    assert result1.type == "RUNNING"
    assert result2.type == "FAILED"
