# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_users_beta_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.users import Users
    return get_mgmt_service_client(cli_ctx,
                                   Users,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_user_user(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_user


def cf_user(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user


def cf_user_outlook(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_outlook


def cf_user_outlook_task_folder(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_outlook_task_folder


def cf_user_outlook_task_folder_task(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_outlook_task_folder_task


def cf_user_outlook_task_group(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_outlook_task_group


def cf_user_outlook_task_group_task_folder(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_outlook_task_group_task_folder


def cf_user_outlook_task_group_task_folder_task(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_outlook_task_group_task_folder_task


def cf_user_outlook_task(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_outlook_task


def cf_user_setting(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_setting


def cf_user_todo(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_todo


def cf_user_todo_list(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_todo_list


def cf_user_todo_list_task(cli_ctx, *_):
    return cf_users_beta_cl(cli_ctx).user_todo_list_task
