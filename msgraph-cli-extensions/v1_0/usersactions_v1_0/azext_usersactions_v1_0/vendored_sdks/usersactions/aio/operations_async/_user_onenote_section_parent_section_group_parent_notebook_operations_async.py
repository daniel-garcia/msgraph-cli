# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UserOnenoteSectionParentSectionGroupParentNotebookOperations:
    """UserOnenoteSectionParentSectionGroupParentNotebookOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_actions.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def copy_notebook(
        self,
        user_id: str,
        onenote_section_id: str,
        group_id: Optional[str] = None,
        rename_as: Optional[str] = None,
        notebook_folder: Optional[str] = None,
        site_collection_id: Optional[str] = None,
        site_id: Optional[str] = None,
        **kwargs
    ) -> "models.MicrosoftGraphOnenoteOperation":
        """Invoke action copyNotebook.

        Invoke action copyNotebook.

        :param user_id: key: id of user.
        :type user_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param group_id:
        :type group_id: str
        :param rename_as:
        :type rename_as: str
        :param notebook_folder:
        :type notebook_folder: str
        :param site_collection_id:
        :type site_collection_id: str
        :param site_id:
        :type site_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenoteOperation, or the result of cls(response)
        :rtype: ~users_actions.models.MicrosoftGraphOnenoteOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenoteOperation"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths1EnvxcpUsersUserIdOnenoteSectionsOnenotesectionIdParentsectiongroupParentnotebookMicrosoftGraphCopynotebookPostRequestbodyContentApplicationJsonSchema(group_id=group_id, rename_as=rename_as, notebook_folder=notebook_folder, site_collection_id=site_collection_id, site_id=site_id)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.copy_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths1EnvxcpUsersUserIdOnenoteSectionsOnenotesectionIdParentsectiongroupParentnotebookMicrosoftGraphCopynotebookPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnenoteOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    copy_notebook.metadata = {'url': '/users/{user-id}/onenote/sections/{onenoteSection-id}/parentSectionGroup/parentNotebook/microsoft.graph.copyNotebook'}  # type: ignore
