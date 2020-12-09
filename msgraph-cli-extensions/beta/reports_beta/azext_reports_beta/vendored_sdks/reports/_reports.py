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

from ._configuration import ReportsConfiguration
from .operations import AuditLogAuditLogRootOperations
from .operations import AuditLogOperations
from .operations import ReportReportRootOperations
from .operations import ReportOperations
from . import models


class Reports(object):
    """Reports.

    :ivar audit_log_audit_log_root: AuditLogAuditLogRootOperations operations
    :vartype audit_log_audit_log_root: reports.operations.AuditLogAuditLogRootOperations
    :ivar audit_log: AuditLogOperations operations
    :vartype audit_log: reports.operations.AuditLogOperations
    :ivar report_report_root: ReportReportRootOperations operations
    :vartype report_report_root: reports.operations.ReportReportRootOperations
    :ivar report: ReportOperations operations
    :vartype report: reports.operations.ReportOperations
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
        self._config = ReportsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.audit_log_audit_log_root = AuditLogAuditLogRootOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.audit_log = AuditLogOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.report_report_root = ReportReportRootOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.report = ReportOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Reports
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
