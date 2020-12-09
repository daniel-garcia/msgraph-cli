# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, IO, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ShareListItemActivityOperations:
    """ShareListItemActivityOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~files.models
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

    async def get_drive_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        select: Optional[List[Union[str, "models.Enum323"]]] = None,
        expand: Optional[List[Union[str, "models.Enum324"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphDriveItem":
        """Get driveItem from shares.

        Get driveItem from shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~files.models.Enum323]
        :param expand: Expand related entities.
        :type expand: list[str or ~files.models.Enum324]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphDriveItem, or the result of cls(response)
        :rtype: ~files.models.MicrosoftGraphDriveItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphDriveItem"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_drive_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphDriveItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_drive_item.metadata = {'url': '/shares/{sharedDriveItem-id}/listItem/activities/{itemActivityOLD-id}/driveItem'}  # type: ignore

    async def update_drive_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        body: "models.MicrosoftGraphDriveItem",
        **kwargs
    ) -> None:
        """Update the navigation property driveItem in shares.

        Update the navigation property driveItem in shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param body: New navigation property values.
        :type body: ~files.models.MicrosoftGraphDriveItem
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_drive_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphDriveItem')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_drive_item.metadata = {'url': '/shares/{sharedDriveItem-id}/listItem/activities/{itemActivityOLD-id}/driveItem'}  # type: ignore

    async def delete_drive_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property driveItem for shares.

        Delete navigation property driveItem for shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_drive_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_drive_item.metadata = {'url': '/shares/{sharedDriveItem-id}/listItem/activities/{itemActivityOLD-id}/driveItem'}  # type: ignore

    async def get_drive_item_content(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        **kwargs
    ) -> IO:
        """Get media content for the navigation property driveItem from shares.

        Get media content for the navigation property driveItem from shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/octet-stream, application/json"

        # Construct URL
        url = self.get_drive_item_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/octet-stream, application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_drive_item_content.metadata = {'url': '/shares/{sharedDriveItem-id}/listItem/activities/{itemActivityOLD-id}/driveItem/content'}  # type: ignore

    async def set_drive_item_content(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        data: IO,
        **kwargs
    ) -> None:
        """Update media content for the navigation property driveItem in shares.

        Update media content for the navigation property driveItem in shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param data: New media content.
        :type data: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/octet-stream")
        accept = "application/json"

        # Construct URL
        url = self.set_drive_item_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs['stream_content'] = data
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    set_drive_item_content.metadata = {'url': '/shares/{sharedDriveItem-id}/listItem/activities/{itemActivityOLD-id}/driveItem/content'}  # type: ignore

    async def get_list_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        select: Optional[List[Union[str, "models.Enum325"]]] = None,
        expand: Optional[List[Union[str, "models.Enum326"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphListItem":
        """Get listItem from shares.

        Get listItem from shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~files.models.Enum325]
        :param expand: Expand related entities.
        :type expand: list[str or ~files.models.Enum326]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphListItem, or the result of cls(response)
        :rtype: ~files.models.MicrosoftGraphListItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphListItem"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_list_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphListItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_list_item.metadata = {'url': '/shares/{sharedDriveItem-id}/listItem/activities/{itemActivityOLD-id}/listItem'}  # type: ignore

    async def update_list_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        id: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        description: Optional[str] = None,
        e_tag: Optional[str] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        name: Optional[str] = None,
        web_url: Optional[str] = None,
        created_by_user: Optional["models.MicrosoftGraphUser"] = None,
        last_modified_by_user: Optional["models.MicrosoftGraphUser"] = None,
        drive_id: Optional[str] = None,
        drive_type: Optional[str] = None,
        microsoft_graph_item_reference_id: Optional[str] = None,
        microsoft_graph_item_reference_name: Optional[str] = None,
        path: Optional[str] = None,
        share_id: Optional[str] = None,
        sharepoint_ids: Optional["models.MicrosoftGraphSharepointIds"] = None,
        site_id: Optional[str] = None,
        application: Optional["models.MicrosoftGraphIdentity"] = None,
        device: Optional["models.MicrosoftGraphIdentity"] = None,
        user: Optional["models.MicrosoftGraphIdentity"] = None,
        microsoft_graph_identity_application: Optional["models.MicrosoftGraphIdentity"] = None,
        microsoft_graph_identity_device: Optional["models.MicrosoftGraphIdentity"] = None,
        microsoft_graph_identity_user: Optional["models.MicrosoftGraphIdentity"] = None,
        content_type_parameter: Optional["models.MicrosoftGraphContentTypeInfo"] = None,
        microsoft_graph_sharepoint_ids: Optional["models.MicrosoftGraphSharepointIds"] = None,
        activities: Optional[List["models.MicrosoftGraphItemActivityOld"]] = None,
        analytics: Optional["models.MicrosoftGraphItemAnalytics"] = None,
        drive_item: Optional["models.MicrosoftGraphDriveItem"] = None,
        versions: Optional[List["models.MicrosoftGraphListItemVersion"]] = None,
        microsoft_graph_entity_id: Optional[str] = None,
        **kwargs
    ) -> None:
        """Update the navigation property listItem in shares.

        Update the navigation property listItem in shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param id: Read-only.
        :type id: str
        :param created_date_time: Date and time of item creation. Read-only.
        :type created_date_time: ~datetime.datetime
        :param description: Provides a user-visible description of the item. Optional.
        :type description: str
        :param e_tag: ETag for the item. Read-only.
        :type e_tag: str
        :param last_modified_date_time: Date and time the item was last modified. Read-only.
        :type last_modified_date_time: ~datetime.datetime
        :param name: The name of the item. Read-write.
        :type name: str
        :param web_url: URL that displays the resource in the browser. Read-only.
        :type web_url: str
        :param created_by_user: Represents an Azure Active Directory user object.
        :type created_by_user: ~files.models.MicrosoftGraphUser
        :param last_modified_by_user: Represents an Azure Active Directory user object.
        :type last_modified_by_user: ~files.models.MicrosoftGraphUser
        :param drive_id: Unique identifier of the drive instance that contains the item. Read-only.
        :type drive_id: str
        :param drive_type: Identifies the type of drive. See [drive][] resource for values.
        :type drive_type: str
        :param microsoft_graph_item_reference_id: Unique identifier of the item in the drive. Read-
         only.
        :type microsoft_graph_item_reference_id: str
        :param microsoft_graph_item_reference_name: The name of the item being referenced. Read-only.
        :type microsoft_graph_item_reference_name: str
        :param path: Path that can be used to navigate to the item. Read-only.
        :type path: str
        :param share_id: A unique identifier for a shared resource that can be accessed via the
         [Shares][] API.
        :type share_id: str
        :param sharepoint_ids: sharepointIds.
        :type sharepoint_ids: ~files.models.MicrosoftGraphSharepointIds
        :param site_id:
        :type site_id: str
        :param application: identity.
        :type application: ~files.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~files.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~files.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~files.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~files.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~files.models.MicrosoftGraphIdentity
        :param content_type_parameter: contentTypeInfo.
        :type content_type_parameter: ~files.models.MicrosoftGraphContentTypeInfo
        :param microsoft_graph_sharepoint_ids: sharepointIds.
        :type microsoft_graph_sharepoint_ids: ~files.models.MicrosoftGraphSharepointIds
        :param activities: The list of recent activities that took place on this item.
        :type activities: list[~files.models.MicrosoftGraphItemActivityOld]
        :param analytics: itemAnalytics.
        :type analytics: ~files.models.MicrosoftGraphItemAnalytics
        :param drive_item: driveItem.
        :type drive_item: ~files.models.MicrosoftGraphDriveItem
        :param versions: The list of previous versions of the list item.
        :type versions: list[~files.models.MicrosoftGraphListItemVersion]
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphListItem(id=id, created_date_time=created_date_time, description=description, e_tag=e_tag, last_modified_date_time=last_modified_date_time, name=name, web_url=web_url, created_by_user=created_by_user, last_modified_by_user=last_modified_by_user, drive_id=drive_id, drive_type=drive_type, id_parent_reference_id=microsoft_graph_item_reference_id, name_parent_reference_name=microsoft_graph_item_reference_name, path=path, share_id=share_id, sharepoint_ids=sharepoint_ids, site_id=site_id, application_last_modified_by_application=application, device_last_modified_by_device=device, user_last_modified_by_user=user, application_created_by_application=microsoft_graph_identity_application, device_created_by_device=microsoft_graph_identity_device, user_created_by_user=microsoft_graph_identity_user, content_type=content_type_parameter, sharepoint_ids=microsoft_graph_sharepoint_ids, activities=activities, analytics=analytics, drive_item=drive_item, versions=versions, id_fields_id=microsoft_graph_entity_id)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_list_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphListItem')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_list_item.metadata = {'url': '/shares/{sharedDriveItem-id}/listItem/activities/{itemActivityOLD-id}/listItem'}  # type: ignore

    async def delete_list_item(
        self,
        shared_drive_item_id: str,
        item_activity_old_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property listItem for shares.

        Delete navigation property listItem for shares.

        :param shared_drive_item_id: key: id of sharedDriveItem.
        :type shared_drive_item_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_list_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_list_item.metadata = {'url': '/shares/{sharedDriveItem-id}/listItem/activities/{itemActivityOLD-id}/listItem'}  # type: ignore
    accept = "application/json"

        # Construct URL
        url = self.delete_list_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'sharedDriveItem-id': self._serialize.url("shared_drive_item_id", shared_drive_item_id, 'str'),
            'listItem-id': self._serialize.url("list_item_id", list_item_id, 'str'),
            'itemActivityOLD-id': self._serialize.url("item_activity_old_id", item_activity_old_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_list_item.metadata = {'url': '/shares/{sharedDriveItem-id}/list/items/{listItem-id}/activities/{itemActivityOLD-id}/listItem'}  # type: ignore
