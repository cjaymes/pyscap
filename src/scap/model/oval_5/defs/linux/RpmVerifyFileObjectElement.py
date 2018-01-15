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

from expatriate.model.decorators import *

from ..EntityObjectType import EntityObjectType

from .EpochElement import EpochElement
from .ObjectType import ObjectType
from .ReleaseElement import ReleaseElement
from .RpmVerifyFileBehaviors import RpmVerifyFileBehaviors
from .VersionElement import VersionElement

logger = logging.getLogger(__name__)

@element(local_name='behaviors', cls=RpmVerifyFileBehaviors, min=0, max=1)
@element(local_name='name', cls=EntityObjectType, min=0, max=1)
@element(local_name='epoch', cls=EpochElement, min=0, max=1)
@element(local_name='version', cls=VersionElement, min=0, max=1)
@element(local_name='release', cls=ReleaseElement, min=0, max=1)
@element(local_name='arch', cls=EntityObjectType, min=0, max=1)
@element(local_name='filepath', cls=EntityObjectType, min=0, max=1)
class RpmVerifyFileObjectElement(ObjectType):
    pass
