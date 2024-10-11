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


import pydantic
import pytest

from foundry.v1.core import models as models_core_v1
from foundry.v1.datasets import models as models_datasets_v1
from foundry.v1.geo import models as models_geo_v1
from foundry.v1.ontologies import models as models_ontologies_v1
from foundry.v2.admin import models as models_admin_v2
from foundry.v2.connectivity import models as models_connectivity_v2
from foundry.v2.core import models as models_core_v2
from foundry.v2.datasets import models as models_datasets_v2
from foundry.v2.filesystem import models as models_filesystem_v2
from foundry.v2.functions import models as models_functions_v2
from foundry.v2.geo import models as models_geo_v2
from foundry.v2.ontologies import models as models_ontologies_v2
from foundry.v2.orchestration import models as models_orchestration_v2
from foundry.v2.streams import models as models_streams_v2
from foundry.v2.third_party_applications import models as models_third_party_applications_v2  # NOQA


def test_can_validate_types():
    """
    The discriminators types are difficult to construct. This test ensures
    that all discriminators are importable without raising any issues.
    """

    for models, model_name in [
        *[(models_core_v1, model_name) for model_name in dir(models_core_v1)],
        *[(models_datasets_v1, model_name) for model_name in dir(models_datasets_v1)],
        *[(models_geo_v1, model_name) for model_name in dir(models_geo_v1)],
        *[(models_ontologies_v1, model_name) for model_name in dir(models_ontologies_v1)],
        *[(models_admin_v2, model_name) for model_name in dir(models_admin_v2)],
        *[(models_connectivity_v2, model_name) for model_name in dir(models_connectivity_v2)],
        *[(models_core_v2, model_name) for model_name in dir(models_core_v2)],
        *[(models_datasets_v2, model_name) for model_name in dir(models_datasets_v2)],
        *[(models_filesystem_v2, model_name) for model_name in dir(models_filesystem_v2)],
        *[(models_functions_v2, model_name) for model_name in dir(models_functions_v2)],
        *[(models_geo_v2, model_name) for model_name in dir(models_geo_v2)],
        *[(models_ontologies_v2, model_name) for model_name in dir(models_ontologies_v2)],
        *[(models_ontologies_v2, model_name) for model_name in dir(models_ontologies_v2)],
        *[(models_orchestration_v2, model_name) for model_name in dir(models_orchestration_v2)],
        *[(models_streams_v2, model_name) for model_name in dir(models_streams_v2)],
        *[
            (models_third_party_applications_v2, model_name)
            for model_name in dir(models_third_party_applications_v2)
        ],
    ]:
        klass = getattr(models, model_name)

        if "Annotated[Union[" not in str(klass):
            continue

        try:
            ta = pydantic.TypeAdapter(klass)
        except pydantic.PydanticUndefinedAnnotation as e:
            print(model_name, str(klass))
            raise e

        with pytest.raises(pydantic.ValidationError) as error:
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
