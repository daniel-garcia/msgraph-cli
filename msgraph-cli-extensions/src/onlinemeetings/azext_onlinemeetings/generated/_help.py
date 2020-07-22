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


helps['onlinemeetings'] = """
    type: group
    short-summary: onlinemeetings
"""

helps['onlinemeetings update'] = """
    type: command
    short-summary: Update the navigation property onlineMeetings in users
    parameters:
      - name: --audio-conferencing
        short-summary: audioConferencing
        long-summary: |
            Usage: --audio-conferencing conference-id=XX toll-number=XX toll-free-number=XX dialin-url=XX

            toll-number: The toll number that connects to the Audio Conference Provider.
            toll-free-number: The toll-free number that connects to the Audio Conference Provider.
            dialin-url: A URL to the externally-accessible web page that contains dial-in information.
      - name: --chat-info
        short-summary: chatInfo
        long-summary: |
            Usage: --chat-info thread-id=XX message-id=XX reply-chain-message-id=XX

            thread-id: The unique identifier for a thread in Microsoft Teams.
            message-id: The unique identifier of a message in a Microsoft Teams channel.
            reply-chain-message-id: The ID of the reply message.
      - name: --join-information
        short-summary: itemBody
        long-summary: |
            Usage: --join-information content-type=XX content=XX

            content: The content of the item.
"""

helps['onlinemeetings create-online-meeting'] = """
    type: command
    short-summary: Create new navigation property to onlineMeetings for users
    parameters:
      - name: --audio-conferencing
        short-summary: audioConferencing
        long-summary: |
            Usage: --audio-conferencing conference-id=XX toll-number=XX toll-free-number=XX dialin-url=XX

            toll-number: The toll number that connects to the Audio Conference Provider.
            toll-free-number: The toll-free number that connects to the Audio Conference Provider.
            dialin-url: A URL to the externally-accessible web page that contains dial-in information.
      - name: --chat-info
        short-summary: chatInfo
        long-summary: |
            Usage: --chat-info thread-id=XX message-id=XX reply-chain-message-id=XX

            thread-id: The unique identifier for a thread in Microsoft Teams.
            message-id: The unique identifier of a message in a Microsoft Teams channel.
            reply-chain-message-id: The ID of the reply message.
      - name: --join-information
        short-summary: itemBody
        long-summary: |
            Usage: --join-information content-type=XX content=XX

            content: The content of the item.
"""

helps['onlinemeetings get-online-meeting'] = """
    type: command
    short-summary: Get onlineMeetings from users
"""

helps['onlinemeetings list-online-meeting'] = """
    type: command
    short-summary: Get onlineMeetings from users
"""