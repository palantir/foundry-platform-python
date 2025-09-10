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


import typing

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.datasets import errors as datasets_errors
from foundry_sdk.v2.datasets import models as datasets_models
from foundry_sdk.v2.filesystem import errors as filesystem_errors
from foundry_sdk.v2.filesystem import models as filesystem_models


class ViewClient:
    """
    The API client for the View Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _ViewClientStreaming(self)
        self.with_raw_response = _ViewClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_backing_datasets(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        backing_datasets: typing.List[datasets_models.ViewBackingDataset],
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.View:
        """
        Adds one or more backing datasets to a View. Any duplicates with the same dataset RID and branch name are
        ignored.

        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param backing_datasets:
        :type backing_datasets: List[ViewBackingDataset]
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.View

        :raises AddBackingDatasetsPermissionDenied: Could not addBackingDatasets the View.
        :raises InputBackingDatasetNotInOutputViewProject: One or more backing datasets do not live in the same project as the view. Either move the input datasets to  the same project as the view or add them as project references.
        :raises InvalidViewBackingDataset: Either you do not have access to one or more of the backing datasets or it does not exist.
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/views/{viewDatasetRid}/addBackingDatasets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branch": branch,
                    "backingDatasets": backing_datasets,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branch": typing.Optional[datasets_models.BranchName],
                        "backingDatasets": typing.List[datasets_models.ViewBackingDataset],
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddBackingDatasetsPermissionDenied": datasets_errors.AddBackingDatasetsPermissionDenied,
                    "InputBackingDatasetNotInOutputViewProject": datasets_errors.InputBackingDatasetNotInOutputViewProject,
                    "InvalidViewBackingDataset": datasets_errors.InvalidViewBackingDataset,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_primary_key(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        primary_key: datasets_models.ViewPrimaryKey,
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.View:
        """
        Adds a primary key to a View that does not already have one. Primary keys are treated as
        guarantees provided by the creator of the dataset.

        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param primary_key:
        :type primary_key: ViewPrimaryKey
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.View

        :raises AddPrimaryKeyPermissionDenied: Could not addPrimaryKey the View.
        :raises InvalidViewPrimaryKeyColumnType: The type of each referenced column in the primary key must be one of the following: BYTE, SHORT, DECIMAL, INTEGER, LONG, STRING, BOOLEAN, TIMESTAMP or DATE.
        :raises InvalidViewPrimaryKeyDeletionColumn: The deletion column must be a boolean.
        :raises NotAllColumnsInPrimaryKeyArePresent: Not all columns in the View's primary key are present in the dataset(s).
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        :raises ViewPrimaryKeyCannotBeModified: A primary key already exits.
        :raises ViewPrimaryKeyDeletionColumnNotInDatasetSchema: The deletion column is not present in the dataset.
        :raises ViewPrimaryKeyMustContainAtLeastOneColumn: No columns were provided as part of the primary key
        :raises ViewPrimaryKeyRequiresBackingDatasets: Cannot add a primary key to a View that does not have any backing datasets.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/views/{viewDatasetRid}/addPrimaryKey",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branch": branch,
                    "primaryKey": primary_key,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branch": typing.Optional[datasets_models.BranchName],
                        "primaryKey": datasets_models.ViewPrimaryKey,
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddPrimaryKeyPermissionDenied": datasets_errors.AddPrimaryKeyPermissionDenied,
                    "InvalidViewPrimaryKeyColumnType": datasets_errors.InvalidViewPrimaryKeyColumnType,
                    "InvalidViewPrimaryKeyDeletionColumn": datasets_errors.InvalidViewPrimaryKeyDeletionColumn,
                    "NotAllColumnsInPrimaryKeyArePresent": datasets_errors.NotAllColumnsInPrimaryKeyArePresent,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                    "ViewPrimaryKeyCannotBeModified": datasets_errors.ViewPrimaryKeyCannotBeModified,
                    "ViewPrimaryKeyDeletionColumnNotInDatasetSchema": datasets_errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchema,
                    "ViewPrimaryKeyMustContainAtLeastOneColumn": datasets_errors.ViewPrimaryKeyMustContainAtLeastOneColumn,
                    "ViewPrimaryKeyRequiresBackingDatasets": datasets_errors.ViewPrimaryKeyRequiresBackingDatasets,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        backing_datasets: typing.List[datasets_models.ViewBackingDataset],
        parent_folder_rid: filesystem_models.FolderRid,
        view_name: datasets_models.DatasetName,
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        primary_key: typing.Optional[datasets_models.ViewPrimaryKey] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.View:
        """
        Create a new View.
        :param backing_datasets:
        :type backing_datasets: List[ViewBackingDataset]
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param view_name:
        :type view_name: DatasetName
        :param branch: The branch name of the View. If not specified, defaults to `master` for most enrollments.
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param primary_key:
        :type primary_key: Optional[ViewPrimaryKey]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.View

        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
        :raises CreateViewPermissionDenied: Could not create the View.
        :raises FolderNotFound: The given Folder could not be found.
        :raises InputBackingDatasetNotInOutputViewProject: One or more backing datasets do not live in the same project as the view. Either move the input datasets to  the same project as the view or add them as project references.
        :raises InvalidViewBackingDataset: Either you do not have access to one or more of the backing datasets or it does not exist.
        :raises InvalidViewPrimaryKeyColumnType: The type of each referenced column in the primary key must be one of the following: BYTE, SHORT, DECIMAL, INTEGER, LONG, STRING, BOOLEAN, TIMESTAMP or DATE.
        :raises InvalidViewPrimaryKeyDeletionColumn: The deletion column must be a boolean.
        :raises NotAllColumnsInPrimaryKeyArePresent: Not all columns in the View's primary key are present in the dataset(s).
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        :raises ViewDatasetCleanupFailed: Failed to delete dataset following View creation failure.
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        :raises ViewPrimaryKeyDeletionColumnNotInDatasetSchema: The deletion column is not present in the dataset.
        :raises ViewPrimaryKeyMustContainAtLeastOneColumn: No columns were provided as part of the primary key
        :raises ViewPrimaryKeyRequiresBackingDatasets: Cannot add a primary key to a View that does not have any backing datasets.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/views",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "viewName": view_name,
                    "backingDatasets": backing_datasets,
                    "branch": branch,
                    "primaryKey": primary_key,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": filesystem_models.FolderRid,
                        "viewName": datasets_models.DatasetName,
                        "backingDatasets": typing.List[datasets_models.ViewBackingDataset],
                        "branch": typing.Optional[datasets_models.BranchName],
                        "primaryKey": typing.Optional[datasets_models.ViewPrimaryKey],
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                    "CreateViewPermissionDenied": datasets_errors.CreateViewPermissionDenied,
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                    "InputBackingDatasetNotInOutputViewProject": datasets_errors.InputBackingDatasetNotInOutputViewProject,
                    "InvalidViewBackingDataset": datasets_errors.InvalidViewBackingDataset,
                    "InvalidViewPrimaryKeyColumnType": datasets_errors.InvalidViewPrimaryKeyColumnType,
                    "InvalidViewPrimaryKeyDeletionColumn": datasets_errors.InvalidViewPrimaryKeyDeletionColumn,
                    "NotAllColumnsInPrimaryKeyArePresent": datasets_errors.NotAllColumnsInPrimaryKeyArePresent,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                    "ViewDatasetCleanupFailed": datasets_errors.ViewDatasetCleanupFailed,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                    "ViewPrimaryKeyDeletionColumnNotInDatasetSchema": datasets_errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchema,
                    "ViewPrimaryKeyMustContainAtLeastOneColumn": datasets_errors.ViewPrimaryKeyMustContainAtLeastOneColumn,
                    "ViewPrimaryKeyRequiresBackingDatasets": datasets_errors.ViewPrimaryKeyRequiresBackingDatasets,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.View:
        """
        Get metadata for a View.
        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.View

        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/views/{viewDatasetRid}",
                query_params={
                    "branch": branch,
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "ViewNotFound": datasets_errors.ViewNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove_backing_datasets(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        backing_datasets: typing.List[datasets_models.ViewBackingDataset],
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.View:
        """
        Removes specified backing datasets from a View. Removing a dataset triggers a
        [SNAPSHOT](https://palantir.com/docs/foundry/data-integration/datasets#snapshot) transaction on the next update. If a
        specified dataset does not exist, no error is thrown.

        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param backing_datasets:
        :type backing_datasets: List[ViewBackingDataset]
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.View

        :raises InputBackingDatasetNotInOutputViewProject: One or more backing datasets do not live in the same project as the view. Either move the input datasets to  the same project as the view or add them as project references.
        :raises InvalidViewBackingDataset: Either you do not have access to one or more of the backing datasets or it does not exist.
        :raises RemoveBackingDatasetsPermissionDenied: Could not removeBackingDatasets the View.
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/views/{viewDatasetRid}/removeBackingDatasets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branch": branch,
                    "backingDatasets": backing_datasets,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branch": typing.Optional[datasets_models.BranchName],
                        "backingDatasets": typing.List[datasets_models.ViewBackingDataset],
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "InputBackingDatasetNotInOutputViewProject": datasets_errors.InputBackingDatasetNotInOutputViewProject,
                    "InvalidViewBackingDataset": datasets_errors.InvalidViewBackingDataset,
                    "RemoveBackingDatasetsPermissionDenied": datasets_errors.RemoveBackingDatasetsPermissionDenied,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace_backing_datasets(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        backing_datasets: typing.List[datasets_models.ViewBackingDataset],
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.View:
        """
        Replaces the backing datasets for a View. Removing any backing dataset triggers a
        [SNAPSHOT](https://palantir.com/docs/foundry/data-integration/datasets#snapshot) transaction the next time the View is updated.

        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param backing_datasets:
        :type backing_datasets: List[ViewBackingDataset]
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.View

        :raises InputBackingDatasetNotInOutputViewProject: One or more backing datasets do not live in the same project as the view. Either move the input datasets to  the same project as the view or add them as project references.
        :raises InvalidViewBackingDataset: Either you do not have access to one or more of the backing datasets or it does not exist.
        :raises ReplaceBackingDatasetsPermissionDenied: Could not replaceBackingDatasets the View.
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/datasets/views/{viewDatasetRid}/replaceBackingDatasets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branch": branch,
                    "backingDatasets": backing_datasets,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branch": typing.Optional[datasets_models.BranchName],
                        "backingDatasets": typing.List[datasets_models.ViewBackingDataset],
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "InputBackingDatasetNotInOutputViewProject": datasets_errors.InputBackingDatasetNotInOutputViewProject,
                    "InvalidViewBackingDataset": datasets_errors.InvalidViewBackingDataset,
                    "ReplaceBackingDatasetsPermissionDenied": datasets_errors.ReplaceBackingDatasetsPermissionDenied,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ViewClientRaw:
    def __init__(self, client: ViewClient) -> None:
        def add_backing_datasets(_: datasets_models.View): ...
        def add_primary_key(_: datasets_models.View): ...
        def create(_: datasets_models.View): ...
        def get(_: datasets_models.View): ...
        def remove_backing_datasets(_: datasets_models.View): ...
        def replace_backing_datasets(_: datasets_models.View): ...

        self.add_backing_datasets = core.with_raw_response(
            add_backing_datasets, client.add_backing_datasets
        )
        self.add_primary_key = core.with_raw_response(add_primary_key, client.add_primary_key)
        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.remove_backing_datasets = core.with_raw_response(
            remove_backing_datasets, client.remove_backing_datasets
        )
        self.replace_backing_datasets = core.with_raw_response(
            replace_backing_datasets, client.replace_backing_datasets
        )


class _ViewClientStreaming:
    def __init__(self, client: ViewClient) -> None:
        def add_backing_datasets(_: datasets_models.View): ...
        def add_primary_key(_: datasets_models.View): ...
        def create(_: datasets_models.View): ...
        def get(_: datasets_models.View): ...
        def remove_backing_datasets(_: datasets_models.View): ...
        def replace_backing_datasets(_: datasets_models.View): ...

        self.add_backing_datasets = core.with_streaming_response(
            add_backing_datasets, client.add_backing_datasets
        )
        self.add_primary_key = core.with_streaming_response(add_primary_key, client.add_primary_key)
        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.remove_backing_datasets = core.with_streaming_response(
            remove_backing_datasets, client.remove_backing_datasets
        )
        self.replace_backing_datasets = core.with_streaming_response(
            replace_backing_datasets, client.replace_backing_datasets
        )


class AsyncViewClient:
    """
    The API client for the View Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncViewClientStreaming(self)
        self.with_raw_response = _AsyncViewClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_backing_datasets(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        backing_datasets: typing.List[datasets_models.ViewBackingDataset],
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.View]:
        """
        Adds one or more backing datasets to a View. Any duplicates with the same dataset RID and branch name are
        ignored.

        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param backing_datasets:
        :type backing_datasets: List[ViewBackingDataset]
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.View]

        :raises AddBackingDatasetsPermissionDenied: Could not addBackingDatasets the View.
        :raises InputBackingDatasetNotInOutputViewProject: One or more backing datasets do not live in the same project as the view. Either move the input datasets to  the same project as the view or add them as project references.
        :raises InvalidViewBackingDataset: Either you do not have access to one or more of the backing datasets or it does not exist.
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/views/{viewDatasetRid}/addBackingDatasets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branch": branch,
                    "backingDatasets": backing_datasets,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branch": typing.Optional[datasets_models.BranchName],
                        "backingDatasets": typing.List[datasets_models.ViewBackingDataset],
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddBackingDatasetsPermissionDenied": datasets_errors.AddBackingDatasetsPermissionDenied,
                    "InputBackingDatasetNotInOutputViewProject": datasets_errors.InputBackingDatasetNotInOutputViewProject,
                    "InvalidViewBackingDataset": datasets_errors.InvalidViewBackingDataset,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_primary_key(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        primary_key: datasets_models.ViewPrimaryKey,
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.View]:
        """
        Adds a primary key to a View that does not already have one. Primary keys are treated as
        guarantees provided by the creator of the dataset.

        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param primary_key:
        :type primary_key: ViewPrimaryKey
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.View]

        :raises AddPrimaryKeyPermissionDenied: Could not addPrimaryKey the View.
        :raises InvalidViewPrimaryKeyColumnType: The type of each referenced column in the primary key must be one of the following: BYTE, SHORT, DECIMAL, INTEGER, LONG, STRING, BOOLEAN, TIMESTAMP or DATE.
        :raises InvalidViewPrimaryKeyDeletionColumn: The deletion column must be a boolean.
        :raises NotAllColumnsInPrimaryKeyArePresent: Not all columns in the View's primary key are present in the dataset(s).
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        :raises ViewPrimaryKeyCannotBeModified: A primary key already exits.
        :raises ViewPrimaryKeyDeletionColumnNotInDatasetSchema: The deletion column is not present in the dataset.
        :raises ViewPrimaryKeyMustContainAtLeastOneColumn: No columns were provided as part of the primary key
        :raises ViewPrimaryKeyRequiresBackingDatasets: Cannot add a primary key to a View that does not have any backing datasets.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/views/{viewDatasetRid}/addPrimaryKey",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branch": branch,
                    "primaryKey": primary_key,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branch": typing.Optional[datasets_models.BranchName],
                        "primaryKey": datasets_models.ViewPrimaryKey,
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddPrimaryKeyPermissionDenied": datasets_errors.AddPrimaryKeyPermissionDenied,
                    "InvalidViewPrimaryKeyColumnType": datasets_errors.InvalidViewPrimaryKeyColumnType,
                    "InvalidViewPrimaryKeyDeletionColumn": datasets_errors.InvalidViewPrimaryKeyDeletionColumn,
                    "NotAllColumnsInPrimaryKeyArePresent": datasets_errors.NotAllColumnsInPrimaryKeyArePresent,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                    "ViewPrimaryKeyCannotBeModified": datasets_errors.ViewPrimaryKeyCannotBeModified,
                    "ViewPrimaryKeyDeletionColumnNotInDatasetSchema": datasets_errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchema,
                    "ViewPrimaryKeyMustContainAtLeastOneColumn": datasets_errors.ViewPrimaryKeyMustContainAtLeastOneColumn,
                    "ViewPrimaryKeyRequiresBackingDatasets": datasets_errors.ViewPrimaryKeyRequiresBackingDatasets,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        backing_datasets: typing.List[datasets_models.ViewBackingDataset],
        parent_folder_rid: filesystem_models.FolderRid,
        view_name: datasets_models.DatasetName,
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        primary_key: typing.Optional[datasets_models.ViewPrimaryKey] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.View]:
        """
        Create a new View.
        :param backing_datasets:
        :type backing_datasets: List[ViewBackingDataset]
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param view_name:
        :type view_name: DatasetName
        :param branch: The branch name of the View. If not specified, defaults to `master` for most enrollments.
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param primary_key:
        :type primary_key: Optional[ViewPrimaryKey]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.View]

        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
        :raises CreateViewPermissionDenied: Could not create the View.
        :raises FolderNotFound: The given Folder could not be found.
        :raises InputBackingDatasetNotInOutputViewProject: One or more backing datasets do not live in the same project as the view. Either move the input datasets to  the same project as the view or add them as project references.
        :raises InvalidViewBackingDataset: Either you do not have access to one or more of the backing datasets or it does not exist.
        :raises InvalidViewPrimaryKeyColumnType: The type of each referenced column in the primary key must be one of the following: BYTE, SHORT, DECIMAL, INTEGER, LONG, STRING, BOOLEAN, TIMESTAMP or DATE.
        :raises InvalidViewPrimaryKeyDeletionColumn: The deletion column must be a boolean.
        :raises NotAllColumnsInPrimaryKeyArePresent: Not all columns in the View's primary key are present in the dataset(s).
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        :raises ViewDatasetCleanupFailed: Failed to delete dataset following View creation failure.
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        :raises ViewPrimaryKeyDeletionColumnNotInDatasetSchema: The deletion column is not present in the dataset.
        :raises ViewPrimaryKeyMustContainAtLeastOneColumn: No columns were provided as part of the primary key
        :raises ViewPrimaryKeyRequiresBackingDatasets: Cannot add a primary key to a View that does not have any backing datasets.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/views",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "viewName": view_name,
                    "backingDatasets": backing_datasets,
                    "branch": branch,
                    "primaryKey": primary_key,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": filesystem_models.FolderRid,
                        "viewName": datasets_models.DatasetName,
                        "backingDatasets": typing.List[datasets_models.ViewBackingDataset],
                        "branch": typing.Optional[datasets_models.BranchName],
                        "primaryKey": typing.Optional[datasets_models.ViewPrimaryKey],
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                    "CreateViewPermissionDenied": datasets_errors.CreateViewPermissionDenied,
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                    "InputBackingDatasetNotInOutputViewProject": datasets_errors.InputBackingDatasetNotInOutputViewProject,
                    "InvalidViewBackingDataset": datasets_errors.InvalidViewBackingDataset,
                    "InvalidViewPrimaryKeyColumnType": datasets_errors.InvalidViewPrimaryKeyColumnType,
                    "InvalidViewPrimaryKeyDeletionColumn": datasets_errors.InvalidViewPrimaryKeyDeletionColumn,
                    "NotAllColumnsInPrimaryKeyArePresent": datasets_errors.NotAllColumnsInPrimaryKeyArePresent,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                    "ViewDatasetCleanupFailed": datasets_errors.ViewDatasetCleanupFailed,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                    "ViewPrimaryKeyDeletionColumnNotInDatasetSchema": datasets_errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchema,
                    "ViewPrimaryKeyMustContainAtLeastOneColumn": datasets_errors.ViewPrimaryKeyMustContainAtLeastOneColumn,
                    "ViewPrimaryKeyRequiresBackingDatasets": datasets_errors.ViewPrimaryKeyRequiresBackingDatasets,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.View]:
        """
        Get metadata for a View.
        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.View]

        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/views/{viewDatasetRid}",
                query_params={
                    "branch": branch,
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "ViewNotFound": datasets_errors.ViewNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove_backing_datasets(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        backing_datasets: typing.List[datasets_models.ViewBackingDataset],
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.View]:
        """
        Removes specified backing datasets from a View. Removing a dataset triggers a
        [SNAPSHOT](https://palantir.com/docs/foundry/data-integration/datasets#snapshot) transaction on the next update. If a
        specified dataset does not exist, no error is thrown.

        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param backing_datasets:
        :type backing_datasets: List[ViewBackingDataset]
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.View]

        :raises InputBackingDatasetNotInOutputViewProject: One or more backing datasets do not live in the same project as the view. Either move the input datasets to  the same project as the view or add them as project references.
        :raises InvalidViewBackingDataset: Either you do not have access to one or more of the backing datasets or it does not exist.
        :raises RemoveBackingDatasetsPermissionDenied: Could not removeBackingDatasets the View.
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/views/{viewDatasetRid}/removeBackingDatasets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branch": branch,
                    "backingDatasets": backing_datasets,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branch": typing.Optional[datasets_models.BranchName],
                        "backingDatasets": typing.List[datasets_models.ViewBackingDataset],
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "InputBackingDatasetNotInOutputViewProject": datasets_errors.InputBackingDatasetNotInOutputViewProject,
                    "InvalidViewBackingDataset": datasets_errors.InvalidViewBackingDataset,
                    "RemoveBackingDatasetsPermissionDenied": datasets_errors.RemoveBackingDatasetsPermissionDenied,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace_backing_datasets(
        self,
        view_dataset_rid: datasets_models.DatasetRid,
        *,
        backing_datasets: typing.List[datasets_models.ViewBackingDataset],
        branch: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.View]:
        """
        Replaces the backing datasets for a View. Removing any backing dataset triggers a
        [SNAPSHOT](https://palantir.com/docs/foundry/data-integration/datasets#snapshot) transaction the next time the View is updated.

        :param view_dataset_rid: The rid of the View.
        :type view_dataset_rid: DatasetRid
        :param backing_datasets:
        :type backing_datasets: List[ViewBackingDataset]
        :param branch:
        :type branch: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.View]

        :raises InputBackingDatasetNotInOutputViewProject: One or more backing datasets do not live in the same project as the view. Either move the input datasets to  the same project as the view or add them as project references.
        :raises InvalidViewBackingDataset: Either you do not have access to one or more of the backing datasets or it does not exist.
        :raises ReplaceBackingDatasetsPermissionDenied: Could not replaceBackingDatasets the View.
        :raises ViewNotFound: The requested View could not be found. Either the view does not exist, the branch is not valid or the  client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/datasets/views/{viewDatasetRid}/replaceBackingDatasets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "viewDatasetRid": view_dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branch": branch,
                    "backingDatasets": backing_datasets,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branch": typing.Optional[datasets_models.BranchName],
                        "backingDatasets": typing.List[datasets_models.ViewBackingDataset],
                    },
                ),
                response_type=datasets_models.View,
                request_timeout=request_timeout,
                throwable_errors={
                    "InputBackingDatasetNotInOutputViewProject": datasets_errors.InputBackingDatasetNotInOutputViewProject,
                    "InvalidViewBackingDataset": datasets_errors.InvalidViewBackingDataset,
                    "ReplaceBackingDatasetsPermissionDenied": datasets_errors.ReplaceBackingDatasetsPermissionDenied,
                    "ViewNotFound": datasets_errors.ViewNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncViewClientRaw:
    def __init__(self, client: AsyncViewClient) -> None:
        def add_backing_datasets(_: datasets_models.View): ...
        def add_primary_key(_: datasets_models.View): ...
        def create(_: datasets_models.View): ...
        def get(_: datasets_models.View): ...
        def remove_backing_datasets(_: datasets_models.View): ...
        def replace_backing_datasets(_: datasets_models.View): ...

        self.add_backing_datasets = core.async_with_raw_response(
            add_backing_datasets, client.add_backing_datasets
        )
        self.add_primary_key = core.async_with_raw_response(add_primary_key, client.add_primary_key)
        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.remove_backing_datasets = core.async_with_raw_response(
            remove_backing_datasets, client.remove_backing_datasets
        )
        self.replace_backing_datasets = core.async_with_raw_response(
            replace_backing_datasets, client.replace_backing_datasets
        )


class _AsyncViewClientStreaming:
    def __init__(self, client: AsyncViewClient) -> None:
        def add_backing_datasets(_: datasets_models.View): ...
        def add_primary_key(_: datasets_models.View): ...
        def create(_: datasets_models.View): ...
        def get(_: datasets_models.View): ...
        def remove_backing_datasets(_: datasets_models.View): ...
        def replace_backing_datasets(_: datasets_models.View): ...

        self.add_backing_datasets = core.async_with_streaming_response(
            add_backing_datasets, client.add_backing_datasets
        )
        self.add_primary_key = core.async_with_streaming_response(
            add_primary_key, client.add_primary_key
        )
        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.remove_backing_datasets = core.async_with_streaming_response(
            remove_backing_datasets, client.remove_backing_datasets
        )
        self.replace_backing_datasets = core.async_with_streaming_response(
            replace_backing_datasets, client.replace_backing_datasets
        )
