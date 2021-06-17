# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.synapse.artifacts.core.rest import HttpRequest

from ... import models as _models
from ...rest import sql_script as rest_sql_script

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SqlScriptOperations:
    """SqlScriptOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_sql_scripts_by_workspace(self, **kwargs: Any) -> AsyncIterable["_models.SqlScriptsListResponse"]:
        """Lists sql scripts.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SqlScriptsListResponse or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.synapse.artifacts.models.SqlScriptsListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SqlScriptsListResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = rest_sql_script.build_get_sql_scripts_by_workspace_request(
                    template_url=self.get_sql_scripts_by_workspace.metadata["url"], **kwargs
                )._internal_request
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:

                request = rest_sql_script.build_get_sql_scripts_by_workspace_request(
                    template_url=self.get_sql_scripts_by_workspace.metadata["url"], **kwargs
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SqlScriptsListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    get_sql_scripts_by_workspace.metadata = {"url": "/sqlScripts"}  # type: ignore

    async def _create_or_update_sql_script_initial(
        self,
        sql_script_name: str,
        sql_script: "_models.SqlScriptResource",
        *,
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> Optional["_models.SqlScriptResource"]:
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.SqlScriptResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(sql_script, "object")

        request = rest_sql_script.build_create_or_update_sql_script_request_initial(
            sql_script_name=sql_script_name,
            if_match=if_match,
            json=json,
            content_type=content_type,
            template_url=self._create_or_update_sql_script_initial.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("SqlScriptResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_sql_script_initial.metadata = {"url": "/sqlScripts/{sqlScriptName}"}  # type: ignore

    async def begin_create_or_update_sql_script(
        self,
        sql_script_name: str,
        sql_script: "_models.SqlScriptResource",
        *,
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncLROPoller["_models.SqlScriptResource"]:
        """Creates or updates a Sql Script.

        :param sql_script_name: The sql script name.
        :type sql_script_name: str
        :param sql_script: Sql Script resource definition.
        :type sql_script: ~azure.synapse.artifacts.models.SqlScriptResource
        :keyword if_match: ETag of the SQL script entity.  Should only be specified for update, for
         which it should match existing entity or can be * for unconditional update.
        :paramtype if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either SqlScriptResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.SqlScriptResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SqlScriptResource"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_sql_script_initial(
                sql_script_name=sql_script_name,
                sql_script=sql_script,
                if_match=if_match,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("SqlScriptResource", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update_sql_script.metadata = {"url": "/sqlScripts/{sqlScriptName}"}  # type: ignore

    async def get_sql_script(
        self, sql_script_name: str, *, if_none_match: Optional[str] = None, **kwargs: Any
    ) -> Optional["_models.SqlScriptResource"]:
        """Gets a sql script.

        :param sql_script_name: The sql script name.
        :type sql_script_name: str
        :keyword if_none_match: ETag of the sql compute entity. Should only be specified for get. If
         the ETag matches the existing entity tag, or if * was provided, then no content will be
         returned.
        :paramtype if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SqlScriptResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.SqlScriptResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.SqlScriptResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_sql_script.build_get_sql_script_request(
            sql_script_name=sql_script_name,
            if_none_match=if_none_match,
            template_url=self.get_sql_script.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("SqlScriptResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_sql_script.metadata = {"url": "/sqlScripts/{sqlScriptName}"}  # type: ignore

    async def _delete_sql_script_initial(self, sql_script_name: str, **kwargs: Any) -> None:
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_sql_script.build_delete_sql_script_request_initial(
            sql_script_name=sql_script_name, template_url=self._delete_sql_script_initial.metadata["url"], **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_sql_script_initial.metadata = {"url": "/sqlScripts/{sqlScriptName}"}  # type: ignore

    async def begin_delete_sql_script(self, sql_script_name: str, **kwargs: Any) -> AsyncLROPoller[None]:
        """Deletes a Sql Script.

        :param sql_script_name: The sql script name.
        :type sql_script_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_sql_script_initial(
                sql_script_name=sql_script_name, cls=lambda x, y, z: x, **kwargs
            )

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if cls:
                return cls(pipeline_response, None, {})

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete_sql_script.metadata = {"url": "/sqlScripts/{sqlScriptName}"}  # type: ignore

    async def _rename_sql_script_initial(
        self, sql_script_name: str, *, new_name: Optional[str] = None, **kwargs: Any
    ) -> None:
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _request = _models.ArtifactRenameRequest(new_name=new_name)
        json = self._serialize.body(_request, "object")

        request = rest_sql_script.build_rename_sql_script_request_initial(
            sql_script_name=sql_script_name,
            json=json,
            content_type=content_type,
            template_url=self._rename_sql_script_initial.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _rename_sql_script_initial.metadata = {"url": "/sqlScripts/{sqlScriptName}/rename"}  # type: ignore

    async def begin_rename_sql_script(
        self, sql_script_name: str, *, new_name: Optional[str] = None, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Renames a sqlScript.

        :param sql_script_name: The sql script name.
        :type sql_script_name: str
        :keyword new_name: New name of the artifact.
        :paramtype new_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._rename_sql_script_initial(
                sql_script_name=sql_script_name, new_name=new_name, cls=lambda x, y, z: x, **kwargs
            )

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if cls:
                return cls(pipeline_response, None, {})

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_rename_sql_script.metadata = {"url": "/sqlScripts/{sqlScriptName}/rename"}  # type: ignore
