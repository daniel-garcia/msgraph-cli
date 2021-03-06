# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Enum11(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVATION_URL = "activationUrl"
    ACTIVITY_SOURCE_HOST = "activitySourceHost"
    APP_ACTIVITY_ID = "appActivityId"
    APP_DISPLAY_NAME = "appDisplayName"
    CONTENT_INFO = "contentInfo"
    CONTENT_URL = "contentUrl"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    FALLBACK_URL = "fallbackUrl"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    VISUAL_ELEMENTS = "visualElements"
    HISTORY_ITEMS = "historyItems"

class Enum12(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    HISTORY_ITEMS = "historyItems"

class Enum13(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    ACCOUNT_ENABLED = "accountEnabled"
    ACCOUNT_ENABLED_DESC = "accountEnabled desc"
    ALTERNATIVE_SECURITY_IDS = "alternativeSecurityIds"
    ALTERNATIVE_SECURITY_IDS_DESC = "alternativeSecurityIds desc"
    APPROXIMATE_LAST_SIGN_IN_DATE_TIME = "approximateLastSignInDateTime"
    APPROXIMATE_LAST_SIGN_IN_DATE_TIME_DESC = "approximateLastSignInDateTime desc"
    COMPLIANCE_EXPIRATION_DATE_TIME = "complianceExpirationDateTime"
    COMPLIANCE_EXPIRATION_DATE_TIME_DESC = "complianceExpirationDateTime desc"
    DEVICE_CATEGORY = "deviceCategory"
    DEVICE_CATEGORY_DESC = "deviceCategory desc"
    DEVICE_ID = "deviceId"
    DEVICE_ID_DESC = "deviceId desc"
    DEVICE_METADATA = "deviceMetadata"
    DEVICE_METADATA_DESC = "deviceMetadata desc"
    DEVICE_OWNERSHIP = "deviceOwnership"
    DEVICE_OWNERSHIP_DESC = "deviceOwnership desc"
    DEVICE_VERSION = "deviceVersion"
    DEVICE_VERSION_DESC = "deviceVersion desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DOMAIN_NAME = "domainName"
    DOMAIN_NAME_DESC = "domainName desc"
    ENROLLMENT_PROFILE_NAME = "enrollmentProfileName"
    ENROLLMENT_PROFILE_NAME_DESC = "enrollmentProfileName desc"
    ENROLLMENT_TYPE = "enrollmentType"
    ENROLLMENT_TYPE_DESC = "enrollmentType desc"
    EXTENSION_ATTRIBUTES = "extensionAttributes"
    EXTENSION_ATTRIBUTES_DESC = "extensionAttributes desc"
    IS_COMPLIANT = "isCompliant"
    IS_COMPLIANT_DESC = "isCompliant desc"
    IS_MANAGED = "isManaged"
    IS_MANAGED_DESC = "isManaged desc"
    IS_ROOTED = "isRooted"
    IS_ROOTED_DESC = "isRooted desc"
    MANAGEMENT_TYPE = "managementType"
    MANAGEMENT_TYPE_DESC = "managementType desc"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_LAST_SYNC_DATE_TIME_DESC = "onPremisesLastSyncDateTime desc"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    ON_PREMISES_SYNC_ENABLED_DESC = "onPremisesSyncEnabled desc"
    OPERATING_SYSTEM = "operatingSystem"
    OPERATING_SYSTEM_DESC = "operatingSystem desc"
    OPERATING_SYSTEM_VERSION = "operatingSystemVersion"
    OPERATING_SYSTEM_VERSION_DESC = "operatingSystemVersion desc"
    PHYSICAL_IDS = "physicalIds"
    PHYSICAL_IDS_DESC = "physicalIds desc"
    PROFILE_TYPE = "profileType"
    PROFILE_TYPE_DESC = "profileType desc"
    REGISTRATION_DATE_TIME = "registrationDateTime"
    REGISTRATION_DATE_TIME_DESC = "registrationDateTime desc"
    SYSTEM_LABELS = "systemLabels"
    SYSTEM_LABELS_DESC = "systemLabels desc"
    TRUST_TYPE = "trustType"
    TRUST_TYPE_DESC = "trustType desc"
    KIND = "kind"
    KIND_DESC = "kind desc"
    MANUFACTURER = "manufacturer"
    MANUFACTURER_DESC = "manufacturer desc"
    MODEL = "model"
    MODEL_DESC = "model desc"
    NAME = "name"
    NAME_DESC = "name desc"
    PLATFORM = "platform"
    PLATFORM_DESC = "platform desc"
    STATUS = "status"
    STATUS_DESC = "status desc"

class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ACCOUNT_ENABLED = "accountEnabled"
    ALTERNATIVE_SECURITY_IDS = "alternativeSecurityIds"
    APPROXIMATE_LAST_SIGN_IN_DATE_TIME = "approximateLastSignInDateTime"
    COMPLIANCE_EXPIRATION_DATE_TIME = "complianceExpirationDateTime"
    DEVICE_CATEGORY = "deviceCategory"
    DEVICE_ID = "deviceId"
    DEVICE_METADATA = "deviceMetadata"
    DEVICE_OWNERSHIP = "deviceOwnership"
    DEVICE_VERSION = "deviceVersion"
    DISPLAY_NAME = "displayName"
    DOMAIN_NAME = "domainName"
    ENROLLMENT_PROFILE_NAME = "enrollmentProfileName"
    ENROLLMENT_TYPE = "enrollmentType"
    EXTENSION_ATTRIBUTES = "extensionAttributes"
    IS_COMPLIANT = "isCompliant"
    IS_MANAGED = "isManaged"
    IS_ROOTED = "isRooted"
    MANAGEMENT_TYPE = "managementType"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    OPERATING_SYSTEM = "operatingSystem"
    OPERATING_SYSTEM_VERSION = "operatingSystemVersion"
    PHYSICAL_IDS = "physicalIds"
    PROFILE_TYPE = "profileType"
    REGISTRATION_DATE_TIME = "registrationDateTime"
    SYSTEM_LABELS = "systemLabels"
    TRUST_TYPE = "trustType"
    KIND = "kind"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    PLATFORM = "platform"
    STATUS = "status"
    MEMBER_OF = "memberOf"
    REGISTERED_OWNERS = "registeredOwners"
    REGISTERED_USERS = "registeredUsers"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"
    EXTENSIONS = "extensions"
    COMMANDS = "commands"

class Enum15(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    MEMBER_OF = "memberOf"
    REGISTERED_OWNERS = "registeredOwners"
    REGISTERED_USERS = "registeredUsers"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"
    EXTENSIONS = "extensions"
    COMMANDS = "commands"

class Enum16(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ACCOUNT_ENABLED = "accountEnabled"
    ALTERNATIVE_SECURITY_IDS = "alternativeSecurityIds"
    APPROXIMATE_LAST_SIGN_IN_DATE_TIME = "approximateLastSignInDateTime"
    COMPLIANCE_EXPIRATION_DATE_TIME = "complianceExpirationDateTime"
    DEVICE_CATEGORY = "deviceCategory"
    DEVICE_ID = "deviceId"
    DEVICE_METADATA = "deviceMetadata"
    DEVICE_OWNERSHIP = "deviceOwnership"
    DEVICE_VERSION = "deviceVersion"
    DISPLAY_NAME = "displayName"
    DOMAIN_NAME = "domainName"
    ENROLLMENT_PROFILE_NAME = "enrollmentProfileName"
    ENROLLMENT_TYPE = "enrollmentType"
    EXTENSION_ATTRIBUTES = "extensionAttributes"
    IS_COMPLIANT = "isCompliant"
    IS_MANAGED = "isManaged"
    IS_ROOTED = "isRooted"
    MANAGEMENT_TYPE = "managementType"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    OPERATING_SYSTEM = "operatingSystem"
    OPERATING_SYSTEM_VERSION = "operatingSystemVersion"
    PHYSICAL_IDS = "physicalIds"
    PROFILE_TYPE = "profileType"
    REGISTRATION_DATE_TIME = "registrationDateTime"
    SYSTEM_LABELS = "systemLabels"
    TRUST_TYPE = "trustType"
    KIND = "kind"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    PLATFORM = "platform"
    STATUS = "status"
    MEMBER_OF = "memberOf"
    REGISTERED_OWNERS = "registeredOwners"
    REGISTERED_USERS = "registeredUsers"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"
    EXTENSIONS = "extensions"
    COMMANDS = "commands"

class Enum17(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    MEMBER_OF = "memberOf"
    REGISTERED_OWNERS = "registeredOwners"
    REGISTERED_USERS = "registeredUsers"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"
    EXTENSIONS = "extensions"
    COMMANDS = "commands"

class Enum6(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    ACTIVE_DURATION_SECONDS = "activeDurationSeconds"
    ACTIVE_DURATION_SECONDS_DESC = "activeDurationSeconds desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    EXPIRATION_DATE_TIME_DESC = "expirationDateTime desc"
    LAST_ACTIVE_DATE_TIME = "lastActiveDateTime"
    LAST_ACTIVE_DATE_TIME_DESC = "lastActiveDateTime desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    STARTED_DATE_TIME = "startedDateTime"
    STARTED_DATE_TIME_DESC = "startedDateTime desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    USER_TIMEZONE = "userTimezone"
    USER_TIMEZONE_DESC = "userTimezone desc"

class Enum7(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVE_DURATION_SECONDS = "activeDurationSeconds"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    LAST_ACTIVE_DATE_TIME = "lastActiveDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STARTED_DATE_TIME = "startedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    ACTIVITY = "activity"

class Enum9(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVE_DURATION_SECONDS = "activeDurationSeconds"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    LAST_ACTIVE_DATE_TIME = "lastActiveDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STARTED_DATE_TIME = "startedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    ACTIVITY = "activity"

class Get2ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVATION_URL = "activationUrl"
    ACTIVITY_SOURCE_HOST = "activitySourceHost"
    APP_ACTIVITY_ID = "appActivityId"
    APP_DISPLAY_NAME = "appDisplayName"
    CONTENT_INFO = "contentInfo"
    CONTENT_URL = "contentUrl"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    FALLBACK_URL = "fallbackUrl"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    VISUAL_ELEMENTS = "visualElements"
    HISTORY_ITEMS = "historyItems"

class Get3ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    HISTORY_ITEMS = "historyItems"

class Get4ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ACTIVITY = "activity"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    ACTIVATION_URL = "activationUrl"
    ACTIVATION_URL_DESC = "activationUrl desc"
    ACTIVITY_SOURCE_HOST = "activitySourceHost"
    ACTIVITY_SOURCE_HOST_DESC = "activitySourceHost desc"
    APP_ACTIVITY_ID = "appActivityId"
    APP_ACTIVITY_ID_DESC = "appActivityId desc"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_DISPLAY_NAME_DESC = "appDisplayName desc"
    CONTENT_INFO = "contentInfo"
    CONTENT_INFO_DESC = "contentInfo desc"
    CONTENT_URL = "contentUrl"
    CONTENT_URL_DESC = "contentUrl desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    EXPIRATION_DATE_TIME_DESC = "expirationDateTime desc"
    FALLBACK_URL = "fallbackUrl"
    FALLBACK_URL_DESC = "fallbackUrl desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    USER_TIMEZONE = "userTimezone"
    USER_TIMEZONE_DESC = "userTimezone desc"
    VISUAL_ELEMENTS = "visualElements"
    VISUAL_ELEMENTS_DESC = "visualElements desc"

class Get7ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIVATION_URL = "activationUrl"
    ACTIVITY_SOURCE_HOST = "activitySourceHost"
    APP_ACTIVITY_ID = "appActivityId"
    APP_DISPLAY_NAME = "appDisplayName"
    CONTENT_INFO = "contentInfo"
    CONTENT_URL = "contentUrl"
    CREATED_DATE_TIME = "createdDateTime"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    FALLBACK_URL = "fallbackUrl"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    STATUS = "status"
    USER_TIMEZONE = "userTimezone"
    VISUAL_ELEMENTS = "visualElements"
    HISTORY_ITEMS = "historyItems"

class Get8ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    HISTORY_ITEMS = "historyItems"

class Get9ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ACTIVITY = "activity"

class MicrosoftGraphStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ACTIVE = "active"
    UPDATED = "updated"
    DELETED = "deleted"
    IGNORED = "ignored"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"
