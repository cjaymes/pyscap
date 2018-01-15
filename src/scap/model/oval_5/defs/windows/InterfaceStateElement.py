# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import logging

from expatriate.model.decorators import *

from ..EntityStateType import EntityStateType

from .EntityStateAddrTypeType import EntityStateAddrTypeType
from .EntityStateInterfaceTypeType import EntityStateInterfaceTypeType
from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='name', cls=EntityStateType, min=0)
@element(local_name='index', cls=EntityStateType, min=0)
@element(local_name='type', cls=EntityStateInterfaceTypeType, min=0)
@element(local_name='hardware_addr', cls=EntityStateType, min=0)
@element(local_name='inet_addr', cls=EntityStateType, min=0)
@element(local_name='broadcast_addr', cls=EntityStateType, min=0)
@element(local_name='netmask', cls=EntityStateType, min=0)
@element(local_name='addr_type', cls=EntityStateAddrTypeType, min=0)
class InterfaceStateElement(StateType):
    pass
