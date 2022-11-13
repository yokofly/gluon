# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Latency(object):
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
        'avg': 'float',
        'latest': 'list[float]',
        'max': 'float',
        'min': 'float',
        'sum': 'float'
    }

    attribute_map = {
        'avg': 'avg',
        'latest': 'latest',
        'max': 'max',
        'min': 'min',
        'sum': 'sum'
    }

    def __init__(self, avg=None, latest=None, max=None, min=None, sum=None):  # noqa: E501
        """Latency - a model defined in Swagger"""  # noqa: E501
        self._avg = None
        self._latest = None
        self._max = None
        self._min = None
        self._sum = None
        self.discriminator = None
        if avg is not None:
            self.avg = avg
        if latest is not None:
            self.latest = latest
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if sum is not None:
            self.sum = sum

    @property
    def avg(self):
        """Gets the avg of this Latency.  # noqa: E501


        :return: The avg of this Latency.  # noqa: E501
        :rtype: float
        """
        return self._avg

    @avg.setter
    def avg(self, avg):
        """Sets the avg of this Latency.


        :param avg: The avg of this Latency.  # noqa: E501
        :type: float
        """

        self._avg = avg

    @property
    def latest(self):
        """Gets the latest of this Latency.  # noqa: E501


        :return: The latest of this Latency.  # noqa: E501
        :rtype: list[float]
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this Latency.


        :param latest: The latest of this Latency.  # noqa: E501
        :type: list[float]
        """

        self._latest = latest

    @property
    def max(self):
        """Gets the max of this Latency.  # noqa: E501


        :return: The max of this Latency.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Latency.


        :param max: The max of this Latency.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this Latency.  # noqa: E501


        :return: The min of this Latency.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this Latency.


        :param min: The min of this Latency.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def sum(self):
        """Gets the sum of this Latency.  # noqa: E501


        :return: The sum of this Latency.  # noqa: E501
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this Latency.


        :param sum: The sum of this Latency.  # noqa: E501
        :type: float
        """

        self._sum = sum

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
        if issubclass(Latency, dict):
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
        if not isinstance(other, Latency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
