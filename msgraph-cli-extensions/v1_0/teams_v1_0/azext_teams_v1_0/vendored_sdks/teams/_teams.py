# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import TeamsConfiguration
from .operations import ChatChatOperations
from .operations import ChatOperations
from .operations import GroupOperations
from .operations import TeamTeamOperations
from .operations import TeamOperations
from .operations import TeamChannelOperations
from .operations import TeamChannelMessageOperations
from .operations import TeamChannelTabOperations
from .operations import TeamInstalledAppOperations
from .operations import TeamPrimaryChannelOperations
from .operations import TeamPrimaryChannelMessageOperations
from .operations import TeamPrimaryChannelTabOperations
from .operations import TeamScheduleOperations
from .operations import TeamworkTeamworkOperations
from .operations import TeamworkOperations
from .operations import UserOperations
from . import models


class Teams(object):
    """Teams.

    :ivar chat_chat: ChatChatOperations operations
    :vartype chat_chat: teams.operations.ChatChatOperations
    :ivar chat: ChatOperations operations
    :vartype chat: teams.operations.ChatOperations
    :ivar group: GroupOperations operations
    :vartype group: teams.operations.GroupOperations
    :ivar team_team: TeamTeamOperations operations
    :vartype team_team: teams.operations.TeamTeamOperations
    :ivar team: TeamOperations operations
    :vartype team: teams.operations.TeamOperations
    :ivar team_channel: TeamChannelOperations operations
    :vartype team_channel: teams.operations.TeamChannelOperations
    :ivar team_channel_message: TeamChannelMessageOperations operations
    :vartype team_channel_message: teams.operations.TeamChannelMessageOperations
    :ivar team_channel_tab: TeamChannelTabOperations operations
    :vartype team_channel_tab: teams.operations.TeamChannelTabOperations
    :ivar team_installed_app: TeamInstalledAppOperations operations
    :vartype team_installed_app: teams.operations.TeamInstalledAppOperations
    :ivar team_primary_channel: TeamPrimaryChannelOperations operations
    :vartype team_primary_channel: teams.operations.TeamPrimaryChannelOperations
    :ivar team_primary_channel_message: TeamPrimaryChannelMessageOperations operations
    :vartype team_primary_channel_message: teams.operations.TeamPrimaryChannelMessageOperations
    :ivar team_primary_channel_tab: TeamPrimaryChannelTabOperations operations
    :vartype team_primary_channel_tab: teams.operations.TeamPrimaryChannelTabOperations
    :ivar team_schedule: TeamScheduleOperations operations
    :vartype team_schedule: teams.operations.TeamScheduleOperations
    :ivar teamwork_teamwork: TeamworkTeamworkOperations operations
    :vartype teamwork_teamwork: teams.operations.TeamworkTeamworkOperations
    :ivar teamwork: TeamworkOperations operations
    :vartype teamwork: teams.operations.TeamworkOperations
    :ivar user: UserOperations operations
    :vartype user: teams.operations.UserOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param top: Show only the first n items.
    :type top: int
    :param skip: Skip the first n items.
    :type skip: int
    :param search: Search items by search phrases.
    :type search: str
    :param filter: Filter items by property values.
    :type filter: str
    :param count: Include count of items.
    :type count: bool
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        top=None,  # type: Optional[int]
        skip=None,  # type: Optional[int]
        search=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        count=None,  # type: Optional[bool]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = TeamsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.chat_chat = ChatChatOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chat = ChatOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group = GroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_team = TeamTeamOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team = TeamOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_channel = TeamChannelOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_channel_message = TeamChannelMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_channel_tab = TeamChannelTabOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_installed_app = TeamInstalledAppOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_primary_channel = TeamPrimaryChannelOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_primary_channel_message = TeamPrimaryChannelMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_primary_channel_tab = TeamPrimaryChannelTabOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_schedule = TeamScheduleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teamwork_teamwork = TeamworkTeamworkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teamwork = TeamworkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Teams
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)