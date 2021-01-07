# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_identitydirmgt_beta.generated._client_factory import cf_administrative_unit_administrative_unit
    identitydirmgt_beta_administrative_unit_administrative_unit = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._administrative_unit_adminis'
        'trative_unit_operations#AdministrativeUnitAdministrativeUnitOperations.{}',
        client_factory=cf_administrative_unit_administrative_unit)
    with self.command_group('identitydirmgt', identitydirmgt_beta_administrative_unit_administrative_unit,
                            client_factory=cf_administrative_unit_administrative_unit) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-administrative-unit', 'identitydirmgt_create_administrative_unit')
        g.custom_command('get-administrative-unit', 'identitydirmgt_get_administrative_unit')
        g.custom_command('list-administrative-unit', 'identitydirmgt_list_administrative_unit')
        g.custom_command('update-administrative-unit', 'identitydirmgt_update_administrative_unit')

    from azext_identitydirmgt_beta.generated._client_factory import cf_administrative_unit
    identitydirmgt_beta_administrative_unit = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._administrative_unit_operati'
        'ons#AdministrativeUnitOperations.{}',
        client_factory=cf_administrative_unit)
    with self.command_group('identitydirmgt', identitydirmgt_beta_administrative_unit,
                            client_factory=cf_administrative_unit) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('check-member-group', 'identitydirmgt_check_member_group')
        g.custom_command('check-member-object', 'identitydirmgt_check_member_object')
        g.custom_command('create-extension', 'identitydirmgt_create_extension')
        g.custom_command('create-ref-member', 'identitydirmgt_create_ref_member')
        g.custom_command('create-scoped-role-member', 'identitydirmgt_create_scoped_role_member')
        g.custom_command('delta', 'identitydirmgt_delta')
        g.custom_command('get-by-id', 'identitydirmgt_get_by_id')
        g.custom_command('get-extension', 'identitydirmgt_get_extension')
        g.custom_command('get-member-group', 'identitydirmgt_get_member_group')
        g.custom_command('get-member-object', 'identitydirmgt_get_member_object')
        g.custom_command('get-scoped-role-member', 'identitydirmgt_get_scoped_role_member')
        g.custom_command('get-user-owned-object', 'identitydirmgt_get_user_owned_object')
        g.custom_command('list-extension', 'identitydirmgt_list_extension')
        g.custom_command('list-member', 'identitydirmgt_list_member')
        g.custom_command('list-ref-member', 'identitydirmgt_list_ref_member')
        g.custom_command('list-scoped-role-member', 'identitydirmgt_list_scoped_role_member')
        g.custom_command('restore', 'identitydirmgt_restore')
        g.custom_command('update-extension', 'identitydirmgt_update_extension')
        g.custom_command('update-scoped-role-member', 'identitydirmgt_update_scoped_role_member')
        g.custom_command('validate-property', 'identitydirmgt_validate_property')

    from azext_identitydirmgt_beta.generated._client_factory import cf_contact_org_contact
    identitydirmgt_beta_contact_org_contact = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._contact_org_contact_operati'
        'ons#ContactOrgContactOperations.{}',
        client_factory=cf_contact_org_contact)
    with self.command_group('identitydirmgt', identitydirmgt_beta_contact_org_contact,
                            client_factory=cf_contact_org_contact) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-org-contact', 'identitydirmgt_create_org_contact')
        g.custom_command('get-org-contact', 'identitydirmgt_get_org_contact')
        g.custom_command('list-org-contact', 'identitydirmgt_list_org_contact')
        g.custom_command('update-org-contact', 'identitydirmgt_update_org_contact')

    from azext_identitydirmgt_beta.generated._client_factory import cf_contact
    identitydirmgt_beta_contact = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._contact_operations#ContactO'
        'perations.{}',
        client_factory=cf_contact)
    with self.command_group('identitydirmgt', identitydirmgt_beta_contact, client_factory=cf_contact) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('check-member-group', 'identitydirmgt_check_member_group')
        g.custom_command('check-member-object', 'identitydirmgt_check_member_object')
        g.custom_command('create-ref-direct-report', 'identitydirmgt_create_ref_direct_report')
        g.custom_command('create-ref-member-of', 'identitydirmgt_create_ref_member_of')
        g.custom_command('create-ref-transitive-member-of', 'identitydirmgt_create_ref_transitive_member_of')
        g.custom_command('delta', 'identitydirmgt_delta')
        g.custom_command('get-by-id', 'identitydirmgt_get_by_id')
        g.custom_command('get-manager', 'identitydirmgt_get_manager')
        g.custom_command('get-member-group', 'identitydirmgt_get_member_group')
        g.custom_command('get-member-object', 'identitydirmgt_get_member_object')
        g.custom_command('get-ref-manager', 'identitydirmgt_get_ref_manager')
        g.custom_command('get-user-owned-object', 'identitydirmgt_get_user_owned_object')
        g.custom_command('list-direct-report', 'identitydirmgt_list_direct_report')
        g.custom_command('list-member-of', 'identitydirmgt_list_member_of')
        g.custom_command('list-ref-direct-report', 'identitydirmgt_list_ref_direct_report')
        g.custom_command('list-ref-member-of', 'identitydirmgt_list_ref_member_of')
        g.custom_command('list-ref-transitive-member-of', 'identitydirmgt_list_ref_transitive_member_of')
        g.custom_command('list-transitive-member-of', 'identitydirmgt_list_transitive_member_of')
        g.custom_command('restore', 'identitydirmgt_restore')
        g.custom_command('set-ref-manager', 'identitydirmgt_set_ref_manager')
        g.custom_command('validate-property', 'identitydirmgt_validate_property')

    from azext_identitydirmgt_beta.generated._client_factory import cf_contract_contract
    identitydirmgt_beta_contract_contract = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._contract_contract_operation'
        's#ContractContractOperations.{}',
        client_factory=cf_contract_contract)
    with self.command_group('identitydirmgt', identitydirmgt_beta_contract_contract,
                            client_factory=cf_contract_contract) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-contract', 'identitydirmgt_create_contract')
        g.custom_command('get-contract', 'identitydirmgt_get_contract')
        g.custom_command('list-contract', 'identitydirmgt_list_contract')
        g.custom_command('update-contract', 'identitydirmgt_update_contract')

    from azext_identitydirmgt_beta.generated._client_factory import cf_contract
    identitydirmgt_beta_contract = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._contract_operations#Contrac'
        'tOperations.{}',
        client_factory=cf_contract)
    with self.command_group('identitydirmgt', identitydirmgt_beta_contract, client_factory=cf_contract) as g:
        g.custom_command('check-member-group', 'identitydirmgt_check_member_group')
        g.custom_command('check-member-object', 'identitydirmgt_check_member_object')
        g.custom_command('get-by-id', 'identitydirmgt_get_by_id')
        g.custom_command('get-member-group', 'identitydirmgt_get_member_group')
        g.custom_command('get-member-object', 'identitydirmgt_get_member_object')
        g.custom_command('get-user-owned-object', 'identitydirmgt_get_user_owned_object')
        g.custom_command('restore', 'identitydirmgt_restore')
        g.custom_command('validate-property', 'identitydirmgt_validate_property')

    from azext_identitydirmgt_beta.generated._client_factory import cf_device_device
    identitydirmgt_beta_device_device = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._device_device_operations#De'
        'viceDeviceOperations.{}',
        client_factory=cf_device_device)
    with self.command_group('identitydirmgt', identitydirmgt_beta_device_device,
                            client_factory=cf_device_device) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-device', 'identitydirmgt_create_device')
        g.custom_command('get-device', 'identitydirmgt_get_device')
        g.custom_command('list-device', 'identitydirmgt_list_device')
        g.custom_command('update-device', 'identitydirmgt_update_device')

    from azext_identitydirmgt_beta.generated._client_factory import cf_device
    identitydirmgt_beta_device = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._device_operations#DeviceOpe'
        'rations.{}',
        client_factory=cf_device)
    with self.command_group('identitydirmgt', identitydirmgt_beta_device, client_factory=cf_device) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('check-member-group', 'identitydirmgt_check_member_group')
        g.custom_command('check-member-object', 'identitydirmgt_check_member_object')
        g.custom_command('create-command', 'identitydirmgt_create_command')
        g.custom_command('create-extension', 'identitydirmgt_create_extension')
        g.custom_command('create-ref-member-of', 'identitydirmgt_create_ref_member_of')
        g.custom_command('create-ref-registered-owner', 'identitydirmgt_create_ref_registered_owner')
        g.custom_command('create-ref-registered-user', 'identitydirmgt_create_ref_registered_user')
        g.custom_command('create-ref-transitive-member-of', 'identitydirmgt_create_ref_transitive_member_of')
        g.custom_command('get-by-id', 'identitydirmgt_get_by_id')
        g.custom_command('get-command', 'identitydirmgt_get_command')
        g.custom_command('get-extension', 'identitydirmgt_get_extension')
        g.custom_command('get-member-group', 'identitydirmgt_get_member_group')
        g.custom_command('get-member-object', 'identitydirmgt_get_member_object')
        g.custom_command('get-user-owned-object', 'identitydirmgt_get_user_owned_object')
        g.custom_command('list-command', 'identitydirmgt_list_command')
        g.custom_command('list-extension', 'identitydirmgt_list_extension')
        g.custom_command('list-member-of', 'identitydirmgt_list_member_of')
        g.custom_command('list-ref-member-of', 'identitydirmgt_list_ref_member_of')
        g.custom_command('list-ref-registered-owner', 'identitydirmgt_list_ref_registered_owner')
        g.custom_command('list-ref-registered-user', 'identitydirmgt_list_ref_registered_user')
        g.custom_command('list-ref-transitive-member-of', 'identitydirmgt_list_ref_transitive_member_of')
        g.custom_command('list-registered-owner', 'identitydirmgt_list_registered_owner')
        g.custom_command('list-registered-user', 'identitydirmgt_list_registered_user')
        g.custom_command('list-transitive-member-of', 'identitydirmgt_list_transitive_member_of')
        g.custom_command('restore', 'identitydirmgt_restore')
        g.custom_command('update-command', 'identitydirmgt_update_command')
        g.custom_command('update-extension', 'identitydirmgt_update_extension')
        g.custom_command('validate-property', 'identitydirmgt_validate_property')

    from azext_identitydirmgt_beta.generated._client_factory import cf_directory_directory
    identitydirmgt_beta_directory_directory = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._directory_directory_operati'
        'ons#DirectoryDirectoryOperations.{}',
        client_factory=cf_directory_directory)
    with self.command_group('identitydirmgt', identitydirmgt_beta_directory_directory,
                            client_factory=cf_directory_directory) as g:
        g.custom_command('get-directory', 'identitydirmgt_get_directory')
        g.custom_command('update-directory', 'identitydirmgt_update_directory')

    from azext_identitydirmgt_beta.generated._client_factory import cf_directory
    identitydirmgt_beta_directory = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._directory_operations#Direct'
        'oryOperations.{}',
        client_factory=cf_directory)
    with self.command_group('identitydirmgt', identitydirmgt_beta_directory, client_factory=cf_directory) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-administrative-unit', 'identitydirmgt_create_administrative_unit')
        g.custom_command('create-deleted-item', 'identitydirmgt_create_deleted_item')
        g.custom_command('create-feature-rollout-policy', 'identitydirmgt_create_feature_rollout_policy')
        g.custom_command('get-administrative-unit', 'identitydirmgt_get_administrative_unit')
        g.custom_command('get-deleted-item', 'identitydirmgt_get_deleted_item')
        g.custom_command('get-feature-rollout-policy', 'identitydirmgt_get_feature_rollout_policy')
        g.custom_command('list-administrative-unit', 'identitydirmgt_list_administrative_unit')
        g.custom_command('list-deleted-item', 'identitydirmgt_list_deleted_item')
        g.custom_command('list-feature-rollout-policy', 'identitydirmgt_list_feature_rollout_policy')
        g.custom_command('update-administrative-unit', 'identitydirmgt_update_administrative_unit')
        g.custom_command('update-deleted-item', 'identitydirmgt_update_deleted_item')
        g.custom_command('update-feature-rollout-policy', 'identitydirmgt_update_feature_rollout_policy')

    from azext_identitydirmgt_beta.generated._client_factory import cf_directory_feature_rollout_policy
    identitydirmgt_beta_directory_feature_rollout_policy = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._directory_feature_rollout_p'
        'olicy_operations#DirectoryFeatureRolloutPolicyOperations.{}',
        client_factory=cf_directory_feature_rollout_policy)
    with self.command_group('identitydirmgt', identitydirmgt_beta_directory_feature_rollout_policy,
                            client_factory=cf_directory_feature_rollout_policy) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-apply-to', 'identitydirmgt_create_apply_to')
        g.custom_command('get-apply-to', 'identitydirmgt_get_apply_to')
        g.custom_command('list-apply-to', 'identitydirmgt_list_apply_to')
        g.custom_command('update-apply-to', 'identitydirmgt_update_apply_to')

    from azext_identitydirmgt_beta.generated._client_factory import cf_directory_role_directory_role
    identitydirmgt_beta_directory_role_directory_role = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._directory_role_directory_ro'
        'le_operations#DirectoryRoleDirectoryRoleOperations.{}',
        client_factory=cf_directory_role_directory_role)
    with self.command_group('identitydirmgt', identitydirmgt_beta_directory_role_directory_role,
                            client_factory=cf_directory_role_directory_role) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-directory-role', 'identitydirmgt_create_directory_role')
        g.custom_command('get-directory-role', 'identitydirmgt_get_directory_role')
        g.custom_command('list-directory-role', 'identitydirmgt_list_directory_role')
        g.custom_command('update-directory-role', 'identitydirmgt_update_directory_role')

    from azext_identitydirmgt_beta.generated._client_factory import cf_directory_role
    identitydirmgt_beta_directory_role = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._directory_role_operations#D'
        'irectoryRoleOperations.{}',
        client_factory=cf_directory_role)
    with self.command_group('identitydirmgt', identitydirmgt_beta_directory_role,
                            client_factory=cf_directory_role) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('check-member-group', 'identitydirmgt_check_member_group')
        g.custom_command('check-member-object', 'identitydirmgt_check_member_object')
        g.custom_command('create-ref-member', 'identitydirmgt_create_ref_member')
        g.custom_command('create-scoped-member', 'identitydirmgt_create_scoped_member')
        g.custom_command('delta', 'identitydirmgt_delta')
        g.custom_command('get-by-id', 'identitydirmgt_get_by_id')
        g.custom_command('get-member-group', 'identitydirmgt_get_member_group')
        g.custom_command('get-member-object', 'identitydirmgt_get_member_object')
        g.custom_command('get-scoped-member', 'identitydirmgt_get_scoped_member')
        g.custom_command('get-user-owned-object', 'identitydirmgt_get_user_owned_object')
        g.custom_command('list-member', 'identitydirmgt_list_member')
        g.custom_command('list-ref-member', 'identitydirmgt_list_ref_member')
        g.custom_command('list-scoped-member', 'identitydirmgt_list_scoped_member')
        g.custom_command('restore', 'identitydirmgt_restore')
        g.custom_command('update-scoped-member', 'identitydirmgt_update_scoped_member')
        g.custom_command('validate-property', 'identitydirmgt_validate_property')

    from azext_identitydirmgt_beta.generated._client_factory import cf_directory_role_template_directory_role_template
    identitydirmgt_beta_directory_role_template_directory_role_template = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._directory_role_template_dir'
        'ectory_role_template_operations#DirectoryRoleTemplateDirectoryRoleTemplateOperations.{}',
        client_factory=cf_directory_role_template_directory_role_template)
    with self.command_group('identitydirmgt', identitydirmgt_beta_directory_role_template_directory_role_template,
                            client_factory=cf_directory_role_template_directory_role_template) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-directory-role-template', 'identitydirmgt_create_directory_role_template')
        g.custom_command('get-directory-role-template', 'identitydirmgt_get_directory_role_template')
        g.custom_command('list-directory-role-template', 'identitydirmgt_list_directory_role_template')
        g.custom_command('update-directory-role-template', 'identitydirmgt_update_directory_role_template')

    from azext_identitydirmgt_beta.generated._client_factory import cf_directory_role_template
    identitydirmgt_beta_directory_role_template = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._directory_role_template_ope'
        'rations#DirectoryRoleTemplateOperations.{}',
        client_factory=cf_directory_role_template)
    with self.command_group('identitydirmgt', identitydirmgt_beta_directory_role_template,
                            client_factory=cf_directory_role_template) as g:
        g.custom_command('check-member-group', 'identitydirmgt_check_member_group')
        g.custom_command('check-member-object', 'identitydirmgt_check_member_object')
        g.custom_command('get-by-id', 'identitydirmgt_get_by_id')
        g.custom_command('get-member-group', 'identitydirmgt_get_member_group')
        g.custom_command('get-member-object', 'identitydirmgt_get_member_object')
        g.custom_command('get-user-owned-object', 'identitydirmgt_get_user_owned_object')
        g.custom_command('restore', 'identitydirmgt_restore')
        g.custom_command('validate-property', 'identitydirmgt_validate_property')

    from azext_identitydirmgt_beta.generated._client_factory import cf_directory_setting_template_directory_setting_template
    identitydirmgt_beta_directory_setting_template_directory_setting_template = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._directory_setting_template_'
        'directory_setting_template_operations#DirectorySettingTemplateDirectorySettingTemplateOperations.{}',
        client_factory=cf_directory_setting_template_directory_setting_template)
    with self.command_group('identitydirmgt',
                            identitydirmgt_beta_directory_setting_template_directory_setting_template,
                            client_factory=cf_directory_setting_template_directory_setting_template) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-directory-setting-template', 'identitydirmgt_create_directory_setting_template')
        g.custom_command('get-directory-setting-template', 'identitydirmgt_get_directory_setting_template')
        g.custom_command('list-directory-setting-template', 'identitydirmgt_list_directory_setting_template')
        g.custom_command('update-directory-setting-template', 'identitydirmgt_update_directory_setting_template')

    from azext_identitydirmgt_beta.generated._client_factory import cf_directory_setting_template
    identitydirmgt_beta_directory_setting_template = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._directory_setting_template_'
        'operations#DirectorySettingTemplateOperations.{}',
        client_factory=cf_directory_setting_template)
    with self.command_group('identitydirmgt', identitydirmgt_beta_directory_setting_template,
                            client_factory=cf_directory_setting_template) as g:
        g.custom_command('check-member-group', 'identitydirmgt_check_member_group')
        g.custom_command('check-member-object', 'identitydirmgt_check_member_object')
        g.custom_command('get-by-id', 'identitydirmgt_get_by_id')
        g.custom_command('get-member-group', 'identitydirmgt_get_member_group')
        g.custom_command('get-member-object', 'identitydirmgt_get_member_object')
        g.custom_command('get-user-owned-object', 'identitydirmgt_get_user_owned_object')
        g.custom_command('restore', 'identitydirmgt_restore')
        g.custom_command('validate-property', 'identitydirmgt_validate_property')

    from azext_identitydirmgt_beta.generated._client_factory import cf_domain_domain
    identitydirmgt_beta_domain_domain = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._domain_domain_operations#Do'
        'mainDomainOperations.{}',
        client_factory=cf_domain_domain)
    with self.command_group('identitydirmgt', identitydirmgt_beta_domain_domain,
                            client_factory=cf_domain_domain) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-domain', 'identitydirmgt_create_domain')
        g.custom_command('get-domain', 'identitydirmgt_get_domain')
        g.custom_command('list-domain', 'identitydirmgt_list_domain')
        g.custom_command('update-domain', 'identitydirmgt_update_domain')

    from azext_identitydirmgt_beta.generated._client_factory import cf_domain
    identitydirmgt_beta_domain = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._domain_operations#DomainOpe'
        'rations.{}',
        client_factory=cf_domain)
    with self.command_group('identitydirmgt', identitydirmgt_beta_domain, client_factory=cf_domain) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-ref-domain-name-reference', 'identitydirmgt_create_ref_domain_name_reference')
        g.custom_command('create-service-configuration-record', 'identitydirmgt_create_service_configuration_record')
        g.custom_command('create-verification-dns-record', 'identitydirmgt_create_verification_dns_record')
        g.custom_command('force-delete', 'identitydirmgt_force_delete')
        g.custom_command('get-service-configuration-record', 'identitydirmgt_get_service_configuration_record')
        g.custom_command('get-verification-dns-record', 'identitydirmgt_get_verification_dns_record')
        g.custom_command('list-domain-name-reference', 'identitydirmgt_list_domain_name_reference')
        g.custom_command('list-ref-domain-name-reference', 'identitydirmgt_list_ref_domain_name_reference')
        g.custom_command('list-service-configuration-record', 'identitydirmgt_list_service_configuration_record')
        g.custom_command('list-verification-dns-record', 'identitydirmgt_list_verification_dns_record')
        g.custom_command('update-service-configuration-record', 'identitydirmgt_update_service_configuration_record')
        g.custom_command('update-verification-dns-record', 'identitydirmgt_update_verification_dns_record')
        g.custom_command('verify', 'identitydirmgt_verify')

    from azext_identitydirmgt_beta.generated._client_factory import cf_organization_organization
    identitydirmgt_beta_organization_organization = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._organization_organization_o'
        'perations#OrganizationOrganizationOperations.{}',
        client_factory=cf_organization_organization)
    with self.command_group('identitydirmgt', identitydirmgt_beta_organization_organization,
                            client_factory=cf_organization_organization) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-organization', 'identitydirmgt_create_organization')
        g.custom_command('get-organization', 'identitydirmgt_get_organization')
        g.custom_command('list-organization', 'identitydirmgt_list_organization')
        g.custom_command('update-organization', 'identitydirmgt_update_organization')

    from azext_identitydirmgt_beta.generated._client_factory import cf_organization
    identitydirmgt_beta_organization = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._organization_operations#Org'
        'anizationOperations.{}',
        client_factory=cf_organization)
    with self.command_group('identitydirmgt', identitydirmgt_beta_organization, client_factory=cf_organization) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('check-member-group', 'identitydirmgt_check_member_group')
        g.custom_command('check-member-object', 'identitydirmgt_check_member_object')
        g.custom_command('create-extension', 'identitydirmgt_create_extension')
        g.custom_command('get-branding', 'identitydirmgt_get_branding')
        g.custom_command('get-by-id', 'identitydirmgt_get_by_id')
        g.custom_command('get-extension', 'identitydirmgt_get_extension')
        g.custom_command('get-member-group', 'identitydirmgt_get_member_group')
        g.custom_command('get-member-object', 'identitydirmgt_get_member_object')
        g.custom_command('get-setting', 'identitydirmgt_get_setting')
        g.custom_command('get-user-owned-object', 'identitydirmgt_get_user_owned_object')
        g.custom_command('list-extension', 'identitydirmgt_list_extension')
        g.custom_command('restore', 'identitydirmgt_restore')
        g.custom_command('set-mobile-device-management-authority', 'identitydirmgt_set_mobile_device_management_authori'
                         'ty')
        g.custom_command('update-branding', 'identitydirmgt_update_branding')
        g.custom_command('update-extension', 'identitydirmgt_update_extension')
        g.custom_command('update-setting', 'identitydirmgt_update_setting')
        g.custom_command('validate-property', 'identitydirmgt_validate_property')

    from azext_identitydirmgt_beta.generated._client_factory import cf_organization_setting
    identitydirmgt_beta_organization_setting = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._organization_setting_operat'
        'ions#OrganizationSettingOperations.{}',
        client_factory=cf_organization_setting)
    with self.command_group('identitydirmgt', identitydirmgt_beta_organization_setting,
                            client_factory=cf_organization_setting) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-profile-card-property', 'identitydirmgt_create_profile_card_property')
        g.custom_command('get-item-insight', 'identitydirmgt_get_item_insight')
        g.custom_command('get-profile-card-property', 'identitydirmgt_get_profile_card_property')
        g.custom_command('list-profile-card-property', 'identitydirmgt_list_profile_card_property')
        g.custom_command('update-item-insight', 'identitydirmgt_update_item_insight')
        g.custom_command('update-profile-card-property', 'identitydirmgt_update_profile_card_property')

    from azext_identitydirmgt_beta.generated._client_factory import cf_setting_directory_setting
    identitydirmgt_beta_setting_directory_setting = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._setting_directory_setting_o'
        'perations#SettingDirectorySettingOperations.{}',
        client_factory=cf_setting_directory_setting)
    with self.command_group('identitydirmgt', identitydirmgt_beta_setting_directory_setting,
                            client_factory=cf_setting_directory_setting) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-directory-setting', 'identitydirmgt_create_directory_setting')
        g.custom_command('get-directory-setting', 'identitydirmgt_get_directory_setting')
        g.custom_command('list-directory-setting', 'identitydirmgt_list_directory_setting')
        g.custom_command('update-directory-setting', 'identitydirmgt_update_directory_setting')

    from azext_identitydirmgt_beta.generated._client_factory import cf_subscribed_sku_subscribed_sku
    identitydirmgt_beta_subscribed_sku_subscribed_sku = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._subscribed_sku_subscribed_s'
        'ku_operations#SubscribedSkuSubscribedSkuOperations.{}',
        client_factory=cf_subscribed_sku_subscribed_sku)
    with self.command_group('identitydirmgt', identitydirmgt_beta_subscribed_sku_subscribed_sku,
                            client_factory=cf_subscribed_sku_subscribed_sku) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-subscribed-sku', 'identitydirmgt_create_subscribed_sku')
        g.custom_command('get-subscribed-sku', 'identitydirmgt_get_subscribed_sku')
        g.custom_command('list-subscribed-sku', 'identitydirmgt_list_subscribed_sku')
        g.custom_command('update-subscribed-sku', 'identitydirmgt_update_subscribed_sku')

    from azext_identitydirmgt_beta.generated._client_factory import cf_user
    identitydirmgt_beta_user = CliCommandType(
        operations_tmpl='azext_identitydirmgt_beta.vendored_sdks.identitydirmgt.operations._user_operations#UserOperati'
        'ons.{}',
        client_factory=cf_user)
    with self.command_group('identitydirmgt', identitydirmgt_beta_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'identitydirmgt_delete', confirmation=True)
        g.custom_command('create-scoped-role-member-of', 'identitydirmgt_create_scoped_role_member_of')
        g.custom_command('get-scoped-role-member-of', 'identitydirmgt_get_scoped_role_member_of')
        g.custom_command('list-scoped-role-member-of', 'identitydirmgt_list_scoped_role_member_of')
        g.custom_command('update-scoped-role-member-of', 'identitydirmgt_update_scoped_role_member_of')