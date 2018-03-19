# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PatchSignalRResourceRequest(Model):
    """Parameters for SignalR service update operation.

    :param location: The location of the SignalR service.
    :type location: str
    :param tags: A list of key value pairs that describe the resource.
    :type tags: dict[str, str]
    :param sku: The billing information of the resource.(e.g. basic vs.
     standard)
    :type sku: ~azure.mgmt.signalr.models.ResourceSku
    :param properties: Settings used to provision or configure the resource
    :type properties: object
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'ResourceSku'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, *, location: str=None, tags=None, sku=None, properties=None, **kwargs) -> None:
        super(PatchSignalRResourceRequest, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.sku = sku
        self.properties = properties
