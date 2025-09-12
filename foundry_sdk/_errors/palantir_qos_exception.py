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


from foundry_sdk._errors.palantir_exception import PalantirException


class PalantirQoSException(PalantirException):
    """The root exception class for all QoS related exceptions."""


class RateLimitError(PalantirQoSException):
    """
    The service is experiencing too many requests. Reduce your request rate and retry your
    request shortly. This error is thrown if a 429 status code is returned.
    """


class ServiceUnavailable(PalantirQoSException):
    """
    The service is currently unavailable. Retry your request shortly. This error is thrown if a
    503 status code is returned.
    """
