# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Response(object):
    """
    Fields `lastTimestamp` and `paginationKey` added when `limit` or `before` parameter provided and there is more data to show

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
        'visitor_id': 'str',
        'visits': 'list[ResponseVisits]',
        'last_timestamp': 'int',
        'pagination_key': 'str'
    }

    attribute_map = {
        'visitor_id': 'visitorId',
        'visits': 'visits',
        'last_timestamp': 'lastTimestamp',
        'pagination_key': 'paginationKey'
    }

    def __init__(self, visitor_id=None, visits=None, last_timestamp=None, pagination_key=None):  # noqa: E501
        """Response - a model defined in Swagger"""  # noqa: E501
        self._visitor_id = None
        self._visits = None
        self._last_timestamp = None
        self._pagination_key = None
        self.discriminator = None
        self.visitor_id = visitor_id
        self.visits = visits
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp
        if pagination_key is not None:
            self.pagination_key = pagination_key

    @property
    def visitor_id(self):
        """Gets the visitor_id of this Response.  # noqa: E501


        :return: The visitor_id of this Response.  # noqa: E501
        :rtype: str
        """
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, visitor_id):
        """Sets the visitor_id of this Response.


        :param visitor_id: The visitor_id of this Response.  # noqa: E501
        :type: str
        """
        if visitor_id is None:
            raise ValueError("Invalid value for `visitor_id`, must not be `None`")  # noqa: E501

        self._visitor_id = visitor_id

    @property
    def visits(self):
        """Gets the visits of this Response.  # noqa: E501


        :return: The visits of this Response.  # noqa: E501
        :rtype: list[ResponseVisits]
        """
        return self._visits

    @visits.setter
    def visits(self, visits):
        """Sets the visits of this Response.


        :param visits: The visits of this Response.  # noqa: E501
        :type: list[ResponseVisits]
        """
        if visits is None:
            raise ValueError("Invalid value for `visits`, must not be `None`")  # noqa: E501

        self._visits = visits

    @property
    def last_timestamp(self):
        """Gets the last_timestamp of this Response.  # noqa: E501

        ⚠️ Deprecated paging attribute, please use `paginationKey` instead. Timestamp of the last visit in the current page of results.   # noqa: E501

        :return: The last_timestamp of this Response.  # noqa: E501
        :rtype: int
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """Sets the last_timestamp of this Response.

        ⚠️ Deprecated paging attribute, please use `paginationKey` instead. Timestamp of the last visit in the current page of results.   # noqa: E501

        :param last_timestamp: The last_timestamp of this Response.  # noqa: E501
        :type: int
        """

        self._last_timestamp = last_timestamp

    @property
    def pagination_key(self):
        """Gets the pagination_key of this Response.  # noqa: E501

        Request ID of the last visit in the current page of results. Use this value in the following request as the `paginationKey` parameter to get the next page of results.  # noqa: E501

        :return: The pagination_key of this Response.  # noqa: E501
        :rtype: str
        """
        return self._pagination_key

    @pagination_key.setter
    def pagination_key(self, pagination_key):
        """Sets the pagination_key of this Response.

        Request ID of the last visit in the current page of results. Use this value in the following request as the `paginationKey` parameter to get the next page of results.  # noqa: E501

        :param pagination_key: The pagination_key of this Response.  # noqa: E501
        :type: str
        """

        self._pagination_key = pagination_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Response, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Response):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Response):
            return True

        return self.to_dict() != other.to_dict()
