# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DirectorySettingTemplateOperations:
    """DirectorySettingTemplateOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_directory_management.models
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

    async def check_member_group(
        self,
        directory_setting_template_id: str,
        group_ids: Optional[List[str]] = None,
        **kwargs
    ) -> List[str]:
        """Invoke action checkMemberGroups.

        Invoke action checkMemberGroups.

        :param directory_setting_template_id: key: id of directorySettingTemplate.
        :type directory_setting_template_id: str
        :param group_ids:
        :type group_ids: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.PathsMtp8GiDirectorysettingtemplatesDirectorysettingtemplateIdMicrosoftGraphCheckmembergroupsPostRequestbodyContentApplicationJsonSchema(group_ids=group_ids)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.check_member_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'directorySettingTemplate-id': self._serialize.url("directory_setting_template_id", directory_setting_template_id, 'str'),
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
        body_content = self._serialize.body(_body, 'PathsMtp8GiDirectorysettingtemplatesDirectorysettingtemplateIdMicrosoftGraphCheckmembergroupsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    check_member_group.metadata = {'url': '/directorySettingTemplates/{directorySettingTemplate-id}/microsoft.graph.checkMemberGroups'}  # type: ignore

    async def check_member_object(
        self,
        directory_setting_template_id: str,
        ids: Optional[List[str]] = None,
        **kwargs
    ) -> List[str]:
        """Invoke action checkMemberObjects.

        Invoke action checkMemberObjects.

        :param directory_setting_template_id: key: id of directorySettingTemplate.
        :type directory_setting_template_id: str
        :param ids:
        :type ids: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths1P1U1G2DirectorysettingtemplatesDirectorysettingtemplateIdMicrosoftGraphCheckmemberobjectsPostRequestbodyContentApplicationJsonSchema(ids=ids)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.check_member_object.metadata['url']  # type: ignore
        path_format_arguments = {
            'directorySettingTemplate-id': self._serialize.url("directory_setting_template_id", directory_setting_template_id, 'str'),
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
        body_content = self._serialize.body(_body, 'Paths1P1U1G2DirectorysettingtemplatesDirectorysettingtemplateIdMicrosoftGraphCheckmemberobjectsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    check_member_object.metadata = {'url': '/directorySettingTemplates/{directorySettingTemplate-id}/microsoft.graph.checkMemberObjects'}  # type: ignore

    async def get_member_group(
        self,
        directory_setting_template_id: str,
        security_enabled_only: Optional[bool] = False,
        **kwargs
    ) -> List[str]:
        """Invoke action getMemberGroups.

        Invoke action getMemberGroups.

        :param directory_setting_template_id: key: id of directorySettingTemplate.
        :type directory_setting_template_id: str
        :param security_enabled_only:
        :type security_enabled_only: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.PathsOliirpDirectorysettingtemplatesDirectorysettingtemplateIdMicrosoftGraphGetmembergroupsPostRequestbodyContentApplicationJsonSchema(security_enabled_only=security_enabled_only)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_member_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'directorySettingTemplate-id': self._serialize.url("directory_setting_template_id", directory_setting_template_id, 'str'),
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
        body_content = self._serialize.body(_body, 'PathsOliirpDirectorysettingtemplatesDirectorysettingtemplateIdMicrosoftGraphGetmembergroupsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_member_group.metadata = {'url': '/directorySettingTemplates/{directorySettingTemplate-id}/microsoft.graph.getMemberGroups'}  # type: ignore

    async def get_member_object(
        self,
        directory_setting_template_id: str,
        security_enabled_only: Optional[bool] = False,
        **kwargs
    ) -> List[str]:
        """Invoke action getMemberObjects.

        Invoke action getMemberObjects.

        :param directory_setting_template_id: key: id of directorySettingTemplate.
        :type directory_setting_template_id: str
        :param security_enabled_only:
        :type security_enabled_only: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths17Hg0B5DirectorysettingtemplatesDirectorysettingtemplateIdMicrosoftGraphGetmemberobjectsPostRequestbodyContentApplicationJsonSchema(security_enabled_only=security_enabled_only)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_member_object.metadata['url']  # type: ignore
        path_format_arguments = {
            'directorySettingTemplate-id': self._serialize.url("directory_setting_template_id", directory_setting_template_id, 'str'),
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
        body_content = self._serialize.body(_body, 'Paths17Hg0B5DirectorysettingtemplatesDirectorysettingtemplateIdMicrosoftGraphGetmemberobjectsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_member_object.metadata = {'url': '/directorySettingTemplates/{directorySettingTemplate-id}/microsoft.graph.getMemberObjects'}  # type: ignore

    async def restore(
        self,
        directory_setting_template_id: str,
        **kwargs
    ) -> "models.MicrosoftGraphDirectoryObject":
        """Invoke action restore.

        Invoke action restore.

        :param directory_setting_template_id: key: id of directorySettingTemplate.
        :type directory_setting_template_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphDirectoryObject, or the result of cls(response)
        :rtype: ~identity_directory_management.models.MicrosoftGraphDirectoryObject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphDirectoryObject"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.restore.metadata['url']  # type: ignore
        path_format_arguments = {
            'directorySettingTemplate-id': self._serialize.url("directory_setting_template_id", directory_setting_template_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphDirectoryObject', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    restore.metadata = {'url': '/directorySettingTemplates/{directorySettingTemplate-id}/microsoft.graph.restore'}  # type: ignore

    async def get_by_id(
        self,
        ids: Optional[List[str]] = None,
        types: Optional[List[str]] = None,
        **kwargs
    ) -> List["models.MicrosoftGraphDirectoryObject"]:
        """Invoke action getByIds.

        Invoke action getByIds.

        :param ids:
        :type ids: list[str]
        :param types:
        :type types: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphDirectoryObject, or the result of cls(response)
        :rtype: list[~identity_directory_management.models.MicrosoftGraphDirectoryObject]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphDirectoryObject"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths53Kc5ADirectorysettingtemplatesMicrosoftGraphGetbyidsPostRequestbodyContentApplicationJsonSchema(ids=ids, types=types)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_by_id.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths53Kc5ADirectorysettingtemplatesMicrosoftGraphGetbyidsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphDirectoryObject]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_by_id.metadata = {'url': '/directorySettingTemplates/microsoft.graph.getByIds'}  # type: ignore

    async def get_user_owned_object(
        self,
        user_id: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs
    ) -> "models.MicrosoftGraphDirectoryObject":
        """Invoke action getUserOwnedObjects.

        Invoke action getUserOwnedObjects.

        :param user_id:
        :type user_id: str
        :param type:
        :type type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphDirectoryObject, or the result of cls(response)
        :rtype: ~identity_directory_management.models.MicrosoftGraphDirectoryObject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphDirectoryObject"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths6Pdj1BDirectorysettingtemplatesMicrosoftGraphGetuserownedobjectsPostRequestbodyContentApplicationJsonSchema(user_id=user_id, type=type)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_user_owned_object.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths6Pdj1BDirectorysettingtemplatesMicrosoftGraphGetuserownedobjectsPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphDirectoryObject', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_user_owned_object.metadata = {'url': '/directorySettingTemplates/microsoft.graph.getUserOwnedObjects'}  # type: ignore

    async def validate_property(
        self,
        entity_type: Optional[str] = None,
        display_name: Optional[str] = None,
        mail_nickname: Optional[str] = None,
        on_behalf_of_user_id: Optional[str] = None,
        **kwargs
    ) -> None:
        """Invoke action validateProperties.

        Invoke action validateProperties.

        :param entity_type:
        :type entity_type: str
        :param display_name:
        :type display_name: str
        :param mail_nickname:
        :type mail_nickname: str
        :param on_behalf_of_user_id:
        :type on_behalf_of_user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.PathsO8B6ApDirectorysettingtemplatesMicrosoftGraphValidatepropertiesPostRequestbodyContentApplicationJsonSchema(entity_type=entity_type, display_name=display_name, mail_nickname=mail_nickname, on_behalf_of_user_id=on_behalf_of_user_id)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.validate_property.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'PathsO8B6ApDirectorysettingtemplatesMicrosoftGraphValidatepropertiesPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    validate_property.metadata = {'url': '/directorySettingTemplates/microsoft.graph.validateProperties'}  # type: ignore
