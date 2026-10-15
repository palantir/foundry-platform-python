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

import dataclasses
import io
import json
import os
import typing
from datetime import date as Date
from datetime import datetime

import click

from foundry_sdk import EnvironmentNotConfigured
from foundry_sdk import UserTokenAuth
from foundry_sdk.v3 import FoundryClient


@dataclasses.dataclass
class _Context:
    obj: FoundryClient


def get_from_environ(key: str) -> str:
    value = os.environ.get(key)
    if value is None:
        raise EnvironmentNotConfigured(f"Please set {key} using `export {key}=<{key}>`")

    return value


@click.group()  # type: ignore
@click.pass_context  # type: ignore
def cli(ctx: _Context):
    """An experimental CLI for the Foundry API"""
    ctx.obj = FoundryClient(
        auth=UserTokenAuth(token=get_from_environ("FOUNDRY_TOKEN")),
        hostname=get_from_environ("FOUNDRY_HOSTNAME"),
    )


@cli.group("core")
def core():
    pass


@cli.group("endpoints")
def endpoints():
    pass


@endpoints.group("endpoint_set")
def endpoints_endpoint_set():
    pass


@endpoints_endpoint_set.command("get")
@click.argument("endpoint_set_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def endpoints_endpoint_set_op_get(
    client: FoundryClient,
    endpoint_set_rid: str,
    preview: typing.Optional[bool],
):
    """ """
    result = client.endpoints.EndpointSet.get(
        endpoint_set_rid=endpoint_set_rid,
        preview=preview,
    )
    click.echo(repr(result))


@endpoints_endpoint_set.group("endpoint_set_version")
def endpoints_endpoint_set_endpoint_set_version():
    pass


@endpoints_endpoint_set_endpoint_set_version.command("get")
@click.argument("endpoint_set_rid", type=str, required=True)
@click.argument("version_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def endpoints_endpoint_set_endpoint_set_version_op_get(
    client: FoundryClient,
    endpoint_set_rid: str,
    version_id: str,
    preview: typing.Optional[bool],
):
    """ """
    result = client.endpoints.EndpointSet.Version.get(
        endpoint_set_rid=endpoint_set_rid,
        version_id=version_id,
        preview=preview,
    )
    click.echo(repr(result))


