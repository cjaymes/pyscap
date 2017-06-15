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
class ProcessStateElement(StateType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'command', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'exec_time', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'pid', 'class': 'scap.model.oval_5.defs.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'ppid', 'class': 'scap.model.oval_5.defs.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'priority', 'class': 'scap.model.oval_5.defs.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'ruid', 'class': 'scap.model.oval_5.defs.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'scheduling_class', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'start_time', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'tty', 'class': 'scap.model.oval_5.defs.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'user_id', 'class': 'scap.model.oval_5.defs.EntityStateIntType', 'min': 0, 'max': 1},
        ],
        'attributes': {
        },
    }
