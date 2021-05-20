# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class TillageDataOperations(object):
    """TillageDataOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.agrifood.farming.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_farmer_id(
        self,
        farmer_id,  # type: str
        min_tillage_depth=None,  # type: Optional[float]
        max_tillage_depth=None,  # type: Optional[float]
        min_tillage_pressure=None,  # type: Optional[float]
        max_tillage_pressure=None,  # type: Optional[float]
        sources=None,  # type: Optional[List[str]]
        associated_boundary_ids=None,  # type: Optional[List[str]]
        operation_boundary_ids=None,  # type: Optional[List[str]]
        min_operation_start_date_time=None,  # type: Optional[datetime.datetime]
        max_operation_start_date_time=None,  # type: Optional[datetime.datetime]
        min_operation_end_date_time=None,  # type: Optional[datetime.datetime]
        max_operation_end_date_time=None,  # type: Optional[datetime.datetime]
        min_operation_modified_date_time=None,  # type: Optional[datetime.datetime]
        max_operation_modified_date_time=None,  # type: Optional[datetime.datetime]
        min_area=None,  # type: Optional[float]
        max_area=None,  # type: Optional[float]
        ids=None,  # type: Optional[List[str]]
        names=None,  # type: Optional[List[str]]
        property_filters=None,  # type: Optional[List[str]]
        statuses=None,  # type: Optional[List[str]]
        min_created_date_time=None,  # type: Optional[datetime.datetime]
        max_created_date_time=None,  # type: Optional[datetime.datetime]
        min_last_modified_date_time=None,  # type: Optional[datetime.datetime]
        max_last_modified_date_time=None,  # type: Optional[datetime.datetime]
        max_page_size=50,  # type: Optional[int]
        skip_token=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.TillageDataListResponse"]
        """Returns a paginated list of tillage data resources under a particular farm.

        :param farmer_id: ID of the associated farmer.
        :type farmer_id: str
        :param min_tillage_depth: Minimum measured tillage depth (inclusive).
        :type min_tillage_depth: float
        :param max_tillage_depth: Maximum measured tillage depth (inclusive).
        :type max_tillage_depth: float
        :param min_tillage_pressure: Minimum pressure applied by a tillage implement (inclusive).
        :type min_tillage_pressure: float
        :param max_tillage_pressure: Maximum pressure applied by a tillage implement (inclusive).
        :type max_tillage_pressure: float
        :param sources: Sources of the operation data.
        :type sources: list[str]
        :param associated_boundary_ids: Boundary IDs associated with operation data.
        :type associated_boundary_ids: list[str]
        :param operation_boundary_ids: Operation boundary IDs associated with operation data.
        :type operation_boundary_ids: list[str]
        :param min_operation_start_date_time: Minimum start date-time of the operation data, sample
         format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_start_date_time: ~datetime.datetime
        :param max_operation_start_date_time: Maximum start date-time of the operation data, sample
         format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_start_date_time: ~datetime.datetime
        :param min_operation_end_date_time: Minimum end date-time of the operation data, sample format:
         yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_end_date_time: ~datetime.datetime
        :param max_operation_end_date_time: Maximum end date-time of the operation data, sample format:
         yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_end_date_time: ~datetime.datetime
        :param min_operation_modified_date_time: Minimum modified date-time of the operation data,
         sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_modified_date_time: ~datetime.datetime
        :param max_operation_modified_date_time: Maximum modified date-time of the operation data,
         sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_modified_date_time: ~datetime.datetime
        :param min_area: Minimum area for which operation was applied (inclusive).
        :type min_area: float
        :param max_area: Maximum area for which operation was applied (inclusive).
        :type max_area: float
        :param ids: Ids of the resource.
        :type ids: list[str]
        :param names: Names of the resource.
        :type names: list[str]
        :param property_filters: Filters on key-value pairs within the Properties object.
         eg. "{testKey} eq {testValue}".
        :type property_filters: list[str]
        :param statuses: Statuses of the resource.
        :type statuses: list[str]
        :param min_created_date_time: Minimum creation date of resource (inclusive).
        :type min_created_date_time: ~datetime.datetime
        :param max_created_date_time: Maximum creation date of resource (inclusive).
        :type max_created_date_time: ~datetime.datetime
        :param min_last_modified_date_time: Minimum last modified date of resource (inclusive).
        :type min_last_modified_date_time: ~datetime.datetime
        :param max_last_modified_date_time: Maximum last modified date of resource (inclusive).
        :type max_last_modified_date_time: ~datetime.datetime
        :param max_page_size: Maximum number of items needed (inclusive).
         Minimum = 10, Maximum = 1000, Default value = 50.
        :type max_page_size: int
        :param skip_token: Skip token for getting next set of results.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TillageDataListResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.agrifood.farming.models.TillageDataListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TillageDataListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_farmer_id.metadata['url']  # type: ignore
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if min_tillage_depth is not None:
                    query_parameters['minTillageDepth'] = self._serialize.query("min_tillage_depth", min_tillage_depth, 'float')
                if max_tillage_depth is not None:
                    query_parameters['maxTillageDepth'] = self._serialize.query("max_tillage_depth", max_tillage_depth, 'float')
                if min_tillage_pressure is not None:
                    query_parameters['minTillagePressure'] = self._serialize.query("min_tillage_pressure", min_tillage_pressure, 'float')
                if max_tillage_pressure is not None:
                    query_parameters['maxTillagePressure'] = self._serialize.query("max_tillage_pressure", max_tillage_pressure, 'float')
                if sources is not None:
                    query_parameters['sources'] = [self._serialize.query("sources", q, 'str') if q is not None else '' for q in sources]
                if associated_boundary_ids is not None:
                    query_parameters['associatedBoundaryIds'] = [self._serialize.query("associated_boundary_ids", q, 'str') if q is not None else '' for q in associated_boundary_ids]
                if operation_boundary_ids is not None:
                    query_parameters['operationBoundaryIds'] = [self._serialize.query("operation_boundary_ids", q, 'str') if q is not None else '' for q in operation_boundary_ids]
                if min_operation_start_date_time is not None:
                    query_parameters['minOperationStartDateTime'] = self._serialize.query("min_operation_start_date_time", min_operation_start_date_time, 'iso-8601')
                if max_operation_start_date_time is not None:
                    query_parameters['maxOperationStartDateTime'] = self._serialize.query("max_operation_start_date_time", max_operation_start_date_time, 'iso-8601')
                if min_operation_end_date_time is not None:
                    query_parameters['minOperationEndDateTime'] = self._serialize.query("min_operation_end_date_time", min_operation_end_date_time, 'iso-8601')
                if max_operation_end_date_time is not None:
                    query_parameters['maxOperationEndDateTime'] = self._serialize.query("max_operation_end_date_time", max_operation_end_date_time, 'iso-8601')
                if min_operation_modified_date_time is not None:
                    query_parameters['minOperationModifiedDateTime'] = self._serialize.query("min_operation_modified_date_time", min_operation_modified_date_time, 'iso-8601')
                if max_operation_modified_date_time is not None:
                    query_parameters['maxOperationModifiedDateTime'] = self._serialize.query("max_operation_modified_date_time", max_operation_modified_date_time, 'iso-8601')
                if min_area is not None:
                    query_parameters['minArea'] = self._serialize.query("min_area", min_area, 'float')
                if max_area is not None:
                    query_parameters['maxArea'] = self._serialize.query("max_area", max_area, 'float')
                if ids is not None:
                    query_parameters['ids'] = [self._serialize.query("ids", q, 'str') if q is not None else '' for q in ids]
                if names is not None:
                    query_parameters['names'] = [self._serialize.query("names", q, 'str') if q is not None else '' for q in names]
                if property_filters is not None:
                    query_parameters['propertyFilters'] = [self._serialize.query("property_filters", q, 'str') if q is not None else '' for q in property_filters]
                if statuses is not None:
                    query_parameters['statuses'] = [self._serialize.query("statuses", q, 'str') if q is not None else '' for q in statuses]
                if min_created_date_time is not None:
                    query_parameters['minCreatedDateTime'] = self._serialize.query("min_created_date_time", min_created_date_time, 'iso-8601')
                if max_created_date_time is not None:
                    query_parameters['maxCreatedDateTime'] = self._serialize.query("max_created_date_time", max_created_date_time, 'iso-8601')
                if min_last_modified_date_time is not None:
                    query_parameters['minLastModifiedDateTime'] = self._serialize.query("min_last_modified_date_time", min_last_modified_date_time, 'iso-8601')
                if max_last_modified_date_time is not None:
                    query_parameters['maxLastModifiedDateTime'] = self._serialize.query("max_last_modified_date_time", max_last_modified_date_time, 'iso-8601')
                if max_page_size is not None:
                    query_parameters['$maxPageSize'] = self._serialize.query("max_page_size", max_page_size, 'int', maximum=1000, minimum=10)
                if skip_token is not None:
                    query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('TillageDataListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_farmer_id.metadata = {'url': '/farmers/{farmerId}/tillage-data'}  # type: ignore

    def list(
        self,
        min_tillage_depth=None,  # type: Optional[float]
        max_tillage_depth=None,  # type: Optional[float]
        min_tillage_pressure=None,  # type: Optional[float]
        max_tillage_pressure=None,  # type: Optional[float]
        sources=None,  # type: Optional[List[str]]
        associated_boundary_ids=None,  # type: Optional[List[str]]
        operation_boundary_ids=None,  # type: Optional[List[str]]
        min_operation_start_date_time=None,  # type: Optional[datetime.datetime]
        max_operation_start_date_time=None,  # type: Optional[datetime.datetime]
        min_operation_end_date_time=None,  # type: Optional[datetime.datetime]
        max_operation_end_date_time=None,  # type: Optional[datetime.datetime]
        min_operation_modified_date_time=None,  # type: Optional[datetime.datetime]
        max_operation_modified_date_time=None,  # type: Optional[datetime.datetime]
        min_area=None,  # type: Optional[float]
        max_area=None,  # type: Optional[float]
        ids=None,  # type: Optional[List[str]]
        names=None,  # type: Optional[List[str]]
        property_filters=None,  # type: Optional[List[str]]
        statuses=None,  # type: Optional[List[str]]
        min_created_date_time=None,  # type: Optional[datetime.datetime]
        max_created_date_time=None,  # type: Optional[datetime.datetime]
        min_last_modified_date_time=None,  # type: Optional[datetime.datetime]
        max_last_modified_date_time=None,  # type: Optional[datetime.datetime]
        max_page_size=50,  # type: Optional[int]
        skip_token=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.TillageDataListResponse"]
        """Returns a paginated list of tillage data resources across all farmers.

        :param min_tillage_depth: Minimum measured tillage depth (inclusive).
        :type min_tillage_depth: float
        :param max_tillage_depth: Maximum measured tillage depth (inclusive).
        :type max_tillage_depth: float
        :param min_tillage_pressure: Minimum pressure applied by a tillage implement (inclusive).
        :type min_tillage_pressure: float
        :param max_tillage_pressure: Maximum pressure applied by a tillage implement (inclusive).
        :type max_tillage_pressure: float
        :param sources: Sources of the operation data.
        :type sources: list[str]
        :param associated_boundary_ids: Boundary IDs associated with operation data.
        :type associated_boundary_ids: list[str]
        :param operation_boundary_ids: Operation boundary IDs associated with operation data.
        :type operation_boundary_ids: list[str]
        :param min_operation_start_date_time: Minimum start date-time of the operation data, sample
         format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_start_date_time: ~datetime.datetime
        :param max_operation_start_date_time: Maximum start date-time of the operation data, sample
         format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_start_date_time: ~datetime.datetime
        :param min_operation_end_date_time: Minimum end date-time of the operation data, sample format:
         yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_end_date_time: ~datetime.datetime
        :param max_operation_end_date_time: Maximum end date-time of the operation data, sample format:
         yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_end_date_time: ~datetime.datetime
        :param min_operation_modified_date_time: Minimum modified date-time of the operation data,
         sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_modified_date_time: ~datetime.datetime
        :param max_operation_modified_date_time: Maximum modified date-time of the operation data,
         sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_modified_date_time: ~datetime.datetime
        :param min_area: Minimum area for which operation was applied (inclusive).
        :type min_area: float
        :param max_area: Maximum area for which operation was applied (inclusive).
        :type max_area: float
        :param ids: Ids of the resource.
        :type ids: list[str]
        :param names: Names of the resource.
        :type names: list[str]
        :param property_filters: Filters on key-value pairs within the Properties object.
         eg. "{testKey} eq {testValue}".
        :type property_filters: list[str]
        :param statuses: Statuses of the resource.
        :type statuses: list[str]
        :param min_created_date_time: Minimum creation date of resource (inclusive).
        :type min_created_date_time: ~datetime.datetime
        :param max_created_date_time: Maximum creation date of resource (inclusive).
        :type max_created_date_time: ~datetime.datetime
        :param min_last_modified_date_time: Minimum last modified date of resource (inclusive).
        :type min_last_modified_date_time: ~datetime.datetime
        :param max_last_modified_date_time: Maximum last modified date of resource (inclusive).
        :type max_last_modified_date_time: ~datetime.datetime
        :param max_page_size: Maximum number of items needed (inclusive).
         Minimum = 10, Maximum = 1000, Default value = 50.
        :type max_page_size: int
        :param skip_token: Skip token for getting next set of results.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TillageDataListResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.agrifood.farming.models.TillageDataListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TillageDataListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if min_tillage_depth is not None:
                    query_parameters['minTillageDepth'] = self._serialize.query("min_tillage_depth", min_tillage_depth, 'float')
                if max_tillage_depth is not None:
                    query_parameters['maxTillageDepth'] = self._serialize.query("max_tillage_depth", max_tillage_depth, 'float')
                if min_tillage_pressure is not None:
                    query_parameters['minTillagePressure'] = self._serialize.query("min_tillage_pressure", min_tillage_pressure, 'float')
                if max_tillage_pressure is not None:
                    query_parameters['maxTillagePressure'] = self._serialize.query("max_tillage_pressure", max_tillage_pressure, 'float')
                if sources is not None:
                    query_parameters['sources'] = [self._serialize.query("sources", q, 'str') if q is not None else '' for q in sources]
                if associated_boundary_ids is not None:
                    query_parameters['associatedBoundaryIds'] = [self._serialize.query("associated_boundary_ids", q, 'str') if q is not None else '' for q in associated_boundary_ids]
                if operation_boundary_ids is not None:
                    query_parameters['operationBoundaryIds'] = [self._serialize.query("operation_boundary_ids", q, 'str') if q is not None else '' for q in operation_boundary_ids]
                if min_operation_start_date_time is not None:
                    query_parameters['minOperationStartDateTime'] = self._serialize.query("min_operation_start_date_time", min_operation_start_date_time, 'iso-8601')
                if max_operation_start_date_time is not None:
                    query_parameters['maxOperationStartDateTime'] = self._serialize.query("max_operation_start_date_time", max_operation_start_date_time, 'iso-8601')
                if min_operation_end_date_time is not None:
                    query_parameters['minOperationEndDateTime'] = self._serialize.query("min_operation_end_date_time", min_operation_end_date_time, 'iso-8601')
                if max_operation_end_date_time is not None:
                    query_parameters['maxOperationEndDateTime'] = self._serialize.query("max_operation_end_date_time", max_operation_end_date_time, 'iso-8601')
                if min_operation_modified_date_time is not None:
                    query_parameters['minOperationModifiedDateTime'] = self._serialize.query("min_operation_modified_date_time", min_operation_modified_date_time, 'iso-8601')
                if max_operation_modified_date_time is not None:
                    query_parameters['maxOperationModifiedDateTime'] = self._serialize.query("max_operation_modified_date_time", max_operation_modified_date_time, 'iso-8601')
                if min_area is not None:
                    query_parameters['minArea'] = self._serialize.query("min_area", min_area, 'float')
                if max_area is not None:
                    query_parameters['maxArea'] = self._serialize.query("max_area", max_area, 'float')
                if ids is not None:
                    query_parameters['ids'] = [self._serialize.query("ids", q, 'str') if q is not None else '' for q in ids]
                if names is not None:
                    query_parameters['names'] = [self._serialize.query("names", q, 'str') if q is not None else '' for q in names]
                if property_filters is not None:
                    query_parameters['propertyFilters'] = [self._serialize.query("property_filters", q, 'str') if q is not None else '' for q in property_filters]
                if statuses is not None:
                    query_parameters['statuses'] = [self._serialize.query("statuses", q, 'str') if q is not None else '' for q in statuses]
                if min_created_date_time is not None:
                    query_parameters['minCreatedDateTime'] = self._serialize.query("min_created_date_time", min_created_date_time, 'iso-8601')
                if max_created_date_time is not None:
                    query_parameters['maxCreatedDateTime'] = self._serialize.query("max_created_date_time", max_created_date_time, 'iso-8601')
                if min_last_modified_date_time is not None:
                    query_parameters['minLastModifiedDateTime'] = self._serialize.query("min_last_modified_date_time", min_last_modified_date_time, 'iso-8601')
                if max_last_modified_date_time is not None:
                    query_parameters['maxLastModifiedDateTime'] = self._serialize.query("max_last_modified_date_time", max_last_modified_date_time, 'iso-8601')
                if max_page_size is not None:
                    query_parameters['$maxPageSize'] = self._serialize.query("max_page_size", max_page_size, 'int', maximum=1000, minimum=10)
                if skip_token is not None:
                    query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('TillageDataListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/tillage-data'}  # type: ignore

    def get(
        self,
        farmer_id,  # type: str
        tillage_data_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.TillageData"
        """Get a specified tillage data resource under a particular farmer.

        :param farmer_id: ID of the associated farmer resource.
        :type farmer_id: str
        :param tillage_data_id: ID of the tillage data resource.
        :type tillage_data_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TillageData, or the result of cls(response)
        :rtype: ~azure.agrifood.farming.models.TillageData
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TillageData"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
            'tillageDataId': self._serialize.url("tillage_data_id", tillage_data_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('TillageData', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/farmers/{farmerId}/tillage-data/{tillageDataId}'}  # type: ignore

    def create_or_update(
        self,
        farmer_id,  # type: str
        tillage_data_id,  # type: str
        tillage_data=None,  # type: Optional["_models.TillageData"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.TillageData"
        """Creates or updates an tillage data resource under a particular farmer.

        :param farmer_id: ID of the associated farmer.
        :type farmer_id: str
        :param tillage_data_id: ID of the tillage data resource.
        :type tillage_data_id: str
        :param tillage_data: Tillage data resource payload to create or update.
        :type tillage_data: ~azure.agrifood.farming.models.TillageData
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TillageData, or the result of cls(response)
        :rtype: ~azure.agrifood.farming.models.TillageData
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TillageData"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        content_type = kwargs.pop("content_type", "application/merge-patch+json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
            'tillageDataId': self._serialize.url("tillage_data_id", tillage_data_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if tillage_data is not None:
            body_content = self._serialize.body(tillage_data, 'TillageData')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('TillageData', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('TillageData', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/farmers/{farmerId}/tillage-data/{tillageDataId}'}  # type: ignore

    def delete(
        self,
        farmer_id,  # type: str
        tillage_data_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a specified tillage data resource under a particular farmer.

        :param farmer_id: ID of the associated farmer resource.
        :type farmer_id: str
        :param tillage_data_id: ID of the tillage data.
        :type tillage_data_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
            'tillageDataId': self._serialize.url("tillage_data_id", tillage_data_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/farmers/{farmerId}/tillage-data/{tillageDataId}'}  # type: ignore
