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
from fingerprint_pro_server_api_sdk.models.error import Error


class ErrorResponse(BaseModel):
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
        'error': 'Error'
    }

    nullable_map = {
        'error': False
    }

    attribute_map = {
        'error': 'error'
    }

    def __init__(self, error=None):  # noqa: E501
        """ErrorResponse - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self.discriminator = None
        self.error = error

    @property
    def error(self) -> Error:
        """Gets the error of this ErrorResponse.  # noqa: E501


        :return: The error of this ErrorResponse.  # noqa: E501
        """
        return self._error

    @error.setter
    def error(self, error: Error):
        """Sets the error of this ErrorResponse.


        :param error: The error of this ErrorResponse.  # noqa: E501
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