@endpoints_endpoint_set_endpoint_set_version.command("list")
@click.argument("endpoint_set_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def endpoints_endpoint_set_endpoint_set_version_op_list(
    client: FoundryClient,
    endpoint_set_rid: str,
    page_size: typing.Optional[int],
    page_token: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """ """
    result = client.endpoints.EndpointSet.Version.list(
        endpoint_set_rid=endpoint_set_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@endpoints_endpoint_set.group("endpoint_set_endpoint")
def endpoints_endpoint_set_endpoint_set_endpoint():
    pass


@endpoints_endpoint_set_endpoint_set_endpoint.command("get")
@click.argument("endpoint_set_rid", type=str, required=True)
@click.argument("endpoint_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def endpoints_endpoint_set_endpoint_set_endpoint_op_get(
    client: FoundryClient,
    endpoint_set_rid: str,
    endpoint_rid: str,
    preview: typing.Optional[bool],
):
    """ """
    result = client.endpoints.EndpointSet.Endpoint.get(
        endpoint_set_rid=endpoint_set_rid,
        endpoint_rid=endpoint_rid,
        preview=preview,
    )
    click.echo(repr(result))


@endpoints_endpoint_set_endpoint_set_endpoint.command("list")
@click.argument("endpoint_set_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def endpoints_endpoint_set_endpoint_set_endpoint_op_list(
    client: FoundryClient,
    endpoint_set_rid: str,
    page_size: typing.Optional[int],
    page_token: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """ """
    result = client.endpoints.EndpointSet.Endpoint.list(
        endpoint_set_rid=endpoint_set_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("filesystem")
def filesystem():
    pass


@filesystem.group("space")
def filesystem_space():
    pass


@filesystem_space.command("delete")
@click.argument("space_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_space_op_delete(
    client: FoundryClient,
    space_rid: str,
    preview: typing.Optional[bool],
):
    """
    Move the given space to the trash. Following this operation, the space can be restored, using the
    `restore` operation, or permanently deleted using the `permanentlyDelete` operation.
    """
    result = client.filesystem.Space.delete(
        space_rid=space_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_space.command("delete_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_space_op_delete_batch(
    client: FoundryClient,
    body: str,
    preview: typing.Optional[bool],
):
    """
    Trash multiple spaces in a single request.
    """
    result = client.filesystem.Space.delete_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_space.command("get")
@click.argument("space_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_space_op_get(
    client: FoundryClient,
    space_rid: str,
    preview: typing.Optional[bool],
):
    """
    Get the space with the specified resource identifier (RID).
    """
    result = client.filesystem.Space.get(
        space_rid=space_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_space.command("get_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_space_op_get_batch(
    client: FoundryClient,
    body: str,
    preview: typing.Optional[bool],
):
    """
    Fetch multiple spaces in a single request.
    """
    result = client.filesystem.Space.get_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_space.command("list")
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_space_op_list(
    client: FoundryClient,
    page_size: typing.Optional[int],
    page_token: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    Lists all spaces.

    This is a paginated endpoint. Each page may be smaller or larger than the requested page size.
    It is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
    To get the next page, make the same request again, but set the value of the `pageToken` query parameter
    to be value of the `nextPageToken` value of the previous response.
    If there is no `nextPageToken` field in the response, you are on the last page.

    The default page size is 200. The maximum page size is 200. Requests for a larger page size will be
    clamped to 200. If pageSize is 0, the default page size is used.
    """
    result = client.filesystem.Space.list(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_space.command("restore")
@click.argument("space_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_space_op_restore(
    client: FoundryClient,
    space_rid: str,
    preview: typing.Optional[bool],
):
    """
    Restore the given space and any directly trashed ancestors from the trash. If the space is not
    directly trashed, this operation will return an error.
    """
    result = client.filesystem.Space.restore(
        space_rid=space_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem.group("resource")
def filesystem_resource():
    pass


@filesystem_resource.command("delete")
@click.argument("resource_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_resource_op_delete(
    client: FoundryClient,
    resource_rid: str,
    preview: typing.Optional[bool],
):
    """
    Move the given resource to the trash. Following this operation, the resource can be restored, using the
    `restore` operation, or permanently deleted using the `permanentlyDelete` operation.
    """
    result = client.filesystem.Resource.delete(
        resource_rid=resource_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_resource.command("delete_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_resource_op_delete_batch(
    client: FoundryClient,
    body: str,
    preview: typing.Optional[bool],
):
    """
    Trash multiple resources in a single request.
    """
    result = client.filesystem.Resource.delete_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_resource.command("get")
@click.argument("resource_rid", type=str, required=True)
@click.option("--include", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_resource_op_get(
    client: FoundryClient,
    resource_rid: str,
    include: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    Get the resource with the specified resource identifier (RID).
    """
    result = client.filesystem.Resource.get(
        resource_rid=resource_rid,
        include=None if include is None else json.loads(include),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_resource.command("get_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_resource_op_get_batch(
    client: FoundryClient,
    body: str,
    preview: typing.Optional[bool],
):
    """
    Fetch multiple resources in a single request.
    """
    result = client.filesystem.Resource.get_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_resource.command("get_by_path")
@click.option("--path", type=str, required=True, help="""""")
@click.option("--include", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_resource_op_get_by_path(
    client: FoundryClient,
    path: str,
    include: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    Get a resource by its absolute path. The leading slash is optional.
    """
    result = client.filesystem.Resource.get_by_path(
        path=path,
        include=None if include is None else json.loads(include),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_resource.command("restore")
@click.argument("resource_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_resource_op_restore(
    client: FoundryClient,
    resource_rid: str,
    preview: typing.Optional[bool],
):
    """
    Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
    directly trashed, this operation will return an error.
    """
    result = client.filesystem.Resource.restore(
        resource_rid=resource_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem.group("project")
def filesystem_project():
    pass


@filesystem_project.command("delete")
@click.argument("project_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_project_op_delete(
    client: FoundryClient,
    project_rid: str,
    preview: typing.Optional[bool],
):
    """
    Move the given project to the trash. Following this operation, the project can be restored, using the
    `restore` operation, or permanently deleted using the `permanentlyDelete` operation.
    """
    result = client.filesystem.Project.delete(
        project_rid=project_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_project.command("delete_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_project_op_delete_batch(
    client: FoundryClient,
    body: str,
    preview: typing.Optional[bool],
):
    """
    Trash multiple projects in a single request.
    """
    result = client.filesystem.Project.delete_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_project.command("get")
@click.argument("project_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_project_op_get(
    client: FoundryClient,
    project_rid: str,
    preview: typing.Optional[bool],
):
    """
    Get the project with the specified resource identifier (RID).
    """
    result = client.filesystem.Project.get(
        project_rid=project_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_project.command("get_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_project_op_get_batch(
    client: FoundryClient,
    body: str,
    preview: typing.Optional[bool],
):
    """
    Fetch multiple projects in a single request.
    """
    result = client.filesystem.Project.get_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_project.command("restore")
@click.argument("project_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_project_op_restore(
    client: FoundryClient,
    project_rid: str,
    preview: typing.Optional[bool],
):
    """
    Restore the given project and any directly trashed ancestors from the trash. If the project is not
    directly trashed, this operation will return an error.
    """
    result = client.filesystem.Project.restore(
        project_rid=project_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem.group("folder")
def filesystem_folder():
    pass


@filesystem_folder.command("create")
@click.option("--display_name", type=str, required=True, help="""The display name of the folder.""")
@click.option(
    "--parent_folder_rid",
    type=str,
    required=True,
    help="""The RID of the existing project or folder in which to create the new folder. The parent must be inside a project.""",
)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_folder_op_create(
    client: FoundryClient,
    display_name: str,
    parent_folder_rid: str,
    preview: typing.Optional[bool],
):
    """
    Create a new folder in the given parent folder.
    """
    result = client.filesystem.Folder.create(
        display_name=display_name,
        parent_folder_rid=parent_folder_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_folder.command("delete")
@click.argument("folder_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_folder_op_delete(
    client: FoundryClient,
    folder_rid: str,
    preview: typing.Optional[bool],
):
    """
    Move the given folder to the trash. Following this operation, the folder can be restored, using the
    `restore` operation, or permanently deleted using the `permanentlyDelete` operation.
    """
    result = client.filesystem.Folder.delete(
        folder_rid=folder_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_folder.command("delete_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_folder_op_delete_batch(
    client: FoundryClient,
    body: str,
    preview: typing.Optional[bool],
):
    """
    Trash multiple folders in a single request.
    """
    result = client.filesystem.Folder.delete_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_folder.command("get")
@click.argument("folder_rid", type=str, required=True)
@click.option("--include", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_folder_op_get(
    client: FoundryClient,
    folder_rid: str,
    include: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    Get the folder with the specified resource identifier (RID).
    """
    result = client.filesystem.Folder.get(
        folder_rid=folder_rid,
        include=None if include is None else json.loads(include),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_folder.command("get_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_folder_op_get_batch(
    client: FoundryClient,
    body: str,
    preview: typing.Optional[bool],
):
    """
    Fetch multiple folders in a single request.
    """
    result = client.filesystem.Folder.get_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_folder.command("restore")
@click.argument("folder_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def filesystem_folder_op_restore(
    client: FoundryClient,
    folder_rid: str,
    preview: typing.Optional[bool],
):
    """
    Restore the given folder and any directly trashed ancestors from the trash. If the folder is not
    directly trashed, this operation will return an error.
    """
    result = client.filesystem.Folder.restore(
        folder_rid=folder_rid,
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("orchestrator")
def orchestrator():
    pass


@orchestrator.group("process_execution")
def orchestrator_process_execution():
    pass


@orchestrator_process_execution.group("process_execution_signal")
def orchestrator_process_execution_process_execution_signal():
    pass


@orchestrator_process_execution_process_execution_signal.command("complete")
@click.argument("process_execution_id", type=str, required=True)
@click.argument("signal_id", type=str, required=True)
@click.option(
    "--payload",
    type=str,
    required=False,
    help="""Arbitrary JSON passed to the process execution that consumes the signal. Empty when the completion
carries no payload.""",
)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def orchestrator_process_execution_process_execution_signal_op_complete(
    client: FoundryClient,
    process_execution_id: str,
    signal_id: str,
    payload: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    Complete a signal on a process execution.

    A signal may be completed multiple times, each contributing toward the execution's wait conditions.
    If the execution is suspended waiting on this signal, it resumes once its wait conditions are
    satisfied. Resuming an execution runs user-authored logic. Only the token that originally invoked the
    process execution can complete its signals.
    """
    result = client.orchestrator.ProcessExecution.Signal.complete(
        process_execution_id=process_execution_id,
        signal_id=signal_id,
        payload=None if payload is None else json.loads(payload),
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("tiles")
def tiles():
    pass


@tiles.group("tile_source")
def tiles_tile_source():
    pass


@tiles_tile_source.command("compute_elevation")
@click.argument("tile_source_id", type=str, required=True)
@click.option(
    "--points",
    type=str,
    required=True,
    help="""The points to compute elevation for. Results are returned in the same order as the request.
A request may contain at most 1,000 points by default, though the configured limit may differ;
exceeding it returns a `MaxElevationPointCountExceeded` error that reports the limit.""",
)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def tiles_tile_source_op_compute_elevation(
    client: FoundryClient,
    tile_source_id: str,
    points: str,
    preview: typing.Optional[bool],
):
    """
    Compute ground elevation at one or more points using this tile source. Results are returned in
    the same order as the requested points. Returns a not-found error if the source does not exist
    or the token cannot access it.
    """
    result = client.tiles.TileSource.compute_elevation(
        tile_source_id=tile_source_id,
        points=json.loads(points),
        preview=preview,
    )
    click.echo(repr(result))


@tiles_tile_source.command("get")
@click.argument("tile_source_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def tiles_tile_source_op_get(
    client: FoundryClient,
    tile_source_id: str,
    preview: typing.Optional[bool],
):
    """
    Get metadata for a single tile source, including its tile sets. Returns a not-found error if
    the source does not exist or the token cannot access it.
    """
    result = client.tiles.TileSource.get(
        tile_source_id=tile_source_id,
        preview=preview,
    )
    click.echo(repr(result))


@tiles_tile_source.command("list")
@click.option(
    "--capability",
    type=click.Choice(["ELEVATION", "IMAGERY_TILES", "VECTOR_TILES", "TERRAIN_TILES"]),
    required=False,
    help="""""",
)
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def tiles_tile_source_op_list(
    client: FoundryClient,
    capability: typing.Optional[
        typing.Literal["ELEVATION", "IMAGERY_TILES", "VECTOR_TILES", "TERRAIN_TILES"]
    ],
    page_size: typing.Optional[int],
    page_token: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    List the tile sources accessible by the token.
    """
    result = client.tiles.TileSource.list(
        capability=capability,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


if __name__ == "__main__":
    cli()
