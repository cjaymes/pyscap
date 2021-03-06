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

from scap.model.oval_5 import DATATYPE_ENUMERATION
from scap.model.oval_5 import OPERATION_ENUMERATION
from scap.model.oval_5 import CHECK_ENUMERATION
from scap.model.xs.AnySimpleType import AnySimpleType

logger = logging.getLogger(__name__)
class EntityStateFieldType(AnySimpleType):
    MODEL_MAP = {
        'attributes': {
            'name': {'required': True, 'type': 'StringType'}, # TODO <xsd:pattern value="[^A-Z]+"/>
            'datatype': {'enum': DATATYPE_ENUMERATION, 'default': 'string'},
            'operation': {'enum': OPERATION_ENUMERATION, 'default': 'equals'},
            'mask': {'type': 'BooleanType', 'default': False},
            'var_ref': {'type': 'scap.model.oval_5.VariableIdPattern'},
            'var_check': {'enum': CHECK_ENUMERATION},
            'entity_check': {'enum': CHECK_ENUMERATION, 'default': 'all'},
        }
    }
