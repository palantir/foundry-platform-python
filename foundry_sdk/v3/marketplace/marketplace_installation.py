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
from functools import cached_property

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v3.core import models as core_models
from foundry_sdk.v3.marketplace import errors as marketplace_errors
from foundry_sdk.v3.marketplace import models as marketplace_models


class MarketplaceInstallationClient:
    """
    The API client for the MarketplaceInstallation Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _MarketplaceInstallationClientStreaming(self)
        self.with_raw_response = _MarketplaceInstallationClientRaw(self)

    @cached_property
    def Inputs(self):
        from foundry_sdk.v3.marketplace.marketplace_installation_inputs import (
            MarketplaceInstallationInputsClient,
        )  # NOQA

        return MarketplaceInstallationInputsClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        marketplace_rid: marketplace_models.MarketplaceRid,
        parent_folder_rid: core_models.FolderRid,
        product_id: marketplace_models.ProductId,
        installation_suffix: typing.Optional[str] = None,
        ontology_rid: typing.Optional[core_models.OntologyRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        target_version_hint: typing.Optional[marketplace_models.ProductVersionSelector] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> marketplace_models.MarketplaceInstallation:
        """
        Register a product installation in the given project or folder without running an installation job or
        installing product resources. Returns the created installation with its current Compass metadata and
        no latest target version. A subsequent installation job selects the version to install.

        This operation is not idempotent. Repeated requests create separate installations unless the selected
        product version's singleton policy prohibits another installation in the destination namespace, in
        which case SingletonMarketplaceInstallationAlreadyExists is returned.

        Required scopes: [api:v3:marketplace-installation:write:create]

        :param marketplace_rid:
        :type marketplace_rid: MarketplaceRid
        :param parent_folder_rid: The RID of the Compass project or folder that currently contains the installation. On creation, this is the destination where the installation is registered and its jobs create resources.
        :type parent_folder_rid: FolderRid
        :param product_id:
        :type product_id: ProductId
        :param installation_suffix: An optional suffix appended to the product title to form the initial display name, for example "Product title - CI staging". If omitted, the display name uses the product title alone.
        :type installation_suffix: Optional[str]
        :param ontology_rid: The ontology where jobs for this installation create or update ontology resources. Omit if the product does not interact with the ontology.
        :type ontology_rid: Optional[OntologyRid]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param target_version_hint: If provided:  - validations that are version specific (e.g. singleton validations) are executed assuming     the installation will later have a job run to transition it to this specific target version.  - the installation title is resolved from the product title at that version.  If not provided, the latest released version of the product is used to resolve information for the steps above.
        :type target_version_hint: Optional[ProductVersionSelector]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: marketplace_models.MarketplaceInstallation

        :raises CreateMarketplaceInstallationPermissionDenied: Could not register the installation due to insufficient permissions on the marketplace, product, or destination project or folder.
        :raises InvalidInstallationTargetVersionHint: The semantic version in the hint must be an exact major.minor.patch version with non-negative integer components and no leading zeros. Version ranges, wildcards, prerelease identifiers, and build metadata are not supported.
        :raises MarketplaceProductNotFound: The product could not be found in the specified marketplace or has no released version available for registration.
        :raises MarketplaceProductVersionNotFound: The hinted product version could not be found in the specified product and marketplace.
        :raises ParentFolderNotFound: The destination project or folder could not be found.
        :raises SingletonMarketplaceInstallationAlreadyExists: Another installation of this product already exists in the destination namespace, and the product version used for registration requires a single installation per namespace.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/marketplaceInstallations",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=marketplace_models.CreateMarketplaceInstallationRequest(
                    installation_suffix=installation_suffix,
                    marketplace_rid=marketplace_rid,
                    ontology_rid=ontology_rid,
                    parent_folder_rid=parent_folder_rid,
                    product_id=product_id,
                    target_version_hint=target_version_hint,
                ),
                response_type=marketplace_models.MarketplaceInstallation,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateMarketplaceInstallationPermissionDenied": marketplace_errors.CreateMarketplaceInstallationPermissionDenied,
                    "InvalidInstallationTargetVersionHint": marketplace_errors.InvalidInstallationTargetVersionHint,
                    "MarketplaceProductNotFound": marketplace_errors.MarketplaceProductNotFound,
                    "MarketplaceProductVersionNotFound": marketplace_errors.MarketplaceProductVersionNotFound,
                    "ParentFolderNotFound": marketplace_errors.ParentFolderNotFound,
                    "SingletonMarketplaceInstallationAlreadyExists": marketplace_errors.SingletonMarketplaceInstallationAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_installation_rid: marketplace_models.MarketplaceInstallationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> marketplace_models.MarketplaceInstallation:
        """
        Get a registered installation and the product version targeted by its latest submitted job.

        Required scopes: [api:v3:marketplace-installation:read:get]

        :param marketplace_installation_rid:
        :type marketplace_installation_rid: MarketplaceInstallationRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: marketplace_models.MarketplaceInstallation

        :raises MarketplaceInstallationNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaceInstallations/{marketplaceInstallationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceInstallationRid": marketplace_installation_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.MarketplaceInstallation,
                request_timeout=request_timeout,
                throwable_errors={
                    "MarketplaceInstallationNotFound": marketplace_errors.MarketplaceInstallationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MarketplaceInstallationClientRaw:
    def __init__(self, client: MarketplaceInstallationClient) -> None:
        def create(_: marketplace_models.MarketplaceInstallation): ...
        def get(_: marketplace_models.MarketplaceInstallation): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)


class _MarketplaceInstallationClientStreaming:
    def __init__(self, client: MarketplaceInstallationClient) -> None:
        def create(_: marketplace_models.MarketplaceInstallation): ...
        def get(_: marketplace_models.MarketplaceInstallation): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)


class AsyncMarketplaceInstallationClient:
    """
    The API client for the MarketplaceInstallation Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncMarketplaceInstallationClientStreaming(self)
        self.with_raw_response = _AsyncMarketplaceInstallationClientRaw(self)

    @cached_property
    def Inputs(self):
        from foundry_sdk.v3.marketplace.marketplace_installation_inputs import (
            AsyncMarketplaceInstallationInputsClient,
        )  # NOQA

        return AsyncMarketplaceInstallationInputsClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        marketplace_rid: marketplace_models.MarketplaceRid,
        parent_folder_rid: core_models.FolderRid,
        product_id: marketplace_models.ProductId,
        installation_suffix: typing.Optional[str] = None,
        ontology_rid: typing.Optional[core_models.OntologyRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        target_version_hint: typing.Optional[marketplace_models.ProductVersionSelector] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[marketplace_models.MarketplaceInstallation]:
        """
        Register a product installation in the given project or folder without running an installation job or
        installing product resources. Returns the created installation with its current Compass metadata and
        no latest target version. A subsequent installation job selects the version to install.

        This operation is not idempotent. Repeated requests create separate installations unless the selected
        product version's singleton policy prohibits another installation in the destination namespace, in
        which case SingletonMarketplaceInstallationAlreadyExists is returned.

        Required scopes: [api:v3:marketplace-installation:write:create]

        :param marketplace_rid:
        :type marketplace_rid: MarketplaceRid
        :param parent_folder_rid: The RID of the Compass project or folder that currently contains the installation. On creation, this is the destination where the installation is registered and its jobs create resources.
        :type parent_folder_rid: FolderRid
        :param product_id:
        :type product_id: ProductId
        :param installation_suffix: An optional suffix appended to the product title to form the initial display name, for example "Product title - CI staging". If omitted, the display name uses the product title alone.
        :type installation_suffix: Optional[str]
        :param ontology_rid: The ontology where jobs for this installation create or update ontology resources. Omit if the product does not interact with the ontology.
        :type ontology_rid: Optional[OntologyRid]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param target_version_hint: If provided:  - validations that are version specific (e.g. singleton validations) are executed assuming     the installation will later have a job run to transition it to this specific target version.  - the installation title is resolved from the product title at that version.  If not provided, the latest released version of the product is used to resolve information for the steps above.
        :type target_version_hint: Optional[ProductVersionSelector]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[marketplace_models.MarketplaceInstallation]

        :raises CreateMarketplaceInstallationPermissionDenied: Could not register the installation due to insufficient permissions on the marketplace, product, or destination project or folder.
        :raises InvalidInstallationTargetVersionHint: The semantic version in the hint must be an exact major.minor.patch version with non-negative integer components and no leading zeros. Version ranges, wildcards, prerelease identifiers, and build metadata are not supported.
        :raises MarketplaceProductNotFound: The product could not be found in the specified marketplace or has no released version available for registration.
        :raises MarketplaceProductVersionNotFound: The hinted product version could not be found in the specified product and marketplace.
        :raises ParentFolderNotFound: The destination project or folder could not be found.
        :raises SingletonMarketplaceInstallationAlreadyExists: Another installation of this product already exists in the destination namespace, and the product version used for registration requires a single installation per namespace.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/marketplaceInstallations",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=marketplace_models.CreateMarketplaceInstallationRequest(
                    installation_suffix=installation_suffix,
                    marketplace_rid=marketplace_rid,
                    ontology_rid=ontology_rid,
                    parent_folder_rid=parent_folder_rid,
                    product_id=product_id,
                    target_version_hint=target_version_hint,
                ),
                response_type=marketplace_models.MarketplaceInstallation,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateMarketplaceInstallationPermissionDenied": marketplace_errors.CreateMarketplaceInstallationPermissionDenied,
                    "InvalidInstallationTargetVersionHint": marketplace_errors.InvalidInstallationTargetVersionHint,
                    "MarketplaceProductNotFound": marketplace_errors.MarketplaceProductNotFound,
                    "MarketplaceProductVersionNotFound": marketplace_errors.MarketplaceProductVersionNotFound,
                    "ParentFolderNotFound": marketplace_errors.ParentFolderNotFound,
                    "SingletonMarketplaceInstallationAlreadyExists": marketplace_errors.SingletonMarketplaceInstallationAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_installation_rid: marketplace_models.MarketplaceInstallationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[marketplace_models.MarketplaceInstallation]:
        """
        Get a registered installation and the product version targeted by its latest submitted job.

        Required scopes: [api:v3:marketplace-installation:read:get]

        :param marketplace_installation_rid:
        :type marketplace_installation_rid: MarketplaceInstallationRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[marketplace_models.MarketplaceInstallation]

        :raises MarketplaceInstallationNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaceInstallations/{marketplaceInstallationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceInstallationRid": marketplace_installation_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.MarketplaceInstallation,
                request_timeout=request_timeout,
                throwable_errors={
                    "MarketplaceInstallationNotFound": marketplace_errors.MarketplaceInstallationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncMarketplaceInstallationClientRaw:
    def __init__(self, client: AsyncMarketplaceInstallationClient) -> None:
        def create(_: marketplace_models.MarketplaceInstallation): ...
        def get(_: marketplace_models.MarketplaceInstallation): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)


class _AsyncMarketplaceInstallationClientStreaming:
    def __init__(self, client: AsyncMarketplaceInstallationClient) -> None:
        def create(_: marketplace_models.MarketplaceInstallation): ...
        def get(_: marketplace_models.MarketplaceInstallation): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
