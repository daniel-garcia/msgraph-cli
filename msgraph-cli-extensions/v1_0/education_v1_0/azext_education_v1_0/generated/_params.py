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
# pylint: disable=too-many-statements

from msgraph.cli.core.commands.parameters import get_enum_type
from msgraph.cli.core.commands.validators import validate_file_or_dict
from azext_education_v1_0.action import (
    AddTerm,
    AddCreatedByApplication,
    AddAddress
)


def load_arguments(self, _):

    with self.argument_context('education get-education-root') as c:
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education update-education-root') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('classes', type=validate_file_or_dict, help='Read-only. Nullable. Expected value: '
                   'json-string/@json-file.')
        c.argument('me', type=validate_file_or_dict, help='educationUser Expected value: json-string/@json-file.')
        c.argument('schools', type=validate_file_or_dict, help='Read-only. Nullable. Expected value: '
                   'json-string/@json-file.')
        c.argument('users', type=validate_file_or_dict, help='Read-only. Nullable. Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education delete') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('if_match', type=str, help='ETag')
        c.argument('education_school_id', type=str, help='key: id of educationSchool')
        c.argument('education_user_id', type=str, help='key: id of educationUser')

    with self.argument_context('education create-class') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('class_code', type=str, help='Class code used by the school to identify the class.')
        c.argument('description', type=str, help='Description of the class.')
        c.argument('display_name', type=str, help='Name of the class.')
        c.argument('external_id', type=str, help='ID of the class from the syncing system.')
        c.argument('external_name', type=str, help='Name of the class in the syncing system.')
        c.argument('external_source', arg_type=get_enum_type(['sis', 'manual', 'unknownFutureValue']), help='')
        c.argument('mail_nickname', type=str, help='Mail name for sending email to all members, if this is enabled.')
        c.argument('term', action=AddTerm, nargs='*', help='educationTerm')
        c.argument('group', type=validate_file_or_dict, help='Represents an Azure Active Directory object. The '
                   'directoryObject type is the base type for many other directory entity types. Expected value: '
                   'json-string/@json-file.')
        c.argument('members', type=validate_file_or_dict, help='All users in the class. Nullable. Expected value: '
                   'json-string/@json-file.')
        c.argument('schools', type=validate_file_or_dict, help='All schools that this class is associated with. '
                   'Nullable. Expected value: json-string/@json-file.')
        c.argument('teachers', type=validate_file_or_dict, help='All teachers in the class. Nullable. Expected value: '
                   'json-string/@json-file.')
        c.argument('created_by_application', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_device', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_user', action=AddCreatedByApplication, nargs='*', help='identity')

    with self.argument_context('education create-school') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('description', type=str, help='Organization description.')
        c.argument('display_name', type=str, help='Organization display name.')
        c.argument('external_source', arg_type=get_enum_type(['sis', 'manual', 'unknownFutureValue']), help='')
        c.argument('address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('external_id', type=str, help='ID of school in syncing system.')
        c.argument('external_principal_id', type=str, help='ID of principal in syncing system.')
        c.argument('fax', type=str, help='')
        c.argument('highest_grade', type=str, help='Highest grade taught.')
        c.argument('lowest_grade', type=str, help='Lowest grade taught.')
        c.argument('phone', type=str, help='Phone number of school.')
        c.argument('principal_email', type=str, help='Email address of the principal.')
        c.argument('principal_name', type=str, help='Name of the principal.')
        c.argument('school_number', type=str, help='School Number.')
        c.argument('classes', type=validate_file_or_dict, help='Classes taught at the school. Nullable. Expected '
                   'value: json-string/@json-file.')
        c.argument('users', type=validate_file_or_dict, help='Users in the school. Nullable. Expected value: '
                   'json-string/@json-file.')
        c.argument('created_by_application', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_device', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_user', action=AddCreatedByApplication, nargs='*', help='identity')

    with self.argument_context('education create-user') as c:
        c.argument('body', type=validate_file_or_dict, help='New navigation property Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education get-class') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education get-me') as c:
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education get-school') as c:
        c.argument('education_school_id', type=str, help='key: id of educationSchool')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education get-user') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-class') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-school') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-user') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education update-class') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('class_code', type=str, help='Class code used by the school to identify the class.')
        c.argument('description', type=str, help='Description of the class.')
        c.argument('display_name', type=str, help='Name of the class.')
        c.argument('external_id', type=str, help='ID of the class from the syncing system.')
        c.argument('external_name', type=str, help='Name of the class in the syncing system.')
        c.argument('external_source', arg_type=get_enum_type(['sis', 'manual', 'unknownFutureValue']), help='')
        c.argument('mail_nickname', type=str, help='Mail name for sending email to all members, if this is enabled.')
        c.argument('term', action=AddTerm, nargs='*', help='educationTerm')
        c.argument('group', type=validate_file_or_dict, help='Represents an Azure Active Directory object. The '
                   'directoryObject type is the base type for many other directory entity types. Expected value: '
                   'json-string/@json-file.')
        c.argument('members', type=validate_file_or_dict, help='All users in the class. Nullable. Expected value: '
                   'json-string/@json-file.')
        c.argument('schools', type=validate_file_or_dict, help='All schools that this class is associated with. '
                   'Nullable. Expected value: json-string/@json-file.')
        c.argument('teachers', type=validate_file_or_dict, help='All teachers in the class. Nullable. Expected value: '
                   'json-string/@json-file.')
        c.argument('created_by_application', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_device', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_user', action=AddCreatedByApplication, nargs='*', help='identity')

    with self.argument_context('education update-me') as c:
        c.argument('body', type=validate_file_or_dict, help='New navigation property values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education update-school') as c:
        c.argument('education_school_id', type=str, help='key: id of educationSchool')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('description', type=str, help='Organization description.')
        c.argument('display_name', type=str, help='Organization display name.')
        c.argument('external_source', arg_type=get_enum_type(['sis', 'manual', 'unknownFutureValue']), help='')
        c.argument('address', action=AddAddress, nargs='*', help='physicalAddress')
        c.argument('external_id', type=str, help='ID of school in syncing system.')
        c.argument('external_principal_id', type=str, help='ID of principal in syncing system.')
        c.argument('fax', type=str, help='')
        c.argument('highest_grade', type=str, help='Highest grade taught.')
        c.argument('lowest_grade', type=str, help='Lowest grade taught.')
        c.argument('phone', type=str, help='Phone number of school.')
        c.argument('principal_email', type=str, help='Email address of the principal.')
        c.argument('principal_name', type=str, help='Name of the principal.')
        c.argument('school_number', type=str, help='School Number.')
        c.argument('classes', type=validate_file_or_dict, help='Classes taught at the school. Nullable. Expected '
                   'value: json-string/@json-file.')
        c.argument('users', type=validate_file_or_dict, help='Users in the school. Nullable. Expected value: '
                   'json-string/@json-file.')
        c.argument('created_by_application', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_device', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_user', action=AddCreatedByApplication, nargs='*', help='identity')

    with self.argument_context('education update-user') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('body', type=validate_file_or_dict, help='New navigation property values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education delete') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('education create-ref-member') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref value Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education create-ref-school') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref value Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education create-ref-teacher') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref value Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education get-group') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education get-ref-group') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')

    with self.argument_context('education list-member') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-ref-member') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('orderby', nargs='*', help='Order items by property values')

    with self.argument_context('education list-ref-school') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('orderby', nargs='*', help='Order items by property values')

    with self.argument_context('education list-ref-teacher') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('orderby', nargs='*', help='Order items by property values')

    with self.argument_context('education list-school') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-teacher') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education set-ref-group') as c:
        c.argument('education_class_id', type=str, help='key: id of educationClass')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education delete') as c:
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('education create-ref-class') as c:
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref value Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education create-ref-school') as c:
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref value Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education get-user') as c:
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-class') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-ref-class') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')

    with self.argument_context('education list-ref-school') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')

    with self.argument_context('education list-school') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education set-ref-user') as c:
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education create-ref-class') as c:
        c.argument('education_school_id', type=str, help='key: id of educationSchool')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref value Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education create-ref-user') as c:
        c.argument('education_school_id', type=str, help='key: id of educationSchool')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref value Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education list-class') as c:
        c.argument('education_school_id', type=str, help='key: id of educationSchool')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-ref-class') as c:
        c.argument('education_school_id', type=str, help='key: id of educationSchool')
        c.argument('orderby', nargs='*', help='Order items by property values')

    with self.argument_context('education list-ref-user') as c:
        c.argument('education_school_id', type=str, help='key: id of educationSchool')
        c.argument('orderby', nargs='*', help='Order items by property values')

    with self.argument_context('education list-user') as c:
        c.argument('education_school_id', type=str, help='key: id of educationSchool')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education delete') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('education create-ref-class') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref value Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education create-ref-school') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref value Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('education get-ref-user') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')

    with self.argument_context('education get-user') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-class') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education list-ref-class') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('orderby', nargs='*', help='Order items by property values')

    with self.argument_context('education list-ref-school') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('orderby', nargs='*', help='Order items by property values')

    with self.argument_context('education list-school') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('education set-ref-user') as c:
        c.argument('education_user_id', type=str, help='key: id of educationUser')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')
