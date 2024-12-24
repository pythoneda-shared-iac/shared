# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/stack_operation.py

This script defines the StackOperation class.

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
from pythoneda.shared import BaseObject, Event, primary_key_attribute
from pythoneda.shared.iac.events import (
    InfrastructureUpdateRequested,
    InfrastructureRemovalRequested,
)
from .resource import Resource
from typing import Any, Dict, List, Union


class StackOperation(BaseObject, abc.ABC):
    """
    An operation on a IaC stack.

    Class name: StackOperation

    Responsibilities:
        - Performs an action on a IaC stack.

    Collaborators:
        - None
    """

    def __init__(
        self,
        event: Union[InfrastructureUpdateRequested, InfrastructureRemovalRequested],
    ):
        """
        Creates a new stack instance.
        :param event: The event.
        :type event: Union[org.acmsl.iac.licdata.domain.InfrastructureUpdateRequested, org.acmsl.iac.licdata.domain.InfrastructureRemovalRequested]
        """
        super().__init__()
        self._event = event
        self._resources = []
        self._outcome = None

    @property
    @primary_key_attribute
    def event(
        self,
    ) -> Union[InfrastructureUpdateRequested, InfrastructureRemovalRequested]:
        """
        Retrieves the request event.
        :return: Such event.
        :rtype: Union[pythoneda.shared.iac.events.InfrastructureUpdateRequested, pythoneda.shared.iac.events.InfrastructureRemovalRequested]
        """
        return self._event

    @property
    def resources(self) -> List[Resource]:
        """
        Retrieves the resources.
        :return: The resources.
        :rtype: List[Resource]
        """
        return self._resources

    @property
    def outcome(self) -> Any:
        """
        Retrieves the outcome of the "up" operation.
        :return: Such outcome.
        :rtype: Any
        """
        return self._outcome

    @abc.abstractmethod
    async def perform(self) -> List[Event]:
        """
        Performs the operation on the stack.
        :return: A list of events representing the outcome.
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
