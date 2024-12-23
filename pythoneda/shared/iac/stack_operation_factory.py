# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/stack_operation_factory.py

This script defines the StackOperationFactory class.

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
import abc
from pythoneda.shared import BaseObject, Port
from pythoneda.shared.iac.events import (
    InfrastructureRemovalRequested,
    InfrastructureUpdateRequested,
)


class StackOperationFactory(Port, BaseObject):
    """
    Creates stacks.

    Class name: StackOperationFactory

    Responsibilities:
        - Create StackOperation instances.

    Collaborators:
        - pythoneda.iac.Stack
    """

    def __init__(self):
        """
        Creates a new StackOperationFactory instance.
        """
        super().__init__()

    @abc.abstractmethod
    def new(
        self,
        event: Union[InfrastructureUpdateRequested, InfrastructureRemovalRequested],
    ) -> StackOperation:
        """
        Creates a new stack operation.
        :param event: The event.
        :type event: Union[InfrastructureUpdateRequested, InfrastructureRemovalRequested]
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
