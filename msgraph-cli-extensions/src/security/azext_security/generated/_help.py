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


helps['security'] = """
    type: group
    short-summary: security
"""

helps['security get-security'] = """
    type: command
    short-summary: "Get Security"
"""

helps['security update-security'] = """
    type: command
    short-summary: "Update Security"
"""

helps['security'] = """
    type: group
    short-summary: security
"""

helps['security delete'] = """
    type: command
    short-summary: "Delete navigation property secureScores for Security"
"""

helps['security create-alert'] = """
    type: command
    short-summary: "Create new navigation property to alerts for Security"
"""

helps['security create-secure-score'] = """
    type: command
    short-summary: "Create new navigation property to secureScores for Security"
    parameters:
      - name: --average-comparative-scores
        short-summary: "Average score by different scopes (for example, average by industry, average by seating) and \
control category (Identity, Data, Device, Apps, Infrastructure) within the scope."
        long-summary: |
            Usage: --average-comparative-scores average-score=XX basis=XX

            average-score: Average score within specified basis.
            basis: Scope type. The possible values are: AllTenants, TotalSeats, IndustryTypes.

            Multiple actions can be specified by using more than one --average-comparative-scores argument.
      - name: --control-scores
        short-summary: "Contains tenant scores for a set of controls."
        long-summary: |
            Usage: --control-scores control-category=XX control-name=XX description=XX score=XX

            control-category: Control action category (Identity, Data, Device, Apps, Infrastructure).
            control-name: Control unique name.
            description: Description of the control.
            score: Tenant achieved score for the control (it varies day by day depending on tenant operations on the \
control).

            Multiple actions can be specified by using more than one --control-scores argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
"""

helps['security create-secure-score-control-profile'] = """
    type: command
    short-summary: "Create new navigation property to secureScoreControlProfiles for Security"
    parameters:
      - name: --compliance-information
        long-summary: |
            Usage: --compliance-information certification-controls=XX certification-name=XX

            certification-controls: Collection of the certification controls associated with certification
            certification-name: Compliance certification name (for example, ISO 27018:2014, GDPR, FedRAMP, NIST \
800-171)

            Multiple actions can be specified by using more than one --compliance-information argument.
      - name: --control-state-updates
        long-summary: |
            Usage: --control-state-updates assigned-to=XX comment=XX state=XX updated-by=XX updated-date-time=XX

            assigned-to: Assigns the control to the user who will take the action.
            comment: Provides optional comment about the control.
            state: State of the control, which can be modified via a PATCH command (for example, ignored, thirdParty).
            updated-by: ID of the user who updated tenant state.
            updated-date-time: Time at which the control state was updated.

            Multiple actions can be specified by using more than one --control-state-updates argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
"""

helps['security get-alert'] = """
    type: command
    short-summary: "Get alerts from Security"
"""

helps['security get-secure-score'] = """
    type: command
    short-summary: "Get secureScores from Security"
"""

helps['security get-secure-score-control-profile'] = """
    type: command
    short-summary: "Get secureScoreControlProfiles from Security"
"""

helps['security list-alert'] = """
    type: command
    short-summary: "Get alerts from Security"
"""

helps['security list-secure-score'] = """
    type: command
    short-summary: "Get secureScores from Security"
"""

helps['security list-secure-score-control-profile'] = """
    type: command
    short-summary: "Get secureScoreControlProfiles from Security"
"""

helps['security update-alert'] = """
    type: command
    short-summary: "Update the navigation property alerts in Security"
"""

helps['security update-secure-score'] = """
    type: command
    short-summary: "Update the navigation property secureScores in Security"
    parameters:
      - name: --average-comparative-scores
        short-summary: "Average score by different scopes (for example, average by industry, average by seating) and \
control category (Identity, Data, Device, Apps, Infrastructure) within the scope."
        long-summary: |
            Usage: --average-comparative-scores average-score=XX basis=XX

            average-score: Average score within specified basis.
            basis: Scope type. The possible values are: AllTenants, TotalSeats, IndustryTypes.

            Multiple actions can be specified by using more than one --average-comparative-scores argument.
      - name: --control-scores
        short-summary: "Contains tenant scores for a set of controls."
        long-summary: |
            Usage: --control-scores control-category=XX control-name=XX description=XX score=XX

            control-category: Control action category (Identity, Data, Device, Apps, Infrastructure).
            control-name: Control unique name.
            description: Description of the control.
            score: Tenant achieved score for the control (it varies day by day depending on tenant operations on the \
control).

            Multiple actions can be specified by using more than one --control-scores argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
"""

helps['security update-secure-score-control-profile'] = """
    type: command
    short-summary: "Update the navigation property secureScoreControlProfiles in Security"
    parameters:
      - name: --compliance-information
        long-summary: |
            Usage: --compliance-information certification-controls=XX certification-name=XX

            certification-controls: Collection of the certification controls associated with certification
            certification-name: Compliance certification name (for example, ISO 27018:2014, GDPR, FedRAMP, NIST \
800-171)

            Multiple actions can be specified by using more than one --compliance-information argument.
      - name: --control-state-updates
        long-summary: |
            Usage: --control-state-updates assigned-to=XX comment=XX state=XX updated-by=XX updated-date-time=XX

            assigned-to: Assigns the control to the user who will take the action.
            comment: Provides optional comment about the control.
            state: State of the control, which can be modified via a PATCH command (for example, ignored, thirdParty).
            updated-by: ID of the user who updated tenant state.
            updated-date-time: Time at which the control state was updated.

            Multiple actions can be specified by using more than one --control-state-updates argument.
      - name: --vendor-information
        short-summary: "securityVendorInformation"
        long-summary: |
            Usage: --vendor-information provider=XX provider-version=XX sub-provider=XX vendor=XX

            provider: Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
            provider-version: Version of the provider or subprovider, if it exists, that generated the alert. Required
            sub-provider: Specific subprovider (under aggregating provider); for example, \
WindowsDefenderATP.SmartScreen.
            vendor: Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
"""
