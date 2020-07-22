# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines


def usersdevices_update(client,
                        user_id,
                        device_id,
                        id_=None,
                        deleted_date_time=None,
                        account_enabled=None,
                        alternative_security_ids=None,
                        approximate_last_sign_in_date_time=None,
                        compliance_expiration_date_time=None,
                        microsoft_graph_device_id=None,
                        device_metadata=None,
                        device_version=None,
                        display_name=None,
                        is_compliant=None,
                        is_managed=None,
                        on_premises_last_sync_date_time=None,
                        on_premises_sync_enabled=None,
                        operating_system=None,
                        operating_system_version=None,
                        physical_ids=None,
                        profile_type=None,
                        system_labels=None,
                        trust_type=None,
                        name=None,
                        manufacturer=None,
                        model=None,
                        kind=None,
                        status=None,
                        platform=None,
                        member_of=None,
                        registered_owners=None,
                        registered_users=None,
                        transitive_member_of=None,
                        extensions=None,
                        commands=None):
    return client.update_device(user_id=user_id,
                                device_id=device_id,
                                id=id_,
                                deleted_date_time=deleted_date_time,
                                account_enabled=account_enabled,
                                alternative_security_ids=alternative_security_ids,
                                approximate_last_sign_in_date_time=approximate_last_sign_in_date_time,
                                compliance_expiration_date_time=compliance_expiration_date_time,
                                microsoft_graph_device_id=microsoft_graph_device_id,
                                device_metadata=device_metadata,
                                device_version=device_version,
                                display_name=display_name,
                                is_compliant=is_compliant,
                                is_managed=is_managed,
                                on_premises_last_sync_date_time=on_premises_last_sync_date_time,
                                on_premises_sync_enabled=on_premises_sync_enabled,
                                operating_system=operating_system,
                                operating_system_version=operating_system_version,
                                physical_ids=physical_ids,
                                profile_type=profile_type,
                                system_labels=system_labels,
                                trust_type=trust_type,
                                name=name,
                                manufacturer=manufacturer,
                                model=model,
                                kind=kind,
                                status=status,
                                platform=platform,
                                member_of=member_of,
                                registered_owners=registered_owners,
                                registered_users=registered_users,
                                transitive_member_of=transitive_member_of,
                                extensions=extensions,
                                commands=commands)


def usersdevices_create_device(client,
                               user_id,
                               id_=None,
                               deleted_date_time=None,
                               account_enabled=None,
                               alternative_security_ids=None,
                               approximate_last_sign_in_date_time=None,
                               compliance_expiration_date_time=None,
                               device_id=None,
                               device_metadata=None,
                               device_version=None,
                               display_name=None,
                               is_compliant=None,
                               is_managed=None,
                               on_premises_last_sync_date_time=None,
                               on_premises_sync_enabled=None,
                               operating_system=None,
                               operating_system_version=None,
                               physical_ids=None,
                               profile_type=None,
                               system_labels=None,
                               trust_type=None,
                               name=None,
                               manufacturer=None,
                               model=None,
                               kind=None,
                               status=None,
                               platform=None,
                               member_of=None,
                               registered_owners=None,
                               registered_users=None,
                               transitive_member_of=None,
                               extensions=None,
                               commands=None):
    return client.create_device(user_id=user_id,
                                id=id_,
                                deleted_date_time=deleted_date_time,
                                account_enabled=account_enabled,
                                alternative_security_ids=alternative_security_ids,
                                approximate_last_sign_in_date_time=approximate_last_sign_in_date_time,
                                compliance_expiration_date_time=compliance_expiration_date_time,
                                device_id=device_id,
                                device_metadata=device_metadata,
                                device_version=device_version,
                                display_name=display_name,
                                is_compliant=is_compliant,
                                is_managed=is_managed,
                                on_premises_last_sync_date_time=on_premises_last_sync_date_time,
                                on_premises_sync_enabled=on_premises_sync_enabled,
                                operating_system=operating_system,
                                operating_system_version=operating_system_version,
                                physical_ids=physical_ids,
                                profile_type=profile_type,
                                system_labels=system_labels,
                                trust_type=trust_type,
                                name=name,
                                manufacturer=manufacturer,
                                model=model,
                                kind=kind,
                                status=status,
                                platform=platform,
                                member_of=member_of,
                                registered_owners=registered_owners,
                                registered_users=registered_users,
                                transitive_member_of=transitive_member_of,
                                extensions=extensions,
                                commands=commands)


def usersdevices_get_device(client,
                            user_id,
                            device_id,
                            select=None,
                            expand=None):
    return client.get_device(user_id=user_id,
                             device_id=device_id,
                             select=select,
                             expand=expand)


def usersdevices_list_device(client,
                             user_id,
                             orderby=None,
                             select=None,
                             expand=None):
    return client.list_device(user_id=user_id,
                              orderby=orderby,
                              select=select,
                              expand=expand)