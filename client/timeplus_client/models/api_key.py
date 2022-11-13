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

class APIKey(object):
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
        'created_at': 'int',
        'expire_at': 'int',
        'id': 'str',
        'name': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'created_at': 'created_at',
        'expire_at': 'expire_at',
        'id': 'id',
        'name': 'name',
        'permissions': 'permissions'
    }

    def __init__(self, created_at=None, expire_at=None, id=None, name=None, permissions=None):  # noqa: E501
        """APIKey - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._expire_at = None
        self._id = None
        self._name = None
        self._permissions = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if expire_at is not None:
            self.expire_at = expire_at
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions

    @property
    def created_at(self):
        """Gets the created_at of this APIKey.  # noqa: E501

        creation time represented as the number of seconds elapsed since January 1, 1970 UTC  # noqa: E501

        :return: The created_at of this APIKey.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this APIKey.

        creation time represented as the number of seconds elapsed since January 1, 1970 UTC  # noqa: E501

        :param created_at: The created_at of this APIKey.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def expire_at(self):
        """Gets the expire_at of this APIKey.  # noqa: E501

        expiration time represented as the number of seconds elapsed since January 1, 1970 UTC  # noqa: E501

        :return: The expire_at of this APIKey.  # noqa: E501
        :rtype: int
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        """Sets the expire_at of this APIKey.

        expiration time represented as the number of seconds elapsed since January 1, 1970 UTC  # noqa: E501

        :param expire_at: The expire_at of this APIKey.  # noqa: E501
        :type: int
        """

        self._expire_at = expire_at

    @property
    def id(self):
        """Gets the id of this APIKey.  # noqa: E501

        a string that identifies an API key, readonly.  # noqa: E501

        :return: The id of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this APIKey.

        a string that identifies an API key, readonly.  # noqa: E501

        :param id: The id of this APIKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this APIKey.  # noqa: E501

        the name of the API key  # noqa: E501

        :return: The name of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this APIKey.

        the name of the API key  # noqa: E501

        :param name: The name of this APIKey.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this APIKey.  # noqa: E501

        list of permissions associated with the API key  # noqa: E501

        :return: The permissions of this APIKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this APIKey.

        list of permissions associated with the API key  # noqa: E501

        :param permissions: The permissions of this APIKey.  # noqa: E501
        :type: list[str]
        """

        self._permissions = permissions

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
        if issubclass(APIKey, dict):
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
        if not isinstance(other, APIKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
