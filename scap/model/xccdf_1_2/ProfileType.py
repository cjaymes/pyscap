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
class ProfileType(Model):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'ProfileIDPattern'},
            'prohibitChanges': {'ignore': True, 'type': 'Boolean', 'default': False},
            'abstract': {'ignore': True, 'type': 'Boolean', 'default': False},
            'note-tag': {'ignore': True, 'type': 'NCName'},
            'extends': {'notImplemented': True, 'type': 'NCName'},
            'Id': {'ignore': True, 'type': 'ID'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.2}status': {'ignore': True, 'class': 'StatusType', 'append': 'statuses'},
            '{http://checklists.nist.gov/xccdf/1.2}dc-status': {'ignore': True, 'class': 'DCStatusType', 'append': 'dc_statuses'},
            '{http://checklists.nist.gov/xccdf/1.2}version': {'ignore': True, 'class': 'VersionType'},
            '{http://checklists.nist.gov/xccdf/1.2}title': {'ignore': True, 'class': 'TextWithSubType', 'append': 'titles'},
            '{http://checklists.nist.gov/xccdf/1.2}description': {'ignore': True, 'class': 'HTMLTextWithSubType', 'append': 'descriptions'},
            '{http://checklists.nist.gov/xccdf/1.2}reference': {'ignore': True, 'class': 'ReferenceType', 'append': 'references'},
            '{http://checklists.nist.gov/xccdf/1.2}platform': {'ignore': True, 'class': 'OverrideableCPE2IDRefType', 'append': 'platforms'},
            '{http://checklists.nist.gov/xccdf/1.2}select': {'class': 'ProfileSelectType', 'map': 'selects', 'key': 'idref'},
            '{http://checklists.nist.gov/xccdf/1.2}set-complex-value': {'class': 'ProfileSetComplexValueType', 'map': 'set_complex_values', 'key': 'idref'},
            '{http://checklists.nist.gov/xccdf/1.2}set-value': {'class': 'ProfileSetValueType', 'map': 'set_values', 'key': 'idref'},
            '{http://checklists.nist.gov/xccdf/1.2}refine-value': {'class': 'ProfileRefineValueType', 'map': 'refine_values', 'key': 'idref'},
            '{http://checklists.nist.gov/xccdf/1.2}refine-rule': {'class': 'ProfileRefineRuleType', 'map': 'refine_rules', 'key': 'idref'},
            '{http://checklists.nist.gov/xccdf/1.2}metadata': {'ignore': True, 'class': 'MetadataType', 'append': 'metadata'},
            '{http://checklists.nist.gov/xccdf/1.2}signature': {'ignore': True, 'class': 'SignatureType'},
        },
    }
    # def __init__(self):
    #     super(ProfileType, self).__init__()
    #
    #     self.extends = None
    #
    #     self.selects = {}
    #     self.set_complex_values = {}
    #     self.set_values = {}
    #     self.refine_values = {}
    #     self.refine_rules = {}

    # def parse_attribute(self, name, value):
    #     if name == 'extends':
    #         logger.critical('Profiles with @extends are not supported')
    #         import sys
    #         sys.exit()
    #     else:
    #         return super(ProfileType, self).parse_attribute(name, value)
    #     return True
    #
    # def parse_element(self, sub_el):
    #     if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}select':
    #         if sub_el.attrib['idref'] not in self.parent.rules:
    #             logger.critical('Rule idref in Profile not found: ' + sub_el.attrib['idref'])
    #             import sys
    #             sys.exit()
    #         r = self.parent.rules[sub_el.attrib['idref']]
    #         if sub_el.attrib['selected'] == 'true':
    #             logger.debug('Rule ' + sub_el.attrib['idref'] + ' selected by profile ' + self.id)
    #             self.selected_rules.append(sub_el.attrib['idref'])
    #
    #             if sub_el.attrib['idref'] not in self.rule_check_selections:
    #                 self.rule_check_selections[sub_el.attrib['idref']] = None
    #         else:
    #             try:
    #                 logger.debug('Rule ' + sub_el.attrib['idref'] + ' un-selected by profile ' + self.id)
    #                 self.selected_rules.remove(sub_el.attrib['idref'])
    #             except KeyError:
    #                 logger.warning('Rule ' + sub_el.attrib['idref'] + ' was not previously selected by profile ' + self.id)
    #     elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}refine-value':
    #         if sub_el.attrib['idref'] not in self.parent.values:
    #             logger.critical('Value idref in Profile not found: ' + sub_el.attrib['idref'])
    #             import sys
    #             sys.exit()
    #         v = self.parent.values[sub_el.attrib['idref']]
    #         if sub_el.attrib['selector'] not in v.selectors:
    #             logger.critical('Selector in Value not found: ' + sub_el.attrib['selector'])
    #             import sys
    #             sys.exit()
    #         logger.info('Using selector ' + sub_el.attrib['selector'] + ' for value ' + v.id + ' in profile ' + self.id)
    #         self.value_selections[v.id] = sub_el.attrib['selector']
    #     elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}refine-rule':
    #         if sub_el.attrib['idref'] not in self.parent.rules:
    #             logger.critical('Rule idref in Profile not found: ' + sub_el.attrib['idref'])
    #             import sys
    #             sys.exit()
    #         logger.info('Using check selector ' + sub_el.attrib['selector'] + ' for rule ' + sub_el.attrib['idref'] + ' in profile ' + self.id)
    #         self.rule_check_selections[sub_el.attrib['idref']] = sub_el.attrib['selector']
    #     else:
    #         return super(ProfileType, self).parse_element(sub_el)
    #     return True

    # def from_xml(self, parent, el):
    #     # copy in the rules that are selected by default
    #     for rule_id in parent.selected_rules:
    #         self.selected_rules[rule_id] = parent.rules[rule_id]
    #
    #     super(ProfileType, self).from_xml(parent, el)
