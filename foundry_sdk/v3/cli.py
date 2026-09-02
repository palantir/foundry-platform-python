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

from foundry_sdk import EnvironmentNotConfigured, UserTokenAuth
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
@click.pass_obj
def endpoints_endpoint_set_op_get(
    client: FoundryClient,
    endpoint_set_rid: str,
):
    """ """
    result = client.endpoints.EndpointSet.get(
        endpoint_set_rid=endpoint_set_rid,
    )
    click.echo(repr(result))


@endpoints_endpoint_set.group("endpoint_set_version")
def endpoints_endpoint_set_endpoint_set_version():
    pass


@endpoints_endpoint_set_endpoint_set_version.command("get")
@click.argument("endpoint_set_rid", type=str, required=True)
@click.argument("version_id", type=str, required=True)
@click.pass_obj
def endpoints_endpoint_set_endpoint_set_version_op_get(
    client: FoundryClient,
    endpoint_set_rid: str,
    version_id: str,
):
    """ """
    result = client.endpoints.EndpointSet.Version.get(
        endpoint_set_rid=endpoint_set_rid,
        version_id=version_id,
    )
    click.echo(repr(result))


@endpoints_endpoint_set_endpoint_set_version.command("list")
@click.argument("endpoint_set_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.pass_obj
def endpoints_endpoint_set_endpoint_set_version_op_list(
    client: FoundryClient,
    endpoint_set_rid: str,
    page_size: typing.Optional[int],
    page_token: typing.Optional[str],
):
    """ """
    result = client.endpoints.EndpointSet.Version.list(
        endpoint_set_rid=endpoint_set_rid,
        page_size=page_size,
        page_token=page_token,
    )
    click.echo(repr(result))


@endpoints_endpoint_set.group("endpoint_set_endpoint")
def endpoints_endpoint_set_endpoint_set_endpoint():
    pass


@endpoints_endpoint_set_endpoint_set_endpoint.command("get")
@click.argument("endpoint_set_rid", type=str, required=True)
@click.argument("endpoint_rid", type=str, required=True)
@click.pass_obj
def endpoints_endpoint_set_endpoint_set_endpoint_op_get(
    client: FoundryClient,
    endpoint_set_rid: str,
    endpoint_rid: str,
):
    """ """
    result = client.endpoints.EndpointSet.Endpoint.get(
        endpoint_set_rid=endpoint_set_rid,
        endpoint_rid=endpoint_rid,
    )
    click.echo(repr(result))


@endpoints_endpoint_set_endpoint_set_endpoint.command("list")
@click.argument("endpoint_set_rid", type=str, required=True)
@click.option("--page_size", type=int, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.pass_obj
def endpoints_endpoint_set_endpoint_set_endpoint_op_list(
    client: FoundryClient,
    endpoint_set_rid: str,
    page_size: typing.Optional[int],
    page_token: typing.Optional[str],
):
    """ """
    result = client.endpoints.EndpointSet.Endpoint.list(
        endpoint_set_rid=endpoint_set_rid,
        page_size=page_size,
        page_token=page_token,
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
@click.pass_obj
def orchestrator_process_execution_process_execution_signal_op_complete(
    client: FoundryClient,
    process_execution_id: str,
    signal_id: str,
    payload: typing.Optional[str],
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
    )
    click.echo(repr(result))


if __name__ == "__main__":
    cli()
