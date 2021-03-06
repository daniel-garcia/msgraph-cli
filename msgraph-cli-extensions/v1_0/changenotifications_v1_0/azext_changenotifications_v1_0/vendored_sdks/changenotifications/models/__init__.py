# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CollectionOfSubscription
    from ._models_py3 import MicrosoftGraphEntity
    from ._models_py3 import MicrosoftGraphSubscription
    from ._models_py3 import OdataError
    from ._models_py3 import OdataErrorDetail
    from ._models_py3 import OdataErrorMain
except (SyntaxError, ImportError):
    from ._models import CollectionOfSubscription  # type: ignore
    from ._models import MicrosoftGraphEntity  # type: ignore
    from ._models import MicrosoftGraphSubscription  # type: ignore
    from ._models import OdataError  # type: ignore
    from ._models import OdataErrorDetail  # type: ignore
    from ._models import OdataErrorMain  # type: ignore

from ._change_notifications_enums import (
    Get1ItemsItem,
    Get5ItemsItem,
    Get6ItemsItem,
)

__all__ = [
    'CollectionOfSubscription',
    'MicrosoftGraphEntity',
    'MicrosoftGraphSubscription',
    'OdataError',
    'OdataErrorDetail',
    'OdataErrorMain',
    'Get1ItemsItem',
    'Get5ItemsItem',
    'Get6ItemsItem',
]
