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

from scap.model.xs import *
from scap.model.xs.AnnotatedType import AnnotatedType

logger = logging.getLogger(__name__)
class ComplexTypeType(AnnotatedType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'simpleContent', 'class': 'SimpleContentElement', 'min': 0, 'max': None},
            {'tag_name': 'complexContent', 'class': 'ComplexContentElement', 'min': 0, 'max': None},
            {'tag_name': 'group', 'class': 'GroupType', 'min': 0},
            {'tag_name': 'all', 'class': 'AllType', 'min': 0},
            {'tag_name': 'choice', 'class': 'ChoiceElement', 'min': 0},
            {'tag_name': 'sequence', 'class': 'GroupType', 'min': 0},
            {'tag_name': 'attribute', 'class': 'AttributeType', 'min': 0, 'max': None},
            {'tag_name': 'attributeGroup', 'class': 'AttributeGroupType', 'min': 0, 'max': None},
            {'tag_name': 'anyAttribute', 'class': 'WildcardType', 'min': 0},
        ],
        'attributes': {
            'name': {'type': 'NCNameType'},
            'mixed': {'type': 'BooleanType', 'default': False},
            'abstract': {'type': 'BooleanType', 'default': False},
            'final': {'enum': ['#all', 'extension', 'restriction']},
            'block': {'enum': ['#all', 'extension', 'restriction']},
            '*': {},
        }
    }
    # TODO .mixed & simpleContent sub-elements are mutulally exclusive