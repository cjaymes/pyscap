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
import pathlib
import pytest
import xml.etree.ElementTree as ET

from scap.Model import Model
import scap.model.xccdf_1_1

logging.basicConfig(level=logging.DEBUG)
Model.register_namespace('scap.model.xccdf_1_1', 'http://checklists.nist.gov/xccdf/1.1')
Model.register_namespace('scap.model.xhtml', 'http://www.w3.org/1999/xhtml')
Model.register_namespace('scap.model.dc_elements_1_1', 'http://purl.org/dc/elements/1.1/')
Model.register_namespace('scap.model.cpe_lang_2_3', 'http://cpe.mitre.org/language/2.0')

def test_benchmark():
    path = pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xccdf_1_1.xml'
    model = Model.load(None, ET.parse(str(path)).getroot())
