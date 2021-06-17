# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.synapse.artifacts.core.rest import HttpRequest

from ... import models as _models
from ...rest import trigger_run as rest_trigger_run

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class TriggerRunOperations:
    """TriggerRunOperations async operations.

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

    async def rerun_trigger_instance(self, trigger_name: str, run_id: str, **kwargs: Any) -> None:
        """Rerun single trigger instance by runId.

        :param trigger_name: The trigger name.
        :type trigger_name: str
        :param run_id: The pipeline run identifier.
        :type run_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_trigger_run.build_rerun_trigger_instance_request(
            trigger_name=trigger_name, run_id=run_id, template_url=self.rerun_trigger_instance.metadata["url"], **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    rerun_trigger_instance.metadata = {"url": "/triggers/{triggerName}/triggerRuns/{runId}/rerun"}  # type: ignore

    async def cancel_trigger_instance(self, trigger_name: str, run_id: str, **kwargs: Any) -> None:
        """Cancel single trigger instance by runId.

        :param trigger_name: The trigger name.
        :type trigger_name: str
        :param run_id: The pipeline run identifier.
        :type run_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_trigger_run.build_cancel_trigger_instance_request(
            trigger_name=trigger_name,
            run_id=run_id,
            template_url=self.cancel_trigger_instance.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    cancel_trigger_instance.metadata = {"url": "/triggers/{triggerName}/triggerRuns/{runId}/cancel"}  # type: ignore

    async def query_trigger_runs_by_workspace(
        self, filter_parameters: "_models.RunFilterParameters", **kwargs: Any
    ) -> "_models.TriggerRunsQueryResponse":
        """Query trigger runs.

        :param filter_parameters: Parameters to filter the pipeline run.
        :type filter_parameters: ~azure.synapse.artifacts.models.RunFilterParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerRunsQueryResponse, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.TriggerRunsQueryResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.TriggerRunsQueryResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(filter_parameters, "object")

        request = rest_trigger_run.build_query_trigger_runs_by_workspace_request(
            json=json,
            content_type=content_type,
            template_url=self.query_trigger_runs_by_workspace.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("TriggerRunsQueryResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query_trigger_runs_by_workspace.metadata = {"url": "/queryTriggerRuns"}  # type: ignore
