from pydantic import TypeAdapter, ValidationError
import pytest
from foundry.models import CreateDatasetRequest

validator = TypeAdapter(CreateDatasetRequest)


def test_from_dict():
    req = validator.validate_python(
        {"name": "FOLDER_NAME", "parentFolderRid": "ri.foundry.main.folder.1234567890"}
    )

    assert req["name"] == "FOLDER_NAME"
    assert req["parentFolderRid"] == "ri.foundry.main.folder.1234567890"


def test_to_dict():
    req = CreateDatasetRequest(
        name="FOLDER_NAME",
        parentFolderRid="ri.foundry.main.folder.1234567890",
    )

    assert req == {
        "name": "FOLDER_NAME",
        "parentFolderRid": "ri.foundry.main.folder.1234567890",
    }


def test_from_fails_bad_type():
    assert pytest.raises(
        ValidationError,
        lambda: validator.validate_python({"name": "FOLDER_NAME", "parentFolderRid": 123}),
    )


def test_from_fails_missing():
    assert pytest.raises(
        ValidationError,
        lambda: validator.validate_python({"name": "FOLDER_NAME"}),
    )
