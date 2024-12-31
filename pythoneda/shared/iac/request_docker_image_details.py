# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/request_docker_image_details.py

This script defines the RequestDockerImageDetails class.

Copyright (C) 2024-today pythoneda IaC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import abc
from .stack_operation import StackOperation
from pythoneda.shared import Event
from pythoneda.shared.iac.events import (
    DockerImageDetailsRequested,
)
from typing import Dict, List


class RequestDockerImageDetails(StackOperation, abc.ABC):
    """
    Fills-in the details of the desired Docker image to request.

    Class name: RequestDockerImageDetails

    Responsibilities:
        - Represent the action of asking for details of a Docker image.

    Collaborators:
        - None
    """

    def __init__(self, event: DockerImageDetailsRequested):
        """
        Creates a new RequestDockerImageDetails instance.
        :param event: The event.
        :type event: pythoneda.shared.iac.events.DockerImageDetailsRequested
        """
        super().__init__(event)

    @abc.abstractmethod
    async def perform(self) -> List[Event]:
        """
        Brings up the stack.
        :return: A DockerImageRequested event.
        :rtype: List[pythoneda.shared.Event]
        """
        pass


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End: