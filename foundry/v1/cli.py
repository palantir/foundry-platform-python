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

import foundry.v1


@dataclasses.dataclass
class _Context:
    obj: foundry.v1.FoundryClient


def get_from_environ(key: str) -> str:
    value = os.environ.get(key)
    if value is None:
        raise foundry.EnvironmentNotConfigured(f"Please set {key} using `export {key}=<{key}>`")

    return value


@click.group()  # type: ignore
@click.pass_context  # type: ignore
def cli(ctx: _Context):
    "An experimental CLI for the Foundry API"
    ctx.obj = foundry.v1.FoundryClient(
        auth=foundry.UserTokenAuth(
            hostname=get_from_environ("FOUNDRY_HOSTNAME"),
            token=get_from_environ("FOUNDRY_TOKEN"),
        ),
        hostname=get_from_environ("FOUNDRY_HOSTNAME"),
    )


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
@click.pass_obj
def datasets_dataset_create(
    client: foundry.v1.FoundryClient,
    name: str,
    parent_folder_rid: str,
):
    """
    Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

    """
    result = client.datasets.Dataset.create(
        name=name,
        parent_folder_rid=parent_folder_rid,
    )
    click.echo(repr(result))


@datasets_dataset.command("delete_schema")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--transaction_rid", type=str, required=False, help="""transactionRid""")
@click.pass_obj
def datasets_dataset_delete_schema(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    branch_id: Optional[str],
    preview: Optional[bool],
    transaction_rid: Optional[str],
):
    """
    Deletes the Schema from a Dataset and Branch.

    """
    result = client.datasets.Dataset.delete_schema(
        dataset_rid=dataset_rid,
        branch_id=branch_id,
        preview=preview,
        transaction_rid=transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.pass_obj
def datasets_dataset_get(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
):
    """
    Gets the Dataset with the given DatasetRid.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.get(
        dataset_rid=dataset_rid,
    )
    click.echo(repr(result))


