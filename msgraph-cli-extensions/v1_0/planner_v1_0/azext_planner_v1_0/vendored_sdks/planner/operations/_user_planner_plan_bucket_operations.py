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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UserPlannerPlanBucketOperations(object):
    """UserPlannerPlanBucketOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~planner.models
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

    def list_task(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum98"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum99"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum100"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfPlannerTask5"]
        """Get tasks from users.

        Get tasks from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~planner.models.Enum98]
        :param select: Select properties to be returned.
        :type select: list[str or ~planner.models.Enum99]
        :param expand: Expand related entities.
        :type expand: list[str or ~planner.models.Enum100]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfPlannerTask5 or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~planner.models.CollectionOfPlannerTask5]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfPlannerTask5"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_task.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
                    'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
                    'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfPlannerTask5', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_task.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks'}  # type: ignore

    def create_task(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        body,  # type: "models.MicrosoftGraphPlannerTask"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPlannerTask"
        """Create new navigation property to tasks for users.

        Create new navigation property to tasks for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param body: New navigation property.
        :type body: ~planner.models.MicrosoftGraphPlannerTask
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPlannerTask, or the result of cls(response)
        :rtype: ~planner.models.MicrosoftGraphPlannerTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPlannerTask"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_task.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
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
        body_content = self._serialize.body(body, 'MicrosoftGraphPlannerTask')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPlannerTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_task.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks'}  # type: ignore

    def get_task(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum101"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum102"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPlannerTask"
        """Get tasks from users.

        Get tasks from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~planner.models.Enum101]
        :param expand: Expand related entities.
        :type expand: list[str or ~planner.models.Enum102]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPlannerTask, or the result of cls(response)
        :rtype: ~planner.models.MicrosoftGraphPlannerTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPlannerTask"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_task.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphPlannerTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_task.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}'}  # type: ignore

    def update_task(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        body,  # type: "models.MicrosoftGraphPlannerTask"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property tasks in users.

        Update the navigation property tasks in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
        :param body: New navigation property values.
        :type body: ~planner.models.MicrosoftGraphPlannerTask
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
        url = self.update_task.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphPlannerTask')
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

    update_task.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}'}  # type: ignore

    def delete_task(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property tasks for users.

        Delete navigation property tasks for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param planner_plan_id: key: id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: id of plannerTask.
        :type planner_task_id: str
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
        url = self.delete_task.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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

    delete_task.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}'}  # type: ignore
