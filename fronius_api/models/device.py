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


class Device(object):
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
        'device_type': 'str',
        'device_id': 'str',
        'device_name': 'str',
        'device_manufacturer': 'str',
        'serial_number': 'str',
        'datalogger_id': 'str',
        'node_type': 'int',
        'number_mpp_trackers': 'int',
        'number_phases': 'int',
        'peak_power_dc1': 'float',
        'peak_power_dc2': 'float',
        'nominal_ac_power': 'float',
        'capacity': 'int',
        'update_available': 'bool',
        'is_active': 'bool',
        'deactivation_date': 'str',
        'sensors': 'list[Sensor]'
    }

    attribute_map = {
        'device_type': 'deviceType',
        'device_id': 'deviceId',
        'device_name': 'deviceName',
        'device_manufacturer': 'deviceManufacturer',
        'serial_number': 'serialNumber',
        'datalogger_id': 'dataloggerId',
        'node_type': 'nodeType',
        'number_mpp_trackers': 'numberMPPTrackers',
        'number_phases': 'numberPhases',
        'peak_power_dc1': 'peakPowerDc1',
        'peak_power_dc2': 'peakPowerDc2',
        'nominal_ac_power': 'nominalAcPower',
        'capacity': 'capacity',
        'update_available': 'updateAvailable',
        'is_active': 'isActive',
        'deactivation_date': 'deactivationDate',
        'sensors': 'sensors'
    }

    def __init__(self, device_type=None, device_id=None, device_name=None, device_manufacturer=None, serial_number=None, datalogger_id=None, node_type=None, number_mpp_trackers=None, number_phases=None, peak_power_dc1=None, peak_power_dc2=None, nominal_ac_power=None, capacity=None, update_available=None, is_active=None, deactivation_date=None, sensors=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._device_type = None
        self._device_id = None
        self._device_name = None
        self._device_manufacturer = None
        self._serial_number = None
        self._datalogger_id = None
        self._node_type = None
        self._number_mpp_trackers = None
        self._number_phases = None
        self._peak_power_dc1 = None
        self._peak_power_dc2 = None
        self._nominal_ac_power = None
        self._capacity = None
        self._update_available = None
        self._is_active = None
        self._deactivation_date = None
        self._sensors = None
        self.discriminator = None
        if device_type is not None:
            self.device_type = device_type
        if device_id is not None:
            self.device_id = device_id
        if device_name is not None:
            self.device_name = device_name
        if device_manufacturer is not None:
            self.device_manufacturer = device_manufacturer
        if serial_number is not None:
            self.serial_number = serial_number
        if datalogger_id is not None:
            self.datalogger_id = datalogger_id
        if node_type is not None:
            self.node_type = node_type
        if number_mpp_trackers is not None:
            self.number_mpp_trackers = number_mpp_trackers
        if number_phases is not None:
            self.number_phases = number_phases
        if peak_power_dc1 is not None:
            self.peak_power_dc1 = peak_power_dc1
        if peak_power_dc2 is not None:
            self.peak_power_dc2 = peak_power_dc2
        if nominal_ac_power is not None:
            self.nominal_ac_power = nominal_ac_power
        if capacity is not None:
            self.capacity = capacity
        if update_available is not None:
            self.update_available = update_available
        if is_active is not None:
            self.is_active = is_active
        if deactivation_date is not None:
            self.deactivation_date = deactivation_date
        if sensors is not None:
            self.sensors = sensors

    @property
    def device_type(self):
        """Gets the device_type of this Device.  # noqa: E501


        :return: The device_type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this Device.


        :param device_type: The device_type of this Device.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def device_id(self):
        """Gets the device_id of this Device.  # noqa: E501


        :return: The device_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Device.


        :param device_id: The device_id of this Device.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def device_name(self):
        """Gets the device_name of this Device.  # noqa: E501


        :return: The device_name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this Device.


        :param device_name: The device_name of this Device.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def device_manufacturer(self):
        """Gets the device_manufacturer of this Device.  # noqa: E501


        :return: The device_manufacturer of this Device.  # noqa: E501
        :rtype: str
        """
        return self._device_manufacturer

    @device_manufacturer.setter
    def device_manufacturer(self, device_manufacturer):
        """Sets the device_manufacturer of this Device.


        :param device_manufacturer: The device_manufacturer of this Device.  # noqa: E501
        :type: str
        """

        self._device_manufacturer = device_manufacturer

    @property
    def serial_number(self):
        """Gets the serial_number of this Device.  # noqa: E501


        :return: The serial_number of this Device.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this Device.


        :param serial_number: The serial_number of this Device.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def datalogger_id(self):
        """Gets the datalogger_id of this Device.  # noqa: E501


        :return: The datalogger_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._datalogger_id

    @datalogger_id.setter
    def datalogger_id(self, datalogger_id):
        """Sets the datalogger_id of this Device.


        :param datalogger_id: The datalogger_id of this Device.  # noqa: E501
        :type: str
        """

        self._datalogger_id = datalogger_id

    @property
    def node_type(self):
        """Gets the node_type of this Device.  # noqa: E501


        :return: The node_type of this Device.  # noqa: E501
        :rtype: int
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Device.


        :param node_type: The node_type of this Device.  # noqa: E501
        :type: int
        """

        self._node_type = node_type

    @property
    def number_mpp_trackers(self):
        """Gets the number_mpp_trackers of this Device.  # noqa: E501


        :return: The number_mpp_trackers of this Device.  # noqa: E501
        :rtype: int
        """
        return self._number_mpp_trackers

    @number_mpp_trackers.setter
    def number_mpp_trackers(self, number_mpp_trackers):
        """Sets the number_mpp_trackers of this Device.


        :param number_mpp_trackers: The number_mpp_trackers of this Device.  # noqa: E501
        :type: int
        """

        self._number_mpp_trackers = number_mpp_trackers

    @property
    def number_phases(self):
        """Gets the number_phases of this Device.  # noqa: E501


        :return: The number_phases of this Device.  # noqa: E501
        :rtype: int
        """
        return self._number_phases

    @number_phases.setter
    def number_phases(self, number_phases):
        """Sets the number_phases of this Device.


        :param number_phases: The number_phases of this Device.  # noqa: E501
        :type: int
        """

        self._number_phases = number_phases

    @property
    def peak_power_dc1(self):
        """Gets the peak_power_dc1 of this Device.  # noqa: E501


        :return: The peak_power_dc1 of this Device.  # noqa: E501
        :rtype: float
        """
        return self._peak_power_dc1

    @peak_power_dc1.setter
    def peak_power_dc1(self, peak_power_dc1):
        """Sets the peak_power_dc1 of this Device.


        :param peak_power_dc1: The peak_power_dc1 of this Device.  # noqa: E501
        :type: float
        """

        self._peak_power_dc1 = peak_power_dc1

    @property
    def peak_power_dc2(self):
        """Gets the peak_power_dc2 of this Device.  # noqa: E501


        :return: The peak_power_dc2 of this Device.  # noqa: E501
        :rtype: float
        """
        return self._peak_power_dc2

    @peak_power_dc2.setter
    def peak_power_dc2(self, peak_power_dc2):
        """Sets the peak_power_dc2 of this Device.


        :param peak_power_dc2: The peak_power_dc2 of this Device.  # noqa: E501
        :type: float
        """

        self._peak_power_dc2 = peak_power_dc2

    @property
    def nominal_ac_power(self):
        """Gets the nominal_ac_power of this Device.  # noqa: E501


        :return: The nominal_ac_power of this Device.  # noqa: E501
        :rtype: float
        """
        return self._nominal_ac_power

    @nominal_ac_power.setter
    def nominal_ac_power(self, nominal_ac_power):
        """Sets the nominal_ac_power of this Device.


        :param nominal_ac_power: The nominal_ac_power of this Device.  # noqa: E501
        :type: float
        """

        self._nominal_ac_power = nominal_ac_power

    @property
    def capacity(self):
        """Gets the capacity of this Device.  # noqa: E501


        :return: The capacity of this Device.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this Device.


        :param capacity: The capacity of this Device.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def update_available(self):
        """Gets the update_available of this Device.  # noqa: E501


        :return: The update_available of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._update_available

    @update_available.setter
    def update_available(self, update_available):
        """Sets the update_available of this Device.


        :param update_available: The update_available of this Device.  # noqa: E501
        :type: bool
        """

        self._update_available = update_available

    @property
    def is_active(self):
        """Gets the is_active of this Device.  # noqa: E501


        :return: The is_active of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Device.


        :param is_active: The is_active of this Device.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def deactivation_date(self):
        """Gets the deactivation_date of this Device.  # noqa: E501


        :return: The deactivation_date of this Device.  # noqa: E501
        :rtype: str
        """
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        """Sets the deactivation_date of this Device.


        :param deactivation_date: The deactivation_date of this Device.  # noqa: E501
        :type: str
        """

        self._deactivation_date = deactivation_date

    @property
    def sensors(self):
        """Gets the sensors of this Device.  # noqa: E501


        :return: The sensors of this Device.  # noqa: E501
        :rtype: list[Sensor]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this Device.


        :param sensors: The sensors of this Device.  # noqa: E501
        :type: list[Sensor]
        """

        self._sensors = sensors

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
