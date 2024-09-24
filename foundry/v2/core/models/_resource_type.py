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
    "Academy_Tutorial",
    "Artifacts_Repository",
    "Automate_Automation",
    "Builder_Pipeline",
    "Carbon_Workspace",
    "Cipher_Channel",
    "Code_Repository",
    "Code_Workbook",
    "Code_Workspace",
    "Connectivity_Agent",
    "Connectivity_Source",
    "Connectivity_VirtualTable",
    "Contour_Analysis",
    "Data_Lineage_Graph",
    "Datasets_Dataset",
    "Filesystem_Document",
    "Filesystem_Folder",
    "Filesystem_Image",
    "Filesystem_Project",
    "Filesystem_Space",
    "Filesystem_WebLink",
    "Foundry_Form",
    "Foundry_Report",
    "Foundry_Template",
    "FoundryRules_Workflow",
    "Fusion_Document",
    "Logic_Function",
    "Machinery_ProcessGraph",
    "Maps_Layer",
    "Maps_Map",
    "Marketplace_Installation",
    "Marketplace_LocalStore",
    "Marketplace_RemoteStore",
    "Media_Set",
    "Modeling_Model",
    "Modeling_ModelVersion",
    "Modeling_Objective",
    "Monitoring_MonitoringView",
    "Notepad_Document",
    "Notepad_Template",
    "ObjectExploration_Exploration",
    "ObjectExploration_Layout",
    "Quiver_Analysis",
    "Slate_Application",
    "SolutionDesigner_Diagram",
    "ThirdPartyApplication_ThirdPartyApplication",
    "Unknown",
    "Vertex_Graph",
    "Workshop_Module",
]
"""The type of a resource."""
