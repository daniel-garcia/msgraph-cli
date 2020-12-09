# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import UsersFunctionsConfiguration
from .operations_async import UserActivityOperations
from .operations_async import UserCalendarCalendarViewCalendarOperations
from .operations_async import UserCalendarCalendarViewExceptionOccurrenceOperations
from .operations_async import UserCalendarCalendarViewInstanceOperations
from .operations_async import UserCalendarCalendarViewOperations
from .operations_async import UserCalendarEventCalendarOperations
from .operations_async import UserCalendarEventExceptionOccurrenceOperations
from .operations_async import UserCalendarEventInstanceOperations
from .operations_async import UserCalendarEventOperations
from .operations_async import UserCalendarOperations
from .operations_async import UserCalendarGroupCalendarCalendarViewCalendarOperations
from .operations_async import UserCalendarGroupCalendarCalendarViewExceptionOccurrenceOperations
from .operations_async import UserCalendarGroupCalendarCalendarViewInstanceOperations
from .operations_async import UserCalendarGroupCalendarCalendarViewOperations
from .operations_async import UserCalendarGroupCalendarEventCalendarOperations
from .operations_async import UserCalendarGroupCalendarEventExceptionOccurrenceOperations
from .operations_async import UserCalendarGroupCalendarEventInstanceOperations
from .operations_async import UserCalendarGroupCalendarEventOperations
from .operations_async import UserCalendarGroupCalendarOperations
from .operations_async import UserCalendarCalendarViewCalendarOperations
from .operations_async import UserCalendarCalendarViewExceptionOccurrenceOperations
from .operations_async import UserCalendarCalendarViewInstanceOperations
from .operations_async import UserCalendarCalendarViewOperations
from .operations_async import UserCalendarEventCalendarOperations
from .operations_async import UserCalendarEventExceptionOccurrenceOperations
from .operations_async import UserCalendarEventInstanceOperations
from .operations_async import UserCalendarEventOperations
from .operations_async import UserCalendarOperations
from .operations_async import UserCalendarViewCalendarCalendarViewOperations
from .operations_async import UserCalendarViewCalendarEventOperations
from .operations_async import UserCalendarViewCalendarOperations
from .operations_async import UserCalendarViewExceptionOccurrenceOperations
from .operations_async import UserCalendarViewInstanceOperations
from .operations_async import UserCalendarViewOperations
from .operations_async import UserContactFolderChildFolderOperations
from .operations_async import UserContactFolderContactOperations
from .operations_async import UserContactFolderOperations
from .operations_async import UserContactOperations
from .operations_async import UserEventCalendarCalendarViewOperations
from .operations_async import UserEventCalendarEventOperations
from .operations_async import UserEventCalendarOperations
from .operations_async import UserEventExceptionOccurrenceOperations
from .operations_async import UserEventInstanceOperations
from .operations_async import UserEventOperations
from .operations_async import UserMailFolderChildFolderOperations
from .operations_async import UserMailFolderMessageOperations
from .operations_async import UserMailFolderOperations
from .operations_async import UserManagedAppRegistrationOperations
from .operations_async import UserManagedDeviceOperations
from .operations_async import UserMessageOperations
from .operations_async import UserOperations
from .operations_async import UserOnenoteNotebookSectionGroupSectionPageOperations
from .operations_async import UserOnenoteNotebookSectionPageOperations
from .operations_async import UserOnenoteNotebookOperations
from .operations_async import UserOnenotePageOperations
from .operations_async import UserOnenotePageParentNotebookSectionGroupSectionPageOperations
from .operations_async import UserOnenotePageParentNotebookSectionPageOperations
from .operations_async import UserOnenotePageParentSectionPageOperations
from .operations_async import UserOnenoteSectionGroupParentNotebookSectionPageOperations
from .operations_async import UserOnenoteSectionGroupSectionPageOperations
from .operations_async import UserOnenoteSectionPageOperations
from .operations_async import UserOutlookOperations
from .operations_async import UserPlannerAllOperations
from .operations_async import UserTodoListTaskOperations
from .operations_async import UserTodoListOperations
from .. import models


