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
class DefinitionType(Model):
    TAG_MAP = {
        '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria': {
            'class': 'CriteriaType',
            'minCount': 1,
        },
    }

    def __init__(self):
        super(DefinitionType, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5}definition

        self.criteria = None

        self.ignore_attributes.extend([
            'version',
            'class',
        ])
        self.required_attributes.extend([
            'id',
            'version',
            'class',
        ])
        self.ignore_sub_elements.extend([
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}metadata',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}notes',
        ])
        self.required_sub_elements.append('{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria')

    def parse_attribute(self, name, value):
        if name == 'deprecated':
            logger.warning('Using deprecated definition ' + self.id)
        else:
            return super(DefinitionType, self).parse_attribute(name, value)
        return True

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria':
            self.criteria = Model.load(self, sub_el)
        else:
            return super(DefinitionType, self).parse_element(sub_el)
        return True
