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

from .ArtifactResultsType import ArtifactResultsType
from .QuestionIDPattern import QuestionIDPattern
from .ResultType import ResultType

logger = logging.getLogger(__name__)

@attribute(local_name='questionnaire_ref', type=QuestionIDPattern, required=True)
@attribute(local_name='result', cls=ResultType, required=True)
@element(local_name='artifact_results', cls=ArtifactResultsType, min=0, max=1)
class QuestionnaireResultType(Model):
    pass
