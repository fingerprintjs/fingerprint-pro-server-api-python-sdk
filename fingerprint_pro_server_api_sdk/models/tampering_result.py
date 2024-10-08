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


class TamperingResult(BaseModel):
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
        'anomaly_score': 'float'
    }

    attribute_map = {
        'result': 'result',
        'anomaly_score': 'anomalyScore'
    }

    def __init__(self, result=None, anomaly_score=None):  # noqa: E501
        """TamperingResult - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._anomaly_score = None
        self.discriminator = None
        self.result = result
        self.anomaly_score = anomaly_score

    @property
    def result(self) -> bool:
        """Gets the result of this TamperingResult.  # noqa: E501

        Flag indicating whether browser tampering was detected according to our internal thresholds.  # noqa: E501

        :return: The result of this TamperingResult.  # noqa: E501
        """
        return self._result

    @result.setter
    def result(self, result: bool):
        """Sets the result of this TamperingResult.

        Flag indicating whether browser tampering was detected according to our internal thresholds.  # noqa: E501

        :param result: The result of this TamperingResult.  # noqa: E501
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def anomaly_score(self) -> float:
        """Gets the anomaly_score of this TamperingResult.  # noqa: E501

        Confidence score (`0.0 - 1.0`) for the tampering detection. Values above `0.5` suggest that we're reasonably sure there was a tampering attempt. Values below `0.5` are genuine browsers.  # noqa: E501

        :return: The anomaly_score of this TamperingResult.  # noqa: E501
        """
        return self._anomaly_score

    @anomaly_score.setter
    def anomaly_score(self, anomaly_score: float):
        """Sets the anomaly_score of this TamperingResult.

        Confidence score (`0.0 - 1.0`) for the tampering detection. Values above `0.5` suggest that we're reasonably sure there was a tampering attempt. Values below `0.5` are genuine browsers.  # noqa: E501

        :param anomaly_score: The anomaly_score of this TamperingResult.  # noqa: E501
        """
        if anomaly_score is None:
            raise ValueError("Invalid value for `anomaly_score`, must not be `None`")  # noqa: E501

        self._anomaly_score = anomaly_score

