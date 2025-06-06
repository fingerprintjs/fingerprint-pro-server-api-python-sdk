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


class ErrorCode(BaseModel):
    """
    Error code:  * `RequestCannotBeParsed` - the query parameters or JSON payload contains some errors            that prevented us from parsing it (wrong type/surpassed limits).  * `TokenRequired` - `Auth-API-Key` header is missing or empty.  * `TokenNotFound` - no Fingerprint application found for specified secret key.  * `SubscriptionNotActive` - Fingerprint application is not active.  * `WrongRegion` - server and application region differ.  * `FeatureNotEnabled` - this feature (for example, Delete API) is not enabled for your application.  * `RequestNotFound` - the specified request ID was not found. It never existed, expired, or it has been deleted.  * `VisitorNotFound` - The specified visitor ID was not found. It never existed or it may have already been deleted.  * `TooManyRequests` - the limit on secret API key requests per second has been exceeded.  * `429 Too Many Requests` - the limit on secret API key requests per second has been exceeded.  * `StateNotReady` - The event specified with request id is           not ready for updates yet. Try again.           This error happens in rare cases when update API is called immediately           after receiving the request id on the client. In case you need to send           information right away, we recommend using the JS agent API instead.  * `Failed` - internal server error. 

    NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    REQUESTCANNOTBEPARSED = "RequestCannotBeParsed"
    TOKENREQUIRED = "TokenRequired"
    TOKENNOTFOUND = "TokenNotFound"
    SUBSCRIPTIONNOTACTIVE = "SubscriptionNotActive"
    WRONGREGION = "WrongRegion"
    FEATURENOTENABLED = "FeatureNotEnabled"
    REQUESTNOTFOUND = "RequestNotFound"
    VISITORNOTFOUND = "VisitorNotFound"
    TOOMANYREQUESTS = "TooManyRequests"
    _429_TOO_MANY_REQUESTS = "429 Too Many Requests"
    STATENOTREADY = "StateNotReady"
    FAILED = "Failed"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    nullable_map = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """ErrorCode - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

