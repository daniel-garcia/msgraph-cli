# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_planner_v1_0.generated._client_factory import cf_group
    planner_v1_0_group = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._group_operations#GroupOperations.{}',
        client_factory=cf_group)
    with self.command_group('planner', planner_v1_0_group, client_factory=cf_group) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-planner', 'planner_get_planner')
        g.custom_command('update-planner', 'planner_update_planner')

    from azext_planner_v1_0.generated._client_factory import cf_group_planner
    planner_v1_0_group_planner = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._group_planner_operations#GroupPlannerOper'
        'ations.{}',
        client_factory=cf_group_planner)
    with self.command_group('planner', planner_v1_0_group_planner, client_factory=cf_group_planner) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-plan', 'planner_create_plan')
        g.custom_command('get-plan', 'planner_get_plan')
        g.custom_command('list-plan', 'planner_list_plan')
        g.custom_command('update-plan', 'planner_update_plan')

    from azext_planner_v1_0.generated._client_factory import cf_group_planner_plan
    planner_v1_0_group_planner_plan = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._group_planner_plan_operations#GroupPlanne'
        'rPlanOperations.{}',
        client_factory=cf_group_planner_plan)
    with self.command_group('planner', planner_v1_0_group_planner_plan, client_factory=cf_group_planner_plan) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-bucket', 'planner_create_bucket')
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('get-bucket', 'planner_get_bucket')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-task', 'planner_get_task')
        g.custom_command('list-bucket', 'planner_list_bucket')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('update-bucket', 'planner_update_bucket')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-task', 'planner_update_task')

    from azext_planner_v1_0.generated._client_factory import cf_group_planner_plan_bucket
    planner_v1_0_group_planner_plan_bucket = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._group_planner_plan_bucket_operations#Grou'
        'pPlannerPlanBucketOperations.{}',
        client_factory=cf_group_planner_plan_bucket)
    with self.command_group('planner', planner_v1_0_group_planner_plan_bucket,
                            client_factory=cf_group_planner_plan_bucket) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('get-task', 'planner_get_task')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('update-task', 'planner_update_task')

    from azext_planner_v1_0.generated._client_factory import cf_group_planner_plan_bucket_task
    planner_v1_0_group_planner_plan_bucket_task = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._group_planner_plan_bucket_task_operations'
        '#GroupPlannerPlanBucketTaskOperations.{}',
        client_factory=cf_group_planner_plan_bucket_task)
    with self.command_group('planner', planner_v1_0_group_planner_plan_bucket_task,
                            client_factory=cf_group_planner_plan_bucket_task) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-assigned-to-task-board-format', 'planner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'planner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-progress-task-board-format', 'planner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'planner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'planner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_update_progress_task_board_format')

    from azext_planner_v1_0.generated._client_factory import cf_group_planner_plan_task
    planner_v1_0_group_planner_plan_task = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._group_planner_plan_task_operations#GroupP'
        'lannerPlanTaskOperations.{}',
        client_factory=cf_group_planner_plan_task)
    with self.command_group('planner', planner_v1_0_group_planner_plan_task,
                            client_factory=cf_group_planner_plan_task) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-assigned-to-task-board-format', 'planner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'planner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-progress-task-board-format', 'planner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'planner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'planner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_update_progress_task_board_format')

    from azext_planner_v1_0.generated._client_factory import cf_planner_planner
    planner_v1_0_planner_planner = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._planner_planner_operations#PlannerPlanner'
        'Operations.{}',
        client_factory=cf_planner_planner)
    with self.command_group('planner', planner_v1_0_planner_planner, client_factory=cf_planner_planner) as g:
        g.custom_command('get-planner', 'planner_get_planner')
        g.custom_command('update-planner', 'planner_update_planner')

    from azext_planner_v1_0.generated._client_factory import cf_planner
    planner_v1_0_planner = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._planner_operations#PlannerOperations.{}',
        client_factory=cf_planner)
    with self.command_group('planner', planner_v1_0_planner, client_factory=cf_planner) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-bucket', 'planner_create_bucket')
        g.custom_command('create-plan', 'planner_create_plan')
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('get-bucket', 'planner_get_bucket')
        g.custom_command('get-plan', 'planner_get_plan')
        g.custom_command('get-task', 'planner_get_task')
        g.custom_command('list-bucket', 'planner_list_bucket')
        g.custom_command('list-plan', 'planner_list_plan')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('update-bucket', 'planner_update_bucket')
        g.custom_command('update-plan', 'planner_update_plan')
        g.custom_command('update-task', 'planner_update_task')

    from azext_planner_v1_0.generated._client_factory import cf_planner_bucket
    planner_v1_0_planner_bucket = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._planner_bucket_operations#PlannerBucketOp'
        'erations.{}',
        client_factory=cf_planner_bucket)
    with self.command_group('planner', planner_v1_0_planner_bucket, client_factory=cf_planner_bucket) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('get-task', 'planner_get_task')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('update-task', 'planner_update_task')

    from azext_planner_v1_0.generated._client_factory import cf_planner_bucket_task
    planner_v1_0_planner_bucket_task = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._planner_bucket_task_operations#PlannerBuc'
        'ketTaskOperations.{}',
        client_factory=cf_planner_bucket_task)
    with self.command_group('planner', planner_v1_0_planner_bucket_task, client_factory=cf_planner_bucket_task) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-assigned-to-task-board-format', 'planner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'planner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-progress-task-board-format', 'planner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'planner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'planner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_update_progress_task_board_format')

    from azext_planner_v1_0.generated._client_factory import cf_planner_plan
    planner_v1_0_planner_plan = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._planner_plan_operations#PlannerPlanOperat'
        'ions.{}',
        client_factory=cf_planner_plan)
    with self.command_group('planner', planner_v1_0_planner_plan, client_factory=cf_planner_plan) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-bucket', 'planner_create_bucket')
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('get-bucket', 'planner_get_bucket')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-task', 'planner_get_task')
        g.custom_command('list-bucket', 'planner_list_bucket')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('update-bucket', 'planner_update_bucket')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-task', 'planner_update_task')

    from azext_planner_v1_0.generated._client_factory import cf_planner_plan_bucket
    planner_v1_0_planner_plan_bucket = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._planner_plan_bucket_operations#PlannerPla'
        'nBucketOperations.{}',
        client_factory=cf_planner_plan_bucket)
    with self.command_group('planner', planner_v1_0_planner_plan_bucket, client_factory=cf_planner_plan_bucket) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('get-task', 'planner_get_task')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('update-task', 'planner_update_task')

    from azext_planner_v1_0.generated._client_factory import cf_planner_plan_bucket_task
    planner_v1_0_planner_plan_bucket_task = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._planner_plan_bucket_task_operations#Plann'
        'erPlanBucketTaskOperations.{}',
        client_factory=cf_planner_plan_bucket_task)
    with self.command_group('planner', planner_v1_0_planner_plan_bucket_task,
                            client_factory=cf_planner_plan_bucket_task) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-assigned-to-task-board-format', 'planner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'planner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-progress-task-board-format', 'planner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'planner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'planner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_update_progress_task_board_format')

    from azext_planner_v1_0.generated._client_factory import cf_planner_plan_task
    planner_v1_0_planner_plan_task = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._planner_plan_task_operations#PlannerPlanT'
        'askOperations.{}',
        client_factory=cf_planner_plan_task)
    with self.command_group('planner', planner_v1_0_planner_plan_task, client_factory=cf_planner_plan_task) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-assigned-to-task-board-format', 'planner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'planner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-progress-task-board-format', 'planner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'planner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'planner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_update_progress_task_board_format')

    from azext_planner_v1_0.generated._client_factory import cf_planner_task
    planner_v1_0_planner_task = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._planner_task_operations#PlannerTaskOperat'
        'ions.{}',
        client_factory=cf_planner_task)
    with self.command_group('planner', planner_v1_0_planner_task, client_factory=cf_planner_task) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-assigned-to-task-board-format', 'planner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'planner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-progress-task-board-format', 'planner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'planner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'planner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_update_progress_task_board_format')

    from azext_planner_v1_0.generated._client_factory import cf_user
    planner_v1_0_user = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('planner', planner_v1_0_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-planner', 'planner_get_planner')
        g.custom_command('update-planner', 'planner_update_planner')

    from azext_planner_v1_0.generated._client_factory import cf_user_planner
    planner_v1_0_user_planner = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._user_planner_operations#UserPlannerOperat'
        'ions.{}',
        client_factory=cf_user_planner)
    with self.command_group('planner', planner_v1_0_user_planner, client_factory=cf_user_planner) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-plan', 'planner_create_plan')
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('get-plan', 'planner_get_plan')
        g.custom_command('get-task', 'planner_get_task')
        g.custom_command('list-plan', 'planner_list_plan')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('update-plan', 'planner_update_plan')
        g.custom_command('update-task', 'planner_update_task')

    from azext_planner_v1_0.generated._client_factory import cf_user_planner_plan
    planner_v1_0_user_planner_plan = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._user_planner_plan_operations#UserPlannerP'
        'lanOperations.{}',
        client_factory=cf_user_planner_plan)
    with self.command_group('planner', planner_v1_0_user_planner_plan, client_factory=cf_user_planner_plan) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-bucket', 'planner_create_bucket')
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('get-bucket', 'planner_get_bucket')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-task', 'planner_get_task')
        g.custom_command('list-bucket', 'planner_list_bucket')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('update-bucket', 'planner_update_bucket')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-task', 'planner_update_task')

    from azext_planner_v1_0.generated._client_factory import cf_user_planner_plan_bucket
    planner_v1_0_user_planner_plan_bucket = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._user_planner_plan_bucket_operations#UserP'
        'lannerPlanBucketOperations.{}',
        client_factory=cf_user_planner_plan_bucket)
    with self.command_group('planner', planner_v1_0_user_planner_plan_bucket,
                            client_factory=cf_user_planner_plan_bucket) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('get-task', 'planner_get_task')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('update-task', 'planner_update_task')

    from azext_planner_v1_0.generated._client_factory import cf_user_planner_plan_bucket_task
    planner_v1_0_user_planner_plan_bucket_task = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._user_planner_plan_bucket_task_operations#'
        'UserPlannerPlanBucketTaskOperations.{}',
        client_factory=cf_user_planner_plan_bucket_task)
    with self.command_group('planner', planner_v1_0_user_planner_plan_bucket_task,
                            client_factory=cf_user_planner_plan_bucket_task) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-assigned-to-task-board-format', 'planner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'planner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-progress-task-board-format', 'planner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'planner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'planner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_update_progress_task_board_format')

    from azext_planner_v1_0.generated._client_factory import cf_user_planner_plan_task
    planner_v1_0_user_planner_plan_task = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._user_planner_plan_task_operations#UserPla'
        'nnerPlanTaskOperations.{}',
        client_factory=cf_user_planner_plan_task)
    with self.command_group('planner', planner_v1_0_user_planner_plan_task,
                            client_factory=cf_user_planner_plan_task) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-assigned-to-task-board-format', 'planner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'planner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-progress-task-board-format', 'planner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'planner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'planner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_update_progress_task_board_format')

    from azext_planner_v1_0.generated._client_factory import cf_user_planner_task
    planner_v1_0_user_planner_task = CliCommandType(
        operations_tmpl='azext_planner_v1_0.vendored_sdks.planner.operations._user_planner_task_operations#UserPlannerT'
        'askOperations.{}',
        client_factory=cf_user_planner_task)
    with self.command_group('planner', planner_v1_0_user_planner_task, client_factory=cf_user_planner_task) as g:
        g.custom_command('delete', 'planner_delete', confirmation=True)
        g.custom_command('get-assigned-to-task-board-format', 'planner_get_assigned_to_task_board_format')
        g.custom_command('get-bucket-task-board-format', 'planner_get_bucket_task_board_format')
        g.custom_command('get-detail', 'planner_get_detail')
        g.custom_command('get-progress-task-board-format', 'planner_get_progress_task_board_format')
        g.custom_command('update-assigned-to-task-board-format', 'planner_update_assigned_to_task_board_format')
        g.custom_command('update-bucket-task-board-format', 'planner_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_update_progress_task_board_format')