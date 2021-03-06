# coding: utf-8

"""
    Solar.web Query API (SWQAPI)

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ErrorResponse(object):
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
        'response_error': 'int',
        'response_message': 'str'
    }

    attribute_map = {
        'response_error': 'responseError',
        'response_message': 'responseMessage'
    }

    def __init__(self, response_error=None, response_message=None):  # noqa: E501
        """ErrorResponse - a model defined in Swagger"""  # noqa: E501
        self._response_error = None
        self._response_message = None
        self.discriminator = None
        if response_error is not None:
            self.response_error = response_error
        if response_message is not None:
            self.response_message = response_message

    @property
    def response_error(self):
        """Gets the response_error of this ErrorResponse.  # noqa: E501


        :return: The response_error of this ErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._response_error

    @response_error.setter
    def response_error(self, response_error):
        """Sets the response_error of this ErrorResponse.


        :param response_error: The response_error of this ErrorResponse.  # noqa: E501
        :type: int
        """

        self._response_error = response_error

    @property
    def response_message(self):
        """Gets the response_message of this ErrorResponse.  # noqa: E501


        :return: The response_message of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        """Sets the response_message of this ErrorResponse.


        :param response_message: The response_message of this ErrorResponse.  # noqa: E501
        :type: str
        """

        self._response_message = response_message

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
        if issubclass(ErrorResponse, dict):
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
        if not isinstance(other, ErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
