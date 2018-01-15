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
from expatriate.model.xs.NCNameType import NCNameType

from .RemoteResourceElement import RemoteResourceElement
from .ReportRequestContentElement import ReportRequestContentElement

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=NCNameType, required=True)
@attribute(namespace='*', local_name='*')
@element(local_name='content', cls=ReportRequestContentElement)
@element(local_name='remote-resource', cls=RemoteResourceElement)
class ReportRequestType(Model):
    pass