class UsersFunctions(object):
    """UsersFunctions.

    :ivar user_activity: UserActivityOperations operations
    :vartype user_activity: users_functions.aio.operations_async.UserActivityOperations
    :ivar user_calendar_calendar_view_calendar: UserCalendarCalendarViewCalendarOperations operations
    :vartype user_calendar_calendar_view_calendar: users_functions.aio.operations_async.UserCalendarCalendarViewCalendarOperations
    :ivar user_calendar_calendar_view_exception_occurrence: UserCalendarCalendarViewExceptionOccurrenceOperations operations
    :vartype user_calendar_calendar_view_exception_occurrence: users_functions.aio.operations_async.UserCalendarCalendarViewExceptionOccurrenceOperations
    :ivar user_calendar_calendar_view_instance: UserCalendarCalendarViewInstanceOperations operations
    :vartype user_calendar_calendar_view_instance: users_functions.aio.operations_async.UserCalendarCalendarViewInstanceOperations
    :ivar user_calendar_calendar_view: UserCalendarCalendarViewOperations operations
    :vartype user_calendar_calendar_view: users_functions.aio.operations_async.UserCalendarCalendarViewOperations
    :ivar user_calendar_event_calendar: UserCalendarEventCalendarOperations operations
    :vartype user_calendar_event_calendar: users_functions.aio.operations_async.UserCalendarEventCalendarOperations
    :ivar user_calendar_event_exception_occurrence: UserCalendarEventExceptionOccurrenceOperations operations
    :vartype user_calendar_event_exception_occurrence: users_functions.aio.operations_async.UserCalendarEventExceptionOccurrenceOperations
    :ivar user_calendar_event_instance: UserCalendarEventInstanceOperations operations
    :vartype user_calendar_event_instance: users_functions.aio.operations_async.UserCalendarEventInstanceOperations
    :ivar user_calendar_event: UserCalendarEventOperations operations
    :vartype user_calendar_event: users_functions.aio.operations_async.UserCalendarEventOperations
    :ivar user_calendar: UserCalendarOperations operations
    :vartype user_calendar: users_functions.aio.operations_async.UserCalendarOperations
    :ivar user_calendar_group_calendar_calendar_view_calendar: UserCalendarGroupCalendarCalendarViewCalendarOperations operations
    :vartype user_calendar_group_calendar_calendar_view_calendar: users_functions.aio.operations_async.UserCalendarGroupCalendarCalendarViewCalendarOperations
    :ivar user_calendar_group_calendar_calendar_view_exception_occurrence: UserCalendarGroupCalendarCalendarViewExceptionOccurrenceOperations operations
    :vartype user_calendar_group_calendar_calendar_view_exception_occurrence: users_functions.aio.operations_async.UserCalendarGroupCalendarCalendarViewExceptionOccurrenceOperations
    :ivar user_calendar_group_calendar_calendar_view_instance: UserCalendarGroupCalendarCalendarViewInstanceOperations operations
    :vartype user_calendar_group_calendar_calendar_view_instance: users_functions.aio.operations_async.UserCalendarGroupCalendarCalendarViewInstanceOperations
    :ivar user_calendar_group_calendar_calendar_view: UserCalendarGroupCalendarCalendarViewOperations operations
    :vartype user_calendar_group_calendar_calendar_view: users_functions.aio.operations_async.UserCalendarGroupCalendarCalendarViewOperations
    :ivar user_calendar_group_calendar_event_calendar: UserCalendarGroupCalendarEventCalendarOperations operations
    :vartype user_calendar_group_calendar_event_calendar: users_functions.aio.operations_async.UserCalendarGroupCalendarEventCalendarOperations
    :ivar user_calendar_group_calendar_event_exception_occurrence: UserCalendarGroupCalendarEventExceptionOccurrenceOperations operations
    :vartype user_calendar_group_calendar_event_exception_occurrence: users_functions.aio.operations_async.UserCalendarGroupCalendarEventExceptionOccurrenceOperations
    :ivar user_calendar_group_calendar_event_instance: UserCalendarGroupCalendarEventInstanceOperations operations
    :vartype user_calendar_group_calendar_event_instance: users_functions.aio.operations_async.UserCalendarGroupCalendarEventInstanceOperations
    :ivar user_calendar_group_calendar_event: UserCalendarGroupCalendarEventOperations operations
    :vartype user_calendar_group_calendar_event: users_functions.aio.operations_async.UserCalendarGroupCalendarEventOperations
    :ivar user_calendar_group_calendar: UserCalendarGroupCalendarOperations operations
    :vartype user_calendar_group_calendar: users_functions.aio.operations_async.UserCalendarGroupCalendarOperations
    :ivar user_calendar_calendar_view_calendar: UserCalendarCalendarViewCalendarOperations operations
    :vartype user_calendar_calendar_view_calendar: users_functions.aio.operations_async.UserCalendarCalendarViewCalendarOperations
    :ivar user_calendar_calendar_view_exception_occurrence: UserCalendarCalendarViewExceptionOccurrenceOperations operations
    :vartype user_calendar_calendar_view_exception_occurrence: users_functions.aio.operations_async.UserCalendarCalendarViewExceptionOccurrenceOperations
    :ivar user_calendar_calendar_view_instance: UserCalendarCalendarViewInstanceOperations operations
    :vartype user_calendar_calendar_view_instance: users_functions.aio.operations_async.UserCalendarCalendarViewInstanceOperations
    :ivar user_calendar_calendar_view: UserCalendarCalendarViewOperations operations
    :vartype user_calendar_calendar_view: users_functions.aio.operations_async.UserCalendarCalendarViewOperations
    :ivar user_calendar_event_calendar: UserCalendarEventCalendarOperations operations
    :vartype user_calendar_event_calendar: users_functions.aio.operations_async.UserCalendarEventCalendarOperations
    :ivar user_calendar_event_exception_occurrence: UserCalendarEventExceptionOccurrenceOperations operations
    :vartype user_calendar_event_exception_occurrence: users_functions.aio.operations_async.UserCalendarEventExceptionOccurrenceOperations
    :ivar user_calendar_event_instance: UserCalendarEventInstanceOperations operations
    :vartype user_calendar_event_instance: users_functions.aio.operations_async.UserCalendarEventInstanceOperations
    :ivar user_calendar_event: UserCalendarEventOperations operations
    :vartype user_calendar_event: users_functions.aio.operations_async.UserCalendarEventOperations
    :ivar user_calendar: UserCalendarOperations operations
    :vartype user_calendar: users_functions.aio.operations_async.UserCalendarOperations
    :ivar user_calendar_view_calendar_calendar_view: UserCalendarViewCalendarCalendarViewOperations operations
    :vartype user_calendar_view_calendar_calendar_view: users_functions.aio.operations_async.UserCalendarViewCalendarCalendarViewOperations
    :ivar user_calendar_view_calendar_event: UserCalendarViewCalendarEventOperations operations
    :vartype user_calendar_view_calendar_event: users_functions.aio.operations_async.UserCalendarViewCalendarEventOperations
    :ivar user_calendar_view_calendar: UserCalendarViewCalendarOperations operations
    :vartype user_calendar_view_calendar: users_functions.aio.operations_async.UserCalendarViewCalendarOperations
    :ivar user_calendar_view_exception_occurrence: UserCalendarViewExceptionOccurrenceOperations operations
    :vartype user_calendar_view_exception_occurrence: users_functions.aio.operations_async.UserCalendarViewExceptionOccurrenceOperations
    :ivar user_calendar_view_instance: UserCalendarViewInstanceOperations operations
    :vartype user_calendar_view_instance: users_functions.aio.operations_async.UserCalendarViewInstanceOperations
    :ivar user_calendar_view: UserCalendarViewOperations operations
    :vartype user_calendar_view: users_functions.aio.operations_async.UserCalendarViewOperations
    :ivar user_contact_folder_child_folder: UserContactFolderChildFolderOperations operations
    :vartype user_contact_folder_child_folder: users_functions.aio.operations_async.UserContactFolderChildFolderOperations
    :ivar user_contact_folder_contact: UserContactFolderContactOperations operations
    :vartype user_contact_folder_contact: users_functions.aio.operations_async.UserContactFolderContactOperations
    :ivar user_contact_folder: UserContactFolderOperations operations
    :vartype user_contact_folder: users_functions.aio.operations_async.UserContactFolderOperations
    :ivar user_contact: UserContactOperations operations
    :vartype user_contact: users_functions.aio.operations_async.UserContactOperations
    :ivar user_event_calendar_calendar_view: UserEventCalendarCalendarViewOperations operations
    :vartype user_event_calendar_calendar_view: users_functions.aio.operations_async.UserEventCalendarCalendarViewOperations
    :ivar user_event_calendar_event: UserEventCalendarEventOperations operations
    :vartype user_event_calendar_event: users_functions.aio.operations_async.UserEventCalendarEventOperations
    :ivar user_event_calendar: UserEventCalendarOperations operations
    :vartype user_event_calendar: users_functions.aio.operations_async.UserEventCalendarOperations
    :ivar user_event_exception_occurrence: UserEventExceptionOccurrenceOperations operations
    :vartype user_event_exception_occurrence: users_functions.aio.operations_async.UserEventExceptionOccurrenceOperations
    :ivar user_event_instance: UserEventInstanceOperations operations
    :vartype user_event_instance: users_functions.aio.operations_async.UserEventInstanceOperations
    :ivar user_event: UserEventOperations operations
    :vartype user_event: users_functions.aio.operations_async.UserEventOperations
    :ivar user_mail_folder_child_folder: UserMailFolderChildFolderOperations operations
    :vartype user_mail_folder_child_folder: users_functions.aio.operations_async.UserMailFolderChildFolderOperations
    :ivar user_mail_folder_message: UserMailFolderMessageOperations operations
    :vartype user_mail_folder_message: users_functions.aio.operations_async.UserMailFolderMessageOperations
    :ivar user_mail_folder: UserMailFolderOperations operations
    :vartype user_mail_folder: users_functions.aio.operations_async.UserMailFolderOperations
    :ivar user_managed_app_registration: UserManagedAppRegistrationOperations operations
    :vartype user_managed_app_registration: users_functions.aio.operations_async.UserManagedAppRegistrationOperations
    :ivar user_managed_device: UserManagedDeviceOperations operations
    :vartype user_managed_device: users_functions.aio.operations_async.UserManagedDeviceOperations
    :ivar user_message: UserMessageOperations operations
    :vartype user_message: users_functions.aio.operations_async.UserMessageOperations
    :ivar user: UserOperations operations
    :vartype user: users_functions.aio.operations_async.UserOperations
    :ivar user_onenote_notebook_section_group_section_page: UserOnenoteNotebookSectionGroupSectionPageOperations operations
    :vartype user_onenote_notebook_section_group_section_page: users_functions.aio.operations_async.UserOnenoteNotebookSectionGroupSectionPageOperations
    :ivar user_onenote_notebook_section_page: UserOnenoteNotebookSectionPageOperations operations
    :vartype user_onenote_notebook_section_page: users_functions.aio.operations_async.UserOnenoteNotebookSectionPageOperations
    :ivar user_onenote_notebook: UserOnenoteNotebookOperations operations
    :vartype user_onenote_notebook: users_functions.aio.operations_async.UserOnenoteNotebookOperations
    :ivar user_onenote_page: UserOnenotePageOperations operations
    :vartype user_onenote_page: users_functions.aio.operations_async.UserOnenotePageOperations
    :ivar user_onenote_page_parent_notebook_section_group_section_page: UserOnenotePageParentNotebookSectionGroupSectionPageOperations operations
    :vartype user_onenote_page_parent_notebook_section_group_section_page: users_functions.aio.operations_async.UserOnenotePageParentNotebookSectionGroupSectionPageOperations
    :ivar user_onenote_page_parent_notebook_section_page: UserOnenotePageParentNotebookSectionPageOperations operations
    :vartype user_onenote_page_parent_notebook_section_page: users_functions.aio.operations_async.UserOnenotePageParentNotebookSectionPageOperations
    :ivar user_onenote_page_parent_section_page: UserOnenotePageParentSectionPageOperations operations
    :vartype user_onenote_page_parent_section_page: users_functions.aio.operations_async.UserOnenotePageParentSectionPageOperations
    :ivar user_onenote_section_group_parent_notebook_section_page: UserOnenoteSectionGroupParentNotebookSectionPageOperations operations
    :vartype user_onenote_section_group_parent_notebook_section_page: users_functions.aio.operations_async.UserOnenoteSectionGroupParentNotebookSectionPageOperations
    :ivar user_onenote_section_group_section_page: UserOnenoteSectionGroupSectionPageOperations operations
    :vartype user_onenote_section_group_section_page: users_functions.aio.operations_async.UserOnenoteSectionGroupSectionPageOperations
    :ivar user_onenote_section_page: UserOnenoteSectionPageOperations operations
    :vartype user_onenote_section_page: users_functions.aio.operations_async.UserOnenoteSectionPageOperations
    :ivar user_outlook: UserOutlookOperations operations
    :vartype user_outlook: users_functions.aio.operations_async.UserOutlookOperations
    :ivar user_planner_all: UserPlannerAllOperations operations
    :vartype user_planner_all: users_functions.aio.operations_async.UserPlannerAllOperations
    :ivar user_todo_list_task: UserTodoListTaskOperations operations
    :vartype user_todo_list_task: users_functions.aio.operations_async.UserTodoListTaskOperations
    :ivar user_todo_list: UserTodoListOperations operations
    :vartype user_todo_list: users_functions.aio.operations_async.UserTodoListOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/beta'
        self._config = UsersFunctionsConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.user_activity = UserActivityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_calendar = UserCalendarCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_exception_occurrence = UserCalendarCalendarViewExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_instance = UserCalendarCalendarViewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view = UserCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_calendar = UserCalendarEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_exception_occurrence = UserCalendarEventExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_instance = UserCalendarEventInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event = UserCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar = UserCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view_calendar = UserCalendarGroupCalendarCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view_exception_occurrence = UserCalendarGroupCalendarCalendarViewExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view_instance = UserCalendarGroupCalendarCalendarViewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view = UserCalendarGroupCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event_calendar = UserCalendarGroupCalendarEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event_exception_occurrence = UserCalendarGroupCalendarEventExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event_instance = UserCalendarGroupCalendarEventInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event = UserCalendarGroupCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar = UserCalendarGroupCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_calendar = UserCalendarCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_exception_occurrence = UserCalendarCalendarViewExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_instance = UserCalendarCalendarViewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view = UserCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_calendar = UserCalendarEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_exception_occurrence = UserCalendarEventExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_instance = UserCalendarEventInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event = UserCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar = UserCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_calendar_calendar_view = UserCalendarViewCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_calendar_event = UserCalendarViewCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_calendar = UserCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_exception_occurrence = UserCalendarViewExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_instance = UserCalendarViewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view = UserCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_contact_folder_child_folder = UserContactFolderChildFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_contact_folder_contact = UserContactFolderContactOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_contact_folder = UserContactFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_contact = UserContactOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_calendar_calendar_view = UserEventCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_calendar_event = UserEventCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_calendar = UserEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_exception_occurrence = UserEventExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_instance = UserEventInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event = UserEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_mail_folder_child_folder = UserMailFolderChildFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_mail_folder_message = UserMailFolderMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_mail_folder = UserMailFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_managed_app_registration = UserManagedAppRegistrationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_managed_device = UserManagedDeviceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_message = UserMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section_group_section_page = UserOnenoteNotebookSectionGroupSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section_page = UserOnenoteNotebookSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook = UserOnenoteNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page = UserOnenotePageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_notebook_section_group_section_page = UserOnenotePageParentNotebookSectionGroupSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_notebook_section_page = UserOnenotePageParentNotebookSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_section_page = UserOnenotePageParentSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_parent_notebook_section_page = UserOnenoteSectionGroupParentNotebookSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_section_page = UserOnenoteSectionGroupSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_page = UserOnenoteSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook = UserOutlookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_all = UserPlannerAllOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo_list_task = UserTodoListTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo_list = UserTodoListOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "UsersFunctions":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
