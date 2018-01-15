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
from expatriate.model.xs.NonNegativeIntegerType import NonNegativeIntegerType

from .. import CHECK_ENUMERATION
from .. import EXISTENCE_ENUMERATION
from .. import OPERATOR_ENUMERATION
from .. import RESULT_ENUMERATION
from ..TestIdPattern import TestIdPattern

from .TestedItemType import TestedItemType
from .TestedVariableType import TestedVariableType

logger = logging.getLogger(__name__)

@attribute(local_name='test_id', type=TestIdPattern, required=True)
@attribute(local_name='version', type=NonNegativeIntegerType, required=True)
@attribute(local_name='variable_instance', type=NonNegativeIntegerType, default=1)
@attribute(local_name='check_existence', enum=EXISTENCE_ENUMERATION, default='at_least_one_exists')
@attribute(local_name='check', enum=CHECK_ENUMERATION, required=True)
@attribute(local_name='state_operator', enum=OPERATOR_ENUMERATION, default='AND')
@attribute(local_name='result', enum=RESULT_ENUMERATION, required=True)
@element(namespace='http://oval.mitre.org/XMLSchema/oval-system-characteristics-5', local_name='message', list='messages', min=0, max=None)
@element(local_name='tested_item', list='tested_items', cls=TestedItemType, min=0, max=None)
@element(local_name='tested_variable', list='tested_variables', cls=TestedVariableType, min=0, max=None)
class TestType(Model):
    pass
