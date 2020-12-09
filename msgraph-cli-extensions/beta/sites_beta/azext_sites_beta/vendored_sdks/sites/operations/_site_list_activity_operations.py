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

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, IO, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SiteListActivityOperations(object):
    """SiteListActivityOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~sites.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_drive_item(
        self,
        site_id,  # type: str
        list_id,  # type: str
        item_activity_old_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum159"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum160"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphDriveItem"
        """Get driveItem from sites.

        Get driveItem from sites.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~sites.models.Enum159]
        :param expand: Expand related entities.
        :type expand: list[str or ~sites.models.Enum160]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphDriveItem, or the result of cls(response)
        :rtype: ~sites.models.MicrosoftGraphDriveItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphDriveItem"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_drive_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphDriveItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_drive_item.metadata = {'url': '/sites/{site-id}/lists/{list-id}/activities/{itemActivityOLD-id}/driveItem'}  # type: ignore

    def update_drive_item(
        self,
        site_id,  # type: str
        list_id,  # type: str
        item_activity_old_id,  # type: str
        body,  # type: "models.MicrosoftGraphDriveItem"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property driveItem in sites.

        Update the navigation property driveItem in sites.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param body: New navigation property values.
        :type body: ~sites.models.MicrosoftGraphDriveItem
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
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_drive_item.metadata = {'url': '/sites/{site-id}/lists/{list-id}/activities/{itemActivityOLD-id}/driveItem'}  # type: ignore

    def delete_drive_item(
        self,
        site_id,  # type: str
        list_id,  # type: str
        item_activity_old_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property driveItem for sites.

        Delete navigation property driveItem for sites.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
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
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_drive_item.metadata = {'url': '/sites/{site-id}/lists/{list-id}/activities/{itemActivityOLD-id}/driveItem'}  # type: ignore

    def get_drive_item_content(
        self,
        site_id,  # type: str
        list_id,  # type: str
        item_activity_old_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Get media content for the navigation property driveItem from sites.

        Get media content for the navigation property driveItem from sites.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
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
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_drive_item_content.metadata = {'url': '/sites/{site-id}/lists/{list-id}/activities/{itemActivityOLD-id}/driveItem/content'}  # type: ignore

    def set_drive_item_content(
        self,
        site_id,  # type: str
        list_id,  # type: str
        item_activity_old_id,  # type: str
        data,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update media content for the navigation property driveItem in sites.

        Update media content for the navigation property driveItem in sites.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
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
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    set_drive_item_content.metadata = {'url': '/sites/{site-id}/lists/{list-id}/activities/{itemActivityOLD-id}/driveItem/content'}  # type: ignore

    def get_list_item(
        self,
        site_id,  # type: str
        list_id,  # type: str
        item_activity_old_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum161"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum162"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphListItem"
        """Get listItem from sites.

        Get listItem from sites.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
        :param item_activity_old_id: key: id of itemActivityOLD.
        :type item_activity_old_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~sites.models.Enum161]
        :param expand: Expand related entities.
        :type expand: list[str or ~sites.models.Enum162]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphListItem, or the result of cls(response)
        :rtype: ~sites.models.MicrosoftGraphListItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphListItem"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_list_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphListItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_list_item.metadata = {'url': '/sites/{site-id}/lists/{list-id}/activities/{itemActivityOLD-id}/listItem'}  # type: ignore

    def update_list_item(
        self,
        site_id,  # type: str
        list_id,  # type: str
        item_activity_old_id,  # type: str
        id=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        description=None,  # type: Optional[str]
        e_tag=None,  # type: Optional[str]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        name=None,  # type: Optional[str]
        web_url=None,  # type: Optional[str]
        created_by_user=None,  # type: Optional["models.MicrosoftGraphUser"]
        last_modified_by_user=None,  # type: Optional["models.MicrosoftGraphUser"]
        drive_id=None,  # type: Optional[str]
        drive_type=None,  # type: Optional[str]
        microsoft_graph_item_reference_id=None,  # type: Optional[str]
        microsoft_graph_item_reference_name=None,  # type: Optional[str]
        path=None,  # type: Optional[str]
        share_id=None,  # type: Optional[str]
        sharepoint_ids=None,  # type: Optional["models.MicrosoftGraphSharepointIds"]
        microsoft_graph_item_reference_site_id=None,  # type: Optional[str]
        application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        content_type_parameter=None,  # type: Optional["models.MicrosoftGraphContentTypeInfo"]
        microsoft_graph_sharepoint_ids=None,  # type: Optional["models.MicrosoftGraphSharepointIds"]
        activities=None,  # type: Optional[List["models.MicrosoftGraphItemActivityOld"]]
        analytics=None,  # type: Optional["models.MicrosoftGraphItemAnalytics"]
        drive_item=None,  # type: Optional["models.MicrosoftGraphDriveItem"]
        versions=None,  # type: Optional[List["models.MicrosoftGraphListItemVersion"]]
        microsoft_graph_entity_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property listItem in sites.

        Update the navigation property listItem in sites.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
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
        :type created_by_user: ~sites.models.MicrosoftGraphUser
        :param last_modified_by_user: Represents an Azure Active Directory user object.
        :type last_modified_by_user: ~sites.models.MicrosoftGraphUser
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
        :type sharepoint_ids: ~sites.models.MicrosoftGraphSharepointIds
        :param microsoft_graph_item_reference_site_id:
        :type microsoft_graph_item_reference_site_id: str
        :param application: identity.
        :type application: ~sites.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~sites.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~sites.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~sites.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~sites.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~sites.models.MicrosoftGraphIdentity
        :param content_type_parameter: contentTypeInfo.
        :type content_type_parameter: ~sites.models.MicrosoftGraphContentTypeInfo
        :param microsoft_graph_sharepoint_ids: sharepointIds.
        :type microsoft_graph_sharepoint_ids: ~sites.models.MicrosoftGraphSharepointIds
        :param activities: The list of recent activities that took place on this item.
        :type activities: list[~sites.models.MicrosoftGraphItemActivityOld]
        :param analytics: itemAnalytics.
        :type analytics: ~sites.models.MicrosoftGraphItemAnalytics
        :param drive_item: driveItem.
        :type drive_item: ~sites.models.MicrosoftGraphDriveItem
        :param versions: The list of previous versions of the list item.
        :type versions: list[~sites.models.MicrosoftGraphListItemVersion]
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

        _body = models.MicrosoftGraphListItem(id=id, created_date_time=created_date_time, description=description, e_tag=e_tag, last_modified_date_time=last_modified_date_time, name=name, web_url=web_url, created_by_user=created_by_user, last_modified_by_user=last_modified_by_user, drive_id=drive_id, drive_type=drive_type, id_parent_reference_id=microsoft_graph_item_reference_id, name_parent_reference_name=microsoft_graph_item_reference_name, path=path, share_id=share_id, sharepoint_ids=sharepoint_ids, site_id=microsoft_graph_item_reference_site_id, application_last_modified_by_application=application, device_last_modified_by_device=device, user_last_modified_by_user=user, application_created_by_application=microsoft_graph_identity_application, device_created_by_device=microsoft_graph_identity_device, user_created_by_user=microsoft_graph_identity_user, content_type=content_type_parameter, sharepoint_ids=microsoft_graph_sharepoint_ids, activities=activities, analytics=analytics, drive_item=drive_item, versions=versions, id_fields_id=microsoft_graph_entity_id)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_list_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_list_item.metadata = {'url': '/sites/{site-id}/lists/{list-id}/activities/{itemActivityOLD-id}/listItem'}  # type: ignore

    def delete_list_item(
        self,
        site_id,  # type: str
        list_id,  # type: str
        item_activity_old_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property listItem for sites.

        Delete navigation property listItem for sites.

        :param site_id: key: id of site.
        :type site_id: str
        :param list_id: key: id of list.
        :type list_id: str
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
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'list-id': self._serialize.url("list_id", list_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_list_item.metadata = {'url': '/sites/{site-id}/lists/{list-id}/activities/{itemActivityOLD-id}/listItem'}  # type: ignore
