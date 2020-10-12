# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddNamedLocations(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddNamedLocations, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'created-date-time':
                d['created_date_time'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'modified-date-time':
                d['modified_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddGrantControls(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.grant_controls = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'built-in-controls':
                d['built_in_controls'] = v
            elif kl == 'custom-authentication-factors':
                d['custom_authentication_factors'] = v
            elif kl == 'operator':
                d['operator'] = v[0]
            elif kl == 'terms-of-use':
                d['terms_of_use'] = v
        return d


class AddSessionControlsApplicationEnforcedRestrictions(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.session_controls_application_enforced_restrictions = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'is-enabled':
                d['is_enabled'] = v[0]
        return d


class AddSessionControlsCloudAppSecurity(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.session_controls_cloud_app_security = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'cloud-app-security-type':
                d['cloud_app_security_type'] = v[0]
            elif kl == 'is-enabled':
                d['is_enabled'] = v[0]
        return d


class AddSessionControlsPersistentBrowser(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.session_controls_persistent_browser = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'mode':
                d['mode'] = v[0]
            elif kl == 'is-enabled':
                d['is_enabled'] = v[0]
        return d


class AddSessionControlsSignInFrequency(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.session_controls_sign_in_frequency = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'type':
                d['type'] = v[0]
            elif kl == 'value':
                d['value'] = v[0]
            elif kl == 'is-enabled':
                d['is_enabled'] = v[0]
        return d


class AddConditionsApplications(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.conditions_applications = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'exclude-applications':
                d['exclude_applications'] = v
            elif kl == 'include-applications':
                d['include_applications'] = v
            elif kl == 'include-user-actions':
                d['include_user_actions'] = v
        return d


class AddConditionsLocations(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.conditions_locations = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'exclude-locations':
                d['exclude_locations'] = v
            elif kl == 'include-locations':
                d['include_locations'] = v
        return d


class AddConditionsPlatforms(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.conditions_platforms = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'exclude-platforms':
                d['exclude_platforms'] = v
            elif kl == 'include-platforms':
                d['include_platforms'] = v
        return d


class AddConditionsUsers(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.conditions_users = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'exclude-groups':
                d['exclude_groups'] = v
            elif kl == 'exclude-roles':
                d['exclude_roles'] = v
            elif kl == 'exclude-users':
                d['exclude_users'] = v
            elif kl == 'include-groups':
                d['include_groups'] = v
            elif kl == 'include-roles':
                d['include_roles'] = v
            elif kl == 'include-users':
                d['include_users'] = v
        return d


class AddResults(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddResults, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'created-date-time':
                d['created_date_time'] = v[0]
            elif kl == 'message':
                d['message'] = v[0]
            elif kl == 'result-type':
                d['result_type'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddCreatedByApplication(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.created_by_application = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddActivityBasedTimeoutPolicies(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddActivityBasedTimeoutPolicies, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'definition':
                d['definition'] = v
            elif kl == 'is-organization-default':
                d['is_organization_default'] = v[0]
            elif kl == 'applies-to':
                d['applies_to'] = v
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddClaimsMappingPolicies(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddClaimsMappingPolicies, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'definition':
                d['definition'] = v
            elif kl == 'is-organization-default':
                d['is_organization_default'] = v[0]
            elif kl == 'applies-to':
                d['applies_to'] = v
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddHomeRealmDiscoveryPolicies(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddHomeRealmDiscoveryPolicies, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'definition':
                d['definition'] = v
            elif kl == 'is-organization-default':
                d['is_organization_default'] = v[0]
            elif kl == 'applies-to':
                d['applies_to'] = v
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddTokenIssuancePolicies(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddTokenIssuancePolicies, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'definition':
                d['definition'] = v
            elif kl == 'is-organization-default':
                d['is_organization_default'] = v[0]
            elif kl == 'applies-to':
                d['applies_to'] = v
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddTokenLifetimePolicies(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddTokenLifetimePolicies, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'definition':
                d['definition'] = v
            elif kl == 'is-organization-default':
                d['is_organization_default'] = v[0]
            elif kl == 'applies-to':
                d['applies_to'] = v
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddIdentitySecurityDefaultsEnforcementPolicy(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.identity_security_defaults_enforcement_policy = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'is-enabled':
                d['is_enabled'] = v[0]
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddAppliesTo(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAppliesTo, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddExcludes(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddExcludes, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'client-application-ids':
                d['client_application_ids'] = v
            elif kl == 'client-application-publisher-ids':
                d['client_application_publisher_ids'] = v
            elif kl == 'client-applications-from-verified-publisher-only':
                d['client_applications_from_verified_publisher_only'] = v[0]
            elif kl == 'client-application-tenant-ids':
                d['client_application_tenant_ids'] = v
            elif kl == 'permission-classification':
                d['permission_classification'] = v[0]
            elif kl == 'permissions':
                d['permissions'] = v
            elif kl == 'permission-type':
                d['permission_type'] = v[0]
            elif kl == 'resource-application':
                d['resource_application'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddIncludes(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddIncludes, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'client-application-ids':
                d['client_application_ids'] = v
            elif kl == 'client-application-publisher-ids':
                d['client_application_publisher_ids'] = v
            elif kl == 'client-applications-from-verified-publisher-only':
                d['client_applications_from_verified_publisher_only'] = v[0]
            elif kl == 'client-application-tenant-ids':
                d['client_application_tenant_ids'] = v
            elif kl == 'permission-classification':
                d['permission_classification'] = v[0]
            elif kl == 'permissions':
                d['permissions'] = v
            elif kl == 'permission-type':
                d['permission_type'] = v[0]
            elif kl == 'resource-application':
                d['resource_application'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d
