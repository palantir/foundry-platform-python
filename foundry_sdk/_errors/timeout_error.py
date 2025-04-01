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


from foundry_sdk._errors.connection_error import ConnectionError
from foundry_sdk._errors.palantir_exception import PalantirException


class TimeoutError(PalantirException):
    """The request timed out. This error will catch both ConnectTimeout, ReadTimeout and WriteTimeout."""


class ConnectTimeout(ConnectionError, TimeoutError):
    """The request timed out when attempting to connect to the server."""


class ReadTimeout(TimeoutError):
    """The server did not send any data in the allotted amount of time."""


class WriteTimeout(TimeoutError):
    """There was a timeout when writing data to the server."""
