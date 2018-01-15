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

from .AddressLineType import AddressLineType
from .ThoroughfareNumberFromType import ThoroughfareNumberFromType
from .ThoroughfareNumberToType import ThoroughfareNumberToType

logger = logging.getLogger(__name__)

@attribute(local_name='RangeType', enum=['Odd', 'Even'])
@attribute(local_name='Indicator', )
@attribute(local_name='Separator', )
@attribute(local_name='IndicatorOccurrence', enum=['Before', 'After'])
@attribute(local_name='NumberRangeOccurrence', enum=['BeforeName', 'AfterName', 'BeforeType', 'AfterType'])
@attribute(local_name='Type', )
@attribute(local_name='Code', ) # from grPostal
@attribute(local_name='*', )
@element(local_name='AddressLine', list='address_lines', cls=AddressLineType)
@element(local_name='ThoroughfareNumberFrom', into='thoroughfare_number_from', cls=ThoroughfareNumberFromType)
@element(local_name='ThoroughfareNumberTo', into='thoroughfare_number_to', cls=ThoroughfareNumberToType)
class ThoroughfareNumberRangeType(Model):
    pass
