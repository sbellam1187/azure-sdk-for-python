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

from .linked_service import LinkedService


class CustomDataSourceLinkedService(LinkedService):
    """Custom linked service.

    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    :param type_properties: Custom linked service properties.
    :type type_properties: object
    """

    _validation = {
        'type': {'required': True},
        'type_properties': {'required': True},
    }

    _attribute_map = {
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'type_properties': {'key': 'typeProperties', 'type': 'object'},
    }

    def __init__(self, type_properties, connect_via=None, description=None):
        super(CustomDataSourceLinkedService, self).__init__(connect_via=connect_via, description=description)
        self.type_properties = type_properties
        self.type = 'CustomDataSource'
