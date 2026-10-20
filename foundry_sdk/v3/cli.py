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


@cli.group("marketplace")
def marketplace():
    pass


@marketplace.group("marketplace_installation_job")
def marketplace_marketplace_installation_job():
    pass


@marketplace_marketplace_installation_job.command("abort")
@click.argument("marketplace_installation_job_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def marketplace_marketplace_installation_job_op_abort(
    client: FoundryClient,
    marketplace_installation_job_rid: str,
    preview: typing.Optional[bool],
):
    """
    Abort an installation job draft or request cancellation of a submitted installation job. This operation is
    idempotent while the job remains available. Poll the job with `get` after aborting: submitted jobs may report
    `ABORTING` before reaching `ABORTED`. Aborting a job that has already finished leaves its terminal status
    unchanged.

    A submitted job may already have created resources. Cancelling it can leave the installation in an
    inconsistent state. To recover to a consistent state, attempt a new job to the same target version.

    An aborted draft remains queryable only until automatic cleanup.
    """
    result = client.marketplace.MarketplaceInstallationJob.abort(
        marketplace_installation_job_rid=marketplace_installation_job_rid,
        preview=preview,
    )
    click.echo(repr(result))


@marketplace_marketplace_installation_job.command("create")
@click.option(
    "--installations",
    type=str,
    required=True,
    help="""Existing installations to upgrade to their target versions, along with their input mappings.""",
)
@click.option(
    "--recommendations",
    type=str,
    required=True,
    help="""Strategies for selecting other installations whose outputs can fulfill the targets' inputs. Targets in this request may still supply inputs to one another, independent of recommendation strategy.""",
)
@click.option("--preview", type=bool, required=False, help="""""")
@click.option("--submission_mode", type=str, required=False, help="""""")
@click.pass_obj
def marketplace_marketplace_installation_job_op_create(
    client: FoundryClient,
    installations: str,
    recommendations: str,
    preview: typing.Optional[bool],
    submission_mode: typing.Optional[str],
):
    """
    Create a job to upgrade existing installations to their target versions.

    The operation returns before preparation and validation complete. Poll the job's status to track progress.

    Specify 1 to 10 distinct installations, with at most one installation per product. Targets must share a
    namespace and marketplace and have at most one resulting ontology after applying overrides.

    For each target, `values` and `explicitlyUnset` replace all previously provided values and explicit unsets.

    Inputs omitted from both fields may be fulfilled by defaults, automatic mapping, or recommendations. Use
    `discoverInputs` to inspect available sources.

    This operation is not idempotent. Repeating it may create another draft or return a conflict.
    """
    result = client.marketplace.MarketplaceInstallationJob.create(
        installations=json.loads(installations),
        recommendations=json.loads(recommendations),
        preview=preview,
        submission_mode=None if submission_mode is None else json.loads(submission_mode),
    )
    click.echo(repr(result))


@marketplace_marketplace_installation_job.command("discover_inputs")
@click.option(
    "--installations",
    type=str,
    required=True,
    help="""Between 1 and 10 distinct installations, with at most one installation per product. Targets must share a namespace and marketplace and have at most one resulting ontology after applying overrides.""",
)
@click.option(
    "--recommendations",
    type=str,
    required=True,
    help="""An empty list disables recommendations from installations outside the requested targets. Targets in this request may still supply inputs to one another.""",
)
@click.option("--preview", type=bool, required=False, help="""""")
@click.option(
    "--source_filter",
    type=str,
    required=False,
    help="""When supplied, excludes an input if any of its available sources appears in `excludedSources`. If omitted, returns only inputs whose sole available source is `MANUAL`. Inputs with no available source are always omitted.""",
)
@click.pass_obj
def marketplace_marketplace_installation_job_op_discover_inputs(
    client: FoundryClient,
    installations: str,
    recommendations: str,
    preview: typing.Optional[bool],
    source_filter: typing.Optional[str],
):
    """
    Discover required and optional inputs for existing installations and their proposed target versions.

    Resolves input requirements and available sources using the requested target versions, location overrides,
    and recommendation strategies.

    The request token must have permission to edit each target. Every input in the target product versions must
    have an API name.
    """
    result = client.marketplace.MarketplaceInstallationJob.discover_inputs(
        installations=json.loads(installations),
        recommendations=json.loads(recommendations),
        preview=preview,
        source_filter=None if source_filter is None else json.loads(source_filter),
    )
    click.echo(repr(result))


@marketplace_marketplace_installation_job.command("get")
@click.argument("marketplace_installation_job_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def marketplace_marketplace_installation_job_op_get(
    client: FoundryClient,
    marketplace_installation_job_rid: str,
    preview: typing.Optional[bool],
):
    """
    Get the current status of an installation job through draft preparation and execution.

    The request token must have permission to view the draft or submitted job. Missing or inaccessible jobs return
    `MarketplaceInstallationJobNotFound`. A failed or aborted job still returns HTTP 200 with its current status.
    """
    result = client.marketplace.MarketplaceInstallationJob.get(
        marketplace_installation_job_rid=marketplace_installation_job_rid,
        preview=preview,
    )
    click.echo(repr(result))


@marketplace_marketplace_installation_job.group("marketplace_installation_job_details")
def marketplace_marketplace_installation_job_marketplace_installation_job_details():
    pass


