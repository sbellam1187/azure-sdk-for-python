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

from .dataset import Dataset


class WebTableDataset(Dataset):
    """The dataset points to a HTML table in the web page.

    :param description: Dataset description.
    :type description: str
    :param structure: Columns that define the structure of the dataset. Type:
     array (or Expression with resultType array), itemType: DatasetDataElement.
    :type structure: object
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param parameters: Parameters for dataset.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param type: Constant filled by server.
    :type type: str
    :param index: The zero-based index of the table in the web page. Type:
     integer (or Expression with resultType integer), minimum: 0.
    :type index: object
    :param path: The relative URL to the web page from the linked service URL.
     Type: string (or Expression with resultType string).
    :type path: object
    """

    _validation = {
        'linked_service_name': {'required': True},
        'type': {'required': True},
        'index': {'required': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'structure': {'key': 'structure', 'type': 'object'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'type': {'key': 'type', 'type': 'str'},
        'index': {'key': 'typeProperties.index', 'type': 'object'},
        'path': {'key': 'typeProperties.path', 'type': 'object'},
    }

    def __init__(self, linked_service_name, index, description=None, structure=None, parameters=None, path=None):
        super(WebTableDataset, self).__init__(description=description, structure=structure, linked_service_name=linked_service_name, parameters=parameters)
        self.index = index
        self.path = path
        self.type = 'WebTable'
