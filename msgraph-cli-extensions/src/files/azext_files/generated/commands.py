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

    from azext_files.generated._client_factory import cf_drive_drive
    files_drive_drive = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._drive_drive_operations#DriveDriveOperations.{}',
        client_factory=cf_drive_drive)
    with self.command_group('files', files_drive_drive, client_factory=cf_drive_drive) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-drive', 'files_create_drive')
        g.custom_command('get-drive', 'files_get_drive')
        g.custom_command('list-drive', 'files_list_drive')
        g.custom_command('update-drive', 'files_update_drive')

    from azext_files.generated._client_factory import cf_drive
    files_drive = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._drive_operations#DriveOperations.{}',
        client_factory=cf_drive)
    with self.command_group('files', files_drive, client_factory=cf_drive) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-following', 'files_create_following')
        g.custom_command('create-item', 'files_create_item')
        g.custom_command('create-special', 'files_create_special')
        g.custom_command('get-following', 'files_get_following')
        g.custom_command('get-item', 'files_get_item')
        g.custom_command('get-list', 'files_get_list')
        g.custom_command('get-root', 'files_get_root')
        g.custom_command('get-special', 'files_get_special')
        g.custom_command('list-following', 'files_list_following')
        g.custom_command('list-item', 'files_list_item')
        g.custom_command('list-special', 'files_list_special')
        g.custom_command('recent', 'files_recent')
        g.custom_command('search', 'files_search')
        g.custom_command('shared-with-me', 'files_shared_with_me')
        g.custom_command('update-following', 'files_update_following')
        g.custom_command('update-item', 'files_update_item')
        g.custom_command('update-list', 'files_update_list')
        g.custom_command('update-root', 'files_update_root')
        g.custom_command('update-special', 'files_update_special')

    from azext_files.generated._client_factory import cf_drive_list
    files_drive_list = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._drive_list_operations#DriveListOperations.{}',
        client_factory=cf_drive_list)
    with self.command_group('files', files_drive_list, client_factory=cf_drive_list) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-column', 'files_create_column')
        g.custom_command('create-content-type', 'files_create_content_type')
        g.custom_command('create-item', 'files_create_item')
        g.custom_command('create-subscription', 'files_create_subscription')
        g.custom_command('get-column', 'files_get_column')
        g.custom_command('get-content-type', 'files_get_content_type')
        g.custom_command('get-drive', 'files_get_drive')
        g.custom_command('get-item', 'files_get_item')
        g.custom_command('get-subscription', 'files_get_subscription')
        g.custom_command('list-column', 'files_list_column')
        g.custom_command('list-content-type', 'files_list_content_type')
        g.custom_command('list-item', 'files_list_item')
        g.custom_command('list-subscription', 'files_list_subscription')
        g.custom_command('update-column', 'files_update_column')
        g.custom_command('update-content-type', 'files_update_content_type')
        g.custom_command('update-drive', 'files_update_drive')
        g.custom_command('update-item', 'files_update_item')
        g.custom_command('update-subscription', 'files_update_subscription')

    from azext_files.generated._client_factory import cf_drive_list_content_type
    files_drive_list_content_type = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._drive_list_content_type_operations#DriveListConten'
        'tTypeOperations.{}',
        client_factory=cf_drive_list_content_type)
    with self.command_group('files', files_drive_list_content_type, client_factory=cf_drive_list_content_type) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-column-link', 'files_create_column_link')
        g.custom_command('get-column-link', 'files_get_column_link')
        g.custom_command('list-column-link', 'files_list_column_link')
        g.custom_command('update-column-link', 'files_update_column_link')

    from azext_files.generated._client_factory import cf_drive_list_item
    files_drive_list_item = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._drive_list_item_operations#DriveListItemOperations'
        '.{}',
        client_factory=cf_drive_list_item)
    with self.command_group('files', files_drive_list_item, client_factory=cf_drive_list_item) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-version', 'files_create_version')
        g.custom_command('get-activity-by-interval53-ee', 'files_get_activity_by_interval53_ee')
        g.custom_command('get-activity-by-interval96-b0', 'files_get_activity_by_interval96_b0')
        g.custom_command('get-analytic', 'files_get_analytic')
        g.custom_command('get-drive-item', 'files_get_drive_item')
        g.custom_command('get-field', 'files_get_field')
        g.custom_command('get-ref-analytic', 'files_get_ref_analytic')
        g.custom_command('get-version', 'files_get_version')
        g.custom_command('list-version', 'files_list_version')
        g.custom_command('set-ref-analytic', 'files_set_ref_analytic')
        g.custom_command('update-drive-item', 'files_update_drive_item')
        g.custom_command('update-field', 'files_update_field')
        g.custom_command('update-version', 'files_update_version')

    from azext_files.generated._client_factory import cf_drive_list_item_version
    files_drive_list_item_version = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._drive_list_item_version_operations#DriveListItemVe'
        'rsionOperations.{}',
        client_factory=cf_drive_list_item_version)
    with self.command_group('files', files_drive_list_item_version, client_factory=cf_drive_list_item_version) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('get-field', 'files_get_field')
        g.custom_command('restore-version', 'files_restore_version')
        g.custom_command('update-field', 'files_update_field')

    from azext_files.generated._client_factory import cf_group
    files_group = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._group_operations#GroupOperations.{}',
        client_factory=cf_group)
    with self.command_group('files', files_group, client_factory=cf_group) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-drive', 'files_create_drive')
        g.custom_command('get-drive', 'files_get_drive')
        g.custom_command('list-drive', 'files_list_drive')
        g.custom_command('update-drive', 'files_update_drive')

    from azext_files.generated._client_factory import cf_share_shared_drive_item
    files_share_shared_drive_item = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._share_shared_drive_item_operations#ShareSharedDriv'
        'eItemOperations.{}',
        client_factory=cf_share_shared_drive_item)
    with self.command_group('files', files_share_shared_drive_item, client_factory=cf_share_shared_drive_item) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-shared-drive-item', 'files_create_shared_drive_item')
        g.custom_command('get-shared-drive-item', 'files_get_shared_drive_item')
        g.custom_command('list-shared-drive-item', 'files_list_shared_drive_item')
        g.custom_command('update-shared-drive-item', 'files_update_shared_drive_item')

    from azext_files.generated._client_factory import cf_share
    files_share = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._share_operations#ShareOperations.{}',
        client_factory=cf_share)
    with self.command_group('files', files_share, client_factory=cf_share) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-item', 'files_create_item')
        g.custom_command('get-drive-item', 'files_get_drive_item')
        g.custom_command('get-item', 'files_get_item')
        g.custom_command('get-list', 'files_get_list')
        g.custom_command('get-list-item', 'files_get_list_item')
        g.custom_command('get-permission', 'files_get_permission')
        g.custom_command('get-root', 'files_get_root')
        g.custom_command('get-site', 'files_get_site')
        g.custom_command('list-item', 'files_list_item')
        g.custom_command('update-drive-item', 'files_update_drive_item')
        g.custom_command('update-item', 'files_update_item')
        g.custom_command('update-list', 'files_update_list')
        g.custom_command('update-list-item', 'files_update_list_item')
        g.custom_command('update-permission', 'files_update_permission')
        g.custom_command('update-root', 'files_update_root')
        g.custom_command('update-site', 'files_update_site')

    from azext_files.generated._client_factory import cf_share_list
    files_share_list = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._share_list_operations#ShareListOperations.{}',
        client_factory=cf_share_list)
    with self.command_group('files', files_share_list, client_factory=cf_share_list) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-column', 'files_create_column')
        g.custom_command('create-content-type', 'files_create_content_type')
        g.custom_command('create-item', 'files_create_item')
        g.custom_command('create-subscription', 'files_create_subscription')
        g.custom_command('get-column', 'files_get_column')
        g.custom_command('get-content-type', 'files_get_content_type')
        g.custom_command('get-drive', 'files_get_drive')
        g.custom_command('get-item', 'files_get_item')
        g.custom_command('get-subscription', 'files_get_subscription')
        g.custom_command('list-column', 'files_list_column')
        g.custom_command('list-content-type', 'files_list_content_type')
        g.custom_command('list-item', 'files_list_item')
        g.custom_command('list-subscription', 'files_list_subscription')
        g.custom_command('update-column', 'files_update_column')
        g.custom_command('update-content-type', 'files_update_content_type')
        g.custom_command('update-drive', 'files_update_drive')
        g.custom_command('update-item', 'files_update_item')
        g.custom_command('update-subscription', 'files_update_subscription')

    from azext_files.generated._client_factory import cf_share_list_content_type
    files_share_list_content_type = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._share_list_content_type_operations#ShareListConten'
        'tTypeOperations.{}',
        client_factory=cf_share_list_content_type)
    with self.command_group('files', files_share_list_content_type, client_factory=cf_share_list_content_type) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-column-link', 'files_create_column_link')
        g.custom_command('get-column-link', 'files_get_column_link')
        g.custom_command('list-column-link', 'files_list_column_link')
        g.custom_command('update-column-link', 'files_update_column_link')

    from azext_files.generated._client_factory import cf_share_list_item
    files_share_list_item = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._share_list_item_operations#ShareListItemOperations'
        '.{}',
        client_factory=cf_share_list_item)
    with self.command_group('files', files_share_list_item, client_factory=cf_share_list_item) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-version', 'files_create_version')
        g.custom_command('get-activity-by-interval53-ee', 'files_get_activity_by_interval53_ee')
        g.custom_command('get-activity-by-interval96-b0', 'files_get_activity_by_interval96_b0')
        g.custom_command('get-analytic', 'files_get_analytic')
        g.custom_command('get-drive-item', 'files_get_drive_item')
        g.custom_command('get-field', 'files_get_field')
        g.custom_command('get-ref-analytic', 'files_get_ref_analytic')
        g.custom_command('get-version', 'files_get_version')
        g.custom_command('list-version', 'files_list_version')
        g.custom_command('set-ref-analytic', 'files_set_ref_analytic')
        g.custom_command('update-drive-item', 'files_update_drive_item')
        g.custom_command('update-field', 'files_update_field')
        g.custom_command('update-version', 'files_update_version')

    from azext_files.generated._client_factory import cf_share_list_item_version
    files_share_list_item_version = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._share_list_item_version_operations#ShareListItemVe'
        'rsionOperations.{}',
        client_factory=cf_share_list_item_version)
    with self.command_group('files', files_share_list_item_version, client_factory=cf_share_list_item_version) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('get-field', 'files_get_field')
        g.custom_command('restore-version', 'files_restore_version')
        g.custom_command('update-field', 'files_update_field')

    from azext_files.generated._client_factory import cf_share_list_item
    files_share_list_item = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._share_list_item_operations#ShareListItemOperations'
        '.{}',
        client_factory=cf_share_list_item)
    with self.command_group('files', files_share_list_item, client_factory=cf_share_list_item) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-version', 'files_create_version')
        g.custom_command('get-activity-by-interval53-ee', 'files_get_activity_by_interval53_ee')
        g.custom_command('get-activity-by-interval96-b0', 'files_get_activity_by_interval96_b0')
        g.custom_command('get-analytic', 'files_get_analytic')
        g.custom_command('get-drive-item', 'files_get_drive_item')
        g.custom_command('get-field', 'files_get_field')
        g.custom_command('get-ref-analytic', 'files_get_ref_analytic')
        g.custom_command('get-version', 'files_get_version')
        g.custom_command('list-version', 'files_list_version')
        g.custom_command('set-ref-analytic', 'files_set_ref_analytic')
        g.custom_command('update-drive-item', 'files_update_drive_item')
        g.custom_command('update-field', 'files_update_field')
        g.custom_command('update-version', 'files_update_version')

    from azext_files.generated._client_factory import cf_share_list_item_version
    files_share_list_item_version = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._share_list_item_version_operations#ShareListItemVe'
        'rsionOperations.{}',
        client_factory=cf_share_list_item_version)
    with self.command_group('files', files_share_list_item_version, client_factory=cf_share_list_item_version) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('get-field', 'files_get_field')
        g.custom_command('restore-version', 'files_restore_version')
        g.custom_command('update-field', 'files_update_field')

    from azext_files.generated._client_factory import cf_share_permission
    files_share_permission = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._share_permission_operations#SharePermissionOperati'
        'ons.{}',
        client_factory=cf_share_permission)
    with self.command_group('files', files_share_permission, client_factory=cf_share_permission) as g:
        g.custom_command('grant', 'files_grant')

    from azext_files.generated._client_factory import cf_user
    files_user = CliCommandType(
        operations_tmpl='azext_files.vendored_sdks.files.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('files', files_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'files_delete', confirmation=True)
        g.custom_command('create-drive', 'files_create_drive')
        g.custom_command('get-drive', 'files_get_drive')
        g.custom_command('list-drive', 'files_list_drive')
        g.custom_command('update-drive', 'files_update_drive')
