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
from scap.model.oval_5 import *
from scap.model.oval_5.sc import *
from scap.model.oval_5.sc.ItemType import ItemType
from scap.model.oval_5.sc.linux import *

logger = logging.getLogger(__name__)
class RpmVerifyPackageItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'name', 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'min': 0, 'max': 1},
            {'tag_name': 'epoch', 'class': 'scap.model.oval_5.sc.EntityItemStringIntType', 'min': 0, 'max': 1},
            {'tag_name': 'version', 'class': 'EntityItemStringVersionType', 'min': 0, 'max': 1},
            {'tag_name': 'release', 'class': 'EntityItemStringVersionType', 'min': 0, 'max': 1},
            {'tag_name': 'arch', 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'min': 0, 'max': 1},
            {'tag_name': 'filepath', 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'min': 0, 'max': 1},
            {'tag_name': 'extended_name', 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'min': 0, 'max': 1},
            {'tag_name': 'dependency_check_passed', 'class': 'scap.model.oval_5.sc.EntityItemBoolType', 'min': 0, 'max': 1},
            {'tag_name': 'digest_check_passed', 'class': 'scap.model.oval_5.sc.EntityItemBoolType', 'min': 0, 'max': 1},
            {'tag_name': 'verification_script_successful', 'class': 'scap.model.oval_5.sc.EntityItemBoolType', 'min': 0, 'max': 1},
            {'tag_name': 'signature_check_passed', 'class': 'scap.model.oval_5.sc.EntityItemBoolType', 'min': 0, 'max': 1},
        ],
    }