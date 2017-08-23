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
from scap.model.decorators import *
from scap.model.xs.BooleanType import BooleanType
from scap.model.xs.NonNegativeIntegerType import NonNegativeIntegerType

from .. import RESULT_ENUMERATION
from ..TestIdPattern import TestIdPattern

logger = logging.getLogger(__name__)

@attribute(local_name='applicability_check', type=BooleanType)
@attribute(local_name='test_ref', type=TestIdPattern, required=True)
@attribute(local_name='version', type=NonNegativeIntegerType, required=True)
@attribute(local_name='variable_instance', type=NonNegativeIntegerType, default=1)
@attribute(local_name='negate', type=BooleanType, default=False)
@attribute(local_name='result', enum=RESULT_ENUMERATION, required=True)
class CriterionType(Model):
    pass
