# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UserOperations(object):
    """UserOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_functions.models
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

    def export_device_and_app_management_data_d390(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphDeviceAndAppManagementData"
        """Invoke function exportDeviceAndAppManagementData.

        Invoke function exportDeviceAndAppManagementData.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphDeviceAndAppManagementData, or the result of cls(response)
        :rtype: ~users_functions.models.MicrosoftGraphDeviceAndAppManagementData
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphDeviceAndAppManagementData"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.export_device_and_app_management_data_d390.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('MicrosoftGraphDeviceAndAppManagementData', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    export_device_and_app_management_data_d390.metadata = {'url': '/users/{user-id}/microsoft.graph.exportDeviceAndAppManagementData()'}  # type: ignore

    def export_device_and_app_management_data623_c(
        self,
        user_id,  # type: str
        skip,  # type: int
        top,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphDeviceAndAppManagementData"
        """Invoke function exportDeviceAndAppManagementData.

        Invoke function exportDeviceAndAppManagementData.

        :param user_id: key: id of user.
        :type user_id: str
        :param skip:
        :type skip: int
        :param top:
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphDeviceAndAppManagementData, or the result of cls(response)
        :rtype: ~users_functions.models.MicrosoftGraphDeviceAndAppManagementData
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphDeviceAndAppManagementData"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.export_device_and_app_management_data623_c.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'skip': self._serialize.url("skip", skip, 'int', maximum=2147483647, minimum=-2147483648),
            'top': self._serialize.url("top", top, 'int', maximum=2147483647, minimum=-2147483648),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('MicrosoftGraphDeviceAndAppManagementData', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    export_device_and_app_management_data623_c.metadata = {'url': '/users/{user-id}/microsoft.graph.exportDeviceAndAppManagementData(skip={skip},top={top})'}  # type: ignore

    def find_room_list(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphEmailAddress"]
        """Invoke function findRoomLists.

        Invoke function findRoomLists.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphEmailAddress, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphEmailAddress]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphEmailAddress"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.find_room_list.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphEmailAddress]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    find_room_list.metadata = {'url': '/users/{user-id}/microsoft.graph.findRoomLists()'}  # type: ignore

    def find_room_d266(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphEmailAddress"]
        """Invoke function findRooms.

        Invoke function findRooms.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphEmailAddress, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphEmailAddress]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphEmailAddress"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.find_room_d266.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphEmailAddress]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    find_room_d266.metadata = {'url': '/users/{user-id}/microsoft.graph.findRooms()'}  # type: ignore

    def find_room_ac49(
        self,
        user_id,  # type: str
        room_list,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphEmailAddress"]
        """Invoke function findRooms.

        Invoke function findRooms.

        :param user_id: key: id of user.
        :type user_id: str
        :param room_list:
        :type room_list: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphEmailAddress, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphEmailAddress]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphEmailAddress"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.find_room_ac49.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'RoomList': self._serialize.url("room_list", room_list, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphEmailAddress]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    find_room_ac49.metadata = {'url': '/users/{user-id}/microsoft.graph.findRooms(RoomList=\'{RoomList}\')'}  # type: ignore

    def get_effective_device_enrollment_configuration(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphDeviceEnrollmentConfiguration"]
        """Invoke function getEffectiveDeviceEnrollmentConfigurations.

        Invoke function getEffectiveDeviceEnrollmentConfigurations.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphDeviceEnrollmentConfiguration, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphDeviceEnrollmentConfiguration]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphDeviceEnrollmentConfiguration"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_effective_device_enrollment_configuration.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphDeviceEnrollmentConfiguration]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_effective_device_enrollment_configuration.metadata = {'url': '/users/{user-id}/microsoft.graph.getEffectiveDeviceEnrollmentConfigurations()'}  # type: ignore

    def get_logged_on_managed_device(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphManagedDevice"]
        """Invoke function getLoggedOnManagedDevices.

        Invoke function getLoggedOnManagedDevices.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphManagedDevice, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphManagedDevice]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphManagedDevice"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_logged_on_managed_device.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphManagedDevice]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_logged_on_managed_device.metadata = {'url': '/users/{user-id}/microsoft.graph.getLoggedOnManagedDevices()'}  # type: ignore

    def get_managed_app_diagnostic_statuses(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphManagedAppDiagnosticStatus"]
        """Invoke function getManagedAppDiagnosticStatuses.

        Invoke function getManagedAppDiagnosticStatuses.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphManagedAppDiagnosticStatus, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphManagedAppDiagnosticStatus]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphManagedAppDiagnosticStatus"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_managed_app_diagnostic_statuses.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphManagedAppDiagnosticStatus]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_managed_app_diagnostic_statuses.metadata = {'url': '/users/{user-id}/microsoft.graph.getManagedAppDiagnosticStatuses()'}  # type: ignore

    def get_managed_app_policy(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphManagedAppPolicy"]
        """Invoke function getManagedAppPolicies.

        Invoke function getManagedAppPolicies.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphManagedAppPolicy, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphManagedAppPolicy]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphManagedAppPolicy"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_managed_app_policy.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphManagedAppPolicy]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_managed_app_policy.metadata = {'url': '/users/{user-id}/microsoft.graph.getManagedAppPolicies()'}  # type: ignore

    def get_managed_device_with_app_failure(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List[str]
        """Invoke function getManagedDevicesWithAppFailures.

        Invoke function getManagedDevicesWithAppFailures.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_managed_device_with_app_failure.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_managed_device_with_app_failure.metadata = {'url': '/users/{user-id}/microsoft.graph.getManagedDevicesWithAppFailures()'}  # type: ignore

    def get_managed_device_with_failed_or_pending_app(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphManagedDeviceSummarizedAppState"]
        """Invoke function getManagedDevicesWithFailedOrPendingApps.

        Invoke function getManagedDevicesWithFailedOrPendingApps.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphManagedDeviceSummarizedAppState, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphManagedDeviceSummarizedAppState]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphManagedDeviceSummarizedAppState"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_managed_device_with_failed_or_pending_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphManagedDeviceSummarizedAppState]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_managed_device_with_failed_or_pending_app.metadata = {'url': '/users/{user-id}/microsoft.graph.getManagedDevicesWithFailedOrPendingApps()'}  # type: ignore

    def is_managed_app_user_blocked(
        self,
        user_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> bool
        """Invoke function isManagedAppUserBlocked.

        Invoke function isManagedAppUserBlocked.

        :param user_id: key: id of user.
        :type user_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[bool]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.is_managed_app_user_blocked.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('bool', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    is_managed_app_user_blocked.metadata = {'url': '/users/{user-id}/microsoft.graph.isManagedAppUserBlocked()'}  # type: ignore

    def reminder_view(
        self,
        user_id,  # type: str
        start_date_time,  # type: str
        end_date_time,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphReminder"]
        """Invoke function reminderView.

        Invoke function reminderView.

        :param user_id: key: id of user.
        :type user_id: str
        :param start_date_time:
        :type start_date_time: str
        :param end_date_time:
        :type end_date_time: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphReminder, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphReminder]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphReminder"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.reminder_view.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'StartDateTime': self._serialize.url("start_date_time", start_date_time, 'str'),
            'EndDateTime': self._serialize.url("end_date_time", end_date_time, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphReminder]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    reminder_view.metadata = {'url': '/users/{user-id}/microsoft.graph.reminderView(StartDateTime=\'{StartDateTime}\',EndDateTime=\'{EndDateTime}\')'}  # type: ignore

    def delta(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphUser"]
        """Invoke function delta.

        Invoke function delta.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphUser, or the result of cls(response)
        :rtype: list[~users_functions.models.MicrosoftGraphUser]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphUser"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delta.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[MicrosoftGraphUser]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delta.metadata = {'url': '/users/microsoft.graph.delta()'}  # type: ignore

    def get_managed_app_blocked_user(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> List[str]
        """Invoke function getManagedAppBlockedUsers.

        Invoke function getManagedAppBlockedUsers.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_managed_app_blocked_user.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_managed_app_blocked_user.metadata = {'url': '/users/microsoft.graph.getManagedAppBlockedUsers()'}  # type: ignore