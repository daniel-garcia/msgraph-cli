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

from ._configuration_async import PlannerConfiguration
from .operations_async import GroupOperations
from .operations_async import GroupPlannerOperations
from .operations_async import GroupPlannerPlanOperations
from .operations_async import GroupPlannerPlanBucketOperations
from .operations_async import GroupPlannerPlanBucketTaskOperations
from .operations_async import GroupPlannerPlanTaskOperations
from .operations_async import PlannerPlannerOperations
from .operations_async import PlannerOperations
from .operations_async import PlannerBucketOperations
from .operations_async import PlannerBucketTaskOperations
from .operations_async import PlannerPlanOperations
from .operations_async import PlannerPlanBucketOperations
from .operations_async import PlannerPlanBucketTaskOperations
from .operations_async import PlannerPlanTaskOperations
from .operations_async import PlannerTaskOperations
from .operations_async import UserOperations
from .operations_async import UserPlannerOperations
from .operations_async import UserPlannerPlanOperations
from .operations_async import UserPlannerPlanBucketOperations
from .operations_async import UserPlannerPlanBucketTaskOperations
from .operations_async import UserPlannerPlanTaskOperations
from .operations_async import UserPlannerTaskOperations
from .. import models


class Planner(object):
    """Planner.

    :ivar group: GroupOperations operations
    :vartype group: planner.aio.operations_async.GroupOperations
    :ivar group_planner: GroupPlannerOperations operations
    :vartype group_planner: planner.aio.operations_async.GroupPlannerOperations
    :ivar group_planner_plan: GroupPlannerPlanOperations operations
    :vartype group_planner_plan: planner.aio.operations_async.GroupPlannerPlanOperations
    :ivar group_planner_plan_bucket: GroupPlannerPlanBucketOperations operations
    :vartype group_planner_plan_bucket: planner.aio.operations_async.GroupPlannerPlanBucketOperations
    :ivar group_planner_plan_bucket_task: GroupPlannerPlanBucketTaskOperations operations
    :vartype group_planner_plan_bucket_task: planner.aio.operations_async.GroupPlannerPlanBucketTaskOperations
    :ivar group_planner_plan_task: GroupPlannerPlanTaskOperations operations
    :vartype group_planner_plan_task: planner.aio.operations_async.GroupPlannerPlanTaskOperations
    :ivar planner_planner: PlannerPlannerOperations operations
    :vartype planner_planner: planner.aio.operations_async.PlannerPlannerOperations
    :ivar planner: PlannerOperations operations
    :vartype planner: planner.aio.operations_async.PlannerOperations
    :ivar planner_bucket: PlannerBucketOperations operations
    :vartype planner_bucket: planner.aio.operations_async.PlannerBucketOperations
    :ivar planner_bucket_task: PlannerBucketTaskOperations operations
    :vartype planner_bucket_task: planner.aio.operations_async.PlannerBucketTaskOperations
    :ivar planner_plan: PlannerPlanOperations operations
    :vartype planner_plan: planner.aio.operations_async.PlannerPlanOperations
    :ivar planner_plan_bucket: PlannerPlanBucketOperations operations
    :vartype planner_plan_bucket: planner.aio.operations_async.PlannerPlanBucketOperations
    :ivar planner_plan_bucket_task: PlannerPlanBucketTaskOperations operations
    :vartype planner_plan_bucket_task: planner.aio.operations_async.PlannerPlanBucketTaskOperations
    :ivar planner_plan_task: PlannerPlanTaskOperations operations
    :vartype planner_plan_task: planner.aio.operations_async.PlannerPlanTaskOperations
    :ivar planner_task: PlannerTaskOperations operations
    :vartype planner_task: planner.aio.operations_async.PlannerTaskOperations
    :ivar user: UserOperations operations
    :vartype user: planner.aio.operations_async.UserOperations
    :ivar user_planner: UserPlannerOperations operations
    :vartype user_planner: planner.aio.operations_async.UserPlannerOperations
    :ivar user_planner_plan: UserPlannerPlanOperations operations
    :vartype user_planner_plan: planner.aio.operations_async.UserPlannerPlanOperations
    :ivar user_planner_plan_bucket: UserPlannerPlanBucketOperations operations
    :vartype user_planner_plan_bucket: planner.aio.operations_async.UserPlannerPlanBucketOperations
    :ivar user_planner_plan_bucket_task: UserPlannerPlanBucketTaskOperations operations
    :vartype user_planner_plan_bucket_task: planner.aio.operations_async.UserPlannerPlanBucketTaskOperations
    :ivar user_planner_plan_task: UserPlannerPlanTaskOperations operations
    :vartype user_planner_plan_task: planner.aio.operations_async.UserPlannerPlanTaskOperations
    :ivar user_planner_task: UserPlannerTaskOperations operations
    :vartype user_planner_task: planner.aio.operations_async.UserPlannerTaskOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
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
        credential: "AsyncTokenCredential",
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/beta'
        self._config = PlannerConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.group = GroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_planner = GroupPlannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_planner_plan = GroupPlannerPlanOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_planner_plan_bucket = GroupPlannerPlanBucketOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_planner_plan_bucket_task = GroupPlannerPlanBucketTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_planner_plan_task = GroupPlannerPlanTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_planner = PlannerPlannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner = PlannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_bucket = PlannerBucketOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_bucket_task = PlannerBucketTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_plan = PlannerPlanOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_plan_bucket = PlannerPlanBucketOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_plan_bucket_task = PlannerPlanBucketTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_plan_task = PlannerPlanTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_task = PlannerTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner = UserPlannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_plan = UserPlannerPlanOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_plan_bucket = UserPlannerPlanBucketOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_plan_bucket_task = UserPlannerPlanBucketTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_plan_task = UserPlannerPlanTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_task = UserPlannerTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "Planner":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
