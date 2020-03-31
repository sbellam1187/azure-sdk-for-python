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

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.runtime_operations import RuntimeOperations
from . import models


class QnAMakerRuntimeClientConfiguration(Configuration):
    """Configuration for QnAMakerRuntimeClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param runtime_endpoint: QnA Maker App Service endpoint (for example:
     https://{qnaservice-hostname}.azurewebsites.net).
    :type runtime_endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, runtime_endpoint, credentials):

        if runtime_endpoint is None:
            raise ValueError("Parameter 'runtime_endpoint' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = '{RuntimeEndpoint}/qnamaker'

        super(QnAMakerRuntimeClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-knowledge-qnamaker/{}'.format(VERSION))

        self.runtime_endpoint = runtime_endpoint
        self.credentials = credentials


class QnAMakerRuntimeClient(SDKClient):
    """An API for QnAMaker runtime

    :ivar config: Configuration for client.
    :vartype config: QnAMakerRuntimeClientConfiguration

    :ivar runtime: Runtime operations
    :vartype runtime: azure.cognitiveservices.knowledge.qnamaker.runtime.operations.RuntimeOperations

    :param runtime_endpoint: QnA Maker App Service endpoint (for example:
     https://{qnaservice-hostname}.azurewebsites.net).
    :type runtime_endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, runtime_endpoint, credentials):

        self.config = QnAMakerRuntimeClientConfiguration(runtime_endpoint, credentials)
        super(QnAMakerRuntimeClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '4.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.runtime = RuntimeOperations(
            self._client, self.config, self._serialize, self._deserialize)