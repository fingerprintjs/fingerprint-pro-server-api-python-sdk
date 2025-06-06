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
from fingerprint_pro_server_api_sdk.models.tag import Tag


class EventsUpdateRequest(BaseModel):
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
        'linked_id': 'str',
        'tag': 'Tag',
        'suspect': 'bool'
    }

    nullable_map = {
        'linked_id': False,
        'tag': False,
        'suspect': False
    }

    attribute_map = {
        'linked_id': 'linkedId',
        'tag': 'tag',
        'suspect': 'suspect'
    }

    def __init__(self, linked_id=None, tag=None, suspect=None):  # noqa: E501
        """EventsUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._linked_id = None
        self._tag = None
        self._suspect = None
        self.discriminator = None
        if linked_id is not None:
            self.linked_id = linked_id
        if tag is not None:
            self.tag = tag
        if suspect is not None:
            self.suspect = suspect

    @property
    def linked_id(self) -> Optional[str]:
        """Gets the linked_id of this EventsUpdateRequest.  # noqa: E501

        LinkedID value to assign to the existing event  # noqa: E501

        :return: The linked_id of this EventsUpdateRequest.  # noqa: E501
        """
        return self._linked_id

    @linked_id.setter
    def linked_id(self, linked_id: Optional[str]):
        """Sets the linked_id of this EventsUpdateRequest.

        LinkedID value to assign to the existing event  # noqa: E501

        :param linked_id: The linked_id of this EventsUpdateRequest.  # noqa: E501
        """

        self._linked_id = linked_id

    @property
    def tag(self) -> Optional[Tag]:
        """Gets the tag of this EventsUpdateRequest.  # noqa: E501


        :return: The tag of this EventsUpdateRequest.  # noqa: E501
        """
        return self._tag

    @tag.setter
    def tag(self, tag: Optional[Tag]):
        """Sets the tag of this EventsUpdateRequest.


        :param tag: The tag of this EventsUpdateRequest.  # noqa: E501
        """

        self._tag = tag

    @property
    def suspect(self) -> Optional[bool]:
        """Gets the suspect of this EventsUpdateRequest.  # noqa: E501

        Suspect flag indicating observed suspicious or fraudulent event  # noqa: E501

        :return: The suspect of this EventsUpdateRequest.  # noqa: E501
        """
        return self._suspect

    @suspect.setter
    def suspect(self, suspect: Optional[bool]):
        """Sets the suspect of this EventsUpdateRequest.

        Suspect flag indicating observed suspicious or fraudulent event  # noqa: E501

        :param suspect: The suspect of this EventsUpdateRequest.  # noqa: E501
        """

        self._suspect = suspect

