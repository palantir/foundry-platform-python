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
from typing import Literal
from typing import Optional

import click

import foundry.v2
import foundry.v2.models


@dataclasses.dataclass
class _Context:
    obj: foundry.v2.FoundryV2Client


def get_from_environ(key: str) -> str:
    value = os.environ.get(key)
    if value is None:
        raise foundry.EnvironmentNotConfigured(f"Please set {key} using `export {key}=<{key}>`")

    return value


@click.group()
@click.pass_context  # type: ignore
def cli(ctx: _Context):
    "An experimental CLI for the Foundry API"
    ctx.obj = foundry.v2.FoundryV2Client(
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
    client: foundry.v2.FoundryV2Client,
    user_id: str,
    preview: Optional[bool],
):
    """
    Deletes the given User
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
    client: foundry.v2.FoundryV2Client,
    user_id: str,
    preview: Optional[bool],
):
    """
    Get the User
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
    preview: Optional[bool],
):
    """ """
    result = client.admin.User.get_current(
        preview=preview,
    )
    click.echo(repr(result))


@admin_user.command("list")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_user_list(
    client: foundry.v2.FoundryV2Client,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    Lists all Users
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
    client: foundry.v2.FoundryV2Client,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    Lists all Users
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
    where: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """ """
    result = client.admin.User.search(
        search_users_request=foundry.v2.models.SearchUsersRequest.model_validate(
            {
                "where": where,
                "pageSize": page_size,
                "pageToken": page_token,
            }
        ),
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
    client: foundry.v2.FoundryV2Client,
    user_id: str,
    page_size: Optional[int],
    preview: Optional[bool],
    transitive: Optional[bool],
):
    """
    Lists all GroupMemberships
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
    client: foundry.v2.FoundryV2Client,
    user_id: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
    transitive: Optional[bool],
):
    """
    Lists all GroupMemberships
    """
    result = client.admin.User.GroupMembership.page(
        user_id=user_id,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        transitive=transitive,
    )
    click.echo(repr(result))


@admin.group("group")
def admin_group():
    pass


@admin_group.command("create")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--organizations", type=str, required=True, help="""""")
@click.option("--description", type=str, required=False, help="""""")
@click.option(
    "--attributes",
    type=str,
    required=True,
    help="""A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.""",
)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_create(
    client: foundry.v2.FoundryV2Client,
    name: str,
    organizations: str,
    description: Optional[str],
    attributes: str,
    preview: Optional[bool],
):
    """
    Creates a new Group
    """
    result = client.admin.Group.create(
        create_group_request=foundry.v2.models.CreateGroupRequest.model_validate(
            {
                "name": name,
                "organizations": organizations,
                "description": description,
                "attributes": attributes,
            }
        ),
        preview=preview,
    )
    click.echo(repr(result))


@admin_group.command("delete")
@click.argument("group_id", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_delete(
    client: foundry.v2.FoundryV2Client,
    group_id: str,
    preview: Optional[bool],
):
    """
    Deletes the given Group
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
    client: foundry.v2.FoundryV2Client,
    group_id: str,
    preview: Optional[bool],
):
    """
    Get the Group
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
    page_size: Optional[int],
    preview: Optional[bool],
):
    """
    Lists all Groups
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
    client: foundry.v2.FoundryV2Client,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """
    Lists all Groups
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
    client: foundry.v2.FoundryV2Client,
    where: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
):
    """ """
    result = client.admin.Group.search(
        search_groups_request=foundry.v2.models.SearchGroupsRequest.model_validate(
            {
                "where": where,
                "pageSize": page_size,
                "pageToken": page_token,
            }
        ),
        preview=preview,
    )
    click.echo(repr(result))


@admin_group.group("group_member")
def admin_group_group_member():
    pass


@admin_group_group_member.command("add")
@click.argument("group_id", type=str, required=True)
@click.option("--principal_ids", type=str, required=True, help="""""")
@click.option("--expiration", type=str, required=False, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def admin_group_group_member_add(
    client: foundry.v2.FoundryV2Client,
    group_id: str,
    principal_ids: str,
    expiration: Optional[str],
    preview: Optional[bool],
):
    """ """
    result = client.admin.Group.GroupMember.add(
        group_id=group_id,
        add_group_members_request=foundry.v2.models.AddGroupMembersRequest.model_validate(
            {
                "principalIds": principal_ids,
                "expiration": expiration,
            }
        ),
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
    client: foundry.v2.FoundryV2Client,
    group_id: str,
    page_size: Optional[int],
    preview: Optional[bool],
    transitive: Optional[bool],
):
    """
    Lists all GroupMembers
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
    client: foundry.v2.FoundryV2Client,
    group_id: str,
    page_size: Optional[int],
    page_token: Optional[str],
    preview: Optional[bool],
    transitive: Optional[bool],
):
    """
    Lists all GroupMembers
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
    client: foundry.v2.FoundryV2Client,
    group_id: str,
    principal_ids: str,
    preview: Optional[bool],
):
    """ """
    result = client.admin.Group.GroupMember.remove(
        group_id=group_id,
        remove_group_members_request=foundry.v2.models.RemoveGroupMembersRequest.model_validate(
            {
                "principalIds": principal_ids,
            }
        ),
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("datasets")
def datasets():
    pass


@datasets.group("dataset")
def datasets_dataset():
    pass


@datasets_dataset.command("create")
@click.option("--parent_folder_rid", type=str, required=True, help="""""")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_create(
    client: foundry.v2.FoundryV2Client,
    parent_folder_rid: str,
    name: str,
    preview: Optional[bool],
):
    """
    Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

    """
    result = client.datasets.Dataset.create(
        create_dataset_request=foundry.v2.models.CreateDatasetRequest.model_validate(
            {
                "parentFolderRid": parent_folder_rid,
                "name": name,
            }
        ),
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_get(
    client: foundry.v2.FoundryV2Client,
    dataset_rid: str,
    preview: Optional[bool],
):
    """
    Get the Dataset
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
    client: foundry.v2.FoundryV2Client,
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


