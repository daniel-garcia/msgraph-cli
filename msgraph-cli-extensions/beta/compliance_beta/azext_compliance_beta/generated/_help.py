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

from knack.help_files import helps


helps['compliance'] = """
    type: group
    short-summary: compliance
"""

helps['compliance get-compliance'] = """
    type: command
    short-summary: "Get compliance"
"""

helps['compliance update-compliance'] = """
    type: command
    short-summary: "Update compliance"
"""

helps['compliance'] = """
    type: group
    short-summary: compliance
"""

helps['compliance delete'] = """
    type: command
    short-summary: "Delete navigation property ediscovery for compliance"
"""

helps['compliance get-ediscovery'] = """
    type: command
    short-summary: "Get ediscovery from compliance"
"""

helps['compliance update-ediscovery'] = """
    type: command
    short-summary: "Update the navigation property ediscovery in compliance"
"""

helps['compliance'] = """
    type: group
    short-summary: compliance
"""

helps['compliance delete'] = """
    type: command
    short-summary: "Delete navigation property cases for compliance"
"""

helps['compliance create-case'] = """
    type: command
    short-summary: "Create new navigation property to cases for compliance"
    parameters:
      - name: --last-modified-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --closed-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --closed-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --closed-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --closed-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --closed-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --closed-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance get-case'] = """
    type: command
    short-summary: "Get cases from compliance"
"""

helps['compliance list-case'] = """
    type: command
    short-summary: "Get cases from compliance"
"""

helps['compliance update-case'] = """
    type: command
    short-summary: "Update the navigation property cases in compliance"
    parameters:
      - name: --last-modified-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --closed-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --closed-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --closed-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --closed-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --closed-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --closed-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance'] = """
    type: group
    short-summary: compliance
"""

helps['compliance delete'] = """
    type: command
    short-summary: "Delete navigation property reviewSets for compliance"
"""

helps['compliance close'] = """
    type: command
    short-summary: "Invoke action close"
"""

helps['compliance create-custodian'] = """
    type: command
    short-summary: "Create new navigation property to custodians for compliance"
    parameters:
      - name: --last-index-operation
        short-summary: "caseIndexOperation"
        long-summary: |
            Usage: --last-index-operation action=XX completed-date-time=XX created-date-time=XX display-name=XX \
percent-progress=XX status=XX id=XX

            id: Read-only.
      - name: --user-sources
        long-summary: |
            Usage: --user-sources email=XX included-sources=XX created-date-time=XX display-name=XX application=XX \
device=XX user=XX id=XX

            application: identity
            device: identity
            user: identity
            id: Read-only.

            Multiple actions can be specified by using more than one --user-sources argument.
"""

helps['compliance create-review-set'] = """
    type: command
    short-summary: "Create new navigation property to reviewSets for compliance"
    parameters:
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance get-custodian'] = """
    type: command
    short-summary: "Get custodians from compliance"
"""

helps['compliance get-review-set'] = """
    type: command
    short-summary: "Get reviewSets from compliance"
"""

helps['compliance list-custodian'] = """
    type: command
    short-summary: "Get custodians from compliance"
"""

helps['compliance list-review-set'] = """
    type: command
    short-summary: "Get reviewSets from compliance"
"""

helps['compliance reopen'] = """
    type: command
    short-summary: "Invoke action reopen"
"""

helps['compliance update-custodian'] = """
    type: command
    short-summary: "Update the navigation property custodians in compliance"
    parameters:
      - name: --last-index-operation
        short-summary: "caseIndexOperation"
        long-summary: |
            Usage: --last-index-operation action=XX completed-date-time=XX created-date-time=XX display-name=XX \
percent-progress=XX status=XX id=XX

            id: Read-only.
      - name: --user-sources
        long-summary: |
            Usage: --user-sources email=XX included-sources=XX created-date-time=XX display-name=XX application=XX \
device=XX user=XX id=XX

            application: identity
            device: identity
            user: identity
            id: Read-only.

            Multiple actions can be specified by using more than one --user-sources argument.
