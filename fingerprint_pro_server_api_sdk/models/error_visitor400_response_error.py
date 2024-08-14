# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import Dict, List  # noqa: F401
from fingerprint_pro_server_api_sdk.base_model import BaseModel


class ErrorVisitor400ResponseError(BaseModel):
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
        'code': 'str',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, code=None, message=None):  # noqa: E501
        """ErrorVisitor400ResponseError - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self.discriminator = None
        self.code = code
        self.message = message

    @property
    def code(self) -> str:
        """Gets the code of this ErrorVisitor400ResponseError.  # noqa: E501

        Error code: * `RequestCannotBeParsed` - The visitor ID parameter is missing or in the wrong format.   # noqa: E501

        :return: The code of this ErrorVisitor400ResponseError.  # noqa: E501
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this ErrorVisitor400ResponseError.

        Error code: * `RequestCannotBeParsed` - The visitor ID parameter is missing or in the wrong format.   # noqa: E501

        :param code: The code of this ErrorVisitor400ResponseError.  # noqa: E501
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        allowed_values = ["RequestCannotBeParsed"]  # noqa: E501
        if (code not in allowed_values):
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this ErrorVisitor400ResponseError.  # noqa: E501


        :return: The message of this ErrorVisitor400ResponseError.  # noqa: E501
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ErrorVisitor400ResponseError.


        :param message: The message of this ErrorVisitor400ResponseError.  # noqa: E501
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message
