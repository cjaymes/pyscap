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

from scap.Model import Model
from scap.model.oval_5 import *
from scap.model.oval_5.sc import *
from scap.model.xs.AnySimpleType import AnySimpleType

logger = logging.getLogger(__name__)
class VariableValueType(AnySimpleType):
    MODEL_MAP = {
        'attributes': {
            'variable_id': {'type': 'scap.model.oval_5.VariableIdPattern', 'required': True},
        }
    }
