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
from scap.Model import Model

from .ResultType import ResultType
from .TestActionRefType import TestActionRefType
from .ArtifactRefsType import ArtifactRefsType

logger = logging.getLogger(__name__)

@element(local_name='result', cls=ResultType, min=0, max=1)
@element(local_name='test_action_ref', cls=TestActionRefType, min=0, max=1)
@element(local_name='artifact_refs', cls=ArtifactRefsType, min=0, max=1)
class TestActionConditionType(Model):
    # TODO: at least one result or test_action_ref
    pass