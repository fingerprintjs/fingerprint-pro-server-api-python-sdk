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
from fingerprint_pro_server_api_sdk.models.velocity_data import VelocityData
from fingerprint_pro_server_api_sdk.models.velocity_data import VelocityData
from fingerprint_pro_server_api_sdk.models.velocity_data import VelocityData
from fingerprint_pro_server_api_sdk.models.velocity_data import VelocityData
from fingerprint_pro_server_api_sdk.models.velocity_data import VelocityData
from fingerprint_pro_server_api_sdk.models.velocity_data import VelocityData
from fingerprint_pro_server_api_sdk.models.velocity_data import VelocityData


class WebhookVelocity(BaseModel):
    """
    Sums key data points for a specific `visitorId`, `ipAddress` and `linkedId` at three distinct time intervals: 5 minutes, 1 hour, and 24 hours as follows:   - Number of distinct IP addresses associated to the visitor ID. - Number of distinct linked IDs associated with the visitor ID. - Number of distinct countries associated with the visitor ID. - Number of identification events associated with the visitor ID. - Number of identification events associated with the detected IP address. - Number of distinct IP addresses associated with the provided linked ID. - Number of distinct visitor IDs associated with the provided linked ID.  The `24h` interval of `distinctIp`, `distinctLinkedId`, `distinctCountry`, `distinctIpByLinkedId` and `distinctVisitorIdByLinkedId` will be omitted  if the number of `events` for the visitor ID in the last 24 hours (`events.intervals.['24h']`) is higher than 20.000. 

    NOTE: This class is auto generated by the swagger code generator program.

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
        'distinct_ip': 'VelocityData',
        'distinct_linked_id': 'VelocityData',
        'distinct_country': 'VelocityData',
        'events': 'VelocityData',
        'ip_events': 'VelocityData',
        'distinct_ip_by_linked_id': 'VelocityData',
        'distinct_visitor_id_by_linked_id': 'VelocityData'
    }

    attribute_map = {
        'distinct_ip': 'distinctIp',
        'distinct_linked_id': 'distinctLinkedId',
        'distinct_country': 'distinctCountry',
        'events': 'events',
        'ip_events': 'ipEvents',
        'distinct_ip_by_linked_id': 'distinctIpByLinkedId',
        'distinct_visitor_id_by_linked_id': 'distinctVisitorIdByLinkedId'
    }

    def __init__(self, distinct_ip=None, distinct_linked_id=None, distinct_country=None, events=None, ip_events=None, distinct_ip_by_linked_id=None, distinct_visitor_id_by_linked_id=None):  # noqa: E501
        """WebhookVelocity - a model defined in Swagger"""  # noqa: E501
        self._distinct_ip = None
        self._distinct_linked_id = None
        self._distinct_country = None
        self._events = None
        self._ip_events = None
        self._distinct_ip_by_linked_id = None
        self._distinct_visitor_id_by_linked_id = None
        self.discriminator = None
        if distinct_ip is not None:
            self.distinct_ip = distinct_ip
        if distinct_linked_id is not None:
            self.distinct_linked_id = distinct_linked_id
        if distinct_country is not None:
            self.distinct_country = distinct_country
        if events is not None:
            self.events = events
        if ip_events is not None:
            self.ip_events = ip_events
        if distinct_ip_by_linked_id is not None:
            self.distinct_ip_by_linked_id = distinct_ip_by_linked_id
        if distinct_visitor_id_by_linked_id is not None:
            self.distinct_visitor_id_by_linked_id = distinct_visitor_id_by_linked_id

    @property
    def distinct_ip(self) -> Optional[VelocityData]:
        """Gets the distinct_ip of this WebhookVelocity.  # noqa: E501


        :return: The distinct_ip of this WebhookVelocity.  # noqa: E501
        """
        return self._distinct_ip

    @distinct_ip.setter
    def distinct_ip(self, distinct_ip: Optional[VelocityData]):
        """Sets the distinct_ip of this WebhookVelocity.


        :param distinct_ip: The distinct_ip of this WebhookVelocity.  # noqa: E501
        """

        self._distinct_ip = distinct_ip

    @property
    def distinct_linked_id(self) -> Optional[VelocityData]:
        """Gets the distinct_linked_id of this WebhookVelocity.  # noqa: E501


        :return: The distinct_linked_id of this WebhookVelocity.  # noqa: E501
        """
        return self._distinct_linked_id

    @distinct_linked_id.setter
    def distinct_linked_id(self, distinct_linked_id: Optional[VelocityData]):
        """Sets the distinct_linked_id of this WebhookVelocity.


        :param distinct_linked_id: The distinct_linked_id of this WebhookVelocity.  # noqa: E501
        """

        self._distinct_linked_id = distinct_linked_id

    @property
    def distinct_country(self) -> Optional[VelocityData]:
        """Gets the distinct_country of this WebhookVelocity.  # noqa: E501


        :return: The distinct_country of this WebhookVelocity.  # noqa: E501
        """
        return self._distinct_country

    @distinct_country.setter
    def distinct_country(self, distinct_country: Optional[VelocityData]):
        """Sets the distinct_country of this WebhookVelocity.


        :param distinct_country: The distinct_country of this WebhookVelocity.  # noqa: E501
        """

        self._distinct_country = distinct_country

    @property
    def events(self) -> Optional[VelocityData]:
        """Gets the events of this WebhookVelocity.  # noqa: E501


        :return: The events of this WebhookVelocity.  # noqa: E501
        """
        return self._events

    @events.setter
    def events(self, events: Optional[VelocityData]):
        """Sets the events of this WebhookVelocity.


        :param events: The events of this WebhookVelocity.  # noqa: E501
        """

        self._events = events

    @property
    def ip_events(self) -> Optional[VelocityData]:
        """Gets the ip_events of this WebhookVelocity.  # noqa: E501


        :return: The ip_events of this WebhookVelocity.  # noqa: E501
        """
        return self._ip_events

    @ip_events.setter
    def ip_events(self, ip_events: Optional[VelocityData]):
        """Sets the ip_events of this WebhookVelocity.


        :param ip_events: The ip_events of this WebhookVelocity.  # noqa: E501
        """

        self._ip_events = ip_events

    @property
    def distinct_ip_by_linked_id(self) -> Optional[VelocityData]:
        """Gets the distinct_ip_by_linked_id of this WebhookVelocity.  # noqa: E501


        :return: The distinct_ip_by_linked_id of this WebhookVelocity.  # noqa: E501
        """
        return self._distinct_ip_by_linked_id

    @distinct_ip_by_linked_id.setter
    def distinct_ip_by_linked_id(self, distinct_ip_by_linked_id: Optional[VelocityData]):
        """Sets the distinct_ip_by_linked_id of this WebhookVelocity.


        :param distinct_ip_by_linked_id: The distinct_ip_by_linked_id of this WebhookVelocity.  # noqa: E501
        """

        self._distinct_ip_by_linked_id = distinct_ip_by_linked_id

    @property
    def distinct_visitor_id_by_linked_id(self) -> Optional[VelocityData]:
        """Gets the distinct_visitor_id_by_linked_id of this WebhookVelocity.  # noqa: E501


        :return: The distinct_visitor_id_by_linked_id of this WebhookVelocity.  # noqa: E501
        """
        return self._distinct_visitor_id_by_linked_id

    @distinct_visitor_id_by_linked_id.setter
    def distinct_visitor_id_by_linked_id(self, distinct_visitor_id_by_linked_id: Optional[VelocityData]):
        """Sets the distinct_visitor_id_by_linked_id of this WebhookVelocity.


        :param distinct_visitor_id_by_linked_id: The distinct_visitor_id_by_linked_id of this WebhookVelocity.  # noqa: E501
        """

        self._distinct_visitor_id_by_linked_id = distinct_visitor_id_by_linked_id
