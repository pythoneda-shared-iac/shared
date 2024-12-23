# vim: set fileencoding=utf-8
"""
pythoneda/iac/stack.py

This script defines the Stack class.

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
from pythoneda.shared import BaseObject, Event, Port, primary_key_attribute
from pythoneda.shared.iac.events import InfrastructureUpdated
from .resource import Resource
from typing import Any, Dict, List


class Stack(Port, BaseObject):
    """
    A PythonEDA IaC stack.

    Class name: Stack

    Responsibilities:
        - Represent a IaC stack.

    Collaborators:
        - None
    """

    def __init__(self, stackName: str, projectName: str, location: str):
        """
        Creates a new stack instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The location.
        :type location: str
        """
        super().__init__()
        self._stack_name = stackName
        self._project_name = projectName
        self._location = location
        self._resources = []
        self._outcome = None

    @property
    @primary_key_attribute
    def stack_name(self) -> str:
        """
        Retrieves the stack name.
        :return: The name of the stack.
        :rtype: str
        """
        return self._stack_name

    @property
    @primary_key_attribute
    def project_name(self) -> str:
        """
        Retrieves the project name.
        :return: The name of the project.
        :rtype: str
        """
        return self._project_name

    @property
    def location(self) -> str:
        """
        Retrieves the location.
        :return: The location.
        :rtype: str
        """
        return self._location

    @property
    def resources(self) -> List[Resource]:
        """
        Retrieves the resources.
        :return: The resources.
        :rtype: List[Resource]
        """
        return self._resources

    @abc.abstractmethod
    async def up(self) -> List[Event]:
        """
        Brings up the stack.
        :return: Either an InfrastructureUpdated event or an InfrastructureNotUpdated.
        :rtype: List[pythoneda.shared.Event]
        """
        pass

    @property
    def outcome(self) -> Any:
        """
        Retrieves the outcome of the "up" operation.
        :return: Such outcome.
        :rtype: Any
        """
        return self._outcome

    @abc.abstractmethod
    async def declare_docker_resources(
        self,
        imageName: str,
        imageVersion: str,
        imageUrl: str = None,
    ):
        """
        Declares the Docker-dependent infrastructure resources.
        :param imageName: The name of the Docker image.
        :type imageName: str
        :param imageVersion: The version of the Docker image.
        :type imageVersion: str
        :param imageUrl: The url of the Docker image.
        :type imageUrl: str
        :return: Either a DockerResourcesUpdated or DockerResourcesUpdateFailed event.
        :rtype: pythoneda.shared.iac.events.DockerResourcesUpdated
        """
        pass

    @abc.abstractmethod
    async def retrieve_container_registry_credentials(self) -> Dict[str, str]:
        """
        Retrieves the container registry credentials.
        :return: A dictionary with the credentials.
        :rtype: Dict[str, str]
        """
        pass

    @abc.abstractmethod
    def request_docker_image(self, secretName: str, registryUrl: str):
        """
        Emits a request for the Docker image.
        :param secretName: The name of the secret.
        :type secretName: str
        :param registryUrl: The url of the registry.
        :type registryUrl: str
        :return: A DockerImageRequested event.
        :rtype: pythoneda.shared.artifact.events.DockerImageRequested
        """
        pass

    @abc.abstractmethod
    async def destroy(self):
        """
        Deletes the stack.
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
