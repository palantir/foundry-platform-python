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
from datetime import datetime
from typing import Literal
from typing import Optional

import click

import foundry.v2


@dataclasses.dataclass
class _Context:
    obj: foundry.v2.FoundryClient


def get_from_environ(key: str) -> str:
    value = os.environ.get(key)
    if value is None:
        raise foundry.EnvironmentNotConfigured(f"Please set {key} using `export {key}=<{key}>`")

    return value


@click.group()  # type: ignore
@click.pass_context  # type: ignore
def cli(ctx: _Context):
    "An experimental CLI for the Foundry API"
    ctx.obj = foundry.v2.FoundryClient(
        auth=foundry.UserTokenAuth(
            hostname=get_from_environ("FOUNDRY_HOSTNAME"),
            token=get_from_environ("FOUNDRY_TOKEN"),
        ),
        hostname=get_from_environ("FOUNDRY_HOSTNAME"),
    )


@cli.group("admin")
def admin():
    pass


@admin.group("user")
def admin_user():
    pass


@admin_user.command("delete")
@click.argument("user_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_delete(
    client: foundry.v2.FoundryClient,
    user_id: str,
    preview: Optional[bool],
):
    """
    Delete the User with the specified id.
    """
    result = client.admin.User.delete(
        user_id=user_id,
        preview=preview,
    )
    click.echo(repr(result))


@admin_user.command("get")
@click.argument("user_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_get(
    client: foundry.v2.FoundryClient,
    user_id: str,
    preview: Optional[bool],
):
    """
    Get the User with the specified id.
    """
    result = client.admin.User.get(
        user_id=user_id,
        preview=preview,
    )
    click.echo(repr(result))


@admin_user.command("get_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_get_batch(
    client: foundry.v2.FoundryClient,
    body: str,
    preview: Optional[bool],
):
    """
    Execute multiple get requests on User.

    The maximum batch size for this endpoint is 500.
    """
    result = client.admin.User.get_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@admin_user.command("get_current")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_get_current(
    client: foundry.v2.FoundryClient,
    preview: Optional[bool],
):
    """ """
    result = client.admin.User.get_current(
        preview=preview,
    )
    click.echo(repr(result))


@admin_user.command("get_markings")
@click.argument("user_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_get_markings(
    client: foundry.v2.FoundryClient,
    user_id: str,
    preview: Optional[bool],
):
    """
    Retrieve Markings that the user is currently a member of.
    """
    result = client.admin.User.get_markings(
        user_id=user_id,
        preview=preview,
    )
    click.echo(repr(result))


