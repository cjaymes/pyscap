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

from scap.model.oval_5.defs.unix.StateType import StateType

logger = logging.getLogger(__name__)
class GconfStateElement(StateType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'key', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'source', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'type', 'class': 'EntityStateGconfTypeType', 'min': 0, 'max': 1},
            {'tag_name': 'is_writable', 'class': 'scap.model.oval_5.defs.EntityStateBoolType', 'min': 0, 'max': 1},
            {'tag_name': 'mod_user', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'mod_time', 'class': 'scap.model.oval_5.defs.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'is_default', 'class': 'scap.model.oval_5.defs.EntityStateBoolType', 'min': 0, 'max': 1},
            {'tag_name': 'value', 'class': 'scap.model.oval_5.defs.EntityStateAnySimpleType', 'min': 0, 'max': 1},
        ],
        'attributes': {
        },
    }
