# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class GroupOperations:
    """GroupOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~teams.models
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

    async def get_team(
        self,
        group_id: str,
        select: Optional[List[Union[str, "models.Enum53"]]] = None,
        expand: Optional[List[Union[str, "models.Enum54"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphTeam":
        """Get team from groups.

        Get team from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~teams.models.Enum53]
        :param expand: Expand related entities.
        :type expand: list[str or ~teams.models.Enum54]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTeam, or the result of cls(response)
        :rtype: ~teams.models.MicrosoftGraphTeam
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTeam"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_team.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphTeam', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_team.metadata = {'url': '/groups/{group-id}/team'}  # type: ignore

    async def update_team(
        self,
        group_id: str,
        id: Optional[str] = None,
        classification: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        fun_settings: Optional["models.MicrosoftGraphTeamFunSettings"] = None,
        guest_settings: Optional["models.MicrosoftGraphTeamGuestSettings"] = None,
        internal_id: Optional[str] = None,
        is_archived: Optional[bool] = None,
        is_membership_limited_to_owners: Optional[bool] = None,
        member_settings: Optional["models.MicrosoftGraphTeamMemberSettings"] = None,
        messaging_settings: Optional["models.MicrosoftGraphTeamMessagingSettings"] = None,
        specialization: Optional[Union[str, "models.MicrosoftGraphTeamSpecialization"]] = None,
        visibility: Optional[Union[str, "models.MicrosoftGraphTeamVisibilityType"]] = None,
        web_url: Optional[str] = None,
        channels: Optional[List["models.MicrosoftGraphChannel"]] = None,
        group: Optional["models.MicrosoftGraphGroup"] = None,
        installed_apps: Optional[List["models.MicrosoftGraphTeamsAppInstallation"]] = None,
        members: Optional[List["models.MicrosoftGraphConversationMember"]] = None,
        operations: Optional[List["models.MicrosoftGraphTeamsAsyncOperation"]] = None,
        owners: Optional[List["models.MicrosoftGraphUser"]] = None,
        photo: Optional["models.MicrosoftGraphProfilePhoto"] = None,
        primary_channel: Optional["models.MicrosoftGraphChannel"] = None,
        microsoft_graph_entity_id: Optional[str] = None,
        id1: Optional[str] = None,
        enabled: Optional[bool] = None,
        offer_shift_requests_enabled: Optional[bool] = None,
        open_shifts_enabled: Optional[bool] = None,
        provision_status: Optional[Union[str, "models.MicrosoftGraphOperationStatus"]] = None,
        provision_status_code: Optional[str] = None,
        swap_shifts_requests_enabled: Optional[bool] = None,
        time_clock_enabled: Optional[bool] = None,
        time_off_requests_enabled: Optional[bool] = None,
        time_zone: Optional[str] = None,
        workforce_integration_ids: Optional[List[str]] = None,
        offer_shift_requests: Optional[List["models.MicrosoftGraphOfferShiftRequest"]] = None,
        open_shift_change_requests: Optional[List["models.MicrosoftGraphOpenShiftChangeRequest"]] = None,
        open_shifts: Optional[List["models.MicrosoftGraphOpenShift"]] = None,
        scheduling_groups: Optional[List["models.MicrosoftGraphSchedulingGroup"]] = None,
        shifts: Optional[List["models.MicrosoftGraphShift"]] = None,
        swap_shifts_change_requests: Optional[List["models.MicrosoftGraphSwapShiftsChangeRequest"]] = None,
        time_cards: Optional[List["models.MicrosoftGraphTimeCard"]] = None,
        time_off_reasons: Optional[List["models.MicrosoftGraphTimeOffReason"]] = None,
        time_off_requests: Optional[List["models.MicrosoftGraphTimeOffRequest"]] = None,
        times_off: Optional[List["models.MicrosoftGraphTimeOff"]] = None,
        approved_location: Optional["models.MicrosoftGraphGeoCoordinates"] = None,
        show_in_teams_search_and_suggestions: Optional[bool] = None,
        **kwargs
    ) -> None:
        """Update the navigation property team in groups.

        Update the navigation property team in groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param id: Read-only.
        :type id: str
        :param classification: An optional label. Typically describes the data or business sensitivity
         of the team. Must match one of a pre-configured set in the tenant's directory.
        :type classification: str
        :param created_date_time:
        :type created_date_time: ~datetime.datetime
        :param description: An optional description for the team.
        :type description: str
        :param display_name: The name of the team.
        :type display_name: str
        :param fun_settings: teamFunSettings.
        :type fun_settings: ~teams.models.MicrosoftGraphTeamFunSettings
        :param guest_settings: teamGuestSettings.
        :type guest_settings: ~teams.models.MicrosoftGraphTeamGuestSettings
        :param internal_id: A unique ID for the team that has been used in a few places such as the
         audit log/Office 365 Management Activity API.
        :type internal_id: str
        :param is_archived: Whether this team is in read-only mode.
        :type is_archived: bool
        :param is_membership_limited_to_owners:
        :type is_membership_limited_to_owners: bool
        :param member_settings: teamMemberSettings.
        :type member_settings: ~teams.models.MicrosoftGraphTeamMemberSettings
        :param messaging_settings: teamMessagingSettings.
        :type messaging_settings: ~teams.models.MicrosoftGraphTeamMessagingSettings
        :param specialization:
        :type specialization: str or ~teams.models.MicrosoftGraphTeamSpecialization
        :param visibility:
        :type visibility: str or ~teams.models.MicrosoftGraphTeamVisibilityType
        :param web_url: A hyperlink that will go to the team in the Microsoft Teams client. This is the
         URL that you get when you right-click a team in the Microsoft Teams client and select Get link
         to team. This URL should be treated as an opaque blob, and not parsed.
        :type web_url: str
        :param channels: The collection of channels & messages associated with the team.
        :type channels: list[~teams.models.MicrosoftGraphChannel]
        :param group: Represents an Azure Active Directory object. The directoryObject type is the base
         type for many other directory entity types.
        :type group: ~teams.models.MicrosoftGraphGroup
        :param installed_apps: The apps installed in this team.
        :type installed_apps: list[~teams.models.MicrosoftGraphTeamsAppInstallation]
        :param members: Members and owners of the team.
        :type members: list[~teams.models.MicrosoftGraphConversationMember]
        :param operations: The async operations that ran or are running on this team.
        :type operations: list[~teams.models.MicrosoftGraphTeamsAsyncOperation]
        :param owners:
        :type owners: list[~teams.models.MicrosoftGraphUser]
        :param photo: profilePhoto.
        :type photo: ~teams.models.MicrosoftGraphProfilePhoto
        :param primary_channel: channel.
        :type primary_channel: ~teams.models.MicrosoftGraphChannel
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param id1: Read-only.
        :type id1: str
        :param enabled: Indicates whether the schedule is enabled for the team. Required.
        :type enabled: bool
        :param offer_shift_requests_enabled: Indicates whether offer shift requests are enabled for the
         schedule.
        :type offer_shift_requests_enabled: bool
        :param open_shifts_enabled: Indicates whether open shifts are enabled for the schedule.
        :type open_shifts_enabled: bool
        :param provision_status:
        :type provision_status: str or ~teams.models.MicrosoftGraphOperationStatus
        :param provision_status_code: Additional information about why schedule provisioning failed.
        :type provision_status_code: str
        :param swap_shifts_requests_enabled: Indicates whether swap shifts requests are enabled for the
         schedule.
        :type swap_shifts_requests_enabled: bool
        :param time_clock_enabled: Indicates whether time clock is enabled for the schedule.
        :type time_clock_enabled: bool
        :param time_off_requests_enabled: Indicates whether time off requests are enabled for the
         schedule.
        :type time_off_requests_enabled: bool
        :param time_zone: Indicates the time zone of the schedule team using tz database format.
         Required.
        :type time_zone: str
        :param workforce_integration_ids:
        :type workforce_integration_ids: list[str]
        :param offer_shift_requests:
        :type offer_shift_requests: list[~teams.models.MicrosoftGraphOfferShiftRequest]
        :param open_shift_change_requests:
        :type open_shift_change_requests: list[~teams.models.MicrosoftGraphOpenShiftChangeRequest]
        :param open_shifts:
        :type open_shifts: list[~teams.models.MicrosoftGraphOpenShift]
        :param scheduling_groups: The logical grouping of users in the schedule (usually by role).
        :type scheduling_groups: list[~teams.models.MicrosoftGraphSchedulingGroup]
        :param shifts: The shifts in the schedule.
        :type shifts: list[~teams.models.MicrosoftGraphShift]
        :param swap_shifts_change_requests:
        :type swap_shifts_change_requests: list[~teams.models.MicrosoftGraphSwapShiftsChangeRequest]
        :param time_cards:
        :type time_cards: list[~teams.models.MicrosoftGraphTimeCard]
        :param time_off_reasons: The set of reasons for a time off in the schedule.
        :type time_off_reasons: list[~teams.models.MicrosoftGraphTimeOffReason]
        :param time_off_requests:
        :type time_off_requests: list[~teams.models.MicrosoftGraphTimeOffRequest]
        :param times_off: The instances of times off in the schedule.
        :type times_off: list[~teams.models.MicrosoftGraphTimeOff]
        :param approved_location: geoCoordinates.
        :type approved_location: ~teams.models.MicrosoftGraphGeoCoordinates
        :param show_in_teams_search_and_suggestions:
        :type show_in_teams_search_and_suggestions: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphTeam(id=id, classification=classification, created_date_time=created_date_time, description=description, display_name=display_name, fun_settings=fun_settings, guest_settings=guest_settings, internal_id=internal_id, is_archived=is_archived, is_membership_limited_to_owners=is_membership_limited_to_owners, member_settings=member_settings, messaging_settings=messaging_settings, specialization=specialization, visibility=visibility, web_url=web_url, channels=channels, group=group, installed_apps=installed_apps, members=members, operations=operations, owners=owners, photo=photo, primary_channel=primary_channel, id_template_id=microsoft_graph_entity_id, id_schedule_id=id1, enabled=enabled, offer_shift_requests_enabled=offer_shift_requests_enabled, open_shifts_enabled=open_shifts_enabled, provision_status=provision_status, provision_status_code=provision_status_code, swap_shifts_requests_enabled=swap_shifts_requests_enabled, time_clock_enabled=time_clock_enabled, time_off_requests_enabled=time_off_requests_enabled, time_zone=time_zone, workforce_integration_ids=workforce_integration_ids, offer_shift_requests=offer_shift_requests, open_shift_change_requests=open_shift_change_requests, open_shifts=open_shifts, scheduling_groups=scheduling_groups, shifts=shifts, swap_shifts_change_requests=swap_shifts_change_requests, time_cards=time_cards, time_off_reasons=time_off_reasons, time_off_requests=time_off_requests, times_off=times_off, approved_location=approved_location, show_in_teams_search_and_suggestions=show_in_teams_search_and_suggestions)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_team.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphTeam')
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

    update_team.metadata = {'url': '/groups/{group-id}/team'}  # type: ignore

    async def delete_team(
        self,
        group_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property team for groups.

        Delete navigation property team for groups.

        :param group_id: key: id of group.
        :type group_id: str
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
        url = self.delete_team.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
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

    delete_team.metadata = {'url': '/groups/{group-id}/team'}  # type: ignore
