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

from typing import Annotated
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call

from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v2.models._artifact_repository_rid import ArtifactRepositoryRid
from foundry.v2.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.models._ontology_identifier import OntologyIdentifier
from foundry.v2.models._property_api_name import PropertyApiName
from foundry.v2.models._property_value_escaped_string import PropertyValueEscapedString
from foundry.v2.models._sdk_package_name import SdkPackageName
from foundry.v2.models._stream_time_series_points_request import (
    StreamTimeSeriesPointsRequest,
)  # NOQA
from foundry.v2.models._stream_time_series_points_request_dict import (
    StreamTimeSeriesPointsRequestDict,
)  # NOQA
from foundry.v2.models._time_series_point import TimeSeriesPoint


class TimeSeriesPropertyV2Resource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def get_first_point(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> TimeSeriesPoint:
        """
        Get the first point of a time series property.

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
        :rtype: TimeSeriesPoint
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _path_params["primaryKey"] = primary_key

        _path_params["property"] = property

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=TimeSeriesPoint,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_last_point(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> TimeSeriesPoint:
        """
        Get the last point of a time series property.

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
        :rtype: TimeSeriesPoint
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _path_params["primaryKey"] = primary_key

        _path_params["property"] = property

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=TimeSeriesPoint,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def stream_points(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        property: PropertyApiName,
        stream_time_series_points_request: Union[
            StreamTimeSeriesPointsRequest, StreamTimeSeriesPointsRequestDict
        ],
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """
        Stream all of the points of a time series property.

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
        :param stream_time_series_points_request: Body of the request
        :type stream_time_series_points_request: Union[StreamTimeSeriesPointsRequest, StreamTimeSeriesPointsRequestDict]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = stream_time_series_points_request
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _path_params["primaryKey"] = primary_key

        _path_params["property"] = property

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "*/*"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[StreamTimeSeriesPointsRequest, StreamTimeSeriesPointsRequestDict],
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )
