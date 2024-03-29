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

class VpnResultMethods(object):
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
        'timezone_mismatch': 'bool',
        'public_vpn': 'bool',
        'auxiliary_mobile': 'bool'
    }

    attribute_map = {
        'timezone_mismatch': 'timezoneMismatch',
        'public_vpn': 'publicVPN',
        'auxiliary_mobile': 'auxiliaryMobile'
    }

    def __init__(self, timezone_mismatch=None, public_vpn=None, auxiliary_mobile=None):  # noqa: E501
        """VpnResultMethods - a model defined in Swagger"""  # noqa: E501
        self._timezone_mismatch = None
        self._public_vpn = None
        self._auxiliary_mobile = None
        self.discriminator = None
        self.timezone_mismatch = timezone_mismatch
        self.public_vpn = public_vpn
        self.auxiliary_mobile = auxiliary_mobile

    @property
    def timezone_mismatch(self):
        """Gets the timezone_mismatch of this VpnResultMethods.  # noqa: E501

        User's browser timezone doesn't match the timezone from which the request was originally made.  # noqa: E501

        :return: The timezone_mismatch of this VpnResultMethods.  # noqa: E501
        :rtype: bool
        """
        return self._timezone_mismatch

    @timezone_mismatch.setter
    def timezone_mismatch(self, timezone_mismatch):
        """Sets the timezone_mismatch of this VpnResultMethods.

        User's browser timezone doesn't match the timezone from which the request was originally made.  # noqa: E501

        :param timezone_mismatch: The timezone_mismatch of this VpnResultMethods.  # noqa: E501
        :type: bool
        """
        if timezone_mismatch is None:
            raise ValueError("Invalid value for `timezone_mismatch`, must not be `None`")  # noqa: E501

        self._timezone_mismatch = timezone_mismatch

    @property
    def public_vpn(self):
        """Gets the public_vpn of this VpnResultMethods.  # noqa: E501

        Request IP address is owned and used by a public VPN service provider.  # noqa: E501

        :return: The public_vpn of this VpnResultMethods.  # noqa: E501
        :rtype: bool
        """
        return self._public_vpn

    @public_vpn.setter
    def public_vpn(self, public_vpn):
        """Sets the public_vpn of this VpnResultMethods.

        Request IP address is owned and used by a public VPN service provider.  # noqa: E501

        :param public_vpn: The public_vpn of this VpnResultMethods.  # noqa: E501
        :type: bool
        """
        if public_vpn is None:
            raise ValueError("Invalid value for `public_vpn`, must not be `None`")  # noqa: E501

        self._public_vpn = public_vpn

    @property
    def auxiliary_mobile(self):
        """Gets the auxiliary_mobile of this VpnResultMethods.  # noqa: E501

        This method applies to mobile devices only. Indicates the result of additional methods used to detect a VPN in mobile devices.  # noqa: E501

        :return: The auxiliary_mobile of this VpnResultMethods.  # noqa: E501
        :rtype: bool
        """
        return self._auxiliary_mobile

    @auxiliary_mobile.setter
    def auxiliary_mobile(self, auxiliary_mobile):
        """Sets the auxiliary_mobile of this VpnResultMethods.

        This method applies to mobile devices only. Indicates the result of additional methods used to detect a VPN in mobile devices.  # noqa: E501

        :param auxiliary_mobile: The auxiliary_mobile of this VpnResultMethods.  # noqa: E501
        :type: bool
        """
        if auxiliary_mobile is None:
            raise ValueError("Invalid value for `auxiliary_mobile`, must not be `None`")  # noqa: E501

        self._auxiliary_mobile = auxiliary_mobile

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
        if issubclass(VpnResultMethods, dict):
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
        if not isinstance(other, VpnResultMethods):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VpnResultMethods):
            return True

        return self.to_dict() != other.to_dict()
