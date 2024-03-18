from pydantic import TypeAdapter
from foundry.models import OntologyDataType


def test_model_validate():
    ta = TypeAdapter(OntologyDataType)
    result = ta.validate_python({"type": "any"})
    assert result.type == "any"
