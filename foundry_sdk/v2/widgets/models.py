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

import typing

import pydantic

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models


class DevModeSettings(core.ModelBase):
    """DevModeSettings"""

    status: DevModeStatus
    widget_set_settings: typing.Dict[WidgetSetRid, WidgetSetDevModeSettings] = pydantic.Field(alias=str("widgetSetSettings"))  # type: ignore[literal-required]
    """The dev mode settings for each widget set, keyed by widget set RID."""


class DevModeSettingsV2(core.ModelBase):
    """DevModeSettingsV2"""

    status: DevModeStatus
    snapshot: typing.Optional[DevModeSnapshot] = None
    """The content-addressed snapshot of the current dev mode settings, if any."""


class DevModeSnapshot(core.ModelBase):
    """
    A content-addressed snapshot of the dev mode settings. Snapshots are immutable
    and identified by their content-addressed ID.
    """

    snapshot_id: DevModeSnapshotId = pydantic.Field(alias=str("snapshotId"))  # type: ignore[literal-required]
    """The content-addressed identifier for this snapshot."""

    widget_set_settings: typing.Dict[WidgetSetRid, WidgetSetDevModeSettingsV2] = pydantic.Field(alias=str("widgetSetSettings"))  # type: ignore[literal-required]
    """The dev mode settings for each widget set, keyed by widget set RID."""


DevModeSnapshotId = str
"""A content-addressed identifier for a dev mode settings snapshot."""


DevModeStatus = typing.Literal["ENABLED", "PAUSED", "DISABLED"]
"""The user's global development mode status for widget sets."""


FilePath = str
"""A locator for a specific file in a widget set's release directory."""


class ListReleasesResponse(core.ModelBase):
    """ListReleasesResponse"""

    data: typing.List[Release]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class OntologySdkInputSpec(core.ModelBase):
    """A specification of an Ontology SDK used by a widget set."""

    sdk_package_rid: OntologySdkPackageRid = pydantic.Field(alias=str("sdkPackageRid"))  # type: ignore[literal-required]
    """The RID of the Ontology SDK package."""

    sdk_version: OntologySdkVersion = pydantic.Field(alias=str("sdkVersion"))  # type: ignore[literal-required]
    """The version of the Ontology SDK."""


OntologySdkPackageRid = core.RID
"""A Resource Identifier (RID) identifying an Ontology SDK package."""


OntologySdkVersion = str
"""A limited semver version string of the format major.minor.patch."""


class Release(core.ModelBase):
    """Release"""

    widget_set_rid: WidgetSetRid = pydantic.Field(alias=str("widgetSetRid"))  # type: ignore[literal-required]
    """The Resource Identifier (RID) of the widget set this release is for."""

    version: ReleaseVersion
    """The semantic version of the widget set."""

    locator: ReleaseLocator
    description: typing.Optional[str] = None
    """The description of this release."""


class ReleaseLocator(core.ModelBase):
    """A locator for where the backing files of a release are stored."""

    repository_rid: RepositoryRid = pydantic.Field(alias=str("repositoryRid"))  # type: ignore[literal-required]
    """The Resource Identifier (RID) of the repository that contains the release."""

    repository_version: RepositoryVersion = pydantic.Field(alias=str("repositoryVersion"))  # type: ignore[literal-required]
    """The version of the repository storing the backing files."""


ReleaseVersion = str
"""The semantic version of the widget set."""


class Repository(core.ModelBase):
    """Repository"""

    rid: RepositoryRid
    """A Resource Identifier (RID) identifying a repository."""

    widget_set_rid: typing.Optional[WidgetSetRid] = pydantic.Field(alias=str("widgetSetRid"), default=None)  # type: ignore[literal-required]
    """
    The Resource Identifier (RID) of the widget set that has authorized this repository
    to publish new widget releases.
    """


RepositoryRid = core.RID
"""A Resource Identifier (RID) identifying a repository."""


RepositoryVersion = str
"""A semantic version of a repository storing backing files."""


class ScriptEntrypoint(core.ModelBase):
    """A script entrypoint to be loaded into the runtime environment."""

    file_path: FilePath = pydantic.Field(alias=str("filePath"))  # type: ignore[literal-required]
    """
    A relative path from the root to a JavaScript entrypoint. It must satisfy:

    - Must contain one or more non-empty segments separated by `/`.
    - Each segment must only contain the following ASCII characters: a-z, A-Z, 0-9 and -_..
    - Must have a maximum length of 100.
    """

    script_type: ScriptType = pydantic.Field(alias=str("scriptType"))  # type: ignore[literal-required]
    """
    Defines HTML "type" attribute to be used for the script entrypoint. The supported
    values are `DEFAULT` and `MODULE`, where `DEFAULT` maps to "text/javascript" and
    `MODULE` maps to "module".
    """


ScriptType = typing.Literal["DEFAULT", "MODULE"]
"""ScriptType"""


class SetWidgetSetDevModeSettingsByIdRequest(core.ModelBase):
    """SetWidgetSetDevModeSettingsByIdRequest"""

    widget_set_rid: WidgetSetRid = pydantic.Field(alias=str("widgetSetRid"))  # type: ignore[literal-required]
    settings: WidgetSetDevModeSettingsById


class SetWidgetSetManifestDevModeSettingsV2Request(core.ModelBase):
    """SetWidgetSetManifestDevModeSettingsV2Request"""

    widget_set_rid: WidgetSetRid = pydantic.Field(alias=str("widgetSetRid"))  # type: ignore[literal-required]
    manifest: typing.Any


