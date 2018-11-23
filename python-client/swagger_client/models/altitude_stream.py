# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.base_stream import BaseStream  # noqa: F401,E501


class AltitudeStream(object):
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
        'original_size': 'int',
        'resolution': 'str',
        'series_type': 'str',
        'data': 'list[float]'
    }

    attribute_map = {
        'original_size': 'original_size',
        'resolution': 'resolution',
        'series_type': 'series_type',
        'data': 'data'
    }

    def __init__(self, original_size=None, resolution=None, series_type=None, data=None):  # noqa: E501
        """AltitudeStream - a model defined in Swagger"""  # noqa: E501

        self._original_size = None
        self._resolution = None
        self._series_type = None
        self._data = None
        self.discriminator = None

        if original_size is not None:
            self.original_size = original_size
        if resolution is not None:
            self.resolution = resolution
        if series_type is not None:
            self.series_type = series_type
        if data is not None:
            self.data = data

    @property
    def original_size(self):
        """Gets the original_size of this AltitudeStream.  # noqa: E501

        The number of data points in this stream  # noqa: E501

        :return: The original_size of this AltitudeStream.  # noqa: E501
        :rtype: int
        """
        return self._original_size

    @original_size.setter
    def original_size(self, original_size):
        """Sets the original_size of this AltitudeStream.

        The number of data points in this stream  # noqa: E501

        :param original_size: The original_size of this AltitudeStream.  # noqa: E501
        :type: int
        """

        self._original_size = original_size

    @property
    def resolution(self):
        """Gets the resolution of this AltitudeStream.  # noqa: E501

        The level of detail (sampling) in which this stream was returned  # noqa: E501

        :return: The resolution of this AltitudeStream.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this AltitudeStream.

        The level of detail (sampling) in which this stream was returned  # noqa: E501

        :param resolution: The resolution of this AltitudeStream.  # noqa: E501
        :type: str
        """
        allowed_values = ["low", "medium", "high"]  # noqa: E501
        if resolution not in allowed_values:
            raise ValueError(
                "Invalid value for `resolution` ({0}), must be one of {1}"  # noqa: E501
                .format(resolution, allowed_values)
            )

        self._resolution = resolution

    @property
    def series_type(self):
        """Gets the series_type of this AltitudeStream.  # noqa: E501

        The base series used in the case the stream was downsampled  # noqa: E501

        :return: The series_type of this AltitudeStream.  # noqa: E501
        :rtype: str
        """
        return self._series_type

    @series_type.setter
    def series_type(self, series_type):
        """Sets the series_type of this AltitudeStream.

        The base series used in the case the stream was downsampled  # noqa: E501

        :param series_type: The series_type of this AltitudeStream.  # noqa: E501
        :type: str
        """
        allowed_values = ["distance", "time"]  # noqa: E501
        if series_type not in allowed_values:
            raise ValueError(
                "Invalid value for `series_type` ({0}), must be one of {1}"  # noqa: E501
                .format(series_type, allowed_values)
            )

        self._series_type = series_type

    @property
    def data(self):
        """Gets the data of this AltitudeStream.  # noqa: E501

        The sequence of altitude values for this stream, in meters  # noqa: E501

        :return: The data of this AltitudeStream.  # noqa: E501
        :rtype: list[float]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AltitudeStream.

        The sequence of altitude values for this stream, in meters  # noqa: E501

        :param data: The data of this AltitudeStream.  # noqa: E501
        :type: list[float]
        """

        self._data = data

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AltitudeStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
