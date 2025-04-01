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


import warnings
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type
from typing import cast
from typing import get_type_hints

import pydantic

from foundry_sdk._errors.palantir_rpc_exception import PalantirRPCException
from foundry_sdk._errors.sdk_internal_error import SDKInternalError


def deserialize_error(
    error_metadata: Dict[str, Any],
    exception_classes: Dict[str, type],
) -> Optional[PalantirRPCException]:
    try:
        name = error_metadata["errorName"]
        parameters = error_metadata["parameters"]
        error_instance_id = error_metadata["errorInstanceId"]
    except KeyError as e:
        warnings.warn(str(SDKInternalError(f"Failed to find required error attributes: {e}")))

        return None

    exc_class = exception_classes.get(name)
    if exc_class is None:
        return None

    annotations = get_type_hints(exc_class)
    parameters_type = cast(Type[Dict[str, Any]], annotations["parameters"])
    adapter = pydantic.TypeAdapter(parameters_type)

    try:
        parameters_instance = adapter.validate_python(parameters)
        return exc_class(
            name=name, parameters=parameters_instance, error_instance_id=error_instance_id
        )
    except pydantic.ValidationError as e:
        # For whatever reason, if we can't properly deserialize the error parameters we will throw PalantirRPCException
        # instead of failing
        # To provide additional details to the user we will add a bunch of metadata to the warning
        # using the "SDKInternalError" class but just emit a warning
        warning_message = str(SDKInternalError(f'Deserialization failed for error "{name}": {e}'))

        warnings.warn(warning_message)
        return None
