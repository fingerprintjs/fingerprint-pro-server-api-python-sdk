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
from fingerprint_pro_server_api_sdk.models.browser_details import BrowserDetails
from fingerprint_pro_server_api_sdk.models.deprecated_geolocation import DeprecatedGeolocation
from datetime import datetime
from fingerprint_pro_server_api_sdk.models.tag import Tag
from fingerprint_pro_server_api_sdk.models.identification_confidence import IdentificationConfidence
from fingerprint_pro_server_api_sdk.models.identification_seen_at import IdentificationSeenAt
from fingerprint_pro_server_api_sdk.models.identification_seen_at import IdentificationSeenAt
from fingerprint_pro_server_api_sdk.models.raw_device_attributes import RawDeviceAttributes


class Visit(BaseModel):
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
        'request_id': 'str',
        'browser_details': 'BrowserDetails',
        'incognito': 'bool',
        'ip': 'str',
        'ip_location': 'DeprecatedGeolocation',
        'linked_id': 'str',
        'timestamp': 'int',
        'time': 'datetime',
        'url': 'str',
        'tag': 'Tag',
        'confidence': 'IdentificationConfidence',
        'visitor_found': 'bool',
        'first_seen_at': 'IdentificationSeenAt',
        'last_seen_at': 'IdentificationSeenAt',
        'components': 'RawDeviceAttributes'
    }

    nullable_map = {
        'request_id': False,
        'browser_details': False,
        'incognito': False,
        'ip': False,
        'ip_location': False,
        'linked_id': False,
        'timestamp': False,
        'time': False,
        'url': False,
        'tag': False,
        'confidence': False,
        'visitor_found': False,
        'first_seen_at': False,
        'last_seen_at': False,
        'components': False
    }

    attribute_map = {
        'request_id': 'requestId',
        'browser_details': 'browserDetails',
        'incognito': 'incognito',
        'ip': 'ip',
        'ip_location': 'ipLocation',
        'linked_id': 'linkedId',
        'timestamp': 'timestamp',
        'time': 'time',
        'url': 'url',
        'tag': 'tag',
        'confidence': 'confidence',
        'visitor_found': 'visitorFound',
        'first_seen_at': 'firstSeenAt',
        'last_seen_at': 'lastSeenAt',
        'components': 'components'
    }

    def __init__(self, request_id=None, browser_details=None, incognito=None, ip=None, ip_location=None, linked_id=None, timestamp=None, time=None, url=None, tag=None, confidence=None, visitor_found=None, first_seen_at=None, last_seen_at=None, components=None):  # noqa: E501
        """Visit - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._browser_details = None
        self._incognito = None
        self._ip = None
        self._ip_location = None
        self._linked_id = None
        self._timestamp = None
        self._time = None
        self._url = None
        self._tag = None
        self._confidence = None
        self._visitor_found = None
        self._first_seen_at = None
        self._last_seen_at = None
        self._components = None
        self.discriminator = None
        self.request_id = request_id
        self.browser_details = browser_details
        self.incognito = incognito
        self.ip = ip
        if ip_location is not None:
            self.ip_location = ip_location
        if linked_id is not None:
            self.linked_id = linked_id
        self.timestamp = timestamp
        self.time = time
        self.url = url
        self.tag = tag
        if confidence is not None:
            self.confidence = confidence
        self.visitor_found = visitor_found
        self.first_seen_at = first_seen_at
        self.last_seen_at = last_seen_at
        if components is not None:
            self.components = components

    @property
    def request_id(self) -> str:
        """Gets the request_id of this Visit.  # noqa: E501

        Unique identifier of the user's request.  # noqa: E501

        :return: The request_id of this Visit.  # noqa: E501
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id: str):
        """Sets the request_id of this Visit.

        Unique identifier of the user's request.  # noqa: E501

        :param request_id: The request_id of this Visit.  # noqa: E501
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def browser_details(self) -> BrowserDetails:
        """Gets the browser_details of this Visit.  # noqa: E501


        :return: The browser_details of this Visit.  # noqa: E501
        """
        return self._browser_details

    @browser_details.setter
    def browser_details(self, browser_details: BrowserDetails):
        """Sets the browser_details of this Visit.


        :param browser_details: The browser_details of this Visit.  # noqa: E501
        """
        if browser_details is None:
            raise ValueError("Invalid value for `browser_details`, must not be `None`")  # noqa: E501

        self._browser_details = browser_details

    @property
    def incognito(self) -> bool:
        """Gets the incognito of this Visit.  # noqa: E501

        Flag if user used incognito session.  # noqa: E501

        :return: The incognito of this Visit.  # noqa: E501
        """
        return self._incognito

    @incognito.setter
    def incognito(self, incognito: bool):
        """Sets the incognito of this Visit.

        Flag if user used incognito session.  # noqa: E501

        :param incognito: The incognito of this Visit.  # noqa: E501
        """
        if incognito is None:
            raise ValueError("Invalid value for `incognito`, must not be `None`")  # noqa: E501

        self._incognito = incognito

    @property
    def ip(self) -> str:
        """Gets the ip of this Visit.  # noqa: E501

        IP address of the requesting browser or bot.  # noqa: E501

        :return: The ip of this Visit.  # noqa: E501
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        """Sets the ip of this Visit.

        IP address of the requesting browser or bot.  # noqa: E501

        :param ip: The ip of this Visit.  # noqa: E501
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def ip_location(self) -> Optional[DeprecatedGeolocation]:
        """Gets the ip_location of this Visit.  # noqa: E501


        :return: The ip_location of this Visit.  # noqa: E501
        """
        return self._ip_location

    @ip_location.setter
    def ip_location(self, ip_location: Optional[DeprecatedGeolocation]):
        """Sets the ip_location of this Visit.


        :param ip_location: The ip_location of this Visit.  # noqa: E501
        """

        self._ip_location = ip_location

    @property
    def linked_id(self) -> Optional[str]:
        """Gets the linked_id of this Visit.  # noqa: E501

        A customer-provided id that was sent with the request.  # noqa: E501

        :return: The linked_id of this Visit.  # noqa: E501
        """
        return self._linked_id

    @linked_id.setter
    def linked_id(self, linked_id: Optional[str]):
        """Sets the linked_id of this Visit.

        A customer-provided id that was sent with the request.  # noqa: E501

        :param linked_id: The linked_id of this Visit.  # noqa: E501
        """

        self._linked_id = linked_id

    @property
    def timestamp(self) -> int:
        """Gets the timestamp of this Visit.  # noqa: E501

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :return: The timestamp of this Visit.  # noqa: E501
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int):
        """Sets the timestamp of this Visit.

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :param timestamp: The timestamp of this Visit.  # noqa: E501
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def time(self) -> datetime:
        """Gets the time of this Visit.  # noqa: E501

        Time expressed according to ISO 8601 in UTC format, when the request from the client agent was made. We recommend to treat requests that are older than 2 minutes as malicious. Otherwise, request replay attacks are possible.  # noqa: E501

        :return: The time of this Visit.  # noqa: E501
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this Visit.

        Time expressed according to ISO 8601 in UTC format, when the request from the client agent was made. We recommend to treat requests that are older than 2 minutes as malicious. Otherwise, request replay attacks are possible.  # noqa: E501

        :param time: The time of this Visit.  # noqa: E501
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def url(self) -> str:
        """Gets the url of this Visit.  # noqa: E501

        Page URL from which the request was sent.  # noqa: E501

        :return: The url of this Visit.  # noqa: E501
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this Visit.

        Page URL from which the request was sent.  # noqa: E501

        :param url: The url of this Visit.  # noqa: E501
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def tag(self) -> Tag:
        """Gets the tag of this Visit.  # noqa: E501


        :return: The tag of this Visit.  # noqa: E501
        """
        return self._tag

    @tag.setter
    def tag(self, tag: Tag):
        """Sets the tag of this Visit.


        :param tag: The tag of this Visit.  # noqa: E501
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def confidence(self) -> Optional[IdentificationConfidence]:
        """Gets the confidence of this Visit.  # noqa: E501


        :return: The confidence of this Visit.  # noqa: E501
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence: Optional[IdentificationConfidence]):
        """Sets the confidence of this Visit.


        :param confidence: The confidence of this Visit.  # noqa: E501
        """

        self._confidence = confidence

    @property
    def visitor_found(self) -> bool:
        """Gets the visitor_found of this Visit.  # noqa: E501

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :return: The visitor_found of this Visit.  # noqa: E501
        """
        return self._visitor_found

    @visitor_found.setter
    def visitor_found(self, visitor_found: bool):
        """Sets the visitor_found of this Visit.

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :param visitor_found: The visitor_found of this Visit.  # noqa: E501
        """
        if visitor_found is None:
            raise ValueError("Invalid value for `visitor_found`, must not be `None`")  # noqa: E501

        self._visitor_found = visitor_found

    @property
    def first_seen_at(self) -> IdentificationSeenAt:
        """Gets the first_seen_at of this Visit.  # noqa: E501


        :return: The first_seen_at of this Visit.  # noqa: E501
        """
        return self._first_seen_at

    @first_seen_at.setter
    def first_seen_at(self, first_seen_at: IdentificationSeenAt):
        """Sets the first_seen_at of this Visit.


        :param first_seen_at: The first_seen_at of this Visit.  # noqa: E501
        """
        if first_seen_at is None:
            raise ValueError("Invalid value for `first_seen_at`, must not be `None`")  # noqa: E501

        self._first_seen_at = first_seen_at

    @property
    def last_seen_at(self) -> IdentificationSeenAt:
        """Gets the last_seen_at of this Visit.  # noqa: E501


        :return: The last_seen_at of this Visit.  # noqa: E501
        """
        return self._last_seen_at

    @last_seen_at.setter
    def last_seen_at(self, last_seen_at: IdentificationSeenAt):
        """Sets the last_seen_at of this Visit.


        :param last_seen_at: The last_seen_at of this Visit.  # noqa: E501
        """
        if last_seen_at is None:
            raise ValueError("Invalid value for `last_seen_at`, must not be `None`")  # noqa: E501

        self._last_seen_at = last_seen_at

    @property
    def components(self) -> Optional[RawDeviceAttributes]:
        """Gets the components of this Visit.  # noqa: E501


        :return: The components of this Visit.  # noqa: E501
        """
        return self._components

    @components.setter
    def components(self, components: Optional[RawDeviceAttributes]):
        """Sets the components of this Visit.


        :param components: The components of this Visit.  # noqa: E501
        """

        self._components = components

