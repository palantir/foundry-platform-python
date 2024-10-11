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


from __future__ import annotations

from foundry.v2.core.models._full_row_change_data_capture_configuration_dict import (
    FullRowChangeDataCaptureConfigurationDict,
)  # NOQA

ChangeDataCaptureConfigurationDict = FullRowChangeDataCaptureConfigurationDict
"""
Configuration for utilizing the stream as a change data capture (CDC) dataset. To configure CDC on a stream, at
least one key needs to be provided.

For more information on CDC in
Foundry, see the [Change Data Capture](/docs/foundry/data-integration/change-data-capture/) user documentation.
"""
