# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_mail_v1_0_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.mail import Mail
    return get_mgmt_service_client(cli_ctx,
                                   Mail,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_user(cli_ctx, *_):
    return cf_mail_v1_0_cl(cli_ctx).user


def cf_user_inference_classification(cli_ctx, *_):
    return cf_mail_v1_0_cl(cli_ctx).user_inference_classification


def cf_user_mail_folder(cli_ctx, *_):
    return cf_mail_v1_0_cl(cli_ctx).user_mail_folder


def cf_user_mail_folder_message(cli_ctx, *_):
    return cf_mail_v1_0_cl(cli_ctx).user_mail_folder_message


def cf_user_message(cli_ctx, *_):
    return cf_mail_v1_0_cl(cli_ctx).user_message
