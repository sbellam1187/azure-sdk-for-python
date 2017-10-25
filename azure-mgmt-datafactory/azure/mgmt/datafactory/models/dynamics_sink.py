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

from .copy_sink import CopySink


class DynamicsSink(CopySink):
    """A copy activity Dynamics sink.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param write_batch_size: Write batch size. Type: integer (or Expression
     with resultType integer), minimum: 0.
    :type write_batch_size: object
    :param write_batch_timeout: Write batch timeout. Type: string (or
     Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type write_batch_timeout: object
    :param sink_retry_count: Sink retry count. Type: integer (or Expression
     with resultType integer).
    :type sink_retry_count: object
    :param sink_retry_wait: Sink retry wait. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type sink_retry_wait: object
    :param type: Constant filled by server.
    :type type: str
    :ivar write_behavior: The write behavior for the operation. Default value:
     "Upsert" .
    :vartype write_behavior: str
    :param ignore_null_values: The flag indicating whether ignore null values
     from input dataset (except key fields) during write operation. Default is
     false. Type: boolean (or Expression with resultType boolean).
    :type ignore_null_values: object
    """

    _validation = {
        'type': {'required': True},
        'write_behavior': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'write_batch_size': {'key': 'writeBatchSize', 'type': 'object'},
        'write_batch_timeout': {'key': 'writeBatchTimeout', 'type': 'object'},
        'sink_retry_count': {'key': 'sinkRetryCount', 'type': 'object'},
        'sink_retry_wait': {'key': 'sinkRetryWait', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'write_behavior': {'key': 'writeBehavior', 'type': 'str'},
        'ignore_null_values': {'key': 'ignoreNullValues', 'type': 'object'},
    }

    write_behavior = "Upsert"

    def __init__(self, write_batch_size=None, write_batch_timeout=None, sink_retry_count=None, sink_retry_wait=None, ignore_null_values=None):
        super(DynamicsSink, self).__init__(write_batch_size=write_batch_size, write_batch_timeout=write_batch_timeout, sink_retry_count=sink_retry_count, sink_retry_wait=sink_retry_wait)
        self.ignore_null_values = ignore_null_values
        self.type = 'DynamicsSink'