"""

helps['compliance update-review-set'] = """
    type: command
    short-summary: "Update the navigation property reviewSets in compliance"
    parameters:
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance'] = """
    type: group
    short-summary: compliance
"""

helps['compliance delete'] = """
    type: command
    short-summary: "Delete ref of navigation property lastIndexOperation for compliance"
"""

helps['compliance activate'] = """
    type: command
    short-summary: "Invoke action activate"
"""

helps['compliance create-site-source'] = """
    type: command
    short-summary: "Create new navigation property to siteSources for compliance"
    parameters:
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance create-unified-group-source'] = """
    type: command
    short-summary: "Create new navigation property to unifiedGroupSources for compliance"
    parameters:
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance create-user-source'] = """
    type: command
    short-summary: "Create new navigation property to userSources for compliance"
    parameters:
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance get-last-index-operation'] = """
    type: command
    short-summary: "Get lastIndexOperation from compliance"
"""

helps['compliance get-ref-last-index-operation'] = """
    type: command
    short-summary: "Get ref of lastIndexOperation from compliance"
"""

helps['compliance get-site-source'] = """
    type: command
    short-summary: "Get siteSources from compliance"
"""

helps['compliance get-unified-group-source'] = """
    type: command
    short-summary: "Get unifiedGroupSources from compliance"
"""

helps['compliance get-user-source'] = """
    type: command
    short-summary: "Get userSources from compliance"
"""

helps['compliance list-site-source'] = """
    type: command
    short-summary: "Get siteSources from compliance"
"""

helps['compliance list-unified-group-source'] = """
    type: command
    short-summary: "Get unifiedGroupSources from compliance"
"""

helps['compliance list-user-source'] = """
    type: command
    short-summary: "Get userSources from compliance"
"""

helps['compliance release'] = """
    type: command
    short-summary: "Invoke action release"
"""

helps['compliance set-ref-last-index-operation'] = """
    type: command
    short-summary: "Update the ref of navigation property lastIndexOperation in compliance"
"""

helps['compliance update-index'] = """
    type: command
    short-summary: "Invoke action updateIndex"
"""

helps['compliance update-site-source'] = """
    type: command
    short-summary: "Update the navigation property siteSources in compliance"
    parameters:
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance update-unified-group-source'] = """
    type: command
    short-summary: "Update the navigation property unifiedGroupSources in compliance"
    parameters:
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance update-user-source'] = """
    type: command
    short-summary: "Update the navigation property userSources in compliance"
    parameters:
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance'] = """
    type: group
    short-summary: compliance
"""

helps['compliance delete'] = """
    type: command
    short-summary: "Delete ref of navigation property site for compliance"
"""

helps['compliance get-ref-site'] = """
    type: command
    short-summary: "Get ref of site from compliance"
"""

helps['compliance get-site'] = """
    type: command
    short-summary: "Get site from compliance"
"""

helps['compliance set-ref-site'] = """
    type: command
    short-summary: "Update the ref of navigation property site in compliance"
"""

helps['compliance'] = """
    type: group
    short-summary: compliance
"""

helps['compliance delete'] = """
    type: command
    short-summary: "Delete ref of navigation property group for compliance"
"""

helps['compliance get-group'] = """
    type: command
    short-summary: "Get group from compliance"
"""

helps['compliance get-ref-group'] = """
    type: command
    short-summary: "Get ref of group from compliance"
"""

helps['compliance set-ref-group'] = """
    type: command
    short-summary: "Update the ref of navigation property group in compliance"
"""

helps['compliance'] = """
    type: group
    short-summary: compliance
"""

helps['compliance delete'] = """
    type: command
    short-summary: "Delete navigation property queries for compliance"
"""

helps['compliance create-query'] = """
    type: command
    short-summary: "Create new navigation property to queries for compliance"
    parameters:
      - name: --last-modified-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance get-query'] = """
    type: command
    short-summary: "Get queries from compliance"
"""

helps['compliance list-query'] = """
    type: command
    short-summary: "Get queries from compliance"
"""

helps['compliance update-query'] = """
    type: command
    short-summary: "Update the navigation property queries in compliance"
    parameters:
      - name: --last-modified-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""