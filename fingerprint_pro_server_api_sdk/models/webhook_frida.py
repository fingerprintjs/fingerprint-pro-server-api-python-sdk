# coding: utf-8

"""
    Fingerprint Server API

    Fingerprint Server API allows you to search, update, and delete identification events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import Dict, List, Optional  # noqa: F401
from fingerprint_pro_server_api_sdk.base_model import BaseModel


class WebhookFrida(BaseModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'result': 'bool'
    }

    nullable_map = {
        'result': False
    }

    attribute_map = {
        'result': 'result'
    }

    def __init__(self, result=None):  # noqa: E501
        """WebhookFrida - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self.discriminator = None
        if result is not None:
            self.result = result

    @property
    def result(self) -> Optional[bool]:
        """Gets the result of this WebhookFrida.  # noqa: E501

        [Frida](https://frida.re/docs/) detection for Android and iOS devices. There are 2 values:   * `true` - Frida detected   * `false` - No signs of Frida or the client is not a mobile device.   # noqa: E501

        :return: The result of this WebhookFrida.  # noqa: E501
        """
        return self._result

    @result.setter
    def result(self, result: Optional[bool]):
        """Sets the result of this WebhookFrida.

        [Frida](https://frida.re/docs/) detection for Android and iOS devices. There are 2 values:   * `true` - Frida detected   * `false` - No signs of Frida or the client is not a mobile device.   # noqa: E501

        :param result: The result of this WebhookFrida.  # noqa: E501
        """

        self._result = result

