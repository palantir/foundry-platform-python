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

import pytest
from pydantic import PydanticUndefinedAnnotation
from pydantic import TypeAdapter
from pydantic import ValidationError

from foundry.v1 import models as models_v1
from foundry.v2 import models as models_v2


def test_can_validate_types():
    """
    The discriminators types are difficult to construct. This test ensures
    that all discriminators are importable without raising any issues.
    """

    for models, model_name in [(models_v1, model_name) for model_name in dir(models_v1)] + [
        (models_v2, model_name) for model_name in dir(models_v2)
    ]:
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
