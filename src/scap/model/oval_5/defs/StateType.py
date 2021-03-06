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
from scap.model.oval_5 import OPERATOR_ENUMERATION

logger = logging.getLogger(__name__)
class StateType(Model):
    MODEL_MAP = {
        'elements': [
            {'xmlns': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'min': 0, 'max': 1},
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-common-5', 'tag_name': 'notes', 'class': 'NotesType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'id': {'type': 'scap.model.oval_5.StateIdPattern', 'required': True},
            'version': {'type': 'NonNegativeIntegerType', 'required': True},
            'operator': {'enum': OPERATOR_ENUMERATION, 'default': 'AND'},
            'comment': {'type': 'scap.model.oval_5.NonEmptyString'}, # required in the spec
            'deprecated': {'type': 'BooleanType', 'default': False},
        }
    }
