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

from ._configuration import DevicesCorporateManagementConfiguration
from .operations import DeviceAppManagementDeviceAppManagementOperations
from .operations import DeviceAppManagementOperations
from .operations import DeviceAppManagementAndroidManagedAppProtectionOperations
from .operations import DeviceAppManagementDefaultManagedAppProtectionOperations
from .operations import DeviceAppManagementIoManagedAppProtectionOperations
from .operations import DeviceAppManagementManagedAppPolicyOperations
from .operations import DeviceAppManagementManagedAppRegistrationOperations
from .operations import DeviceAppManagementManagedAppRegistrationAppliedPolicyOperations
from .operations import DeviceAppManagementManagedAppRegistrationIntendedPolicyOperations
from .operations import DeviceAppManagementManagedEBookOperations
from .operations import DeviceAppManagementManagedEBookUserStateSummaryOperations
from .operations import DeviceAppManagementMobileAppConfigurationOperations
from .operations import DeviceAppManagementMobileAppOperations
from .operations import DeviceAppManagementTargetedManagedAppConfigurationOperations
from .operations import DeviceAppManagementVppTokenOperations
from .operations import UserOperations
from .operations import UserManagedDeviceOperations
from . import models


class DevicesCorporateManagement(object):
    """DevicesCorporateManagement.

    :ivar device_app_management_device_app_management: DeviceAppManagementDeviceAppManagementOperations operations
    :vartype device_app_management_device_app_management: devices_corporate_management.operations.DeviceAppManagementDeviceAppManagementOperations
    :ivar device_app_management: DeviceAppManagementOperations operations
    :vartype device_app_management: devices_corporate_management.operations.DeviceAppManagementOperations
    :ivar device_app_management_android_managed_app_protection: DeviceAppManagementAndroidManagedAppProtectionOperations operations
    :vartype device_app_management_android_managed_app_protection: devices_corporate_management.operations.DeviceAppManagementAndroidManagedAppProtectionOperations
    :ivar device_app_management_default_managed_app_protection: DeviceAppManagementDefaultManagedAppProtectionOperations operations
    :vartype device_app_management_default_managed_app_protection: devices_corporate_management.operations.DeviceAppManagementDefaultManagedAppProtectionOperations
    :ivar device_app_management_io_managed_app_protection: DeviceAppManagementIoManagedAppProtectionOperations operations
    :vartype device_app_management_io_managed_app_protection: devices_corporate_management.operations.DeviceAppManagementIoManagedAppProtectionOperations
    :ivar device_app_management_managed_app_policy: DeviceAppManagementManagedAppPolicyOperations operations
    :vartype device_app_management_managed_app_policy: devices_corporate_management.operations.DeviceAppManagementManagedAppPolicyOperations
    :ivar device_app_management_managed_app_registration: DeviceAppManagementManagedAppRegistrationOperations operations
    :vartype device_app_management_managed_app_registration: devices_corporate_management.operations.DeviceAppManagementManagedAppRegistrationOperations
    :ivar device_app_management_managed_app_registration_applied_policy: DeviceAppManagementManagedAppRegistrationAppliedPolicyOperations operations
    :vartype device_app_management_managed_app_registration_applied_policy: devices_corporate_management.operations.DeviceAppManagementManagedAppRegistrationAppliedPolicyOperations
    :ivar device_app_management_managed_app_registration_intended_policy: DeviceAppManagementManagedAppRegistrationIntendedPolicyOperations operations
    :vartype device_app_management_managed_app_registration_intended_policy: devices_corporate_management.operations.DeviceAppManagementManagedAppRegistrationIntendedPolicyOperations
    :ivar device_app_management_managed_ebook: DeviceAppManagementManagedEBookOperations operations
    :vartype device_app_management_managed_ebook: devices_corporate_management.operations.DeviceAppManagementManagedEBookOperations
    :ivar device_app_management_managed_ebook_user_state_summary: DeviceAppManagementManagedEBookUserStateSummaryOperations operations
    :vartype device_app_management_managed_ebook_user_state_summary: devices_corporate_management.operations.DeviceAppManagementManagedEBookUserStateSummaryOperations
    :ivar device_app_management_mobile_app_configuration: DeviceAppManagementMobileAppConfigurationOperations operations
    :vartype device_app_management_mobile_app_configuration: devices_corporate_management.operations.DeviceAppManagementMobileAppConfigurationOperations
    :ivar device_app_management_mobile_app: DeviceAppManagementMobileAppOperations operations
    :vartype device_app_management_mobile_app: devices_corporate_management.operations.DeviceAppManagementMobileAppOperations
    :ivar device_app_management_targeted_managed_app_configuration: DeviceAppManagementTargetedManagedAppConfigurationOperations operations
    :vartype device_app_management_targeted_managed_app_configuration: devices_corporate_management.operations.DeviceAppManagementTargetedManagedAppConfigurationOperations
    :ivar device_app_management_vpp_token: DeviceAppManagementVppTokenOperations operations
    :vartype device_app_management_vpp_token: devices_corporate_management.operations.DeviceAppManagementVppTokenOperations
    :ivar user: UserOperations operations
    :vartype user: devices_corporate_management.operations.UserOperations
    :ivar user_managed_device: UserManagedDeviceOperations operations
    :vartype user_managed_device: devices_corporate_management.operations.UserManagedDeviceOperations
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
        self._config = DevicesCorporateManagementConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.device_app_management_device_app_management = DeviceAppManagementDeviceAppManagementOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management = DeviceAppManagementOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_android_managed_app_protection = DeviceAppManagementAndroidManagedAppProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_default_managed_app_protection = DeviceAppManagementDefaultManagedAppProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_io_managed_app_protection = DeviceAppManagementIoManagedAppProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_policy = DeviceAppManagementManagedAppPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_registration = DeviceAppManagementManagedAppRegistrationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_registration_applied_policy = DeviceAppManagementManagedAppRegistrationAppliedPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_registration_intended_policy = DeviceAppManagementManagedAppRegistrationIntendedPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_ebook = DeviceAppManagementManagedEBookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_ebook_user_state_summary = DeviceAppManagementManagedEBookUserStateSummaryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_mobile_app_configuration = DeviceAppManagementMobileAppConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_mobile_app = DeviceAppManagementMobileAppOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_targeted_managed_app_configuration = DeviceAppManagementTargetedManagedAppConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_vpp_token = DeviceAppManagementVppTokenOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_managed_device = UserManagedDeviceOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DevicesCorporateManagement
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
