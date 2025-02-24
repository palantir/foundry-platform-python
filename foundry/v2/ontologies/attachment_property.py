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

import warnings
from functools import cached_property
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import deprecated
from typing_extensions import overload

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import BinaryStream
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.ontologies.models._artifact_repository_rid import ArtifactRepositoryRid
from foundry.v2.ontologies.models._attachment_metadata_response import (
    AttachmentMetadataResponse,
)  # NOQA
from foundry.v2.ontologies.models._attachment_rid import AttachmentRid
from foundry.v2.ontologies.models._attachment_v2 import AttachmentV2
from foundry.v2.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.ontologies.models._ontology_identifier import OntologyIdentifier
from foundry.v2.ontologies.models._property_api_name import PropertyApiName
from foundry.v2.ontologies.models._property_value_escaped_string import (
    PropertyValueEscapedString,
)  # NOQA
from foundry.v2.ontologies.models._sdk_package_name import SdkPackageName


class AttachmentPropertyClient:
    """
    The API client for the AttachmentProperty Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _AttachmentPropertyClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _AttachmentPropertyClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_attachment(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> AttachmentMetadataResponse:
        """
        Get the metadata of attachments parented to the given object.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AttachmentMetadataResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AttachmentMetadataResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_attachment_by_rid(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        attachment_rid: AttachmentRid,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> AttachmentV2:
        """
        Get the metadata of a particular attachment in an attachment list.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AttachmentV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AttachmentV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read_attachment(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        stream: Literal[True],
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> BinaryStream:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BinaryStream
        """
        ...

    @overload
    def read_attachment(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        stream: Literal[False] = False,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> bytes:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """
        ...

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read_attachment(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        stream: bool,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]
        """
        ...

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def read_attachment(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        stream: bool = False,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]
        """

        if stream:
            warnings.warn(
                f"client.ontologies.AttachmentProperty.read_attachment(..., stream=True, chunk_size={chunk_size}) is deprecated. Please use:\n\nwith client.ontologies.AttachmentProperty.with_streaming_response.read_attachment(...) as response:\n    response.iter_bytes(chunk_size={chunk_size})\n",
                DeprecationWarning,
                stacklevel=2,
            )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/content",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                stream=stream,
                chunk_size=chunk_size,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read_attachment_by_rid(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        attachment_rid: AttachmentRid,
        *,
        stream: Literal[True],
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> BinaryStream:
        """
        Get the content of an attachment by its RID.

        The RID must exist in the attachment array of the property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BinaryStream
        """
        ...

    @overload
    def read_attachment_by_rid(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        attachment_rid: AttachmentRid,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        stream: Literal[False] = False,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> bytes:
        """
        Get the content of an attachment by its RID.

        The RID must exist in the attachment array of the property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """
        ...

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read_attachment_by_rid(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        attachment_rid: AttachmentRid,
        *,
        stream: bool,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Get the content of an attachment by its RID.

        The RID must exist in the attachment array of the property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]
        """
        ...

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def read_attachment_by_rid(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        attachment_rid: AttachmentRid,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        stream: bool = False,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Get the content of an attachment by its RID.

        The RID must exist in the attachment array of the property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]
        """

        if stream:
            warnings.warn(
                f"client.ontologies.AttachmentProperty.read_attachment_by_rid(..., stream=True, chunk_size={chunk_size}) is deprecated. Please use:\n\nwith client.ontologies.AttachmentProperty.with_streaming_response.read_attachment_by_rid(...) as response:\n    response.iter_bytes(chunk_size={chunk_size})\n",
                DeprecationWarning,
                stacklevel=2,
            )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}/content",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                stream=stream,
                chunk_size=chunk_size,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _AttachmentPropertyClientRaw:
    """
    The API client for the AttachmentProperty Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_attachment(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[AttachmentMetadataResponse]:
        """
        Get the metadata of attachments parented to the given object.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[AttachmentMetadataResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AttachmentMetadataResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_attachment_by_rid(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        attachment_rid: AttachmentRid,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[AttachmentV2]:
        """
        Get the metadata of a particular attachment in an attachment list.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[AttachmentV2]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AttachmentV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def read_attachment(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[bytes]:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[bytes]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/content",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def read_attachment_by_rid(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        attachment_rid: AttachmentRid,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[bytes]:
        """
        Get the content of an attachment by its RID.

        The RID must exist in the attachment array of the property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[bytes]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}/content",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _AttachmentPropertyClientStreaming:
    """
    The API client for the AttachmentProperty Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_attachment(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[AttachmentMetadataResponse]:
        """
        Get the metadata of attachments parented to the given object.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[AttachmentMetadataResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AttachmentMetadataResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_attachment_by_rid(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        attachment_rid: AttachmentRid,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[AttachmentV2]:
        """
        Get the metadata of a particular attachment in an attachment list.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[AttachmentV2]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AttachmentV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def read_attachment(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[bytes]:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[bytes]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/content",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def read_attachment_by_rid(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        attachment_rid: AttachmentRid,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[bytes]:
        """
        Get the content of an attachment by its RID.

        The RID must exist in the attachment array of the property.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param property: property
        :type property: PropertyApiName
        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[bytes]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}/content",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "property": property,
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
