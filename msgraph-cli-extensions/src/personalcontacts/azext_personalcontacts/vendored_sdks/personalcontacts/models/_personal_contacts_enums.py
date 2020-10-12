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


class Enum10(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CATEGORIES = "categories"
    CATEGORIES_DESC = "categories desc"
    CHANGE_KEY = "changeKey"
    CHANGE_KEY_DESC = "changeKey desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    ASSISTANT_NAME = "assistantName"
    ASSISTANT_NAME_DESC = "assistantName desc"
    BIRTHDAY = "birthday"
    BIRTHDAY_DESC = "birthday desc"
    BUSINESS_ADDRESS = "businessAddress"
    BUSINESS_ADDRESS_DESC = "businessAddress desc"
    BUSINESS_HOME_PAGE = "businessHomePage"
    BUSINESS_HOME_PAGE_DESC = "businessHomePage desc"
    BUSINESS_PHONES = "businessPhones"
    BUSINESS_PHONES_DESC = "businessPhones desc"
    CHILDREN = "children"
    CHILDREN_DESC = "children desc"
    COMPANY_NAME = "companyName"
    COMPANY_NAME_DESC = "companyName desc"
    DEPARTMENT = "department"
    DEPARTMENT_DESC = "department desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    EMAIL_ADDRESSES = "emailAddresses"
    EMAIL_ADDRESSES_DESC = "emailAddresses desc"
    FILE_AS = "fileAs"
    FILE_AS_DESC = "fileAs desc"
    GENERATION = "generation"
    GENERATION_DESC = "generation desc"
    GIVEN_NAME = "givenName"
    GIVEN_NAME_DESC = "givenName desc"
    HOME_ADDRESS = "homeAddress"
    HOME_ADDRESS_DESC = "homeAddress desc"
    HOME_PHONES = "homePhones"
    HOME_PHONES_DESC = "homePhones desc"
    IM_ADDRESSES = "imAddresses"
    IM_ADDRESSES_DESC = "imAddresses desc"
    INITIALS = "initials"
    INITIALS_DESC = "initials desc"
    JOB_TITLE = "jobTitle"
    JOB_TITLE_DESC = "jobTitle desc"
    MANAGER = "manager"
    MANAGER_DESC = "manager desc"
    MIDDLE_NAME = "middleName"
    MIDDLE_NAME_DESC = "middleName desc"
    MOBILE_PHONE = "mobilePhone"
    MOBILE_PHONE_DESC = "mobilePhone desc"
    NICK_NAME = "nickName"
    NICK_NAME_DESC = "nickName desc"
    OFFICE_LOCATION = "officeLocation"
    OFFICE_LOCATION_DESC = "officeLocation desc"
    OTHER_ADDRESS = "otherAddress"
    OTHER_ADDRESS_DESC = "otherAddress desc"
    PARENT_FOLDER_ID = "parentFolderId"
    PARENT_FOLDER_ID_DESC = "parentFolderId desc"
    PERSONAL_NOTES = "personalNotes"
    PERSONAL_NOTES_DESC = "personalNotes desc"
    PROFESSION = "profession"
    PROFESSION_DESC = "profession desc"
    SPOUSE_NAME = "spouseName"
    SPOUSE_NAME_DESC = "spouseName desc"
    SURNAME = "surname"
    SURNAME_DESC = "surname desc"
    TITLE = "title"
    TITLE_DESC = "title desc"
    YOMI_COMPANY_NAME = "yomiCompanyName"
    YOMI_COMPANY_NAME_DESC = "yomiCompanyName desc"
    YOMI_GIVEN_NAME = "yomiGivenName"
    YOMI_GIVEN_NAME_DESC = "yomiGivenName desc"
    YOMI_SURNAME = "yomiSurname"
    YOMI_SURNAME_DESC = "yomiSurname desc"

class Enum11(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CATEGORIES = "categories"
    CHANGE_KEY = "changeKey"
    CREATED_DATE_TIME = "createdDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    ASSISTANT_NAME = "assistantName"
    BIRTHDAY = "birthday"
    BUSINESS_ADDRESS = "businessAddress"
    BUSINESS_HOME_PAGE = "businessHomePage"
    BUSINESS_PHONES = "businessPhones"
    CHILDREN = "children"
    COMPANY_NAME = "companyName"
    DEPARTMENT = "department"
    DISPLAY_NAME = "displayName"
    EMAIL_ADDRESSES = "emailAddresses"
    FILE_AS = "fileAs"
    GENERATION = "generation"
    GIVEN_NAME = "givenName"
    HOME_ADDRESS = "homeAddress"
    HOME_PHONES = "homePhones"
    IM_ADDRESSES = "imAddresses"
    INITIALS = "initials"
    JOB_TITLE = "jobTitle"
    MANAGER = "manager"
    MIDDLE_NAME = "middleName"
    MOBILE_PHONE = "mobilePhone"
    NICK_NAME = "nickName"
    OFFICE_LOCATION = "officeLocation"
    OTHER_ADDRESS = "otherAddress"
    PARENT_FOLDER_ID = "parentFolderId"
    PERSONAL_NOTES = "personalNotes"
    PROFESSION = "profession"
    SPOUSE_NAME = "spouseName"
    SURNAME = "surname"
    TITLE = "title"
    YOMI_COMPANY_NAME = "yomiCompanyName"
    YOMI_GIVEN_NAME = "yomiGivenName"
    YOMI_SURNAME = "yomiSurname"
    EXTENSIONS = "extensions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    PHOTO = "photo"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum12(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    EXTENSIONS = "extensions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    PHOTO = "photo"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum13(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CATEGORIES = "categories"
    CHANGE_KEY = "changeKey"
    CREATED_DATE_TIME = "createdDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    ASSISTANT_NAME = "assistantName"
    BIRTHDAY = "birthday"
    BUSINESS_ADDRESS = "businessAddress"
    BUSINESS_HOME_PAGE = "businessHomePage"
    BUSINESS_PHONES = "businessPhones"
    CHILDREN = "children"
    COMPANY_NAME = "companyName"
    DEPARTMENT = "department"
    DISPLAY_NAME = "displayName"
    EMAIL_ADDRESSES = "emailAddresses"
    FILE_AS = "fileAs"
    GENERATION = "generation"
    GIVEN_NAME = "givenName"
    HOME_ADDRESS = "homeAddress"
    HOME_PHONES = "homePhones"
    IM_ADDRESSES = "imAddresses"
    INITIALS = "initials"
    JOB_TITLE = "jobTitle"
    MANAGER = "manager"
    MIDDLE_NAME = "middleName"
    MOBILE_PHONE = "mobilePhone"
    NICK_NAME = "nickName"
    OFFICE_LOCATION = "officeLocation"
    OTHER_ADDRESS = "otherAddress"
    PARENT_FOLDER_ID = "parentFolderId"
    PERSONAL_NOTES = "personalNotes"
    PROFESSION = "profession"
    SPOUSE_NAME = "spouseName"
    SURNAME = "surname"
    TITLE = "title"
    YOMI_COMPANY_NAME = "yomiCompanyName"
    YOMI_GIVEN_NAME = "yomiGivenName"
    YOMI_SURNAME = "yomiSurname"
    EXTENSIONS = "extensions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    PHOTO = "photo"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    EXTENSIONS = "extensions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    PHOTO = "photo"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum15(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"

class Enum16(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum17(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum18(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum19(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    HEIGHT = "height"
    WIDTH = "width"

class Enum20(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum21(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum22(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum23(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum24(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum25(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum26(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum27(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum28(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum29(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CATEGORIES = "categories"
    CATEGORIES_DESC = "categories desc"
    CHANGE_KEY = "changeKey"
    CHANGE_KEY_DESC = "changeKey desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    ASSISTANT_NAME = "assistantName"
    ASSISTANT_NAME_DESC = "assistantName desc"
    BIRTHDAY = "birthday"
    BIRTHDAY_DESC = "birthday desc"
    BUSINESS_ADDRESS = "businessAddress"
    BUSINESS_ADDRESS_DESC = "businessAddress desc"
    BUSINESS_HOME_PAGE = "businessHomePage"
    BUSINESS_HOME_PAGE_DESC = "businessHomePage desc"
    BUSINESS_PHONES = "businessPhones"
    BUSINESS_PHONES_DESC = "businessPhones desc"
    CHILDREN = "children"
    CHILDREN_DESC = "children desc"
    COMPANY_NAME = "companyName"
    COMPANY_NAME_DESC = "companyName desc"
    DEPARTMENT = "department"
    DEPARTMENT_DESC = "department desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    EMAIL_ADDRESSES = "emailAddresses"
    EMAIL_ADDRESSES_DESC = "emailAddresses desc"
    FILE_AS = "fileAs"
    FILE_AS_DESC = "fileAs desc"
    GENERATION = "generation"
    GENERATION_DESC = "generation desc"
    GIVEN_NAME = "givenName"
    GIVEN_NAME_DESC = "givenName desc"
    HOME_ADDRESS = "homeAddress"
    HOME_ADDRESS_DESC = "homeAddress desc"
    HOME_PHONES = "homePhones"
    HOME_PHONES_DESC = "homePhones desc"
    IM_ADDRESSES = "imAddresses"
    IM_ADDRESSES_DESC = "imAddresses desc"
    INITIALS = "initials"
    INITIALS_DESC = "initials desc"
    JOB_TITLE = "jobTitle"
    JOB_TITLE_DESC = "jobTitle desc"
    MANAGER = "manager"
    MANAGER_DESC = "manager desc"
    MIDDLE_NAME = "middleName"
    MIDDLE_NAME_DESC = "middleName desc"
    MOBILE_PHONE = "mobilePhone"
    MOBILE_PHONE_DESC = "mobilePhone desc"
    NICK_NAME = "nickName"
    NICK_NAME_DESC = "nickName desc"
    OFFICE_LOCATION = "officeLocation"
    OFFICE_LOCATION_DESC = "officeLocation desc"
    OTHER_ADDRESS = "otherAddress"
    OTHER_ADDRESS_DESC = "otherAddress desc"
    PARENT_FOLDER_ID = "parentFolderId"
    PARENT_FOLDER_ID_DESC = "parentFolderId desc"
    PERSONAL_NOTES = "personalNotes"
    PERSONAL_NOTES_DESC = "personalNotes desc"
    PROFESSION = "profession"
    PROFESSION_DESC = "profession desc"
    SPOUSE_NAME = "spouseName"
    SPOUSE_NAME_DESC = "spouseName desc"
    SURNAME = "surname"
    SURNAME_DESC = "surname desc"
    TITLE = "title"
    TITLE_DESC = "title desc"
    YOMI_COMPANY_NAME = "yomiCompanyName"
    YOMI_COMPANY_NAME_DESC = "yomiCompanyName desc"
    YOMI_GIVEN_NAME = "yomiGivenName"
    YOMI_GIVEN_NAME_DESC = "yomiGivenName desc"
    YOMI_SURNAME = "yomiSurname"
    YOMI_SURNAME_DESC = "yomiSurname desc"

class Enum30(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CATEGORIES = "categories"
    CHANGE_KEY = "changeKey"
    CREATED_DATE_TIME = "createdDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    ASSISTANT_NAME = "assistantName"
    BIRTHDAY = "birthday"
    BUSINESS_ADDRESS = "businessAddress"
    BUSINESS_HOME_PAGE = "businessHomePage"
    BUSINESS_PHONES = "businessPhones"
    CHILDREN = "children"
    COMPANY_NAME = "companyName"
    DEPARTMENT = "department"
    DISPLAY_NAME = "displayName"
    EMAIL_ADDRESSES = "emailAddresses"
    FILE_AS = "fileAs"
    GENERATION = "generation"
    GIVEN_NAME = "givenName"
    HOME_ADDRESS = "homeAddress"
    HOME_PHONES = "homePhones"
    IM_ADDRESSES = "imAddresses"
    INITIALS = "initials"
    JOB_TITLE = "jobTitle"
    MANAGER = "manager"
    MIDDLE_NAME = "middleName"
    MOBILE_PHONE = "mobilePhone"
    NICK_NAME = "nickName"
    OFFICE_LOCATION = "officeLocation"
    OTHER_ADDRESS = "otherAddress"
    PARENT_FOLDER_ID = "parentFolderId"
    PERSONAL_NOTES = "personalNotes"
    PROFESSION = "profession"
    SPOUSE_NAME = "spouseName"
    SURNAME = "surname"
    TITLE = "title"
    YOMI_COMPANY_NAME = "yomiCompanyName"
    YOMI_GIVEN_NAME = "yomiGivenName"
    YOMI_SURNAME = "yomiSurname"
    EXTENSIONS = "extensions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    PHOTO = "photo"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum31(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    EXTENSIONS = "extensions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    PHOTO = "photo"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum32(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CATEGORIES = "categories"
    CHANGE_KEY = "changeKey"
    CREATED_DATE_TIME = "createdDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    ASSISTANT_NAME = "assistantName"
    BIRTHDAY = "birthday"
    BUSINESS_ADDRESS = "businessAddress"
    BUSINESS_HOME_PAGE = "businessHomePage"
    BUSINESS_PHONES = "businessPhones"
    CHILDREN = "children"
    COMPANY_NAME = "companyName"
    DEPARTMENT = "department"
    DISPLAY_NAME = "displayName"
    EMAIL_ADDRESSES = "emailAddresses"
    FILE_AS = "fileAs"
    GENERATION = "generation"
    GIVEN_NAME = "givenName"
    HOME_ADDRESS = "homeAddress"
    HOME_PHONES = "homePhones"
    IM_ADDRESSES = "imAddresses"
    INITIALS = "initials"
    JOB_TITLE = "jobTitle"
    MANAGER = "manager"
    MIDDLE_NAME = "middleName"
    MOBILE_PHONE = "mobilePhone"
    NICK_NAME = "nickName"
    OFFICE_LOCATION = "officeLocation"
    OTHER_ADDRESS = "otherAddress"
    PARENT_FOLDER_ID = "parentFolderId"
    PERSONAL_NOTES = "personalNotes"
    PROFESSION = "profession"
    SPOUSE_NAME = "spouseName"
    SURNAME = "surname"
    TITLE = "title"
    YOMI_COMPANY_NAME = "yomiCompanyName"
    YOMI_GIVEN_NAME = "yomiGivenName"
    YOMI_SURNAME = "yomiSurname"
    EXTENSIONS = "extensions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    PHOTO = "photo"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum33(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    EXTENSIONS = "extensions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    PHOTO = "photo"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum34(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"

class Enum35(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum36(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum37(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum38(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    HEIGHT = "height"
    WIDTH = "width"

class Enum39(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum40(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum41(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum5(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    PARENT_FOLDER_ID = "parentFolderId"
    PARENT_FOLDER_ID_DESC = "parentFolderId desc"

class Enum6(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    PARENT_FOLDER_ID = "parentFolderId"
    CHILD_FOLDERS = "childFolders"
    CONTACTS = "contacts"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum8(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    PARENT_FOLDER_ID = "parentFolderId"
    CHILD_FOLDERS = "childFolders"
    CONTACTS = "contacts"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Get2ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    PARENT_FOLDER_ID = "parentFolderId"
    CHILD_FOLDERS = "childFolders"
    CONTACTS = "contacts"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Get3ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CHILD_FOLDERS = "childFolders"
    CONTACTS = "contacts"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Get4ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CHILD_FOLDERS = "childFolders"
    CONTACTS = "contacts"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    PARENT_FOLDER_ID = "parentFolderId"
    PARENT_FOLDER_ID_DESC = "parentFolderId desc"

class Get7ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    PARENT_FOLDER_ID = "parentFolderId"
    CHILD_FOLDERS = "childFolders"
    CONTACTS = "contacts"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Get8ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CHILD_FOLDERS = "childFolders"
    CONTACTS = "contacts"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Get9ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CHILD_FOLDERS = "childFolders"
    CONTACTS = "contacts"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"