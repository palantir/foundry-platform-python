from pydantic import PydanticUndefinedAnnotation, ValidationError
from pydantic import TypeAdapter
import pytest
from foundry import models


def test_can_validate_types():
    """
    The discriminators types are difficult to construct. This test ensures
    that all discriminators are importable without raising any issues.
    """

    for model_name in dir(models):
        klass = getattr(models, model_name)

        if "Annotated[Union[" not in str(klass):
            continue

        try:
            ta = TypeAdapter(klass)
        except PydanticUndefinedAnnotation as e:
            print(model_name, str(klass))
            raise e

        with pytest.raises(ValidationError) as error:
            ta.validate_python({})

        assert error.value.errors(include_url=False) == [
            {
                "type": "union_tag_not_found",
                "loc": (),
                "msg": "Unable to extract tag using discriminator 'type'",
                "input": {},
                "ctx": {"discriminator": "'type'"},
            }
        ]
