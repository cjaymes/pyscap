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

from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class QuestionResultsType(Model):
    MODEL_MAP = {
        'elements': [
            # TODO: at least one of *_question_result
            {'tag_name': 'boolean_question_result', 'list': 'question_results', 'class': 'BooleanQuestionResultType', 'min': 0, 'max': None},
            {'tag_name': 'choice_question_result', 'list': 'question_results', 'class': 'ChoiceQuestionResultType', 'min': 0, 'max': None},
            {'tag_name': 'numeric_question_result', 'list': 'question_results', 'class': 'NumericQuestionResultType', 'min': 0, 'max': None},
            {'tag_name': 'string_question_result', 'list': 'question_results', 'class': 'StringQuestionResultType', 'min': 0, 'max': None},
        ],
    }
