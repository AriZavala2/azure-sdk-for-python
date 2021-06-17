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
from ...rest import workspace_git_repo_management as rest_workspace_git_repo_management

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class WorkspaceGitRepoManagementOperations:
    """WorkspaceGitRepoManagementOperations async operations.

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

    async def get_git_hub_access_token(
        self,
        git_hub_access_token_request: "_models.GitHubAccessTokenRequest",
        *,
        client_request_id: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.GitHubAccessTokenResponse":
        """Get the GitHub access token.

        :param git_hub_access_token_request:
        :type git_hub_access_token_request: ~azure.synapse.artifacts.models.GitHubAccessTokenRequest
        :keyword client_request_id: Can provide a guid, which is helpful for debugging and to provide
         better customer support.
        :paramtype client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GitHubAccessTokenResponse, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.GitHubAccessTokenResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.GitHubAccessTokenResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(git_hub_access_token_request, "object")

        request = rest_workspace_git_repo_management.build_get_git_hub_access_token_request(
            client_request_id=client_request_id,
            json=json,
            content_type=content_type,
            template_url=self.get_git_hub_access_token.metadata["url"],
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
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("GitHubAccessTokenResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_git_hub_access_token.metadata = {"url": "/getGitHubAccessToken"}  # type: ignore
