# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class TemplateSummaryDiffTasksNewOld(object):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'cron': 'str',
        'description': 'str',
        'every': 'str',
        'offset': 'str',
        'query': 'str',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cron': 'cron',
        'description': 'description',
        'every': 'every',
        'offset': 'offset',
        'query': 'query',
        'status': 'status'
    }

    def __init__(self, name=None, cron=None, description=None, every=None, offset=None, query=None, status=None):  # noqa: E501,D401,D403
        """TemplateSummaryDiffTasksNewOld - a model defined in OpenAPI."""  # noqa: E501
        self._name = None
        self._cron = None
        self._description = None
        self._every = None
        self._offset = None
        self._query = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cron is not None:
            self.cron = cron
        if description is not None:
            self.description = description
        if every is not None:
            self.every = every
        if offset is not None:
            self.offset = offset
        if query is not None:
            self.query = query
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Get the name of this TemplateSummaryDiffTasksNewOld.

        :return: The name of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this TemplateSummaryDiffTasksNewOld.

        :param name: The name of this TemplateSummaryDiffTasksNewOld.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def cron(self):
        """Get the cron of this TemplateSummaryDiffTasksNewOld.

        :return: The cron of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """  # noqa: E501
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Set the cron of this TemplateSummaryDiffTasksNewOld.

        :param cron: The cron of this TemplateSummaryDiffTasksNewOld.
        :type: str
        """  # noqa: E501
        self._cron = cron

    @property
    def description(self):
        """Get the description of this TemplateSummaryDiffTasksNewOld.

        :return: The description of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this TemplateSummaryDiffTasksNewOld.

        :param description: The description of this TemplateSummaryDiffTasksNewOld.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def every(self):
        """Get the every of this TemplateSummaryDiffTasksNewOld.

        :return: The every of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """  # noqa: E501
        return self._every

    @every.setter
    def every(self, every):
        """Set the every of this TemplateSummaryDiffTasksNewOld.

        :param every: The every of this TemplateSummaryDiffTasksNewOld.
        :type: str
        """  # noqa: E501
        self._every = every

    @property
    def offset(self):
        """Get the offset of this TemplateSummaryDiffTasksNewOld.

        :return: The offset of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """  # noqa: E501
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Set the offset of this TemplateSummaryDiffTasksNewOld.

        :param offset: The offset of this TemplateSummaryDiffTasksNewOld.
        :type: str
        """  # noqa: E501
        self._offset = offset

    @property
    def query(self):
        """Get the query of this TemplateSummaryDiffTasksNewOld.

        :return: The query of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """  # noqa: E501
        return self._query

    @query.setter
    def query(self, query):
        """Set the query of this TemplateSummaryDiffTasksNewOld.

        :param query: The query of this TemplateSummaryDiffTasksNewOld.
        :type: str
        """  # noqa: E501
        self._query = query

    @property
    def status(self):
        """Get the status of this TemplateSummaryDiffTasksNewOld.

        :return: The status of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """  # noqa: E501
        return self._status

    @status.setter
    def status(self, status):
        """Set the status of this TemplateSummaryDiffTasksNewOld.

        :param status: The status of this TemplateSummaryDiffTasksNewOld.
        :type: str
        """  # noqa: E501
        self._status = status

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in self.openapi_types.items():
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, TemplateSummaryDiffTasksNewOld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other