# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import Dict, List, Optional  # noqa: F401
from fingerprint_pro_server_api_sdk.base_model import BaseModel
from fingerprint_pro_server_api_sdk.models.vpn_confidence import VPNConfidence
from fingerprint_pro_server_api_sdk.models.vpn_methods import VPNMethods


class VPN(BaseModel):
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
        'result': 'bool',
        'confidence': 'VPNConfidence',
        'origin_timezone': 'str',
        'origin_country': 'str',
        'methods': 'VPNMethods'
    }

    attribute_map = {
        'result': 'result',
        'confidence': 'confidence',
        'origin_timezone': 'originTimezone',
        'origin_country': 'originCountry',
        'methods': 'methods'
    }

    def __init__(self, result=None, confidence=None, origin_timezone=None, origin_country=None, methods=None):  # noqa: E501
        """VPN - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._confidence = None
        self._origin_timezone = None
        self._origin_country = None
        self._methods = None
        self.discriminator = None
        self.result = result
        self.confidence = confidence
        self.origin_timezone = origin_timezone
        self.origin_country = origin_country
        self.methods = methods

    @property
    def result(self) -> bool:
        """Gets the result of this VPN.  # noqa: E501

        VPN or other anonymizing service has been used when sending the request.  # noqa: E501

        :return: The result of this VPN.  # noqa: E501
        """
        return self._result

    @result.setter
    def result(self, result: bool):
        """Sets the result of this VPN.

        VPN or other anonymizing service has been used when sending the request.  # noqa: E501

        :param result: The result of this VPN.  # noqa: E501
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def confidence(self) -> VPNConfidence:
        """Gets the confidence of this VPN.  # noqa: E501


        :return: The confidence of this VPN.  # noqa: E501
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence: VPNConfidence):
        """Sets the confidence of this VPN.


        :param confidence: The confidence of this VPN.  # noqa: E501
        """
        if confidence is None:
            raise ValueError("Invalid value for `confidence`, must not be `None`")  # noqa: E501

        self._confidence = confidence

    @property
    def origin_timezone(self) -> str:
        """Gets the origin_timezone of this VPN.  # noqa: E501

        Local timezone which is used in timezoneMismatch method.  # noqa: E501

        :return: The origin_timezone of this VPN.  # noqa: E501
        """
        return self._origin_timezone

    @origin_timezone.setter
    def origin_timezone(self, origin_timezone: str):
        """Sets the origin_timezone of this VPN.

        Local timezone which is used in timezoneMismatch method.  # noqa: E501

        :param origin_timezone: The origin_timezone of this VPN.  # noqa: E501
        """
        if origin_timezone is None:
            raise ValueError("Invalid value for `origin_timezone`, must not be `None`")  # noqa: E501

        self._origin_timezone = origin_timezone

    @property
    def origin_country(self) -> str:
        """Gets the origin_country of this VPN.  # noqa: E501

        Country of the request (only for Android SDK version >= 2.4.0, ISO 3166 format or unknown).  # noqa: E501

        :return: The origin_country of this VPN.  # noqa: E501
        """
        return self._origin_country

    @origin_country.setter
    def origin_country(self, origin_country: str):
        """Sets the origin_country of this VPN.

        Country of the request (only for Android SDK version >= 2.4.0, ISO 3166 format or unknown).  # noqa: E501

        :param origin_country: The origin_country of this VPN.  # noqa: E501
        """
        if origin_country is None:
            raise ValueError("Invalid value for `origin_country`, must not be `None`")  # noqa: E501

        self._origin_country = origin_country

    @property
    def methods(self) -> VPNMethods:
        """Gets the methods of this VPN.  # noqa: E501


        :return: The methods of this VPN.  # noqa: E501
        """
        return self._methods

    @methods.setter
    def methods(self, methods: VPNMethods):
        """Sets the methods of this VPN.


        :param methods: The methods of this VPN.  # noqa: E501
        """
        if methods is None:
            raise ValueError("Invalid value for `methods`, must not be `None`")  # noqa: E501

        self._methods = methods
