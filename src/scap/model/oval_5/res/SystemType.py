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

from expatriate.model.Model import Model
from expatriate.model.decorators import *

from .DefinitionsType import DefinitionsType
from .TestsType import TestsType

logger = logging.getLogger(__name__)

@element(local_name='definitions', cls=DefinitionsType, min=0, max=1)
@element(local_name='tests', cls=TestsType, min=0, max=1)
@element(namespace='http://oval.mitre.org/XMLSchema/oval-system-characteristics-5', local_name='oval_system_characteristics')
class SystemType(Model):
    pass
