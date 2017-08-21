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

from scap.model.decorators import *

from .IPv6Type import IPv6Type
from .Source import Source
from .Timestamp import Timestamp

logger = logging.getLogger(__name__)

@attribute(local_name='source', type=Source)
@attribute(local_name='timestamp', type=Timestamp)
@attribute(namespace='*', local_name='*')
class IPAddressIPv6Type(IPv6Type):
    pass