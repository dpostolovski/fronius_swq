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


class HistoricalChannel(object):
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
        'channel_name': 'str',
        'channel_type': 'str',
        'unit': 'str',
        'value': 'float',
        'is_active': 'bool',
        'is_damaged': 'bool'
    }

    attribute_map = {
        'channel_name': 'channelName',
        'channel_type': 'channelType',
        'unit': 'unit',
        'value': 'value',
        'is_active': 'isActive',
        'is_damaged': 'isDamaged'
    }

    def __init__(self, channel_name=None, channel_type=None, unit=None, value=None, is_active=None, is_damaged=None):  # noqa: E501
        """HistoricalChannel - a model defined in Swagger"""  # noqa: E501
        self._channel_name = None
        self._channel_type = None
        self._unit = None
        self._value = None
        self._is_active = None
        self._is_damaged = None
        self.discriminator = None
        if channel_name is not None:
            self.channel_name = channel_name
        if channel_type is not None:
            self.channel_type = channel_type
        if unit is not None:
            self.unit = unit
        if value is not None:
            self.value = value
        if is_active is not None:
            self.is_active = is_active
        if is_damaged is not None:
            self.is_damaged = is_damaged

    @property
    def channel_name(self):
        """Gets the channel_name of this HistoricalChannel.  # noqa: E501


        :return: The channel_name of this HistoricalChannel.  # noqa: E501
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this HistoricalChannel.


        :param channel_name: The channel_name of this HistoricalChannel.  # noqa: E501
        :type: str
        """

        self._channel_name = channel_name

    @property
    def channel_type(self):
        """Gets the channel_type of this HistoricalChannel.  # noqa: E501


        :return: The channel_type of this HistoricalChannel.  # noqa: E501
        :rtype: str
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this HistoricalChannel.


        :param channel_type: The channel_type of this HistoricalChannel.  # noqa: E501
        :type: str
        """

        self._channel_type = channel_type

    @property
    def unit(self):
        """Gets the unit of this HistoricalChannel.  # noqa: E501


        :return: The unit of this HistoricalChannel.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this HistoricalChannel.


        :param unit: The unit of this HistoricalChannel.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def value(self):
        """Gets the value of this HistoricalChannel.  # noqa: E501


        :return: The value of this HistoricalChannel.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this HistoricalChannel.


        :param value: The value of this HistoricalChannel.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def is_active(self):
        """Gets the is_active of this HistoricalChannel.  # noqa: E501


        :return: The is_active of this HistoricalChannel.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this HistoricalChannel.


        :param is_active: The is_active of this HistoricalChannel.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_damaged(self):
        """Gets the is_damaged of this HistoricalChannel.  # noqa: E501


        :return: The is_damaged of this HistoricalChannel.  # noqa: E501
        :rtype: bool
        """
        return self._is_damaged

    @is_damaged.setter
    def is_damaged(self, is_damaged):
        """Sets the is_damaged of this HistoricalChannel.


        :param is_damaged: The is_damaged of this HistoricalChannel.  # noqa: E501
        :type: bool
        """

        self._is_damaged = is_damaged

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
        if issubclass(HistoricalChannel, dict):
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
        if not isinstance(other, HistoricalChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other