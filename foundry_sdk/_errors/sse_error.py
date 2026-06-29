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


class SseContentTypeError(PalantirException):
    """The server response was not a ``text/event-stream`` as required for SSE consumption."""


class SseEventDecodeError(PalantirException):
    """An SSE event's ``data`` could not be parsed as JSON or decoded into the expected event type."""
