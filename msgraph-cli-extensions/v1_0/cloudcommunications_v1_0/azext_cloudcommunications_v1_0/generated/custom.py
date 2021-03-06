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


def cloudcommunications_delete(client,
                               user_id,
                               online_meeting_id,
                               if_match=None):
    return client.delete_online_meeting(user_id=user_id,
                                        online_meeting_id=online_meeting_id,
                                        if_match=if_match)


def cloudcommunications_create_online_meeting(client,
                                              user_id,
                                              id_=None,
                                              audio_conferencing=None,
                                              chat_info=None,
                                              creation_date_time=None,
                                              end_date_time=None,
                                              external_id=None,
                                              join_information=None,
                                              join_web_url=None,
                                              start_date_time=None,
                                              subject=None,
                                              video_teleconference_id=None,
                                              participants_attendees=None,
                                              participants_organizer=None):
    return client.create_online_meeting(user_id=user_id,
                                        id=id_,
                                        audio_conferencing=audio_conferencing,
                                        chat_info=chat_info,
                                        creation_date_time=creation_date_time,
                                        end_date_time=end_date_time,
                                        external_id=external_id,
                                        join_information=join_information,
                                        join_web_url=join_web_url,
                                        start_date_time=start_date_time,
                                        subject=subject,
                                        video_teleconference_id=video_teleconference_id,
                                        attendees=participants_attendees,
                                        organizer=participants_organizer)


def cloudcommunications_get_online_meeting(client,
                                           user_id,
                                           online_meeting_id,
                                           select=None,
                                           expand=None):
    return client.get_online_meeting(user_id=user_id,
                                     online_meeting_id=online_meeting_id,
                                     select=select,
                                     expand=expand)


def cloudcommunications_list_online_meeting(client,
                                            user_id,
                                            orderby=None,
                                            select=None,
                                            expand=None):
    return client.list_online_meeting(user_id=user_id,
                                      orderby=orderby,
                                      select=select,
                                      expand=expand)


def cloudcommunications_update_online_meeting(client,
                                              user_id,
                                              online_meeting_id,
                                              id_=None,
                                              audio_conferencing=None,
                                              chat_info=None,
                                              creation_date_time=None,
                                              end_date_time=None,
                                              external_id=None,
                                              join_information=None,
                                              join_web_url=None,
                                              start_date_time=None,
                                              subject=None,
                                              video_teleconference_id=None,
                                              participants_attendees=None,
                                              participants_organizer=None):
    return client.update_online_meeting(user_id=user_id,
                                        online_meeting_id=online_meeting_id,
                                        id=id_,
                                        audio_conferencing=audio_conferencing,
                                        chat_info=chat_info,
                                        creation_date_time=creation_date_time,
                                        end_date_time=end_date_time,
                                        external_id=external_id,
                                        join_information=join_information,
                                        join_web_url=join_web_url,
                                        start_date_time=start_date_time,
                                        subject=subject,
                                        video_teleconference_id=video_teleconference_id,
                                        attendees=participants_attendees,
                                        organizer=participants_organizer)
