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

from ._configuration import CloudCommunicationsConfiguration
from .operations import CommunicationCloudCommunicationOperations
from .operations import CommunicationOperations
from .operations import CommunicationCallRecordOperations
from .operations import CommunicationCallRecordSessionOperations
from .operations import CommunicationCallOperations
from .operations import CommunicationCallParticipantOperations
from .operations import CommunicationOnlineMeetingOperations
from .operations import UserOperations
from . import models


class CloudCommunications(object):
    """CloudCommunications.

    :ivar communication_cloud_communication: CommunicationCloudCommunicationOperations operations
    :vartype communication_cloud_communication: cloud_communications.operations.CommunicationCloudCommunicationOperations
    :ivar communication: CommunicationOperations operations
    :vartype communication: cloud_communications.operations.CommunicationOperations
    :ivar communication_call_record: CommunicationCallRecordOperations operations
    :vartype communication_call_record: cloud_communications.operations.CommunicationCallRecordOperations
    :ivar communication_call_record_session: CommunicationCallRecordSessionOperations operations
    :vartype communication_call_record_session: cloud_communications.operations.CommunicationCallRecordSessionOperations
    :ivar communication_call: CommunicationCallOperations operations
    :vartype communication_call: cloud_communications.operations.CommunicationCallOperations
    :ivar communication_call_participant: CommunicationCallParticipantOperations operations
    :vartype communication_call_participant: cloud_communications.operations.CommunicationCallParticipantOperations
    :ivar communication_online_meeting: CommunicationOnlineMeetingOperations operations
    :vartype communication_online_meeting: cloud_communications.operations.CommunicationOnlineMeetingOperations
    :ivar user: UserOperations operations
    :vartype user: cloud_communications.operations.UserOperations
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
            base_url = 'https://graph.microsoft.com/beta'
        self._config = CloudCommunicationsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.communication_cloud_communication = CommunicationCloudCommunicationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.communication = CommunicationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.communication_call_record = CommunicationCallRecordOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.communication_call_record_session = CommunicationCallRecordSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.communication_call = CommunicationCallOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.communication_call_participant = CommunicationCallParticipantOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.communication_online_meeting = CommunicationOnlineMeetingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> CloudCommunications
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