@datasets_dataset.group("transaction")
def datasets_dataset_transaction():
    pass


@datasets_dataset_transaction.command("abort")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("transaction_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_transaction_abort(
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
        create_transaction_request=foundry.v2.models.CreateTransactionRequest.model_validate(
            {
                "transactionType": transaction_type,
            }
        ),
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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


@datasets_dataset.group("branch")
def datasets_dataset_branch():
    pass


@datasets_dataset_branch.command("create")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--transaction_rid", type=str, required=False, help="""""")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_branch_create(
    client: foundry.v2.FoundryV2Client,
    dataset_rid: str,
    transaction_rid: Optional[str],
    name: str,
    preview: Optional[bool],
):
    """
    Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

    """
    result = client.datasets.Dataset.Branch.create(
        dataset_rid=dataset_rid,
        create_branch_request=foundry.v2.models.CreateBranchRequest.model_validate(
            {
                "transactionRid": transaction_rid,
                "name": name,
            }
        ),
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("delete")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("branch_name", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_branch_delete(
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
        create_transaction_request=foundry.v2.models.CreateTransactionRequest.model_validate(
            {
                "transactionType": transaction_type,
            }
        ),
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
    client: foundry.v2.FoundryV2Client,
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
@click.option("--transaction_rid", type=str, required=False, help="""""")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_branch_create(
    client: foundry.v2.FoundryV2Client,
    dataset_rid: str,
    transaction_rid: Optional[str],
    name: str,
    preview: Optional[bool],
):
    """
    Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

    """
    result = client.datasets.Dataset.Branch.create(
        dataset_rid=dataset_rid,
        create_branch_request=foundry.v2.models.CreateBranchRequest.model_validate(
            {
                "transactionRid": transaction_rid,
                "name": name,
            }
        ),
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("delete")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("branch_name", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_branch_delete(
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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
    client: foundry.v2.FoundryV2Client,
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


@cli.group("ontologies")
def ontologies():
    pass


@ontologies.group("ontology")
def ontologies_ontology():
    pass


@ontologies_ontology.command("get")
@click.argument("ontology", type=str, required=True)
@click.pass_obj
def ontologies_ontology_get(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology.command("get_full_metadata")
@click.argument("ontology", type=str, required=True)
@click.pass_obj
def ontologies_ontology_get_full_metadata(
    client: foundry.v2.FoundryV2Client,
    ontology: str,
):
    """
    Get the full Ontology metadata. This includes the objects, links, actions, queries, and interfaces.

    """
    result = client.ontologies.Ontology.get_full_metadata(
        ontology=ontology,
    )
    click.echo(repr(result))


@ontologies_ontology.command("list")
@click.pass_obj
def ontologies_ontology_list(
    client: foundry.v2.FoundryV2Client,
):
    """
    Lists the Ontologies visible to the current user.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.list()
    click.echo(repr(result))


@ontologies_ontology.group("query_type")
def ontologies_ontology_query_type():
    pass


@ontologies_ontology_query_type.command("get")
@click.argument("ontology", type=str, required=True)
@click.argument("query_api_name", type=str, required=True)
@click.pass_obj
def ontologies_ontology_query_type_get(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology_query_type.command("list")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_ontology_query_type_list(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology_query_type.command("page")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_ontology_query_type_page(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology.group("object_type")
def ontologies_ontology_object_type():
    pass


@ontologies_ontology_object_type.command("get")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.pass_obj
def ontologies_ontology_object_type_get(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology_object_type.command("get_outgoing_link_type")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("link_type", type=str, required=True)
@click.pass_obj
def ontologies_ontology_object_type_get_outgoing_link_type(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology_object_type.command("list")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_ontology_object_type_list(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology_object_type.command("list_outgoing_link_types")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_ontology_object_type_list_outgoing_link_types(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology_object_type.command("page")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_ontology_object_type_page(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology_object_type.command("page_outgoing_link_types")
@click.argument("ontology", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_ontology_object_type_page_outgoing_link_types(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology.group("action_type")
def ontologies_ontology_action_type():
    pass


@ontologies_ontology_action_type.command("get")
@click.argument("ontology", type=str, required=True)
@click.argument("action_type", type=str, required=True)
@click.pass_obj
def ontologies_ontology_action_type_get(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology_action_type.command("list")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_ontology_action_type_list(
    client: foundry.v2.FoundryV2Client,
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


@ontologies_ontology_action_type.command("page")
@click.argument("ontology", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_ontology_action_type_page(
    client: foundry.v2.FoundryV2Client,
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


@cli.group("orchestration")
def orchestration():
    pass


@orchestration.group("schedule")
def orchestration_schedule():
    pass


@orchestration_schedule.command("get")
@click.argument("schedule_rid", type=str, required=True)
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def orchestration_schedule_get(
    client: foundry.v2.FoundryV2Client,
    schedule_rid: str,
    preview: Optional[bool],
):
    """
    Get the Schedule
    """
    result = client.orchestration.Schedule.get(
        schedule_rid=schedule_rid,
        preview=preview,
    )
    click.echo(repr(result))


if __name__ == "__main__":
    cli()
