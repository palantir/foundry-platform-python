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

from typing import Literal

ResourceType = Literal[
    "ARTIFACTS_REPOSITORY",
    "BELLASO_CIPHER_CHANNEL",
    "BLOBSTER_DOCUMENT",
    "BLOBSTER_IMAGE",
    "CARBON_WORKSPACE",
    "COMPASS_FOLDER",
    "COMPASS_WEB_LINK",
    "CONTOUR_ANALYSIS",
    "DATA_HEALTH_MONITORING_VIEW",
    "EDDIE_LOGIC",
    "EDDIE_PIPELINE",
    "FFORMS_FORM",
    "FOUNDRY_DATASET",
    "FOUNDRY_ACADEMY_TUTORIAL",
    "FOUNDRY_CONTAINER_SERVICE_CONTAINER",
    "FOUNDRY_ML_OBJECTIVE",
    "FOUNDRY_TEMPLATES_TEMPLATE",
    "FUSION_DOCUMENT",
    "HUBBLE_EXPLORATION_LAYOUT",
    "MACHINERY_DOCUMENT",
    "MAGRITTE_AGENT",
    "MAGRITTE_SOURCE",
    "MARKETPLACE_BLOCK_SET_INSTALLATION",
    "MARKETPLACE_LOCAL",
    "MARKETPLACE_REMOTE_STORE",
    "MIO_MEDIA_SET",
    "MODELS_MODEL",
    "MODELS_MODEL_VERSION",
    "MONOCLE_GRAPH",
    "NOTEPAD_NOTEPAD",
    "NOTEPAD_NOTEPAD_TEMPLATE",
    "OBJECT_SENTINEL_MONITOR",
    "OBJECT_SET_VERSIONED_OBJECT_SET",
    "OPUS_GRAPH",
    "OPUS_MAP",
    "OPUS_MAP_LAYER",
    "QUIVER_ANALYSIS",
    "REPORT_REPORT",
    "SLATE_DOCUMENT",
    "SOLUTION_DESIGN_DIAGRAM",
    "STEMMA_REPOSITORY",
    "TABLES_TABLE",
    "TAURUS_WORKFLOW",
    "THIRD_PARTY_APPLICATIONS_APPLICATION",
    "VECTOR_WORKBOOK",
    "WORKSHOP_MODULE",
]
"""The type of the Resource derived from the Resource Identifier (RID)."""
