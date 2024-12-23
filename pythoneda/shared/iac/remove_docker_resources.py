# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/remove_docker_resources.py

This script defines the RemoveDockerResources class.

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
from .stack_operation import StackOperation
from pythoneda.shared.iac.events import (
    DockerResourcesRemovalFailed,
    DockerResourcesRemovalRequested,
    DockerResourcesRemoved,
)
from typing import Union


class RemoveDockerResources(StackOperation):
    """
    Removes Docker resources in a stack.

    Class name: RemoveDockerResources

    Responsibilities:
        - Represent the action of removing Docker resources in a IaC stack.

    Collaborators:
        - None
    """

    def __init__(self, event: DockerResourcesRemovalRequested):
        """
        Creates a new RemoveDockerResources instance.
        :param event: The event.
        :type event: pythoneda.shared.iac.events.DockerResourcesRemovalRequested]
        """
        super().__init__(event)

    @abc.abstractmethod
    async def perform(
        self,
    ) -> Union[DockerResourcesRemoved, DockerResourcesRemovalFailed]:
        """
        Removes the Docker-dependent infrastructure resources.
        :return: Either a DockerResourcesRemoved or DockerResourcesRemovalFailed event.
        :rtype: Union[DockerResourcesRemoved, DockerResourcesRemovalFailed]
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