class StylesheetEntrypoint(core.ModelBase):
    """A stylesheet entrypoint to be loaded into the runtime environment."""

    file_path: FilePath = pydantic.Field(alias=str("filePath"))  # type: ignore[literal-required]
    """
    A relative path from the root to a CSS entrypoint. It must satisfy:

    - Must contain one or more non-empty segments separated by `/`.
    - Each segment must only contain the following ASCII characters: a-z, A-Z, 0-9 and -_..
    - Must have a maximum length of 100.
    """


class WidgetDevModeSettings(core.ModelBase):
    """The settings for a given widget in development mode."""

    script_entrypoints: typing.List[ScriptEntrypoint] = pydantic.Field(alias=str("scriptEntrypoints"))  # type: ignore[literal-required]
    """The entrypoint JavaScript files for the widget."""

    stylesheet_entrypoints: typing.List[StylesheetEntrypoint] = pydantic.Field(alias=str("stylesheetEntrypoints"))  # type: ignore[literal-required]
    """The entrypoint CSS files for the widget."""


class WidgetDevModeSettingsV2(core.ModelBase):
    """The settings for a given widget in development mode (v2)."""

    name: typing.Optional[str] = None
    """The display name of the widget."""

    description: typing.Optional[str] = None
    """A description of the widget."""

    script_entrypoints: typing.List[ScriptEntrypoint] = pydantic.Field(alias=str("scriptEntrypoints"))  # type: ignore[literal-required]
    """The entrypoint JavaScript files for the widget."""

    stylesheet_entrypoints: typing.List[StylesheetEntrypoint] = pydantic.Field(alias=str("stylesheetEntrypoints"))  # type: ignore[literal-required]
    """The entrypoint CSS files for the widget."""


WidgetId = str
"""
Human readable ID for a widget. Must be unique within a widget set.
Considered unsafe as it may contain user defined data.

- Must only contain the following ASCII characters: a-z, A-Z and 0-9.
- Must not start with a number.
- Must have a maximum length of 100.
- Must be camelCase.
"""


WidgetRid = core.RID
"""A Resource Identifier (RID) identifying a widget."""


class WidgetSet(core.ModelBase):
    """WidgetSet"""

    rid: WidgetSetRid
    """A Resource Identifier (RID) identifying a widget set."""

    publish_repository_rid: typing.Optional[RepositoryRid] = pydantic.Field(alias=str("publishRepositoryRid"), default=None)  # type: ignore[literal-required]
    """
    The Resource Identifier (RID) of the repository that is authorized to publish new
    widget releases to this widget set through a manifest.
    """


class WidgetSetDevModeSettings(core.ModelBase):
    """The settings for a widget set in development mode, keyed by widget RID."""

    base_href: str = pydantic.Field(alias=str("baseHref"))  # type: ignore[literal-required]
    """The base path for the HTML file used to render the widget in dev mode."""

    widget_settings: typing.Dict[WidgetRid, WidgetDevModeSettings] = pydantic.Field(alias=str("widgetSettings"))  # type: ignore[literal-required]
    """The dev mode settings for each widget in the widget set, keyed by widget RIDs."""


class WidgetSetDevModeSettingsById(core.ModelBase):
    """The settings for a widget set in development mode, keyed by widget ID."""

    base_href: str = pydantic.Field(alias=str("baseHref"))  # type: ignore[literal-required]
    """The base path for the HTML file used to render the widget in dev mode."""

    widget_settings: typing.Dict[WidgetId, WidgetDevModeSettings] = pydantic.Field(alias=str("widgetSettings"))  # type: ignore[literal-required]
    """The dev mode settings for each widget in the widget set, keyed by widget IDs."""


class WidgetSetDevModeSettingsV2(core.ModelBase):
    """The settings for a widget set in development mode (v2), keyed by widget ID."""

    base_href: str = pydantic.Field(alias=str("baseHref"))  # type: ignore[literal-required]
    """The base path for the HTML file used to render the widget in dev mode."""

    input_spec: typing.Optional[WidgetSetInputSpec] = pydantic.Field(alias=str("inputSpec"), default=None)  # type: ignore[literal-required]
    """The input spec for the widget set in dev mode."""

    widget_settings: typing.Dict[WidgetId, WidgetDevModeSettingsV2] = pydantic.Field(alias=str("widgetSettings"))  # type: ignore[literal-required]
    """The dev mode settings for each widget in the widget set, keyed by widget IDs."""


class WidgetSetInputSpec(core.ModelBase):
    """
    A specification of the Foundry data inputs that a widget set uses. This restricts
    the data access that a widget set has at runtime.
    """

    sdks: typing.List[OntologySdkInputSpec]
    """The Ontology SDK specifications used by the widget set."""


WidgetSetRid = core.RID
"""A Resource Identifier (RID) identifying a widget set."""


__all__ = [
    "DevModeSettings",
    "DevModeSettingsV2",
    "DevModeSnapshot",
    "DevModeSnapshotId",
    "DevModeStatus",
    "FilePath",
    "ListReleasesResponse",
    "OntologySdkInputSpec",
    "OntologySdkPackageRid",
    "OntologySdkVersion",
    "Release",
    "ReleaseLocator",
    "ReleaseVersion",
    "Repository",
    "RepositoryRid",
    "RepositoryVersion",
    "ScriptEntrypoint",
    "ScriptType",
    "SetWidgetSetDevModeSettingsByIdRequest",
    "SetWidgetSetManifestDevModeSettingsV2Request",
    "StylesheetEntrypoint",
    "WidgetDevModeSettings",
    "WidgetDevModeSettingsV2",
    "WidgetId",
    "WidgetRid",
    "WidgetSet",
    "WidgetSetDevModeSettings",
    "WidgetSetDevModeSettingsById",
    "WidgetSetDevModeSettingsV2",
    "WidgetSetInputSpec",
    "WidgetSetRid",
]
