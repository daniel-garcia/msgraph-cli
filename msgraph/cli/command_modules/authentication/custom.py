# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from os import path, remove

from msgraph.cli.core.custom_browser_credential import CustomBrowserCredential
from msgraph.cli.core.constants import CACHE_LOCATION


def login(cmd, scopes):
    login_scopes = [scope.strip() for scope in scopes.split(',')]
    credential = CustomBrowserCredential()

    result = credential.login(login_scopes)
    if result:
        print('Logged in successfully')


def logout(cmd):
    _delete_cache()


def _delete_cache():
    if path.isfile(CACHE_LOCATION):
        remove(CACHE_LOCATION)
        print('Logged out successfully')
    else:
        print('You\'re already logged out')
