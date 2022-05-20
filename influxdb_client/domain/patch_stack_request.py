# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class PatchStackRequest(object):
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
        'description': 'str',
        'template_ur_ls': 'list[str]',
        'additional_resources': 'list[PatchStackRequestAdditionalResources]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'template_ur_ls': 'templateURLs',
        'additional_resources': 'additionalResources'
    }

    def __init__(self, name=None, description=None, template_ur_ls=None, additional_resources=None):  # noqa: E501,D401,D403
        """PatchStackRequest - a model defined in OpenAPI."""  # noqa: E501
        self._name = None
        self._description = None
        self._template_ur_ls = None
        self._additional_resources = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.template_ur_ls = template_ur_ls
        if additional_resources is not None:
            self.additional_resources = additional_resources

    @property
    def name(self):
        """Get the name of this PatchStackRequest.

        :return: The name of this PatchStackRequest.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this PatchStackRequest.

        :param name: The name of this PatchStackRequest.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this PatchStackRequest.

        :return: The description of this PatchStackRequest.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this PatchStackRequest.

        :param description: The description of this PatchStackRequest.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def template_ur_ls(self):
        """Get the template_ur_ls of this PatchStackRequest.

        :return: The template_ur_ls of this PatchStackRequest.
        :rtype: list[str]
        """  # noqa: E501
        return self._template_ur_ls

    @template_ur_ls.setter
    def template_ur_ls(self, template_ur_ls):
        """Set the template_ur_ls of this PatchStackRequest.

        :param template_ur_ls: The template_ur_ls of this PatchStackRequest.
        :type: list[str]
        """  # noqa: E501
        self._template_ur_ls = template_ur_ls

    @property
    def additional_resources(self):
        """Get the additional_resources of this PatchStackRequest.

        :return: The additional_resources of this PatchStackRequest.
        :rtype: list[PatchStackRequestAdditionalResources]
        """  # noqa: E501
        return self._additional_resources

    @additional_resources.setter
    def additional_resources(self, additional_resources):
        """Set the additional_resources of this PatchStackRequest.

        :param additional_resources: The additional_resources of this PatchStackRequest.
        :type: list[PatchStackRequestAdditionalResources]
        """  # noqa: E501
        self._additional_resources = additional_resources

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
        if not isinstance(other, PatchStackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other