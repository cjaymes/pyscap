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
from expatriate.model.xs.IdType import IdType
from expatriate.model.xs.NMTokensType import NMTokensType

from .InlineType import InlineType

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=IdType)
@attribute(local_name='class', type=NMTokensType)
@attribute(local_name='style', type=defer_class_load('scap.model.xhtml.StyleSheetType', 'StyleSheetType'))
@attribute(local_name='title', type=defer_class_load('scap.model.xhtml.TextType', 'TextType'))
@attribute(local_name='lang', type=defer_class_load('scap.model.xhtml.LanguageCodeType', 'LanguageCodeType'))
# xml:lang is defined in scap.model.Model
@attribute(local_name='dir', enum=['ltr', 'rtl'])
@attribute(local_name='onclick', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='ondblclick', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmousedown', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmouseup', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmouseover', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmousemove', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onmouseout', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onkeypress', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onkeydown', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
@attribute(local_name='onkeyup', type=defer_class_load('scap.model.xhtml.ScriptType', 'ScriptType'))
class AddressTag(InlineType):
    pass
