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

from scap.model.xs.LongType import LongType
import logging

logger = logging.getLogger(__name__)
class IntType(LongType):
    def parse_value(self, value):
        value = super(IntType, self).parse_value(value)

        if value > 2147483647:
            raise ValueError('xs:int cannot be > 2147483647')
        if value < -2147483648:
            raise ValueError('xs:int cannot be < -2147483648')

        return value