@admin_user.command("list")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_list(
    client: foundry.v2.FoundryClient,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    Lists all Users.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.admin.User.list(
        page_size=page_size,
        preview=preview,
    )
    click.echo(repr(result))


@admin_user.command("page")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_page(
    client: foundry.v2.FoundryClient,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    Lists all Users.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.admin.User.page(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@admin_user.command("profile_picture")
@click.argument("user_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_profile_picture(
    client: foundry.v2.FoundryClient,
    user_id: str,
    preview: Optional[bool],
):
    """ """
    result = client.admin.User.profile_picture(
        user_id=user_id,
        preview=preview,
    )
    click.echo(result)


@admin_user.command("search")
@click.option("--where", type=str, required=True, help="""""")
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_search(
    client: foundry.v2.FoundryClient,
    where: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """ """
    result = client.admin.User.search(
        where=json.loads(where),
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@admin_user.group("group_membership")
def admin_user_group_membership():
    pass


@admin_user_group_membership.command("list")
@click.argument("user_id", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--transitive", type=bool, required=False, help="""transitive""")
@click.pass_obj
def admin_user_group_membership_list(
    client: foundry.v2.FoundryClient,
    user_id: str,
    page_size: Optional[int],
    preview: Optional[bool],
    transitive: Optional[bool],
):
    """
    Lists all GroupMemberships.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.admin.User.GroupMembership.list(
        user_id=user_id,
        page_size=page_size,
        preview=preview,
        transitive=transitive,
    )
    click.echo(repr(result))


@admin_user_group_membership.command("page")
@click.argument("user_id", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--transitive", type=bool, required=False, help="""transitive""")
@click.pass_obj
def admin_user_group_membership_page(
    client: foundry.v2.FoundryClient,
    user_id: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
    transitive: Optional[bool],
):
    """
    Lists all GroupMemberships.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.admin.User.GroupMembership.page(
        user_id=user_id,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        transitive=transitive,
    )
    click.echo(repr(result))


@admin.group("marking_category")
def admin_marking_category():
    pass


@admin_marking_category.command("get")
@click.argument("marking_category_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_marking_category_get(
    client: foundry.v2.FoundryClient,
    marking_category_id: str,
    preview: Optional[bool],
):
    """
    Get the MarkingCategory with the specified id.
    """
    result = client.admin.MarkingCategory.get(
        marking_category_id=marking_category_id,
        preview=preview,
    )
    click.echo(repr(result))


@admin_marking_category.command("list")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_marking_category_list(
    client: foundry.v2.FoundryClient,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    Maximum page size 100.
    """
    result = client.admin.MarkingCategory.list(
        page_size=page_size,
        preview=preview,
    )
    click.echo(repr(result))


@admin_marking_category.command("page")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_marking_category_page(
    client: foundry.v2.FoundryClient,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    Maximum page size 100.
    """
    result = client.admin.MarkingCategory.page(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@admin.group("marking")
def admin_marking():
    pass


@admin_marking.command("get")
@click.argument("marking_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_marking_get(
    client: foundry.v2.FoundryClient,
    marking_id: str,
    preview: Optional[bool],
):
    """
    Get the Marking with the specified id.
    """
    result = client.admin.Marking.get(
        marking_id=marking_id,
        preview=preview,
    )
    click.echo(repr(result))


@admin_marking.command("get_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_marking_get_batch(
    client: foundry.v2.FoundryClient,
    body: str,
    preview: Optional[bool],
):
    """
    Execute multiple get requests on Marking.

    The maximum batch size for this endpoint is 500.
    """
    result = client.admin.Marking.get_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@admin_marking.command("list")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_marking_list(
    client: foundry.v2.FoundryClient,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    Maximum page size 100.
    """
    result = client.admin.Marking.list(
        page_size=page_size,
        preview=preview,
    )
    click.echo(repr(result))


@admin_marking.command("page")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_marking_page(
    client: foundry.v2.FoundryClient,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    Maximum page size 100.
    """
    result = client.admin.Marking.page(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@admin.group("group")
def admin_group():
    pass


@admin_group.command("create")
@click.option(
    "--attributes",
    type=str,
    required=True,
    help="""A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.""",
)
@click.option("--name", type=str, required=True, help="""The name of the Group.""")
@click.option(
    "--organizations",
    type=str,
    required=True,
    help="""The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
""",
)
@click.option("--description", type=str, required=False, help="""A description of the Group.""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_create(
    client: foundry.v2.FoundryClient,
    attributes: str,
    name: str,
    organizations: str,
    description: Optional[str],
    preview: Optional[bool],
):
    """
    Creates a new Group.
    """
    result = client.admin.Group.create(
        attributes=json.loads(attributes),
        name=name,
        organizations=json.loads(organizations),
        description=description,
        preview=preview,
    )
    click.echo(repr(result))


@admin_group.command("delete")
@click.argument("group_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_delete(
    client: foundry.v2.FoundryClient,
    group_id: str,
    preview: Optional[bool],
):
    """
    Delete the Group with the specified id.
    """
    result = client.admin.Group.delete(
        group_id=group_id,
        preview=preview,
    )
    click.echo(repr(result))


@admin_group.command("get")
@click.argument("group_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_get(
    client: foundry.v2.FoundryClient,
    group_id: str,
    preview: Optional[bool],
):
    """
    Get the Group with the specified id.
    """
    result = client.admin.Group.get(
        group_id=group_id,
        preview=preview,
    )
    click.echo(repr(result))


@admin_group.command("get_batch")
@click.argument("body", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_get_batch(
    client: foundry.v2.FoundryClient,
    body: str,
    preview: Optional[bool],
):
    """
    Execute multiple get requests on Group.

    The maximum batch size for this endpoint is 500.
    """
    result = client.admin.Group.get_batch(
        body=json.loads(body),
        preview=preview,
    )
    click.echo(repr(result))


@admin_group.command("list")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_list(
    client: foundry.v2.FoundryClient,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    Lists all Groups.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.admin.Group.list(
        page_size=page_size,
        preview=preview,
    )
    click.echo(repr(result))


@admin_group.command("page")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_page(
    client: foundry.v2.FoundryClient,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    Lists all Groups.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.admin.Group.page(
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@admin_group.command("search")
@click.option("--where", type=str, required=True, help="""""")
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_search(
    client: foundry.v2.FoundryClient,
    where: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """ """
    result = client.admin.Group.search(
        where=json.loads(where),
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@admin_group.group("group_member")
def admin_group_group_member():
    pass


@admin_group_group_member.command("add")
@click.argument("group_id", type=str, required=True)
@click.option("--principal_ids", type=str, required=True, help="""""")
@click.option("--expiration", type=click.DateTime(), required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_group_member_add(
    client: foundry.v2.FoundryClient,
    group_id: str,
    principal_ids: str,
    expiration: Optional[datetime],
    preview: Optional[bool],
):
    """ """
    result = client.admin.Group.GroupMember.add(
        group_id=group_id,
        principal_ids=json.loads(principal_ids),
        expiration=expiration,
        preview=preview,
    )
    click.echo(repr(result))


@admin_group_group_member.command("list")
@click.argument("group_id", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--transitive", type=bool, required=False, help="""transitive""")
@click.pass_obj
def admin_group_group_member_list(
    client: foundry.v2.FoundryClient,
    group_id: str,
    page_size: Optional[int],
    preview: Optional[bool],
    transitive: Optional[bool],
):
    """
    Lists all GroupMembers.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.admin.Group.GroupMember.list(
        group_id=group_id,
        page_size=page_size,
        preview=preview,
        transitive=transitive,
    )
    click.echo(repr(result))


@admin_group_group_member.command("page")
@click.argument("group_id", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--transitive", type=bool, required=False, help="""transitive""")
@click.pass_obj
def admin_group_group_member_page(
    client: foundry.v2.FoundryClient,
    group_id: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
    transitive: Optional[bool],
):
    """
    Lists all GroupMembers.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.admin.Group.GroupMember.page(
        group_id=group_id,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        transitive=transitive,
    )
    click.echo(repr(result))


@admin_group_group_member.command("remove")
@click.argument("group_id", type=str, required=True)
@click.option("--principal_ids", type=str, required=True, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_group_member_remove(
    client: foundry.v2.FoundryClient,
    group_id: str,
    principal_ids: str,
    preview: Optional[bool],
):
    """ """
    result = client.admin.Group.GroupMember.remove(
        group_id=group_id,
        principal_ids=json.loads(principal_ids),
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("connectivity")
def connectivity():
    pass


@connectivity.group("file_import")
def connectivity_file_import():
    pass


@connectivity_file_import.command("get")
@click.argument("file_import_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def connectivity_file_import_get(
    client: foundry.v2.FoundryClient,
    file_import_rid: str,
    preview: Optional[bool],
):
    """
    Get the FileImport with the specified rid.
    """
    result = client.connectivity.FileImport.get(
        file_import_rid=file_import_rid,
        preview=preview,
    )
    click.echo(repr(result))


@connectivity_file_import.command("trigger")
@click.argument("file_import_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def connectivity_file_import_trigger(
    client: foundry.v2.FoundryClient,
    file_import_rid: str,
    preview: Optional[bool],
):
    """
    Triggers the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
    The returned BuildRid can be used to check the status via the Orchestration API.

    """
    result = client.connectivity.FileImport.trigger(
        file_import_rid=file_import_rid,
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("core")
def core():
    pass


@cli.group("datasets")
def datasets():
    pass


@datasets.group("dataset")
def datasets_dataset():
    pass


@datasets_dataset.command("create")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--parent_folder_rid", type=str, required=True, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_create(
    client: foundry.v2.FoundryClient,
    name: str,
    parent_folder_rid: str,
    preview: Optional[bool],
):
    """
    Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

    """
    result = client.datasets.Dataset.create(
        name=name,
        parent_folder_rid=parent_folder_rid,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_get(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    preview: Optional[bool],
):
    """
    Get the Dataset with the specified rid.
    """
    result = client.datasets.Dataset.get(
        dataset_rid=dataset_rid,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset.command("read_table")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--format", type=click.Choice(["ARROW", "CSV"]), required=True, help="""format""")
@click.option("--branch_name", type=str, required=False, help="""branchName""")
@click.option("--columns", type=str, required=False, help="""columns""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--row_limit", type=int, required=False, help="""rowLimit""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_read_table(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    format: Literal["ARROW", "CSV"],
    branch_name: Optional[str],
    columns: Optional[str],
    end_transaction_rid: Optional[str],
    preview: Optional[bool],
    row_limit: Optional[int],
    start_transaction_rid: Optional[str],
):
    """
    Gets the content of a dataset as a table in the specified format.

    This endpoint currently does not support views (Virtual datasets composed of other datasets).

    """
    result = client.datasets.Dataset.read_table(
        dataset_rid=dataset_rid,
        format=format,
        branch_name=branch_name,
        columns=None if columns is None else json.loads(columns),
        end_transaction_rid=end_transaction_rid,
        preview=preview,
        row_limit=row_limit,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(result)


@datasets_dataset.group("file")
def datasets_dataset_file():
    pass


@datasets_dataset_file.command("content")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("file_path", type=str, required=True)
@click.option("--branch_name", type=str, required=False, help="""branchName""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_file_content(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    file_path: str,
    branch_name: Optional[str],
    end_transaction_rid: Optional[str],
    preview: Optional[bool],
    start_transaction_rid: Optional[str],
):
    """
    Gets the content of a File contained in a Dataset. By default this retrieves the file's content from the latest
    view of the default branch - `master` for most enrollments.
    #### Advanced Usage
    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
    To **get a file's content from a specific Branch** specify the Branch's name as `branchName`. This will
    retrieve the content for the most recent version of the file since the latest snapshot transaction, or the
    earliest ancestor transaction of the branch if there are no snapshot transactions.
    To **get a file's content from the resolved view of a transaction** specify the Transaction's resource identifier
    as `endTransactionRid`. This will retrieve the content for the most recent version of the file since the latest
    snapshot transaction, or the earliest ancestor transaction if there are no snapshot transactions.
    To **get a file's content from the resolved view of a range of transactions** specify the the start transaction's
    resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`.
    This will retrieve the content for the most recent version of the file since the `startTransactionRid` up to the
    `endTransactionRid`. Note that an intermediate snapshot transaction will remove all files from the view. Behavior
    is undefined when the start and end transactions do not belong to the same root-to-leaf path.
    To **get a file's content from a specific transaction** specify the Transaction's resource identifier as both the
    `startTransactionRid` and `endTransactionRid`.

    """
    result = client.datasets.Dataset.File.content(
        dataset_rid=dataset_rid,
        file_path=file_path,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        preview=preview,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(result)


@datasets_dataset_file.command("delete")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("file_path", type=str, required=True)
@click.option("--branch_name", type=str, required=False, help="""branchName""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--transaction_rid", type=str, required=False, help="""transactionRid""")
@click.pass_obj
def datasets_dataset_file_delete(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    file_path: str,
    branch_name: Optional[str],
    preview: Optional[bool],
    transaction_rid: Optional[str],
):
    """
    Deletes a File from a Dataset. By default the file is deleted in a new transaction on the default
    branch - `master` for most enrollments. The file will still be visible on historical views.
    #### Advanced Usage
    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
    To **delete a File from a specific Branch** specify the Branch's name as `branchName`. A new delete Transaction
    will be created and committed on this branch.
    To **delete a File using a manually opened Transaction**, specify the Transaction's resource identifier
    as `transactionRid`. The transaction must be of type `DELETE`. This is useful for deleting multiple files in a
    single transaction. See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to
    open a transaction.

    """
    result = client.datasets.Dataset.File.delete(
        dataset_rid=dataset_rid,
        file_path=file_path,
        branch_name=branch_name,
        preview=preview,
        transaction_rid=transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_file.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("file_path", type=str, required=True)
@click.option("--branch_name", type=str, required=False, help="""branchName""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_file_get(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    file_path: str,
    branch_name: Optional[str],
    end_transaction_rid: Optional[str],
    preview: Optional[bool],
    start_transaction_rid: Optional[str],
):
    """
    Gets metadata about a File contained in a Dataset. By default this retrieves the file's metadata from the latest
    view of the default branch - `master` for most enrollments.
    #### Advanced Usage
    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
    To **get a file's metadata from a specific Branch** specify the Branch's name as `branchName`. This will
    retrieve metadata for the most recent version of the file since the latest snapshot transaction, or the earliest
    ancestor transaction of the branch if there are no snapshot transactions.
    To **get a file's metadata from the resolved view of a transaction** specify the Transaction's resource identifier
    as `endTransactionRid`. This will retrieve metadata for the most recent version of the file since the latest snapshot
    transaction, or the earliest ancestor transaction if there are no snapshot transactions.
    To **get a file's metadata from the resolved view of a range of transactions** specify the the start transaction's
    resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`.
    This will retrieve metadata for the most recent version of the file since the `startTransactionRid` up to the
    `endTransactionRid`. Behavior is undefined when the start and end transactions do not belong to the same root-to-leaf path.
    To **get a file's metadata from a specific transaction** specify the Transaction's resource identifier as both the
    `startTransactionRid` and `endTransactionRid`.

    """
    result = client.datasets.Dataset.File.get(
        dataset_rid=dataset_rid,
        file_path=file_path,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        preview=preview,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_file.command("list")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--branch_name", type=str, required=False, help="""branchName""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_file_list(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    branch_name: Optional[str],
    end_transaction_rid: Optional[str],
    page_size: Optional[int],
    preview: Optional[bool],
    start_transaction_rid: Optional[str],
):
    """
    Lists Files contained in a Dataset. By default files are listed on the latest view of the default
    branch - `master` for most enrollments.
    #### Advanced Usage
    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
    To **list files on a specific Branch** specify the Branch's name as `branchName`. This will include the most
    recent version of all files since the latest snapshot transaction, or the earliest ancestor transaction of the
    branch if there are no snapshot transactions.
    To **list files on the resolved view of a transaction** specify the Transaction's resource identifier
    as `endTransactionRid`. This will include the most recent version of all files since the latest snapshot
    transaction, or the earliest ancestor transaction if there are no snapshot transactions.
    To **list files on the resolved view of a range of transactions** specify the the start transaction's resource
    identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This
    will include the most recent version of all files since the `startTransactionRid` up to the `endTransactionRid`.
    Note that an intermediate snapshot transaction will remove all files from the view. Behavior is undefined when
    the start and end transactions do not belong to the same root-to-leaf path.
    To **list files on a specific transaction** specify the Transaction's resource identifier as both the
    `startTransactionRid` and `endTransactionRid`. This will include only files that were modified as part of that
    Transaction.

    """
    result = client.datasets.Dataset.File.list(
        dataset_rid=dataset_rid,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        page_size=page_size,
        preview=preview,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_file.command("page")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--branch_name", type=str, required=False, help="""branchName""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_file_page(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    branch_name: Optional[str],
    end_transaction_rid: Optional[str],
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
    start_transaction_rid: Optional[str],
):
    """
    Lists Files contained in a Dataset. By default files are listed on the latest view of the default
    branch - `master` for most enrollments.
    #### Advanced Usage
    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
    To **list files on a specific Branch** specify the Branch's name as `branchName`. This will include the most
    recent version of all files since the latest snapshot transaction, or the earliest ancestor transaction of the
    branch if there are no snapshot transactions.
    To **list files on the resolved view of a transaction** specify the Transaction's resource identifier
    as `endTransactionRid`. This will include the most recent version of all files since the latest snapshot
    transaction, or the earliest ancestor transaction if there are no snapshot transactions.
    To **list files on the resolved view of a range of transactions** specify the the start transaction's resource
    identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This
    will include the most recent version of all files since the `startTransactionRid` up to the `endTransactionRid`.
    Note that an intermediate snapshot transaction will remove all files from the view. Behavior is undefined when
    the start and end transactions do not belong to the same root-to-leaf path.
    To **list files on a specific transaction** specify the Transaction's resource identifier as both the
    `startTransactionRid` and `endTransactionRid`. This will include only files that were modified as part of that
    Transaction.

    """
    result = client.datasets.Dataset.File.page(
        dataset_rid=dataset_rid,
        branch_name=branch_name,
        end_transaction_rid=end_transaction_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_file.command("upload")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("file_path", type=str, required=True)
@click.argument("body", type=click.File("rb"), required=True)
@click.option("--branch_name", type=str, required=False, help="""branchName""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--transaction_rid", type=str, required=False, help="""transactionRid""")
@click.option(
    "--transaction_type",
    type=click.Choice(["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]),
    required=False,
    help="""transactionType""",
)
@click.pass_obj
def datasets_dataset_file_upload(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    file_path: str,
    body: io.BufferedReader,
    branch_name: Optional[str],
    preview: Optional[bool],
    transaction_rid: Optional[str],
    transaction_type: Optional[Literal["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]],
):
    """
    Uploads a File to an existing Dataset.
    The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
    By default the file is uploaded to a new transaction on the default branch - `master` for most enrollments.
    If the file already exists only the most recent version will be visible in the updated view.
    #### Advanced Usage
    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
    To **upload a file to a specific Branch** specify the Branch's name as `branchName`. A new transaction will
    be created and committed on this branch. By default the TransactionType will be `UPDATE`, to override this
    default specify `transactionType` in addition to `branchName`.
    See [createBranch](/docs/foundry/api/datasets-resources/branches/create-branch/) to create a custom branch.
    To **upload a file on a manually opened transaction** specify the Transaction's resource identifier as
    `transactionRid`. This is useful for uploading multiple files in a single transaction.
    See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to open a transaction.

    """
    result = client.datasets.Dataset.File.upload(
        dataset_rid=dataset_rid,
        file_path=file_path,
        body=body.read(),
        branch_name=branch_name,
        preview=preview,
        transaction_rid=transaction_rid,
        transaction_type=transaction_type,
    )
    click.echo(repr(result))


@datasets_dataset.group("transaction")
def datasets_dataset_transaction():
    pass


@datasets_dataset_transaction.command("abort")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("transaction_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_transaction_abort(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    transaction_rid: str,
    preview: Optional[bool],
):
    """
    Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
    not updated.

    """
    result = client.datasets.Dataset.Transaction.abort(
        dataset_rid=dataset_rid,
        transaction_rid=transaction_rid,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset_transaction.command("commit")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("transaction_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_transaction_commit(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    transaction_rid: str,
    preview: Optional[bool],
):
    """
    Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
    updated to point to the Transaction.

    """
    result = client.datasets.Dataset.Transaction.commit(
        dataset_rid=dataset_rid,
        transaction_rid=transaction_rid,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset_transaction.command("create")
@click.argument("dataset_rid", type=str, required=True)
@click.option(
    "--transaction_type",
    type=click.Choice(["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]),
    required=True,
    help="""""",
)
@click.option("--branch_name", type=str, required=False, help="""branchName""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_transaction_create(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    transaction_type: Literal["APPEND", "UPDATE", "SNAPSHOT", "DELETE"],
    branch_name: Optional[str],
    preview: Optional[bool],
):
    """
    Creates a Transaction on a Branch of a Dataset.

    """
    result = client.datasets.Dataset.Transaction.create(
        dataset_rid=dataset_rid,
        transaction_type=transaction_type,
        branch_name=branch_name,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset_transaction.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("transaction_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_transaction_get(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    transaction_rid: str,
    preview: Optional[bool],
):
    """
    Gets a Transaction of a Dataset.

    """
    result = client.datasets.Dataset.Transaction.get(
        dataset_rid=dataset_rid,
        transaction_rid=transaction_rid,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset.group("branch")
def datasets_dataset_branch():
    pass


@datasets_dataset_branch.command("create")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--name", type=str, required=True, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--transaction_rid", type=str, required=False, help="""""")
@click.pass_obj
def datasets_dataset_branch_create(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    name: str,
    preview: Optional[bool],
    transaction_rid: Optional[str],
):
    """
    Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

    """
    result = client.datasets.Dataset.Branch.create(
        dataset_rid=dataset_rid,
        name=name,
        preview=preview,
        transaction_rid=transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("delete")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("branch_name", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_branch_delete(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    branch_name: str,
    preview: Optional[bool],
):
    """
    Deletes the Branch with the given BranchName.

    """
    result = client.datasets.Dataset.Branch.delete(
        dataset_rid=dataset_rid,
        branch_name=branch_name,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("branch_name", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_branch_get(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    branch_name: str,
    preview: Optional[bool],
):
    """
    Get a Branch of a Dataset.

    """
    result = client.datasets.Dataset.Branch.get(
        dataset_rid=dataset_rid,
        branch_name=branch_name,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("list")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_branch_list(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    Lists the Branches of a Dataset.

    """
    result = client.datasets.Dataset.Branch.list(
        dataset_rid=dataset_rid,
        page_size=page_size,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("page")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_branch_page(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    Lists the Branches of a Dataset.

    """
    result = client.datasets.Dataset.Branch.page(
        dataset_rid=dataset_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("filesystem")
def filesystem():
    pass


@filesystem.group("resource")
def filesystem_resource():
    pass


@filesystem_resource.command("delete")
@click.argument("resource_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def filesystem_resource_delete(
    client: foundry.v2.FoundryClient,
    resource_rid: str,
    preview: Optional[bool],
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


@filesystem_resource.command("get")
@click.argument("resource_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def filesystem_resource_get(
    client: foundry.v2.FoundryClient,
    resource_rid: str,
    preview: Optional[bool],
):
    """
    Get the Resource with the specified rid.
    """
    result = client.filesystem.Resource.get(
        resource_rid=resource_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_resource.command("permanently_delete")
@click.argument("resource_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def filesystem_resource_permanently_delete(
    client: foundry.v2.FoundryClient,
    resource_rid: str,
    preview: Optional[bool],
):
    """
    Permanently delete the given resource from the trash. If the Resource is not directly trashed, a
    `ResourceNotTrashed` error will be thrown.

    """
    result = client.filesystem.Resource.permanently_delete(
        resource_rid=resource_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_resource.command("restore")
@click.argument("resource_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def filesystem_resource_restore(
    client: foundry.v2.FoundryClient,
    resource_rid: str,
    preview: Optional[bool],
):
    """
    Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
    trashed, this operation will be ignored.

    """
    result = client.filesystem.Resource.restore(
        resource_rid=resource_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem.group("folder")
def filesystem_folder():
    pass


@filesystem_folder.command("children")
@click.argument("folder_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def filesystem_folder_children(
    client: foundry.v2.FoundryClient,
    folder_rid: str,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    List all child Resources of the Folder.

    This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
    provided, this page size will also be used as the default.

    """
    result = client.filesystem.Folder.children(
        folder_rid=folder_rid,
        page_size=page_size,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_folder.command("children_page")
@click.argument("folder_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def filesystem_folder_children_page(
    client: foundry.v2.FoundryClient,
    folder_rid: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    List all child Resources of the Folder.

    This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
    provided, this page size will also be used as the default.

    """
    result = client.filesystem.Folder.children_page(
        folder_rid=folder_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_folder.command("create")
@click.option("--display_name", type=str, required=True, help="""""")
@click.option(
    "--parent_folder_rid",
    type=str,
    required=True,
    help="""The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces,
this value will be the root folder (`ri.compass.main.folder.0`).
""",
)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def filesystem_folder_create(
    client: foundry.v2.FoundryClient,
    display_name: str,
    parent_folder_rid: str,
    preview: Optional[bool],
):
    """
    Creates a new Folder.
    """
    result = client.filesystem.Folder.create(
        display_name=display_name,
        parent_folder_rid=parent_folder_rid,
        preview=preview,
    )
    click.echo(repr(result))


@filesystem_folder.command("get")
@click.argument("folder_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def filesystem_folder_get(
    client: foundry.v2.FoundryClient,
    folder_rid: str,
    preview: Optional[bool],
):
    """
    Get the Folder with the specified rid.
    """
    result = client.filesystem.Folder.get(
        folder_rid=folder_rid,
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("functions")
def functions():
    pass


@functions.group("query")
def functions_query():
    pass


@functions_query.command("execute")
@click.argument("query_api_name", type=str, required=True)
@click.option("--parameters", type=str, required=True, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def functions_query_execute(
    client: foundry.v2.FoundryClient,
    query_api_name: str,
    parameters: str,
    preview: Optional[bool],
):
    """
    Executes a Query using the given parameters.

    Optional parameters do not need to be supplied.

    """
    result = client.functions.Query.execute(
        query_api_name=query_api_name,
        parameters=json.loads(parameters),
        preview=preview,
    )
    click.echo(repr(result))


@functions_query.command("get")
@click.argument("query_api_name", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def functions_query_get(
    client: foundry.v2.FoundryClient,
    query_api_name: str,
    preview: Optional[bool],
):
    """
    Gets a specific query type with the given API name.

    """
    result = client.functions.Query.get(
        query_api_name=query_api_name,
        preview=preview,
    )
    click.echo(repr(result))


@functions_query.command("get_by_rid")
@click.option("--rid", type=str, required=True, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def functions_query_get_by_rid(
    client: foundry.v2.FoundryClient,
    rid: str,
    preview: Optional[bool],
):
    """
    Gets a specific query type with the given RID.

    """
    result = client.functions.Query.get_by_rid(
        rid=rid,
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("geo")
def geo():
    pass


@cli.group("ontologies")
def ontologies():
    pass


@cli.group("ontologies_v2")
def ontologies_v2():
    pass


@ontologies_v2.group("time_series_property_v2")
def ontologies_v2_time_series_property_v2():
    pass


@ontologies_v2_time_series_property_v2.command("get_first_point")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("property", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_time_series_property_v2_get_first_point(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    property: str,
    artifact_repository: Optional[str],
    package_name: Optional[str],
):
    """
    Get the first point of a time series property.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.TimeSeriesPropertyV2.get_first_point(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        property=property,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    click.echo(repr(result))


@ontologies_v2_time_series_property_v2.command("get_last_point")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("property", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_time_series_property_v2_get_last_point(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    property: str,
    artifact_repository: Optional[str],
    package_name: Optional[str],
):
    """
    Get the last point of a time series property.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.TimeSeriesPropertyV2.get_last_point(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        property=property,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    click.echo(repr(result))


@ontologies_v2_time_series_property_v2.command("stream_points")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("property", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--range", type=str, required=False, help="""""")
@click.pass_obj
def ontologies_v2_time_series_property_v2_stream_points(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    property: str,
    artifact_repository: Optional[str],
    package_name: Optional[str],
    range: Optional[str],
):
    """
    Stream all of the points of a time series property.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.TimeSeriesPropertyV2.stream_points(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        property=property,
        artifact_repository=artifact_repository,
        package_name=package_name,
        range=None if range is None else json.loads(range),
    )
    click.echo(result)


@ontologies_v2.group("query")
def ontologies_v2_query():
    pass


@ontologies_v2_query.command("execute")
@click.argument("ontology", type=str, required=True)
@click.argument("query_api_name", type=str, required=True)
@click.option("--parameters", type=str, required=True, help="""""")
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_query_execute(
    client: foundry.v2.FoundryClient,
    ontology: str,
    query_api_name: str,
    parameters: str,
    artifact_repository: Optional[str],
    package_name: Optional[str],
):
    """
    Executes a Query using the given parameters.

    Optional parameters do not need to be supplied.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.Query.execute(
        ontology=ontology,
        query_api_name=query_api_name,
        parameters=json.loads(parameters),
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    click.echo(repr(result))


@ontologies_v2.group("ontology_v2")
def ontologies_v2_ontology_v2():
    pass


@ontologies_v2_ontology_v2.command("get")
@click.argument("ontology", type=str, required=True)
@click.pass_obj
def ontologies_v2_ontology_v2_get(
    client: foundry.v2.FoundryClient,
    ontology: str,
):
    """
    Gets a specific ontology with the given Ontology RID.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.get(
        ontology=ontology,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2.command("get_full_metadata")
@click.argument("ontology", type=str, required=True)
@click.pass_obj
def ontologies_v2_ontology_v2_get_full_metadata(
    client: foundry.v2.FoundryClient,
    ontology: str,
):
    """
    Get the full Ontology metadata. This includes the objects, links, actions, queries, and interfaces.

    """
    result = client.ontologies.Ontology.get_full_metadata(
        ontology=ontology,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2.group("query_type")
def ontologies_v2_ontology_v2_query_type():
    pass


@ontologies_v2_ontology_v2_query_type.command("get")
@click.argument("ontology", type=str, required=True)
@click.argument("query_api_name", type=str, required=True)
@click.pass_obj
def ontologies_v2_ontology_v2_query_type_get(
    client: foundry.v2.FoundryClient,
    ontology: str,
    query_api_name: str,
):
    """
    Gets a specific query type with the given API name.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.QueryType.get(
        ontology=ontology,
        query_api_name=query_api_name,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2_query_type.command("list")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_v2_ontology_v2_query_type_list(
    client: foundry.v2.FoundryClient,
    ontology: str,
    page_size: Optional[int],
):
    """
    Lists the query types for the given Ontology.

    Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
    results available, at least one result will be present in the response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.QueryType.list(
        ontology=ontology,
        page_size=page_size,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2_query_type.command("page")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_v2_ontology_v2_query_type_page(
    client: foundry.v2.FoundryClient,
    ontology: str,
    page_size: Optional[int],
    page_token: Optional[str],
):
    """
    Lists the query types for the given Ontology.

    Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
    results available, at least one result will be present in the response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.QueryType.page(
        ontology=ontology,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2.group("object_type_v2")
def ontologies_v2_ontology_v2_object_type_v2():
    pass


@ontologies_v2_ontology_v2_object_type_v2.command("get")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.pass_obj
def ontologies_v2_ontology_v2_object_type_v2_get(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
):
    """
    Gets a specific object type with the given API name.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ObjectType.get(
        ontology=ontology,
        object_type=object_type,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2_object_type_v2.command("get_outgoing_link_type")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("link_type", type=str, required=True)
@click.pass_obj
def ontologies_v2_ontology_v2_object_type_v2_get_outgoing_link_type(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    link_type: str,
):
    """
    Get an outgoing link for an object type.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ObjectType.get_outgoing_link_type(
        ontology=ontology,
        object_type=object_type,
        link_type=link_type,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2_object_type_v2.command("list")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_v2_ontology_v2_object_type_v2_list(
    client: foundry.v2.FoundryClient,
    ontology: str,
    page_size: Optional[int],
):
    """
    Lists the object types for the given Ontology.

    Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
    more results available, at least one result will be present in the
    response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ObjectType.list(
        ontology=ontology,
        page_size=page_size,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2_object_type_v2.command("list_outgoing_link_types")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_v2_ontology_v2_object_type_v2_list_outgoing_link_types(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    page_size: Optional[int],
):
    """
    List the outgoing links for an object type.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ObjectType.list_outgoing_link_types(
        ontology=ontology,
        object_type=object_type,
        page_size=page_size,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2_object_type_v2.command("page")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_v2_ontology_v2_object_type_v2_page(
    client: foundry.v2.FoundryClient,
    ontology: str,
    page_size: Optional[int],
    page_token: Optional[str],
):
    """
    Lists the object types for the given Ontology.

    Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
    more results available, at least one result will be present in the
    response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ObjectType.page(
        ontology=ontology,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2_object_type_v2.command("page_outgoing_link_types")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_v2_ontology_v2_object_type_v2_page_outgoing_link_types(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    page_size: Optional[int],
    page_token: Optional[str],
):
    """
    List the outgoing links for an object type.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ObjectType.page_outgoing_link_types(
        ontology=ontology,
        object_type=object_type,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2.group("action_type_v2")
def ontologies_v2_ontology_v2_action_type_v2():
    pass


@ontologies_v2_ontology_v2_action_type_v2.command("get")
@click.argument("ontology", type=str, required=True)
@click.argument("action_type", type=str, required=True)
@click.pass_obj
def ontologies_v2_ontology_v2_action_type_v2_get(
    client: foundry.v2.FoundryClient,
    ontology: str,
    action_type: str,
):
    """
    Gets a specific action type with the given API name.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ActionType.get(
        ontology=ontology,
        action_type=action_type,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2_action_type_v2.command("list")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_v2_ontology_v2_action_type_v2_list(
    client: foundry.v2.FoundryClient,
    ontology: str,
    page_size: Optional[int],
):
    """
    Lists the action types for the given Ontology.

    Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
    results available, at least one result will be present in the response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ActionType.list(
        ontology=ontology,
        page_size=page_size,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_v2_action_type_v2.command("page")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_v2_ontology_v2_action_type_v2_page(
    client: foundry.v2.FoundryClient,
    ontology: str,
    page_size: Optional[int],
    page_token: Optional[str],
):
    """
    Lists the action types for the given Ontology.

    Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
    results available, at least one result will be present in the response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ActionType.page(
        ontology=ontology,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies_v2.group("ontology_object_v2")
def ontologies_v2_ontology_object_v2():
    pass


@ontologies_v2_ontology_object_v2.command("aggregate")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--aggregation", type=str, required=True, help="""""")
@click.option("--group_by", type=str, required=True, help="""""")
@click.option(
    "--accuracy",
    type=click.Choice(["REQUIRE_ACCURATE", "ALLOW_APPROXIMATE"]),
    required=False,
    help="""""",
)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--where", type=str, required=False, help="""""")
@click.pass_obj
def ontologies_v2_ontology_object_v2_aggregate(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    aggregation: str,
    group_by: str,
    accuracy: Optional[Literal["REQUIRE_ACCURATE", "ALLOW_APPROXIMATE"]],
    artifact_repository: Optional[str],
    package_name: Optional[str],
    where: Optional[str],
):
    """
    Perform functions on object fields in the specified ontology and object type.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.aggregate(
        ontology=ontology,
        object_type=object_type,
        aggregation=json.loads(aggregation),
        group_by=json.loads(group_by),
        accuracy=accuracy,
        artifact_repository=artifact_repository,
        package_name=package_name,
        where=None if where is None else json.loads(where),
    )
    click.echo(repr(result))


@ontologies_v2_ontology_object_v2.command("count")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_ontology_object_v2_count(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    artifact_repository: Optional[str],
    package_name: Optional[str],
):
    """
    Returns a count of the objects of the given object type.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.count(
        ontology=ontology,
        object_type=object_type,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_object_v2.command("get")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--exclude_rid", type=bool, required=False, help="""excludeRid""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--select", type=str, required=False, help="""select""")
@click.pass_obj
def ontologies_v2_ontology_object_v2_get(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    artifact_repository: Optional[str],
    exclude_rid: Optional[bool],
    package_name: Optional[str],
    select: Optional[str],
):
    """
    Gets a specific object with the given primary key.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.get(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        package_name=package_name,
        select=None if select is None else json.loads(select),
    )
    click.echo(repr(result))


@ontologies_v2_ontology_object_v2.command("list")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--exclude_rid", type=bool, required=False, help="""excludeRid""")
@click.option("--order_by", type=str, required=False, help="""orderBy""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--select", type=str, required=False, help="""select""")
@click.pass_obj
def ontologies_v2_ontology_object_v2_list(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    artifact_repository: Optional[str],
    exclude_rid: Optional[bool],
    order_by: Optional[str],
    package_name: Optional[str],
    page_size: Optional[int],
    select: Optional[str],
):
    """
    Lists the objects for the given Ontology and object type.

    Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
    repeated objects in the response pages.

    For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
    are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

    Each page may be smaller or larger than the requested page size. However, it
    is guaranteed that if there are more results available, at least one result will be present
    in the response.

    Note that null value properties will not be returned.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.list(
        ontology=ontology,
        object_type=object_type,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=order_by,
        package_name=package_name,
        page_size=page_size,
        select=None if select is None else json.loads(select),
    )
    click.echo(repr(result))


@ontologies_v2_ontology_object_v2.command("page")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--exclude_rid", type=bool, required=False, help="""excludeRid""")
@click.option("--order_by", type=str, required=False, help="""orderBy""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--select", type=str, required=False, help="""select""")
@click.pass_obj
def ontologies_v2_ontology_object_v2_page(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    artifact_repository: Optional[str],
    exclude_rid: Optional[bool],
    order_by: Optional[str],
    package_name: Optional[str],
    page_size: Optional[int],
    page_token: Optional[str],
    select: Optional[str],
):
    """
    Lists the objects for the given Ontology and object type.

    Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
    repeated objects in the response pages.

    For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
    are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

    Each page may be smaller or larger than the requested page size. However, it
    is guaranteed that if there are more results available, at least one result will be present
    in the response.

    Note that null value properties will not be returned.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.page(
        ontology=ontology,
        object_type=object_type,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=order_by,
        package_name=package_name,
        page_size=page_size,
        page_token=page_token,
        select=None if select is None else json.loads(select),
    )
    click.echo(repr(result))


@ontologies_v2_ontology_object_v2.command("search")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option(
    "--select",
    type=str,
    required=True,
    help="""The API names of the object type properties to include in the response.
""",
)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option(
    "--exclude_rid",
    type=bool,
    required=False,
    help="""A flag to exclude the retrieval of the `__rid` property.
Setting this to true may improve performance of this endpoint for object types in OSV2.
""",
)
@click.option("--order_by", type=str, required=False, help="""""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.option("--where", type=str, required=False, help="""""")
@click.pass_obj
def ontologies_v2_ontology_object_v2_search(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    select: str,
    artifact_repository: Optional[str],
    exclude_rid: Optional[bool],
    order_by: Optional[str],
    package_name: Optional[str],
    page_size: Optional[int],
    page_token: Optional[str],
    where: Optional[str],
):
    """
    Search for objects in the specified ontology and object type. The request body is used
    to filter objects based on the specified query. The supported queries are:

    | Query type                              | Description                                                                                                       | Supported Types                 |
    |-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------|
    | lt                                      | The provided property is less than the provided value.                                                            | number, string, date, timestamp |
    | gt                                      | The provided property is greater than the provided value.                                                         | number, string, date, timestamp |
    | lte                                     | The provided property is less than or equal to the provided value.                                                | number, string, date, timestamp |
    | gte                                     | The provided property is greater than or equal to the provided value.                                             | number, string, date, timestamp |
    | eq                                      | The provided property is exactly equal to the provided value.                                                     | number, string, date, timestamp |
    | isNull                                  | The provided property is (or is not) null.                                                                        | all                             |
    | contains                                | The provided property contains the provided value.                                                                | array                           |
    | not                                     | The sub-query does not match.                                                                                     | N/A (applied on a query)        |
    | and                                     | All the sub-queries match.                                                                                        | N/A (applied on queries)        |
    | or                                      | At least one of the sub-queries match.                                                                            | N/A (applied on queries)        |
    | startsWith                              | The provided property starts with the provided value.                                                             | string                          |
    | containsAllTermsInOrderPrefixLastTerm   | The provided property contains all the terms provided in order. The last term can be a partial prefix match.      | string                          |
    | containsAllTermsInOrder                 | The provided property contains the provided value as a substring.                                                 | string                          |
    | containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
    | containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.search(
        ontology=ontology,
        object_type=object_type,
        select=json.loads(select),
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=None if order_by is None else json.loads(order_by),
        package_name=package_name,
        page_size=page_size,
        page_token=page_token,
        where=None if where is None else json.loads(where),
    )
    click.echo(repr(result))


@ontologies_v2.group("ontology_object_set")
def ontologies_v2_ontology_object_set():
    pass


@ontologies_v2_ontology_object_set.command("aggregate")
@click.argument("ontology", type=str, required=True)
@click.option("--aggregation", type=str, required=True, help="""""")
@click.option("--group_by", type=str, required=True, help="""""")
@click.option("--object_set", type=str, required=True, help="""""")
@click.option(
    "--accuracy",
    type=click.Choice(["REQUIRE_ACCURATE", "ALLOW_APPROXIMATE"]),
    required=False,
    help="""""",
)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_ontology_object_set_aggregate(
    client: foundry.v2.FoundryClient,
    ontology: str,
    aggregation: str,
    group_by: str,
    object_set: str,
    accuracy: Optional[Literal["REQUIRE_ACCURATE", "ALLOW_APPROXIMATE"]],
    artifact_repository: Optional[str],
    package_name: Optional[str],
):
    """
    Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObjectSet.aggregate(
        ontology=ontology,
        aggregation=json.loads(aggregation),
        group_by=json.loads(group_by),
        object_set=json.loads(object_set),
        accuracy=accuracy,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_object_set.command("create_temporary")
@click.argument("ontology", type=str, required=True)
@click.option("--object_set", type=str, required=True, help="""""")
@click.pass_obj
def ontologies_v2_ontology_object_set_create_temporary(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_set: str,
):
    """
    Creates a temporary `ObjectSet` from the given definition.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read api:ontologies-write`.

    """
    result = client.ontologies.OntologyObjectSet.create_temporary(
        ontology=ontology,
        object_set=json.loads(object_set),
    )
    click.echo(repr(result))


@ontologies_v2_ontology_object_set.command("get")
@click.argument("ontology", type=str, required=True)
@click.argument("object_set_rid", type=str, required=True)
@click.pass_obj
def ontologies_v2_ontology_object_set_get(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_set_rid: str,
):
    """
    Gets the definition of the `ObjectSet` with the given RID.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObjectSet.get(
        ontology=ontology,
        object_set_rid=object_set_rid,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_object_set.command("load")
@click.argument("ontology", type=str, required=True)
@click.option("--object_set", type=str, required=True, help="""""")
@click.option("--select", type=str, required=True, help="""""")
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option(
    "--exclude_rid",
    type=bool,
    required=False,
    help="""A flag to exclude the retrieval of the `__rid` property.
Setting this to true may improve performance of this endpoint for object types in OSV2.
""",
)
@click.option("--order_by", type=str, required=False, help="""""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.pass_obj
def ontologies_v2_ontology_object_set_load(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_set: str,
    select: str,
    artifact_repository: Optional[str],
    exclude_rid: Optional[bool],
    order_by: Optional[str],
    package_name: Optional[str],
    page_size: Optional[int],
    page_token: Optional[str],
):
    """
    Load the ontology objects present in the `ObjectSet` from the provided object set definition.

    For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
    are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

    Note that null value properties will not be returned.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObjectSet.load(
        ontology=ontology,
        object_set=json.loads(object_set),
        select=json.loads(select),
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=None if order_by is None else json.loads(order_by),
        package_name=package_name,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies_v2.group("ontology_interface")
def ontologies_v2_ontology_interface():
    pass


@ontologies_v2_ontology_interface.command("aggregate")
@click.argument("ontology", type=str, required=True)
@click.argument("interface_type", type=str, required=True)
@click.option("--aggregation", type=str, required=True, help="""""")
@click.option("--group_by", type=str, required=True, help="""""")
@click.option(
    "--accuracy",
    type=click.Choice(["REQUIRE_ACCURATE", "ALLOW_APPROXIMATE"]),
    required=False,
    help="""""",
)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--where", type=str, required=False, help="""""")
@click.pass_obj
def ontologies_v2_ontology_interface_aggregate(
    client: foundry.v2.FoundryClient,
    ontology: str,
    interface_type: str,
    aggregation: str,
    group_by: str,
    accuracy: Optional[Literal["REQUIRE_ACCURATE", "ALLOW_APPROXIMATE"]],
    preview: Optional[bool],
    where: Optional[str],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint will be removed once TS OSDK is updated to use `objectSets/aggregate` with interface object
    sets.
    :::
    :::callout{theme=warning title=Warning}
      This endpoint is in preview and may be modified or removed at any time.
      To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Perform functions on object fields in the specified ontology and of the specified interface type. Any
    properties specified in the query must be shared property type API names defined on the interface.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyInterface.aggregate(
        ontology=ontology,
        interface_type=interface_type,
        aggregation=json.loads(aggregation),
        group_by=json.loads(group_by),
        accuracy=accuracy,
        preview=preview,
        where=None if where is None else json.loads(where),
    )
    click.echo(repr(result))


@ontologies_v2_ontology_interface.command("get")
@click.argument("ontology", type=str, required=True)
@click.argument("interface_type", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def ontologies_v2_ontology_interface_get(
    client: foundry.v2.FoundryClient,
    ontology: str,
    interface_type: str,
    preview: Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
      This endpoint is in preview and may be modified or removed at any time.
      To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Gets a specific object type with the given API name.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyInterface.get(
        ontology=ontology,
        interface_type=interface_type,
        preview=preview,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_interface.command("list")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def ontologies_v2_ontology_interface_list(
    client: foundry.v2.FoundryClient,
    ontology: str,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
      This endpoint is in preview and may be modified or removed at any time.
      To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Lists the interface types for the given Ontology.

    Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
    results available, at least one result will be present in the response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyInterface.list(
        ontology=ontology,
        page_size=page_size,
        preview=preview,
    )
    click.echo(repr(result))


@ontologies_v2_ontology_interface.command("page")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def ontologies_v2_ontology_interface_page(
    client: foundry.v2.FoundryClient,
    ontology: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
      This endpoint is in preview and may be modified or removed at any time.
      To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Lists the interface types for the given Ontology.

    Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
    results available, at least one result will be present in the response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyInterface.page(
        ontology=ontology,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@ontologies_v2.group("linked_object_v2")
def ontologies_v2_linked_object_v2():
    pass


@ontologies_v2_linked_object_v2.command("get_linked_object")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("link_type", type=str, required=True)
@click.argument("linked_object_primary_key", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--exclude_rid", type=bool, required=False, help="""excludeRid""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--select", type=str, required=False, help="""select""")
@click.pass_obj
def ontologies_v2_linked_object_v2_get_linked_object(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    link_type: str,
    linked_object_primary_key: str,
    artifact_repository: Optional[str],
    exclude_rid: Optional[bool],
    package_name: Optional[str],
    select: Optional[str],
):
    """
    Get a specific linked object that originates from another object.

    If there is no link between the two objects, `LinkedObjectNotFound` is thrown.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.LinkedObject.get_linked_object(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        link_type=link_type,
        linked_object_primary_key=linked_object_primary_key,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        package_name=package_name,
        select=None if select is None else json.loads(select),
    )
    click.echo(repr(result))


@ontologies_v2_linked_object_v2.command("list_linked_objects")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("link_type", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--exclude_rid", type=bool, required=False, help="""excludeRid""")
@click.option("--order_by", type=str, required=False, help="""orderBy""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--select", type=str, required=False, help="""select""")
@click.pass_obj
def ontologies_v2_linked_object_v2_list_linked_objects(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    link_type: str,
    artifact_repository: Optional[str],
    exclude_rid: Optional[bool],
    order_by: Optional[str],
    package_name: Optional[str],
    page_size: Optional[int],
    select: Optional[str],
):
    """
    Lists the linked objects for a specific object and the given link type.

    Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
    repeated objects in the response pages.

    For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
    are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

    Each page may be smaller or larger than the requested page size. However, it
    is guaranteed that if there are more results available, at least one result will be present
    in the response.

    Note that null value properties will not be returned.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.LinkedObject.list_linked_objects(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        link_type=link_type,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=order_by,
        package_name=package_name,
        page_size=page_size,
        select=None if select is None else json.loads(select),
    )
    click.echo(repr(result))


@ontologies_v2_linked_object_v2.command("page_linked_objects")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("link_type", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--exclude_rid", type=bool, required=False, help="""excludeRid""")
@click.option("--order_by", type=str, required=False, help="""orderBy""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--select", type=str, required=False, help="""select""")
@click.pass_obj
def ontologies_v2_linked_object_v2_page_linked_objects(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    link_type: str,
    artifact_repository: Optional[str],
    exclude_rid: Optional[bool],
    order_by: Optional[str],
    package_name: Optional[str],
    page_size: Optional[int],
    page_token: Optional[str],
    select: Optional[str],
):
    """
    Lists the linked objects for a specific object and the given link type.

    Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
    repeated objects in the response pages.

    For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
    are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

    Each page may be smaller or larger than the requested page size. However, it
    is guaranteed that if there are more results available, at least one result will be present
    in the response.

    Note that null value properties will not be returned.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.LinkedObject.page_linked_objects(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        link_type=link_type,
        artifact_repository=artifact_repository,
        exclude_rid=exclude_rid,
        order_by=order_by,
        package_name=package_name,
        page_size=page_size,
        page_token=page_token,
        select=None if select is None else json.loads(select),
    )
    click.echo(repr(result))


@ontologies_v2.group("attachment_property_v2")
def ontologies_v2_attachment_property_v2():
    pass


@ontologies_v2_attachment_property_v2.command("get_attachment")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("property", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_attachment_property_v2_get_attachment(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    property: str,
    artifact_repository: Optional[str],
    package_name: Optional[str],
):
    """
    Get the metadata of attachments parented to the given object.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.AttachmentProperty.get_attachment(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        property=property,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    click.echo(repr(result))


@ontologies_v2_attachment_property_v2.command("get_attachment_by_rid")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("property", type=str, required=True)
@click.argument("attachment_rid", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_attachment_property_v2_get_attachment_by_rid(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    property: str,
    attachment_rid: str,
    artifact_repository: Optional[str],
    package_name: Optional[str],
):
    """
    Get the metadata of a particular attachment in an attachment list.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.AttachmentProperty.get_attachment_by_rid(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        property=property,
        attachment_rid=attachment_rid,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    click.echo(repr(result))


@ontologies_v2_attachment_property_v2.command("read_attachment")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("property", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_attachment_property_v2_read_attachment(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    property: str,
    artifact_repository: Optional[str],
    package_name: Optional[str],
):
    """
    Get the content of an attachment.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.AttachmentProperty.read_attachment(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        property=property,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    click.echo(result)


@ontologies_v2_attachment_property_v2.command("read_attachment_by_rid")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("property", type=str, required=True)
@click.argument("attachment_rid", type=str, required=True)
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_attachment_property_v2_read_attachment_by_rid(
    client: foundry.v2.FoundryClient,
    ontology: str,
    object_type: str,
    primary_key: str,
    property: str,
    attachment_rid: str,
    artifact_repository: Optional[str],
    package_name: Optional[str],
):
    """
    Get the content of an attachment by its RID.

    The RID must exist in the attachment array of the property.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.AttachmentProperty.read_attachment_by_rid(
        ontology=ontology,
        object_type=object_type,
        primary_key=primary_key,
        property=property,
        attachment_rid=attachment_rid,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    click.echo(result)


@ontologies_v2.group("attachment")
def ontologies_v2_attachment():
    pass


@ontologies_v2_attachment.command("read")
@click.argument("attachment_rid", type=str, required=True)
@click.pass_obj
def ontologies_v2_attachment_read(
    client: foundry.v2.FoundryClient,
    attachment_rid: str,
):
    """
    Get the content of an attachment.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.Attachment.read(
        attachment_rid=attachment_rid,
    )
    click.echo(result)


@ontologies_v2_attachment.command("upload")
@click.argument("body", type=click.File("rb"), required=True)
@click.option("--content_length", type=str, required=True, help="""Content-Length""")
@click.option("--content_type", type=str, required=True, help="""Content-Type""")
@click.option("--filename", type=str, required=True, help="""filename""")
@click.pass_obj
def ontologies_v2_attachment_upload(
    client: foundry.v2.FoundryClient,
    body: io.BufferedReader,
    content_length: str,
    content_type: str,
    filename: str,
):
    """
    Upload an attachment to use in an action. Any attachment which has not been linked to an object via
    an action within one hour after upload will be removed.
    Previously mapped attachments which are not connected to any object anymore are also removed on
    a biweekly basis.
    The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-write`.

    """
    result = client.ontologies.Attachment.upload(
        body=body.read(),
        content_length=content_length,
        content_type=content_type,
        filename=filename,
    )
    click.echo(repr(result))


@ontologies_v2.group("action")
def ontologies_v2_action():
    pass


@ontologies_v2_action.command("apply")
@click.argument("ontology", type=str, required=True)
@click.argument("action", type=str, required=True)
@click.option("--parameters", type=str, required=True, help="""""")
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--options", type=str, required=False, help="""""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_action_apply(
    client: foundry.v2.FoundryClient,
    ontology: str,
    action: str,
    parameters: str,
    artifact_repository: Optional[str],
    options: Optional[str],
    package_name: Optional[str],
):
    """
    Applies an action using the given parameters.

    Changes to the Ontology are eventually consistent and may take some time to be visible.

    Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) are not currently supported by
    this endpoint.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read api:ontologies-write`.

    """
    result = client.ontologies.Action.apply(
        ontology=ontology,
        action=action,
        parameters=json.loads(parameters),
        artifact_repository=artifact_repository,
        options=None if options is None else json.loads(options),
        package_name=package_name,
    )
    click.echo(repr(result))


@ontologies_v2_action.command("apply_batch")
@click.argument("ontology", type=str, required=True)
@click.argument("action", type=str, required=True)
@click.option("--requests", type=str, required=True, help="""""")
@click.option("--artifact_repository", type=str, required=False, help="""artifactRepository""")
@click.option("--options", type=str, required=False, help="""""")
@click.option("--package_name", type=str, required=False, help="""packageName""")
@click.pass_obj
def ontologies_v2_action_apply_batch(
    client: foundry.v2.FoundryClient,
    ontology: str,
    action: str,
    requests: str,
    artifact_repository: Optional[str],
    options: Optional[str],
    package_name: Optional[str],
):
    """
    Applies multiple actions (of the same Action Type) using the given parameters.
    Changes to the Ontology are eventually consistent and may take some time to be visible.

    Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
    call Functions may receive a higher limit.

    Note that [notifications](/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read api:ontologies-write`.

    """
    result = client.ontologies.Action.apply_batch(
        ontology=ontology,
        action=action,
        requests=json.loads(requests),
        artifact_repository=artifact_repository,
        options=None if options is None else json.loads(options),
        package_name=package_name,
    )
    click.echo(repr(result))


@cli.group("orchestration")
def orchestration():
    pass


@orchestration.group("schedule")
def orchestration_schedule():
    pass


@orchestration_schedule.command("create")
@click.option("--action", type=str, required=True, help="""""")
@click.option("--description", type=str, required=False, help="""""")
@click.option("--display_name", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--scope_mode", type=str, required=False, help="""""")
@click.option(
    "--trigger",
    type=str,
    required=False,
    help="""The schedule trigger. If the requesting user does not have
permission to see the trigger, this will be empty.
""",
)
@click.pass_obj
def orchestration_schedule_create(
    client: foundry.v2.FoundryClient,
    action: str,
    description: Optional[str],
    display_name: Optional[str],
    preview: Optional[bool],
    scope_mode: Optional[str],
    trigger: Optional[str],
):
    """
    Creates a new Schedule.
    """
    result = client.orchestration.Schedule.create(
        action=json.loads(action),
        description=description,
        display_name=display_name,
        preview=preview,
        scope_mode=None if scope_mode is None else json.loads(scope_mode),
        trigger=None if trigger is None else json.loads(trigger),
    )
    click.echo(repr(result))


@orchestration_schedule.command("delete")
@click.argument("schedule_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def orchestration_schedule_delete(
    client: foundry.v2.FoundryClient,
    schedule_rid: str,
    preview: Optional[bool],
):
    """
    Delete the Schedule with the specified rid.
    """
    result = client.orchestration.Schedule.delete(
        schedule_rid=schedule_rid,
        preview=preview,
    )
    click.echo(repr(result))


@orchestration_schedule.command("get")
@click.argument("schedule_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def orchestration_schedule_get(
    client: foundry.v2.FoundryClient,
    schedule_rid: str,
    preview: Optional[bool],
):
    """
    Get the Schedule with the specified rid.
    """
    result = client.orchestration.Schedule.get(
        schedule_rid=schedule_rid,
        preview=preview,
    )
    click.echo(repr(result))


@orchestration_schedule.command("pause")
@click.argument("schedule_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def orchestration_schedule_pause(
    client: foundry.v2.FoundryClient,
    schedule_rid: str,
    preview: Optional[bool],
):
    """ """
    result = client.orchestration.Schedule.pause(
        schedule_rid=schedule_rid,
        preview=preview,
    )
    click.echo(repr(result))


@orchestration_schedule.command("replace")
@click.argument("schedule_rid", type=str, required=True)
@click.option("--action", type=str, required=True, help="""""")
@click.option("--description", type=str, required=False, help="""""")
@click.option("--display_name", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--scope_mode", type=str, required=False, help="""""")
@click.option(
    "--trigger",
    type=str,
    required=False,
    help="""The schedule trigger. If the requesting user does not have
permission to see the trigger, this will be empty.
""",
)
@click.pass_obj
def orchestration_schedule_replace(
    client: foundry.v2.FoundryClient,
    schedule_rid: str,
    action: str,
    description: Optional[str],
    display_name: Optional[str],
    preview: Optional[bool],
    scope_mode: Optional[str],
    trigger: Optional[str],
):
    """
    Replace the Schedule with the specified rid.
    """
    result = client.orchestration.Schedule.replace(
        schedule_rid=schedule_rid,
        action=json.loads(action),
        description=description,
        display_name=display_name,
        preview=preview,
        scope_mode=None if scope_mode is None else json.loads(scope_mode),
        trigger=None if trigger is None else json.loads(trigger),
    )
    click.echo(repr(result))


@orchestration_schedule.command("run")
@click.argument("schedule_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def orchestration_schedule_run(
    client: foundry.v2.FoundryClient,
    schedule_rid: str,
    preview: Optional[bool],
):
    """ """
    result = client.orchestration.Schedule.run(
        schedule_rid=schedule_rid,
        preview=preview,
    )
    click.echo(repr(result))


@orchestration_schedule.command("unpause")
@click.argument("schedule_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def orchestration_schedule_unpause(
    client: foundry.v2.FoundryClient,
    schedule_rid: str,
    preview: Optional[bool],
):
    """ """
    result = client.orchestration.Schedule.unpause(
        schedule_rid=schedule_rid,
        preview=preview,
    )
    click.echo(repr(result))


@orchestration.group("build")
def orchestration_build():
    pass


@orchestration_build.command("create")
@click.option("--fallback_branches", type=str, required=True, help="""""")
@click.option("--target", type=str, required=True, help="""The targets of the schedule.""")
@click.option("--abort_on_failure", type=bool, required=False, help="""""")
@click.option(
    "--branch_name", type=str, required=False, help="""The target branch the build should run on."""
)
@click.option("--force_build", type=bool, required=False, help="""""")
@click.option("--notifications_enabled", type=bool, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--retry_backoff_duration", type=str, required=False, help="""""")
@click.option(
    "--retry_count",
    type=int,
    required=False,
    help="""The number of retry attempts for failed jobs.""",
)
@click.pass_obj
def orchestration_build_create(
    client: foundry.v2.FoundryClient,
    fallback_branches: str,
    target: str,
    abort_on_failure: Optional[bool],
    branch_name: Optional[str],
    force_build: Optional[bool],
    notifications_enabled: Optional[bool],
    preview: Optional[bool],
    retry_backoff_duration: Optional[str],
    retry_count: Optional[int],
):
    """ """
    result = client.orchestration.Build.create(
        fallback_branches=json.loads(fallback_branches),
        target=json.loads(target),
        abort_on_failure=abort_on_failure,
        branch_name=branch_name,
        force_build=force_build,
        notifications_enabled=notifications_enabled,
        preview=preview,
        retry_backoff_duration=(
            None if retry_backoff_duration is None else json.loads(retry_backoff_duration)
        ),
        retry_count=retry_count,
    )
    click.echo(repr(result))


@orchestration_build.command("get")
@click.argument("build_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def orchestration_build_get(
    client: foundry.v2.FoundryClient,
    build_rid: str,
    preview: Optional[bool],
):
    """
    Get the Build with the specified rid.
    """
    result = client.orchestration.Build.get(
        build_rid=build_rid,
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("streams")
def streams():
    pass


@streams.group("dataset")
def streams_dataset():
    pass


@streams_dataset.command("create")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--parent_folder_rid", type=str, required=True, help="""""")
@click.option(
    "--branch_name",
    type=str,
    required=False,
    help="""The branch to create the initial stream on. If not specified, the default branch will be used
('master' for most enrollments).
""",
)
@click.option(
    "--compressed",
    type=bool,
    required=False,
    help="""Whether or not compression is enabled for the stream. Defaults to false.
""",
)
@click.option(
    "--partitions_count",
    type=int,
    required=False,
    help="""The number of partitions for the Foundry stream.

Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions
are recommended.

If not specified, 1 partition is used.

This value cannot be changed later.
""",
)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option(
    "--stream_type",
    type=click.Choice(["LOW_LATENCY", "HIGH_THROUGHPUT"]),
    required=False,
    help="""A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and
LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
""",
)
@click.pass_obj
def streams_dataset_create(
    client: foundry.v2.FoundryClient,
    name: str,
    parent_folder_rid: str,
    branch_name: Optional[str],
    compressed: Optional[bool],
    partitions_count: Optional[int],
    preview: Optional[bool],
    stream_type: Optional[Literal["LOW_LATENCY", "HIGH_THROUGHPUT"]],
):
    """
    Creates a streaming dataset with a stream on the specified branch, or if no branch is specified, on the
    default branch ('master' for most enrollments). For more information on streaming datasets, refer to the
    [streams](/docs/foundry/data-integration/streams/) user documentation.

    """
    result = client.streams.Dataset.create(
        name=name,
        parent_folder_rid=parent_folder_rid,
        branch_name=branch_name,
        compressed=compressed,
        partitions_count=partitions_count,
        preview=preview,
        stream_type=stream_type,
    )
    click.echo(repr(result))


@streams_dataset.group("stream")
def streams_dataset_stream():
    pass


@streams_dataset_stream.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("stream_branch_name", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def streams_dataset_stream_get(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    stream_branch_name: str,
    preview: Optional[bool],
):
    """
    Get a stream by its branch name. If the branch does not exist, there is no stream on that branch, or the
    user does not have permission to access the stream, a 404 error will be returned.

    """
    result = client.streams.Dataset.Stream.get(
        dataset_rid=dataset_rid,
        stream_branch_name=stream_branch_name,
        preview=preview,
    )
    click.echo(repr(result))


@streams_dataset_stream.command("publish_record")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("stream_branch_name", type=str, required=True)
@click.option(
    "--record",
    type=str,
    required=True,
    help="""The record to publish to the stream
""",
)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option(
    "--view_rid",
    type=str,
    required=False,
    help="""If provided, this endpoint will only write to the stream corresponding to the specified view rid. If
not provided, this endpoint will write the latest stream on the branch.

Providing this value is an advanced configuration, to be used when additional control over the
underlying streaming data structures is needed.
""",
)
@click.pass_obj
def streams_dataset_stream_publish_record(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    stream_branch_name: str,
    record: str,
    preview: Optional[bool],
    view_rid: Optional[str],
):
    """
    Publish a single record to the stream. The record will be validated against the stream's schema, and
    rejected if it is invalid.

    """
    result = client.streams.Dataset.Stream.publish_record(
        dataset_rid=dataset_rid,
        stream_branch_name=stream_branch_name,
        record=json.loads(record),
        preview=preview,
        view_rid=view_rid,
    )
    click.echo(repr(result))


@streams_dataset_stream.command("publish_records")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("stream_branch_name", type=str, required=True)
@click.option(
    "--records",
    type=str,
    required=True,
    help="""The records to publish to the stream
""",
)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option(
    "--view_rid",
    type=str,
    required=False,
    help="""If provided, this endpoint will only write to the stream corresponding to the specified view rid. If
not provided, this endpoint will write to the latest stream on the branch.

Providing this value is an advanced configuration, to be used when additional control over the
underlying streaming data structures is needed.
""",
)
@click.pass_obj
def streams_dataset_stream_publish_records(
    client: foundry.v2.FoundryClient,
    dataset_rid: str,
    stream_branch_name: str,
    records: str,
    preview: Optional[bool],
    view_rid: Optional[str],
):
    """
    Publish a batch of records to the stream. The records will be validated against the stream's schema, and
    the batch will be rejected if one or more of the records are invalid.

    """
    result = client.streams.Dataset.Stream.publish_records(
        dataset_rid=dataset_rid,
        stream_branch_name=stream_branch_name,
        records=json.loads(records),
        preview=preview,
        view_rid=view_rid,
    )
    click.echo(repr(result))


@cli.group("third_party_applications")
def third_party_applications():
    pass


@third_party_applications.group("third_party_application")
def third_party_applications_third_party_application():
    pass


@third_party_applications_third_party_application.command("get")
@click.argument("third_party_application_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def third_party_applications_third_party_application_get(
    client: foundry.v2.FoundryClient,
    third_party_application_rid: str,
    preview: Optional[bool],
):
    """
    Get the ThirdPartyApplication with the specified rid.
    """
    result = client.third_party_applications.ThirdPartyApplication.get(
        third_party_application_rid=third_party_application_rid,
        preview=preview,
    )
    click.echo(repr(result))


@third_party_applications_third_party_application.group("website")
def third_party_applications_third_party_application_website():
    pass


@third_party_applications_third_party_application_website.command("deploy")
@click.argument("third_party_application_rid", type=str, required=True)
@click.option("--version", type=str, required=True, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def third_party_applications_third_party_application_website_deploy(
    client: foundry.v2.FoundryClient,
    third_party_application_rid: str,
    version: str,
    preview: Optional[bool],
):
    """
    Deploy a version of the Website.
    """
    result = client.third_party_applications.ThirdPartyApplication.Website.deploy(
        third_party_application_rid=third_party_application_rid,
        version=version,
        preview=preview,
    )
    click.echo(repr(result))


@third_party_applications_third_party_application_website.command("get")
@click.argument("third_party_application_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def third_party_applications_third_party_application_website_get(
    client: foundry.v2.FoundryClient,
    third_party_application_rid: str,
    preview: Optional[bool],
):
    """
    Get the Website.
    """
    result = client.third_party_applications.ThirdPartyApplication.Website.get(
        third_party_application_rid=third_party_application_rid,
        preview=preview,
    )
    click.echo(repr(result))


@third_party_applications_third_party_application_website.command("undeploy")
@click.argument("third_party_application_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def third_party_applications_third_party_application_website_undeploy(
    client: foundry.v2.FoundryClient,
    third_party_application_rid: str,
    preview: Optional[bool],
):
    """
    Remove the currently deployed version of the Website.
    """
    result = client.third_party_applications.ThirdPartyApplication.Website.undeploy(
        third_party_application_rid=third_party_application_rid,
        preview=preview,
    )
    click.echo(repr(result))


@third_party_applications_third_party_application_website.group("version")
def third_party_applications_third_party_application_website_version():
    pass


@third_party_applications_third_party_application_website_version.command("delete")
@click.argument("third_party_application_rid", type=str, required=True)
@click.argument("version_version", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def third_party_applications_third_party_application_website_version_delete(
    client: foundry.v2.FoundryClient,
    third_party_application_rid: str,
    version_version: str,
    preview: Optional[bool],
):
    """
    Delete the Version with the specified version.
    """
    result = client.third_party_applications.ThirdPartyApplication.Website.Version.delete(
        third_party_application_rid=third_party_application_rid,
        version_version=version_version,
        preview=preview,
    )
    click.echo(repr(result))


@third_party_applications_third_party_application_website_version.command("get")
@click.argument("third_party_application_rid", type=str, required=True)
@click.argument("version_version", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def third_party_applications_third_party_application_website_version_get(
    client: foundry.v2.FoundryClient,
    third_party_application_rid: str,
    version_version: str,
    preview: Optional[bool],
):
    """
    Get the Version with the specified version.
    """
    result = client.third_party_applications.ThirdPartyApplication.Website.Version.get(
        third_party_application_rid=third_party_application_rid,
        version_version=version_version,
        preview=preview,
    )
    click.echo(repr(result))


@third_party_applications_third_party_application_website_version.command("list")
@click.argument("third_party_application_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def third_party_applications_third_party_application_website_version_list(
    client: foundry.v2.FoundryClient,
    third_party_application_rid: str,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    Lists all Versions.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.third_party_applications.ThirdPartyApplication.Website.Version.list(
        third_party_application_rid=third_party_application_rid,
        page_size=page_size,
        preview=preview,
    )
    click.echo(repr(result))


@third_party_applications_third_party_application_website_version.command("page")
@click.argument("third_party_application_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def third_party_applications_third_party_application_website_version_page(
    client: foundry.v2.FoundryClient,
    third_party_application_rid: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    Lists all Versions.

    This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
    """
    result = client.third_party_applications.ThirdPartyApplication.Website.Version.page(
        third_party_application_rid=third_party_application_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@third_party_applications_third_party_application_website_version.command("upload")
@click.argument("third_party_application_rid", type=str, required=True)
@click.argument("body", type=click.File("rb"), required=True)
@click.option("--version", type=str, required=True, help="""version""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def third_party_applications_third_party_application_website_version_upload(
    client: foundry.v2.FoundryClient,
    third_party_application_rid: str,
    body: io.BufferedReader,
    version: str,
    preview: Optional[bool],
):
    """
    Upload a new version of the Website.
    """
    result = client.third_party_applications.ThirdPartyApplication.Website.Version.upload(
        third_party_application_rid=third_party_application_rid,
        body=body.read(),
        version=version,
        preview=preview,
    )
    click.echo(repr(result))


if __name__ == "__main__":
    cli()
