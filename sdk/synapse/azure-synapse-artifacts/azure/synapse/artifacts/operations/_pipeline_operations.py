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
from ..rest import pipeline as rest_pipeline

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class PipelineOperations(object):
    """PipelineOperations operations.

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

    def get_pipelines_by_workspace(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.PipelineListResponse"]
        """Lists pipelines.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PipelineListResponse or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.synapse.artifacts.models.PipelineListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PipelineListResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = rest_pipeline.build_get_pipelines_by_workspace_request(
                    template_url=self.get_pipelines_by_workspace.metadata["url"], **kwargs
                )._internal_request
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:

                request = rest_pipeline.build_get_pipelines_by_workspace_request(
                    template_url=self.get_pipelines_by_workspace.metadata["url"], **kwargs
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
            deserialized = self._deserialize("PipelineListResponse", pipeline_response)
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

    get_pipelines_by_workspace.metadata = {"url": "/pipelines"}  # type: ignore

    def _create_or_update_pipeline_initial(
        self,
        pipeline_name,  # type: str
        pipeline,  # type: "_models.PipelineResource"
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.PipelineResource"]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.PipelineResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        if_match = kwargs.pop("if_match", None)  # type: Optional[str]

        json = self._serialize.body(pipeline, "object")

        request = rest_pipeline.build_create_or_update_pipeline_request_initial(
            pipeline_name=pipeline_name,
            if_match=if_match,
            json=json,
            content_type=content_type,
            template_url=self._create_or_update_pipeline_initial.metadata["url"],
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
        if response.status_code == 200:
            deserialized = self._deserialize("PipelineResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_pipeline_initial.metadata = {"url": "/pipelines/{pipelineName}"}  # type: ignore

    def begin_create_or_update_pipeline(
        self,
        pipeline_name,  # type: str
        pipeline,  # type: "_models.PipelineResource"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.PipelineResource"]
        """Creates or updates a pipeline.

        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :param pipeline: Pipeline resource definition.
        :type pipeline: ~azure.synapse.artifacts.models.PipelineResource
        :keyword if_match: ETag of the pipeline entity.  Should only be specified for update, for which
         it should match existing entity or can be * for unconditional update.
        :paramtype if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either PipelineResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.PipelineResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PipelineResource"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_pipeline_initial(
                pipeline_name=pipeline_name, pipeline=pipeline, cls=lambda x, y, z: x, **kwargs
            )

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        if_match = kwargs.pop("if_match", None)  # type: Optional[str]

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("PipelineResource", pipeline_response)

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

    begin_create_or_update_pipeline.metadata = {"url": "/pipelines/{pipelineName}"}  # type: ignore

    def get_pipeline(
        self,
        pipeline_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.PipelineResource"]
        """Gets a pipeline.

        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :keyword if_none_match: ETag of the pipeline entity. Should only be specified for get. If the
         ETag matches the existing entity tag, or if * was provided, then no content will be returned.
        :paramtype if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PipelineResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.PipelineResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.PipelineResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        if_none_match = kwargs.pop("if_none_match", None)  # type: Optional[str]
        request = rest_pipeline.build_get_pipeline_request(
            pipeline_name=pipeline_name,
            if_none_match=if_none_match,
            template_url=self.get_pipeline.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("PipelineResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_pipeline.metadata = {"url": "/pipelines/{pipelineName}"}  # type: ignore

    def _delete_pipeline_initial(
        self,
        pipeline_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_pipeline.build_delete_pipeline_request_initial(
            pipeline_name=pipeline_name, template_url=self._delete_pipeline_initial.metadata["url"], **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_pipeline_initial.metadata = {"url": "/pipelines/{pipelineName}"}  # type: ignore

    def begin_delete_pipeline(
        self,
        pipeline_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Deletes a pipeline.

        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_pipeline_initial(pipeline_name=pipeline_name, cls=lambda x, y, z: x, **kwargs)

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

    begin_delete_pipeline.metadata = {"url": "/pipelines/{pipelineName}"}  # type: ignore

    def _rename_pipeline_initial(
        self,
        pipeline_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        new_name = kwargs.pop("new_name", None)  # type: Optional[str]

        _request = _models.ArtifactRenameRequest(new_name=new_name)
        json = self._serialize.body(_request, "object")

        request = rest_pipeline.build_rename_pipeline_request_initial(
            pipeline_name=pipeline_name,
            json=json,
            content_type=content_type,
            template_url=self._rename_pipeline_initial.metadata["url"],
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

        if cls:
            return cls(pipeline_response, None, {})

    _rename_pipeline_initial.metadata = {"url": "/pipelines/{pipelineName}/rename"}  # type: ignore

    def begin_rename_pipeline(
        self,
        pipeline_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Renames a pipeline.

        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :keyword new_name: New name of the artifact.
        :paramtype new_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._rename_pipeline_initial(pipeline_name=pipeline_name, cls=lambda x, y, z: x, **kwargs)

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        new_name = kwargs.pop("new_name", None)  # type: Optional[str]

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if cls:
                return cls(pipeline_response, None, {})

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

    begin_rename_pipeline.metadata = {"url": "/pipelines/{pipelineName}/rename"}  # type: ignore

    def create_pipeline_run(
        self,
        pipeline_name,  # type: str
        parameters=None,  # type: Optional[Dict[str, object]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.CreateRunResponse"
        """Creates a run of a pipeline.

        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :keyword reference_pipeline_run_id: The pipeline run identifier. If run ID is specified the
         parameters of the specified run will be used to create a new run.
        :paramtype reference_pipeline_run_id: str
        :keyword is_recovery: Recovery mode flag. If recovery mode is set to true, the specified
         referenced pipeline run and the new run will be grouped under the same groupId.
        :paramtype is_recovery: bool
        :keyword start_activity_name: In recovery mode, the rerun will start from this activity. If not
         specified, all activities will run.
        :paramtype start_activity_name: str
        :param parameters: Parameters of the pipeline run. These parameters will be used only if the
         runId is not specified.
        :type parameters: dict[str, object]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CreateRunResponse, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.CreateRunResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.CreateRunResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        reference_pipeline_run_id = kwargs.pop("reference_pipeline_run_id", None)  # type: Optional[str]
        is_recovery = kwargs.pop("is_recovery", None)  # type: Optional[bool]
        start_activity_name = kwargs.pop("start_activity_name", None)  # type: Optional[str]

        if parameters is not None:
            json = self._serialize.body(parameters, "object")
        else:
            parameters = None

        request = rest_pipeline.build_create_pipeline_run_request(
            pipeline_name=pipeline_name,
            reference_pipeline_run_id=reference_pipeline_run_id,
            is_recovery=is_recovery,
            start_activity_name=start_activity_name,
            json=json,
            content_type=content_type,
            template_url=self.create_pipeline_run.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("CreateRunResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_pipeline_run.metadata = {"url": "/pipelines/{pipelineName}/createRun"}  # type: ignore
