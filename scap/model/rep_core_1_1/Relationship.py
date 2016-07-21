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

from scap.model.Simple import Simple
import logging

logger = logging.getLogger(__name__)
class Relationship(Simple):
    def __init__(self):
        super(Relationship, self).__init__()

        self.refs = []

        self.type = None
        self.scope = 'inclusive'
        self.subject = None

    def get_tag(self):
        return '{http://scap.nist.gov/schema/reporting-core/1.1}relationship'

    def get_attributes(self):
        attribs = super(Relationship, self).get_attributes()

        if self.type is None:
            logger.critical('A Relationship must define the type attribute')
            import sys
            sys.exit()
        attribs['type'] = self.type

        attribs['scope'] = self.scope

        if self.subject is None:
            logger.critical('A Relationship must define the subject attribute')
            import sys
            sys.exit()
        attribs['subject'] = self.subject

        return attribs

    def get_sub_elements(self):
        sub_els = super(Relationship, self).get_sub_elements()

        if len(self.refs) <= 0:
            logger.critical('A Relationship must define a ref element')
            import sys
            sys.exit()

        for ref in self.refs:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/reporting-core/1.1}ref', ref))

        return sub_els