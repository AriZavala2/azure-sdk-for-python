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

from .container_registry_artifact_event_data_py3 import ContainerRegistryArtifactEventData


class ContainerRegistryChartPushedEventData(ContainerRegistryArtifactEventData):
    """Schema of the Data property of an EventGridEvent for a
    Microsoft.ContainerRegistry.ChartPushed event.

    :param id: The event ID.
    :type id: str
    :param timestamp: The time at which the event occurred.
    :type timestamp: datetime
    :param action: The action that encompasses the provided event.
    :type action: str
    :param target: The target of the event.
    :type target: ~azure.eventgrid.models.ContainerRegistryArtifactEventTarget
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'action': {'key': 'action', 'type': 'str'},
        'target': {'key': 'target', 'type': 'ContainerRegistryArtifactEventTarget'},
    }

    def __init__(self, *, id: str=None, timestamp=None, action: str=None, target=None, **kwargs) -> None:
        super(ContainerRegistryChartPushedEventData, self).__init__(id=id, timestamp=timestamp, action=action, target=target, **kwargs)