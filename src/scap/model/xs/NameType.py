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
import re

from scap.model.xs import *
from scap.model.xs.TokenType import TokenType

logger = logging.getLogger(__name__)
class NameType(TokenType):
    def parse_value(self, value):
        m = re.fullmatch(i_ + c_ + '*', value)
        if not m:
            raise ValueError('xs:Name must match \i\c* ' + value)

        return super(NameType, self).parse_value(value)