@marketplace_marketplace_installation_job_marketplace_installation_job_details.command("get")
@click.argument("marketplace_installation_job_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def marketplace_marketplace_installation_job_marketplace_installation_job_details_op_get(
    client: FoundryClient,
    marketplace_installation_job_rid: str,
    preview: typing.Optional[bool],
):
    """
    Get available validation results and failure diagnostics for an installation job or draft. Use the
    installation job's `status` to track its progress and outcome. These details can help explain why a draft or
    job has not progressed or completed as expected.

    Draft owners receive full validation errors. Other authorized viewers receive a validation summary instead.
    Failed and aborted jobs return HTTP 200 with their available diagnostics. An explicit abort or a
    validation-only submission rejection may have no failure diagnostics.
    The job remains queryable under the same RID after its draft is submitted, subject to retention and access.
    """
    result = client.marketplace.MarketplaceInstallationJob.Details.get(
        marketplace_installation_job_rid=marketplace_installation_job_rid,
        preview=preview,
    )
    click.echo(repr(result))


@marketplace.group("marketplace_installation")
def marketplace_marketplace_installation():
    pass


@marketplace_marketplace_installation.command("create")
@click.option("--marketplace_rid", type=str, required=True, help="""""")
@click.option(
    "--parent_folder_rid",
    type=str,
    required=True,
    help="""The RID of the Compass project or folder that currently contains the installation. On creation, this is the destination where the installation is registered and its jobs create resources.""",
)
@click.option("--product_id", type=str, required=True, help="""""")
@click.option(
    "--installation_suffix",
    type=str,
    required=False,
    help="""An optional suffix appended to the product title to form the initial display name, for example "Product title - CI staging". If omitted, the display name uses the product title alone.""",
)
@click.option(
    "--ontology_rid",
    type=str,
    required=False,
    help="""The ontology where jobs for this installation create or update ontology resources. Omit if the product does not interact with the ontology.""",
)
@click.option("--preview", type=bool, required=False, help="""""")
@click.option(
    "--target_version_hint",
    type=str,
    required=False,
    help="""If provided:
 - validations that are version specific (e.g. singleton validations) are executed assuming
    the installation will later have a job run to transition it to this specific target version.
 - the installation title is resolved from the product title at that version.

If not provided, the latest released version of the product is used to resolve information for
the steps above.""",
)
@click.pass_obj
def marketplace_marketplace_installation_op_create(
    client: FoundryClient,
    marketplace_rid: str,
    parent_folder_rid: str,
    product_id: str,
    installation_suffix: typing.Optional[str],
    ontology_rid: typing.Optional[str],
    preview: typing.Optional[bool],
    target_version_hint: typing.Optional[str],
):
    """
    Register a product installation in the given project or folder without running an installation job or
    installing product resources. Returns the created installation with its current Compass metadata and
    no latest target version. A subsequent installation job selects the version to install.

    This operation is not idempotent. Repeated requests create separate installations unless the selected
    product version's singleton policy prohibits another installation in the destination namespace, in
    which case SingletonMarketplaceInstallationAlreadyExists is returned.
    """
    result = client.marketplace.MarketplaceInstallation.create(
        marketplace_rid=marketplace_rid,
        parent_folder_rid=parent_folder_rid,
        product_id=product_id,
        installation_suffix=installation_suffix,
        ontology_rid=ontology_rid,
        preview=preview,
        target_version_hint=(
            None if target_version_hint is None else json.loads(target_version_hint)
        ),
    )
    click.echo(repr(result))


@marketplace_marketplace_installation.command("get")
@click.argument("marketplace_installation_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.pass_obj
def marketplace_marketplace_installation_op_get(
    client: FoundryClient,
    marketplace_installation_rid: str,
    preview: typing.Optional[bool],
):
    """
    Get a registered installation and the product version targeted by its latest submitted job.
    """
    result = client.marketplace.MarketplaceInstallation.get(
        marketplace_installation_rid=marketplace_installation_rid,
        preview=preview,
    )
    click.echo(repr(result))


@marketplace_marketplace_installation.group("marketplace_installation_inputs")
def marketplace_marketplace_installation_marketplace_installation_inputs():
    pass


@marketplace_marketplace_installation_marketplace_installation_inputs.command("get")
@click.argument("marketplace_installation_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""""")
@click.option("--selection", type=click.Choice(["MANUAL_ONLY", "ALL"]), required=False, help="""""")
@click.pass_obj
def marketplace_marketplace_installation_marketplace_installation_inputs_op_get(
    client: FoundryClient,
    marketplace_installation_rid: str,
    preview: typing.Optional[bool],
    selection: typing.Optional[typing.Literal["MANUAL_ONLY", "ALL"]],
):
    """
    Get the current fulfilled input values and explicit unset inputs of an installation.

    By default, only manually fulfilled inputs are returned. Set `selection` to `ALL` to return fulfilled inputs
    from every stored source. Explicitly unset inputs are returned regardless of `selection`.

    Optional inputs with neither a value nor an explicit unset are omitted.

    Returned values may use a different supported representation from the value originally provided.

    Credential values expose secret names only, never plaintext, and cannot be submitted to another installation job.
    """
    result = client.marketplace.MarketplaceInstallation.Inputs.get(
        marketplace_installation_rid=marketplace_installation_rid,
        preview=preview,
        selection=selection,
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
