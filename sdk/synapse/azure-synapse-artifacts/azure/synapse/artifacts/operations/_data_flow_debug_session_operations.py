# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling
from azure.synapse.artifacts.core.rest import HttpRequest

from .. import models as _models
from ..rest import data_flow_debug_session as rest_data_flow_debug_session

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class DataFlowDebugSessionOperations(object):
    """DataFlowDebugSessionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.artifacts.models
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

    def _create_data_flow_debug_session_initial(
        self,
        request,  # type: "_models.CreateDataFlowDebugSessionRequest"
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.CreateDataFlowDebugSessionResponse"]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.CreateDataFlowDebugSessionResponse"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(request, "object")

        request = rest_data_flow_debug_session.build_create_data_flow_debug_session_request_initial(
            json=json,
            content_type=content_type,
            template_url=self._create_data_flow_debug_session_initial.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("CreateDataFlowDebugSessionResponse", pipeline_response)

        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _create_data_flow_debug_session_initial.metadata = {"url": "/createDataFlowDebugSession"}  # type: ignore

    def begin_create_data_flow_debug_session(
        self,
        request,  # type: "_models.CreateDataFlowDebugSessionRequest"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.CreateDataFlowDebugSessionResponse"]
        """Creates a data flow debug session.

        :param request: Data flow debug session definition.
        :type request: ~azure.synapse.artifacts.models.CreateDataFlowDebugSessionRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either CreateDataFlowDebugSessionResponse or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.CreateDataFlowDebugSessionResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.CreateDataFlowDebugSessionResponse"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_data_flow_debug_session_initial(request=request, cls=lambda x, y, z: x, **kwargs)

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("CreateDataFlowDebugSessionResponse", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_data_flow_debug_session.metadata = {"url": "/createDataFlowDebugSession"}  # type: ignore

    def query_data_flow_debug_sessions_by_workspace(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.QueryDataFlowDebugSessionsResponse"]
        """Query all active data flow debug sessions.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either QueryDataFlowDebugSessionsResponse or the result
         of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.synapse.artifacts.models.QueryDataFlowDebugSessionsResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.QueryDataFlowDebugSessionsResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = rest_data_flow_debug_session.build_query_data_flow_debug_sessions_by_workspace_request(
                    template_url=self.query_data_flow_debug_sessions_by_workspace.metadata["url"], **kwargs
                )._internal_request
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:

                request = rest_data_flow_debug_session.build_query_data_flow_debug_sessions_by_workspace_request(
                    template_url=self.query_data_flow_debug_sessions_by_workspace.metadata["url"], **kwargs
                )._internal_request
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                # little hacky, but this code will soon be replaced with code that won't need the hack
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.method = "GET"
                request.url = self._client.format_url(next_link, **path_format_arguments)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("QueryDataFlowDebugSessionsResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    query_data_flow_debug_sessions_by_workspace.metadata = {"url": "/queryDataFlowDebugSessions"}  # type: ignore

    def add_data_flow(
        self,
        request,  # type: "_models.DataFlowDebugPackage"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AddDataFlowToDebugSessionResponse"
        """Add a data flow into debug session.

        :param request: Data flow debug session definition with debug content.
        :type request: ~azure.synapse.artifacts.models.DataFlowDebugPackage
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AddDataFlowToDebugSessionResponse, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.AddDataFlowToDebugSessionResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.AddDataFlowToDebugSessionResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(request, "object")

        request = rest_data_flow_debug_session.build_add_data_flow_request(
            json=json, content_type=content_type, template_url=self.add_data_flow.metadata["url"], **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("AddDataFlowToDebugSessionResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    add_data_flow.metadata = {"url": "/addDataFlowToDebugSession"}  # type: ignore

    def delete_data_flow_debug_session(
        self,
        request,  # type: "_models.DeleteDataFlowDebugSessionRequest"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a data flow debug session.

        :param request: Data flow debug session definition for deletion.
        :type request: ~azure.synapse.artifacts.models.DeleteDataFlowDebugSessionRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(request, "object")

        request = rest_data_flow_debug_session.build_delete_data_flow_debug_session_request(
            json=json,
            content_type=content_type,
            template_url=self.delete_data_flow_debug_session.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_data_flow_debug_session.metadata = {"url": "/deleteDataFlowDebugSession"}  # type: ignore

    def _execute_command_initial(
        self,
        request,  # type: "_models.DataFlowDebugCommandRequest"
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.DataFlowDebugCommandResponse"]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.DataFlowDebugCommandResponse"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(request, "object")

        request = rest_data_flow_debug_session.build_execute_command_request_initial(
            json=json, content_type=content_type, template_url=self._execute_command_initial.metadata["url"], **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("DataFlowDebugCommandResponse", pipeline_response)

        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _execute_command_initial.metadata = {"url": "/executeDataFlowDebugCommand"}  # type: ignore

    def begin_execute_command(
        self,
        request,  # type: "_models.DataFlowDebugCommandRequest"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.DataFlowDebugCommandResponse"]
        """Execute a data flow debug command.

        :param request: Data flow debug command definition.
        :type request: ~azure.synapse.artifacts.models.DataFlowDebugCommandRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either DataFlowDebugCommandResponse or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.DataFlowDebugCommandResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DataFlowDebugCommandResponse"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._execute_command_initial(request=request, cls=lambda x, y, z: x, **kwargs)

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("DataFlowDebugCommandResponse", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_execute_command.metadata = {"url": "/executeDataFlowDebugCommand"}  # type: ignore
