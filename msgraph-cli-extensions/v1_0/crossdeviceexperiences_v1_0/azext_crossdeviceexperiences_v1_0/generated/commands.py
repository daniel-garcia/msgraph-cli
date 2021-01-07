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

    from azext_crossdeviceexperiences_v1_0.generated._client_factory import cf_user
    crossdeviceexperiences_v1_0_user = CliCommandType(
        operations_tmpl='azext_crossdeviceexperiences_v1_0.vendored_sdks.crossdeviceexperiences.operations._user_operat'
        'ions#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('crossdeviceexperiences', crossdeviceexperiences_v1_0_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'crossdeviceexperiences_delete', confirmation=True)
        g.custom_command('create-activity', 'crossdeviceexperiences_create_activity')
        g.custom_command('get-activity', 'crossdeviceexperiences_get_activity')
        g.custom_command('list-activity', 'crossdeviceexperiences_list_activity')
        g.custom_command('update-activity', 'crossdeviceexperiences_update_activity')

    from azext_crossdeviceexperiences_v1_0.generated._client_factory import cf_user_activity
    crossdeviceexperiences_v1_0_user_activity = CliCommandType(
        operations_tmpl='azext_crossdeviceexperiences_v1_0.vendored_sdks.crossdeviceexperiences.operations._user_activi'
        'ty_operations#UserActivityOperations.{}',
        client_factory=cf_user_activity)
    with self.command_group('crossdeviceexperiences', crossdeviceexperiences_v1_0_user_activity,
                            client_factory=cf_user_activity) as g:
        g.custom_command('delete', 'crossdeviceexperiences_delete', confirmation=True)
        g.custom_command('create-history-item', 'crossdeviceexperiences_create_history_item')
        g.custom_command('get-history-item', 'crossdeviceexperiences_get_history_item')
        g.custom_command('list-history-item', 'crossdeviceexperiences_list_history_item')
        g.custom_command('update-history-item', 'crossdeviceexperiences_update_history_item')

    from azext_crossdeviceexperiences_v1_0.generated._client_factory import cf_user_activity_history_item
    crossdeviceexperiences_v1_0_user_activity_history_item = CliCommandType(
        operations_tmpl='azext_crossdeviceexperiences_v1_0.vendored_sdks.crossdeviceexperiences.operations._user_activi'
        'ty_history_item_operations#UserActivityHistoryItemOperations.{}',
        client_factory=cf_user_activity_history_item)
    with self.command_group('crossdeviceexperiences', crossdeviceexperiences_v1_0_user_activity_history_item,
                            client_factory=cf_user_activity_history_item) as g:
        g.custom_command('delete', 'crossdeviceexperiences_delete', confirmation=True)
        g.custom_command('get-activity', 'crossdeviceexperiences_get_activity')
        g.custom_command('get-ref-activity', 'crossdeviceexperiences_get_ref_activity')
        g.custom_command('set-ref-activity', 'crossdeviceexperiences_set_ref_activity')