@datasets_dataset.command("get_schema")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.option("--transaction_rid", type=str, required=False, help="""transactionRid""")
@click.pass_obj
def datasets_dataset_get_schema(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    branch_id: Optional[str],
    preview: Optional[bool],
    transaction_rid: Optional[str],
):
    """
    Retrieves the Schema for a Dataset and Branch, if it exists.

    """
    result = client.datasets.Dataset.get_schema(
        dataset_rid=dataset_rid,
        branch_id=branch_id,
        preview=preview,
        transaction_rid=transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset.command("read")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--format", type=click.Choice(["ARROW", "CSV"]), required=True, help="""format""")
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--columns", type=str, required=False, help="""columns""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--row_limit", type=int, required=False, help="""rowLimit""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_read(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    format: Literal["ARROW", "CSV"],
    branch_id: Optional[str],
    columns: Optional[str],
    end_transaction_rid: Optional[str],
    row_limit: Optional[int],
    start_transaction_rid: Optional[str],
):
    """
    Gets the content of a dataset as a table in the specified format.

    This endpoint currently does not support views (Virtual datasets composed of other datasets).

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.read(
        dataset_rid=dataset_rid,
        format=format,
        branch_id=branch_id,
        columns=None if columns is None else json.loads(columns),
        end_transaction_rid=end_transaction_rid,
        row_limit=row_limit,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(result)


@datasets_dataset.command("replace_schema")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("body", type=str, required=True)
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--preview", type=bool, required=False, help="""preview""")
@click.pass_obj
def datasets_dataset_replace_schema(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    body: str,
    branch_id: Optional[str],
    preview: Optional[bool],
):
    """
    Puts a Schema on an existing Dataset and Branch.

    """
    result = client.datasets.Dataset.replace_schema(
        dataset_rid=dataset_rid,
        body=json.loads(body),
        branch_id=branch_id,
        preview=preview,
    )
    click.echo(repr(result))


@datasets_dataset.group("transaction")
def datasets_dataset_transaction():
    pass


@datasets_dataset_transaction.command("abort")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("transaction_rid", type=str, required=True)
@click.pass_obj
def datasets_dataset_transaction_abort(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    transaction_rid: str,
):
    """
    Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
    not updated.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

    """
    result = client.datasets.Dataset.Transaction.abort(
        dataset_rid=dataset_rid,
        transaction_rid=transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_transaction.command("commit")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("transaction_rid", type=str, required=True)
@click.pass_obj
def datasets_dataset_transaction_commit(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    transaction_rid: str,
):
    """
    Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
    updated to point to the Transaction.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

    """
    result = client.datasets.Dataset.Transaction.commit(
        dataset_rid=dataset_rid,
        transaction_rid=transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_transaction.command("create")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option(
    "--transaction_type",
    type=click.Choice(["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]),
    required=False,
    help="""""",
)
@click.pass_obj
def datasets_dataset_transaction_create(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    branch_id: Optional[str],
    transaction_type: Optional[Literal["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]],
):
    """
    Creates a Transaction on a Branch of a Dataset.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

    """
    result = client.datasets.Dataset.Transaction.create(
        dataset_rid=dataset_rid,
        branch_id=branch_id,
        transaction_type=transaction_type,
    )
    click.echo(repr(result))


@datasets_dataset_transaction.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("transaction_rid", type=str, required=True)
@click.pass_obj
def datasets_dataset_transaction_get(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    transaction_rid: str,
):
    """
    Gets a Transaction of a Dataset.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.Transaction.get(
        dataset_rid=dataset_rid,
        transaction_rid=transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset.group("file")
def datasets_dataset_file():
    pass


@datasets_dataset_file.command("delete")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("file_path", type=str, required=True)
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--transaction_rid", type=str, required=False, help="""transactionRid""")
@click.pass_obj
def datasets_dataset_file_delete(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    file_path: str,
    branch_id: Optional[str],
    transaction_rid: Optional[str],
):
    """
    Deletes a File from a Dataset. By default the file is deleted in a new transaction on the default
    branch - `master` for most enrollments. The file will still be visible on historical views.

    #### Advanced Usage

    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

    To **delete a File from a specific Branch** specify the Branch's identifier as `branchId`. A new delete Transaction
    will be created and committed on this branch.

    To **delete a File using a manually opened Transaction**, specify the Transaction's resource identifier
    as `transactionRid`. The transaction must be of type `DELETE`. This is useful for deleting multiple files in a
    single transaction. See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to
    open a transaction.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

    """
    result = client.datasets.Dataset.File.delete(
        dataset_rid=dataset_rid,
        file_path=file_path,
        branch_id=branch_id,
        transaction_rid=transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_file.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("file_path", type=str, required=True)
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_file_get(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    file_path: str,
    branch_id: Optional[str],
    end_transaction_rid: Optional[str],
    start_transaction_rid: Optional[str],
):
    """
    Gets metadata about a File contained in a Dataset. By default this retrieves the file's metadata from the latest
    view of the default branch - `master` for most enrollments.

    #### Advanced Usage

    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

    To **get a file's metadata from a specific Branch** specify the Branch's identifier as `branchId`. This will
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

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.File.get(
        dataset_rid=dataset_rid,
        file_path=file_path,
        branch_id=branch_id,
        end_transaction_rid=end_transaction_rid,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_file.command("list")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_file_list(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    branch_id: Optional[str],
    end_transaction_rid: Optional[str],
    page_size: Optional[int],
    start_transaction_rid: Optional[str],
):
    """
    Lists Files contained in a Dataset. By default files are listed on the latest view of the default
    branch - `master` for most enrollments.

    #### Advanced Usage

    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

    To **list files on a specific Branch** specify the Branch's identifier as `branchId`. This will include the most
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

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.File.list(
        dataset_rid=dataset_rid,
        branch_id=branch_id,
        end_transaction_rid=end_transaction_rid,
        page_size=page_size,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_file.command("page")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_file_page(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    branch_id: Optional[str],
    end_transaction_rid: Optional[str],
    page_size: Optional[int],
    page_token: Optional[str],
    start_transaction_rid: Optional[str],
):
    """
    Lists Files contained in a Dataset. By default files are listed on the latest view of the default
    branch - `master` for most enrollments.

    #### Advanced Usage

    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

    To **list files on a specific Branch** specify the Branch's identifier as `branchId`. This will include the most
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

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.File.page(
        dataset_rid=dataset_rid,
        branch_id=branch_id,
        end_transaction_rid=end_transaction_rid,
        page_size=page_size,
        page_token=page_token,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_file.command("read")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("file_path", type=str, required=True)
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--end_transaction_rid", type=str, required=False, help="""endTransactionRid""")
@click.option("--start_transaction_rid", type=str, required=False, help="""startTransactionRid""")
@click.pass_obj
def datasets_dataset_file_read(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    file_path: str,
    branch_id: Optional[str],
    end_transaction_rid: Optional[str],
    start_transaction_rid: Optional[str],
):
    """
    Gets the content of a File contained in a Dataset. By default this retrieves the file's content from the latest
    view of the default branch - `master` for most enrollments.

    #### Advanced Usage

    See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

    To **get a file's content from a specific Branch** specify the Branch's identifier as `branchId`. This will
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

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.File.read(
        dataset_rid=dataset_rid,
        file_path=file_path,
        branch_id=branch_id,
        end_transaction_rid=end_transaction_rid,
        start_transaction_rid=start_transaction_rid,
    )
    click.echo(result)


@datasets_dataset_file.command("upload")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("body", type=click.File("rb"), required=True)
@click.option("--file_path", type=str, required=True, help="""filePath""")
@click.option("--branch_id", type=str, required=False, help="""branchId""")
@click.option("--transaction_rid", type=str, required=False, help="""transactionRid""")
@click.option(
    "--transaction_type",
    type=click.Choice(["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]),
    required=False,
    help="""transactionType""",
)
@click.pass_obj
def datasets_dataset_file_upload(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    body: io.BufferedReader,
    file_path: str,
    branch_id: Optional[str],
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

    To **upload a file to a specific Branch** specify the Branch's identifier as `branchId`. A new transaction will
    be created and committed on this branch. By default the TransactionType will be `UPDATE`, to override this
    default specify `transactionType` in addition to `branchId`.
    See [createBranch](/docs/foundry/api/datasets-resources/branches/create-branch/) to create a custom branch.

    To **upload a file on a manually opened transaction** specify the Transaction's resource identifier as
    `transactionRid`. This is useful for uploading multiple files in a single transaction.
    See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to open a transaction.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

    """
    result = client.datasets.Dataset.File.upload(
        dataset_rid=dataset_rid,
        body=body.read(),
        file_path=file_path,
        branch_id=branch_id,
        transaction_rid=transaction_rid,
        transaction_type=transaction_type,
    )
    click.echo(repr(result))


@datasets_dataset.group("branch")
def datasets_dataset_branch():
    pass


@datasets_dataset_branch.command("create")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--branch_id", type=str, required=True, help="""""")
@click.option("--transaction_rid", type=str, required=False, help="""""")
@click.pass_obj
def datasets_dataset_branch_create(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    branch_id: str,
    transaction_rid: Optional[str],
):
    """
    Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

    """
    result = client.datasets.Dataset.Branch.create(
        dataset_rid=dataset_rid,
        branch_id=branch_id,
        transaction_rid=transaction_rid,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("delete")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("branch_id", type=str, required=True)
@click.pass_obj
def datasets_dataset_branch_delete(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    branch_id: str,
):
    """
    Deletes the Branch with the given BranchId.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

    """
    result = client.datasets.Dataset.Branch.delete(
        dataset_rid=dataset_rid,
        branch_id=branch_id,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("get")
@click.argument("dataset_rid", type=str, required=True)
@click.argument("branch_id", type=str, required=True)
@click.pass_obj
def datasets_dataset_branch_get(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    branch_id: str,
):
    """
    Get a Branch of a Dataset.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.Branch.get(
        dataset_rid=dataset_rid,
        branch_id=branch_id,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("list")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def datasets_dataset_branch_list(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    page_size: Optional[int],
):
    """
    Lists the Branches of a Dataset.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.Branch.list(
        dataset_rid=dataset_rid,
        page_size=page_size,
    )
    click.echo(repr(result))


@datasets_dataset_branch.command("page")
@click.argument("dataset_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def datasets_dataset_branch_page(
    client: foundry.v1.FoundryClient,
    dataset_rid: str,
    page_size: Optional[int],
    page_token: Optional[str],
):
    """
    Lists the Branches of a Dataset.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

    """
    result = client.datasets.Dataset.Branch.page(
        dataset_rid=dataset_rid,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@cli.group("geo")
def geo():
    pass


@cli.group("ontologies")
def ontologies():
    pass


@ontologies.group("query")
def ontologies_query():
    pass


@ontologies_query.command("execute")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("query_api_name", type=str, required=True)
@click.option("--parameters", type=str, required=True, help="""""")
@click.pass_obj
def ontologies_query_execute(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    query_api_name: str,
    parameters: str,
):
    """
    Executes a Query using the given parameters. Optional parameters do not need to be supplied.
    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.Query.execute(
        ontology_rid=ontology_rid,
        query_api_name=query_api_name,
        parameters=json.loads(parameters),
    )
    click.echo(repr(result))


@ontologies.group("ontology_object")
def ontologies_ontology_object():
    pass


@ontologies_ontology_object.command("aggregate")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--aggregation", type=str, required=True, help="""""")
@click.option("--group_by", type=str, required=True, help="""""")
@click.option("--query", type=str, required=False, help="""""")
@click.pass_obj
def ontologies_ontology_object_aggregate(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    aggregation: str,
    group_by: str,
    query: Optional[str],
):
    """
    Perform functions on object fields in the specified ontology and object type.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.aggregate(
        ontology_rid=ontology_rid,
        object_type=object_type,
        aggregation=json.loads(aggregation),
        group_by=json.loads(group_by),
        query=None if query is None else json.loads(query),
    )
    click.echo(repr(result))


@ontologies_ontology_object.command("get")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.option("--properties", type=str, required=False, help="""properties""")
@click.pass_obj
def ontologies_ontology_object_get(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    primary_key: str,
    properties: Optional[str],
):
    """
    Gets a specific object with the given primary key.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.get(
        ontology_rid=ontology_rid,
        object_type=object_type,
        primary_key=primary_key,
        properties=None if properties is None else json.loads(properties),
    )
    click.echo(repr(result))


@ontologies_ontology_object.command("get_linked_object")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("link_type", type=str, required=True)
@click.argument("linked_object_primary_key", type=str, required=True)
@click.option("--properties", type=str, required=False, help="""properties""")
@click.pass_obj
def ontologies_ontology_object_get_linked_object(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    primary_key: str,
    link_type: str,
    linked_object_primary_key: str,
    properties: Optional[str],
):
    """
    Get a specific linked object that originates from another object. If there is no link between the two objects,
    LinkedObjectNotFound is thrown.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.get_linked_object(
        ontology_rid=ontology_rid,
        object_type=object_type,
        primary_key=primary_key,
        link_type=link_type,
        linked_object_primary_key=linked_object_primary_key,
        properties=None if properties is None else json.loads(properties),
    )
    click.echo(repr(result))


@ontologies_ontology_object.command("list")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--order_by", type=str, required=False, help="""orderBy""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--properties", type=str, required=False, help="""properties""")
@click.pass_obj
def ontologies_ontology_object_list(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    order_by: Optional[str],
    page_size: Optional[int],
    properties: Optional[str],
):
    """
    Lists the objects for the given Ontology and object type.

    This endpoint supports filtering objects.
    See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

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
        ontology_rid=ontology_rid,
        object_type=object_type,
        order_by=order_by,
        page_size=page_size,
        properties=None if properties is None else json.loads(properties),
    )
    click.echo(repr(result))


@ontologies_ontology_object.command("list_linked_objects")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("link_type", type=str, required=True)
@click.option("--order_by", type=str, required=False, help="""orderBy""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--properties", type=str, required=False, help="""properties""")
@click.pass_obj
def ontologies_ontology_object_list_linked_objects(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    primary_key: str,
    link_type: str,
    order_by: Optional[str],
    page_size: Optional[int],
    properties: Optional[str],
):
    """
    Lists the linked objects for a specific object and the given link type.

    This endpoint supports filtering objects.
    See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

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
    result = client.ontologies.OntologyObject.list_linked_objects(
        ontology_rid=ontology_rid,
        object_type=object_type,
        primary_key=primary_key,
        link_type=link_type,
        order_by=order_by,
        page_size=page_size,
        properties=None if properties is None else json.loads(properties),
    )
    click.echo(repr(result))


@ontologies_ontology_object.command("page")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--order_by", type=str, required=False, help="""orderBy""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--properties", type=str, required=False, help="""properties""")
@click.pass_obj
def ontologies_ontology_object_page(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    order_by: Optional[str],
    page_size: Optional[int],
    page_token: Optional[str],
    properties: Optional[str],
):
    """
    Lists the objects for the given Ontology and object type.

    This endpoint supports filtering objects.
    See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

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
        ontology_rid=ontology_rid,
        object_type=object_type,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        properties=None if properties is None else json.loads(properties),
    )
    click.echo(repr(result))


@ontologies_ontology_object.command("page_linked_objects")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("primary_key", type=str, required=True)
@click.argument("link_type", type=str, required=True)
@click.option("--order_by", type=str, required=False, help="""orderBy""")
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.option("--properties", type=str, required=False, help="""properties""")
@click.pass_obj
def ontologies_ontology_object_page_linked_objects(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    primary_key: str,
    link_type: str,
    order_by: Optional[str],
    page_size: Optional[int],
    page_token: Optional[str],
    properties: Optional[str],
):
    """
    Lists the linked objects for a specific object and the given link type.

    This endpoint supports filtering objects.
    See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

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
    result = client.ontologies.OntologyObject.page_linked_objects(
        ontology_rid=ontology_rid,
        object_type=object_type,
        primary_key=primary_key,
        link_type=link_type,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        properties=None if properties is None else json.loads(properties),
    )
    click.echo(repr(result))


@ontologies_ontology_object.command("search")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option(
    "--fields",
    type=str,
    required=True,
    help="""The API names of the object type properties to include in the response.
""",
)
@click.option("--query", type=str, required=True, help="""""")
@click.option("--order_by", type=str, required=False, help="""""")
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.pass_obj
def ontologies_ontology_object_search(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    fields: str,
    query: str,
    order_by: Optional[str],
    page_size: Optional[int],
    page_token: Optional[str],
):
    """
    Search for objects in the specified ontology and object type. The request body is used
    to filter objects based on the specified query. The supported queries are:

    | Query type            | Description                                                                       | Supported Types                 |
    |----------|-----------------------------------------------------------------------------------|---------------------------------|
    | lt       | The provided property is less than the provided value.                            | number, string, date, timestamp |
    | gt       | The provided property is greater than the provided value.                         | number, string, date, timestamp |
    | lte      | The provided property is less than or equal to the provided value.                | number, string, date, timestamp |
    | gte      | The provided property is greater than or equal to the provided value.             | number, string, date, timestamp |
    | eq       | The provided property is exactly equal to the provided value.                     | number, string, date, timestamp |
    | isNull   | The provided property is (or is not) null.                                        | all                             |
    | contains | The provided property contains the provided value.                                | array                           |
    | not      | The sub-query does not match.                                                     | N/A (applied on a query)        |
    | and      | All the sub-queries match.                                                        | N/A (applied on queries)        |
    | or       | At least one of the sub-queries match.                                            | N/A (applied on queries)        |
    | prefix   | The provided property starts with the provided value.                             | string                          |
    | phrase   | The provided property contains the provided value as a substring.                 | string                          |
    | anyTerm  | The provided property contains at least one of the terms separated by whitespace. | string                          |
    | allTerms | The provided property contains all the terms separated by whitespace.             | string                          |                                                                            |

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.OntologyObject.search(
        ontology_rid=ontology_rid,
        object_type=object_type,
        fields=json.loads(fields),
        query=json.loads(query),
        order_by=None if order_by is None else json.loads(order_by),
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies.group("ontology")
def ontologies_ontology():
    pass


@ontologies_ontology.command("get")
@click.argument("ontology_rid", type=str, required=True)
@click.pass_obj
def ontologies_ontology_get(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
):
    """
    Gets a specific ontology with the given Ontology RID.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.get(
        ontology_rid=ontology_rid,
    )
    click.echo(repr(result))


@ontologies_ontology.command("list")
@click.pass_obj
def ontologies_ontology_list(
    client: foundry.v1.FoundryClient,
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
@click.argument("ontology_rid", type=str, required=True)
@click.argument("query_api_name", type=str, required=True)
@click.pass_obj
def ontologies_ontology_query_type_get(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    query_api_name: str,
):
    """
    Gets a specific query type with the given API name.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.QueryType.get(
        ontology_rid=ontology_rid,
        query_api_name=query_api_name,
    )
    click.echo(repr(result))


@ontologies_ontology_query_type.command("list")
@click.argument("ontology_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_ontology_query_type_list(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    page_size: Optional[int],
):
    """
    Lists the query types for the given Ontology.

    Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
    results available, at least one result will be present in the response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.QueryType.list(
        ontology_rid=ontology_rid,
        page_size=page_size,
    )
    click.echo(repr(result))


@ontologies_ontology_query_type.command("page")
@click.argument("ontology_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_ontology_query_type_page(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
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
        ontology_rid=ontology_rid,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies_ontology.group("object_type")
def ontologies_ontology_object_type():
    pass


@ontologies_ontology_object_type.command("get")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.pass_obj
def ontologies_ontology_object_type_get(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
):
    """
    Gets a specific object type with the given API name.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ObjectType.get(
        ontology_rid=ontology_rid,
        object_type=object_type,
    )
    click.echo(repr(result))


@ontologies_ontology_object_type.command("get_outgoing_link_type")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.argument("link_type", type=str, required=True)
@click.pass_obj
def ontologies_ontology_object_type_get_outgoing_link_type(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    link_type: str,
):
    """
    Get an outgoing link for an object type.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ObjectType.get_outgoing_link_type(
        ontology_rid=ontology_rid,
        object_type=object_type,
        link_type=link_type,
    )
    click.echo(repr(result))


@ontologies_ontology_object_type.command("list")
@click.argument("ontology_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_ontology_object_type_list(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
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
        ontology_rid=ontology_rid,
        page_size=page_size,
    )
    click.echo(repr(result))


@ontologies_ontology_object_type.command("list_outgoing_link_types")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_ontology_object_type_list_outgoing_link_types(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    object_type: str,
    page_size: Optional[int],
):
    """
    List the outgoing links for an object type.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ObjectType.list_outgoing_link_types(
        ontology_rid=ontology_rid,
        object_type=object_type,
        page_size=page_size,
    )
    click.echo(repr(result))


@ontologies_ontology_object_type.command("page")
@click.argument("ontology_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_ontology_object_type_page(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
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
        ontology_rid=ontology_rid,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies_ontology_object_type.command("page_outgoing_link_types")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("object_type", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_ontology_object_type_page_outgoing_link_types(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
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
        ontology_rid=ontology_rid,
        object_type=object_type,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies_ontology.group("action_type")
def ontologies_ontology_action_type():
    pass


@ontologies_ontology_action_type.command("get")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("action_type_api_name", type=str, required=True)
@click.pass_obj
def ontologies_ontology_action_type_get(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    action_type_api_name: str,
):
    """
    Gets a specific action type with the given API name.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ActionType.get(
        ontology_rid=ontology_rid,
        action_type_api_name=action_type_api_name,
    )
    click.echo(repr(result))


@ontologies_ontology_action_type.command("list")
@click.argument("ontology_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.pass_obj
def ontologies_ontology_action_type_list(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    page_size: Optional[int],
):
    """
    Lists the action types for the given Ontology.

    Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
    results available, at least one result will be present in the response.

    Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

    """
    result = client.ontologies.Ontology.ActionType.list(
        ontology_rid=ontology_rid,
        page_size=page_size,
    )
    click.echo(repr(result))


@ontologies_ontology_action_type.command("page")
@click.argument("ontology_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""pageSize""")
@click.option("--page_token", type=str, required=False, help="""pageToken""")
@click.pass_obj
def ontologies_ontology_action_type_page(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
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
        ontology_rid=ontology_rid,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@ontologies.group("action")
def ontologies_action():
    pass


@ontologies_action.command("apply")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("action_type", type=str, required=True)
@click.option("--parameters", type=str, required=True, help="""""")
@click.pass_obj
def ontologies_action_apply(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    action_type: str,
    parameters: str,
):
    """
    Applies an action using the given parameters. Changes to the Ontology are eventually consistent and may take
    some time to be visible.

    Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) are not currently supported by
    this endpoint.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read api:ontologies-write`.

    """
    result = client.ontologies.Action.apply(
        ontology_rid=ontology_rid,
        action_type=action_type,
        parameters=json.loads(parameters),
    )
    click.echo(repr(result))


@ontologies_action.command("apply_batch")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("action_type", type=str, required=True)
@click.option("--requests", type=str, required=True, help="""""")
@click.pass_obj
def ontologies_action_apply_batch(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    action_type: str,
    requests: str,
):
    """
    Applies multiple actions (of the same Action Type) using the given parameters.
    Changes to the Ontology are eventually consistent and may take some time to be visible.

    Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
    call Functions may receive a higher limit.

    Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) and
    [notifications](/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read api:ontologies-write`.

    """
    result = client.ontologies.Action.apply_batch(
        ontology_rid=ontology_rid,
        action_type=action_type,
        requests=json.loads(requests),
    )
    click.echo(repr(result))


@ontologies_action.command("validate")
@click.argument("ontology_rid", type=str, required=True)
@click.argument("action_type", type=str, required=True)
@click.option("--parameters", type=str, required=True, help="""""")
@click.pass_obj
def ontologies_action_validate(
    client: foundry.v1.FoundryClient,
    ontology_rid: str,
    action_type: str,
    parameters: str,
):
    """
    Validates if an action can be run with the given set of parameters.
    The response contains the evaluation of parameters and **submission criteria**
    that determine if the request is `VALID` or `INVALID`.
    For performance reasons, validations will not consider existing objects or other data in Foundry.
    For example, the uniqueness of a primary key or the existence of a user ID will not be checked.
    Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) are not currently supported by
    this endpoint. Unspecified parameters will be given a default value of `null`.

    Third-party applications using this endpoint via OAuth2 must request the
    following operation scopes: `api:ontologies-read`.

    """
    result = client.ontologies.Action.validate(
        ontology_rid=ontology_rid,
        action_type=action_type,
        parameters=json.loads(parameters),
    )
    click.echo(repr(result))


if __name__ == "__main__":
    cli()
