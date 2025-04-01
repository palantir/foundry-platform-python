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
from typing import Any
from typing import Dict

from foundry_sdk._errors.palantir_exception import PalantirException


def format_error_message(fields: Dict[str, Any]) -> str:
    return json.dumps(fields, sort_keys=True, indent=4, default=str)


class PalantirRPCException(PalantirException):
    def __init__(self, error_metadata: Dict[str, Any]):
        super().__init__(format_error_message(error_metadata))
        self.name = error_metadata.get("errorName")
        self.parameters = error_metadata.get("parameters")
        self.error_instance_id = error_metadata.get("errorInstanceId")


class BadRequestError(PalantirRPCException):
    """
    There was an issue with the request. This error is thrown if a 400 status code is returned.
    """


class UnauthorizedError(PalantirRPCException):
    """
    The authorization header is missing or invalid. This error is thrown if a 401 status code is returned.
    """


class RequestEntityTooLargeError(PalantirRPCException):
    """The request entity is too large. This error is thrown if a 413 status code is returned."""


class PermissionDeniedError(PalantirRPCException):
    """
    You are missing the necessary permissions to complete your request. This error is thrown if a
    403 status code is returned.
    """


class NotFoundError(PalantirRPCException):
    """A Resource was not found. This error is thrown if a 404 status code is returned."""


class UnprocessableEntityError(PalantirRPCException):
    """
    One or more of the request's arguments are invalid. This error is thrown if a 422 status code
    is returned.
    """


class RateLimitError(PalantirRPCException):
    """
    The service is experiencing too many requests. Retry your request shortly and reduce your
    request rate. This error is thrown if a 429 status code is returned.
    """


class ConflictError(PalantirRPCException):
    """
    There was a conflict with another request. This error is thrown if a 409 status code is
    returned.
    """


class InternalServerError(PalantirRPCException):
    """An error occurred within the service. This error is thrown if a 5XX status code is returned."""
