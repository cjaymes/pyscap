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

from scap.model.oval_5 import *
from scap.model.oval_5.defs import *
from scap.model.oval_5.defs.independent import *
from scap.model.oval_5.defs.EntityStateStringType import EntityStateStringType

logger = logging.getLogger(__name__)
class EntityStateVariableRefType(EntityStateStringType):
    MODEL_MAP = {
    }

    def get_value_pattern(self):
        return r'(oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*){0,}'