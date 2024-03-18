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