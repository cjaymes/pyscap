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

logger = logging.getLogger(__name__)
class SelChoicesType(Model):
    MODEL_MAP = {
        'elements': [
            # TODO at least one choice/complex-choice
            {'xml_namespace': 'http://checklists.nist.gov/xccdf/1.1', 'tag_name': 'choice', 'type': 'String', 'append': 'choices', 'min': 1, 'max': None},
        ],
        'attributes': {
            'mustMatch': {'type': 'Boolean'},
            'selector': {'type': 'String', 'default': ''},
        },
    }
